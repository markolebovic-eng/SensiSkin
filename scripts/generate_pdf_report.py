#!/usr/bin/env python3
"""PDF Marketing Report Generator — AI Marketing Suite"""

import json
import sys
import math
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.platypus.flowables import Flowable
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

# ── Palette ────────────────────────────────────────────────────────────────────
PRIMARY   = colors.HexColor('#1B2A4A')
ACCENT    = colors.HexColor('#2D5BFF')
HIGHLIGHT = colors.HexColor('#FF6B35')
SUCCESS   = colors.HexColor('#00C853')
WARNING   = colors.HexColor('#FFB300')
DANGER    = colors.HexColor('#FF1744')
LIGHT_BG  = colors.HexColor('#F5F7FA')
BODY_TEXT = colors.HexColor('#2C3E50')
SECONDARY = colors.HexColor('#7F8C9B')
BORDER    = colors.HexColor('#E0E6ED')
WHITE     = colors.white

PAGE_W, PAGE_H = A4
CONTENT_W = PAGE_W - 4 * cm


def score_color(s):
    if s >= 80: return SUCCESS
    if s >= 60: return ACCENT
    if s >= 40: return WARNING
    return DANGER


def score_grade(s):
    grades = [(93,'A+'),(87,'A'),(80,'A-'),(77,'B+'),(73,'B'),(70,'B-'),
              (67,'C+'),(63,'C'),(60,'C-'),(57,'D+'),(53,'D'),(50,'D-')]
    for threshold, grade in grades:
        if s >= threshold:
            return grade
    return 'F'


class ScoreGauge(Flowable):
    def __init__(self, score, size=130):
        super().__init__()
        self.score = score
        self.size = size
        self.width = size
        self.height = size

    def draw(self):
        cx, cy = self.size / 2, self.size / 2
        r = self.size * 0.40
        track_w = self.size * 0.09
        col = score_color(self.score)

        # Background ring
        self.canv.setStrokeColor(BORDER)
        self.canv.setLineWidth(track_w)
        self.canv.circle(cx, cy, r)

        # Score arc
        self.canv.setStrokeColor(col)
        self.canv.setLineWidth(track_w)
        angle = -(self.score / 100) * 360
        self.canv.arc(cx - r, cy - r, cx + r, cy + r, 90, angle)

        # Score number
        self.canv.setFont('Helvetica-Bold', int(self.size * 0.20))
        self.canv.setFillColor(PRIMARY)
        self.canv.drawCentredString(cx, cy + 2, str(self.score))

        self.canv.setFont('Helvetica', int(self.size * 0.09))
        self.canv.setFillColor(SECONDARY)
        self.canv.drawCentredString(cx, cy - self.size * 0.14, '/100')


def S(name, **kw):
    defaults = dict(fontName='Helvetica', textColor=BODY_TEXT, leading=14)
    defaults.update(kw)
    return ParagraphStyle(name, **defaults)


STYLES = {
    'H1':      S('H1',  fontSize=24, fontName='Helvetica-Bold', textColor=WHITE, leading=30),
    'H2':      S('H2',  fontSize=15, fontName='Helvetica-Bold', textColor=PRIMARY, leading=20,
                  spaceBefore=10, spaceAfter=6),
    'H3':      S('H3',  fontSize=11, fontName='Helvetica-Bold', textColor=PRIMARY, leading=15,
                  spaceBefore=8, spaceAfter=4),
    'Body':    S('Body', fontSize=9.5, leading=14, spaceAfter=5),
    'Small':   S('Small', fontSize=8.5, leading=12),
    'Label':   S('Label', fontSize=8, fontName='Helvetica-Bold', textColor=SECONDARY, leading=12),
    'CoverSub':S('CoverSub', fontSize=10, textColor=colors.HexColor('#B8C9E5'), leading=15),
    'FindTxt': S('FindTxt', fontSize=9, leading=13),
    'Center':  S('Center', fontSize=9.5, leading=14, alignment=TA_CENTER),
    'Footer':  S('Footer', fontSize=8, textColor=SECONDARY, alignment=TA_CENTER, leading=11),
}


# ── Page builders ──────────────────────────────────────────────────────────────

def cover_page(data):
    el = []

    # Dark header band
    hdr = Table([[Paragraph(data.get('report_title', 'Marketing Audit Report'), STYLES['H1'])],
                 [Paragraph(data.get('report_subtitle', ''), STYLES['CoverSub'])]],
                colWidths=[CONTENT_W])
    hdr.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), PRIMARY),
        ('TOPPADDING',    (0,0), (-1,-1), 28),
        ('BOTTOMPADDING', (0,0), (-1,-1), 22),
        ('LEFTPADDING',   (0,0), (-1,-1), 28),
        ('RIGHTPADDING',  (0,0), (-1,-1), 20),
    ]))
    el.append(hdr)
    el.append(Spacer(1, 18))

    # URL + date row
    meta = Table([[Paragraph(f"<b>{data['url']}</b>", STYLES['H3']),
                   Paragraph(data['date'], STYLES['Small'])]],
                 colWidths=[CONTENT_W * 0.65, CONTENT_W * 0.35])
    meta.setStyle(TableStyle([
        ('ALIGN', (1,0), (1,0), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    el.append(meta)
    el.append(Spacer(1, 12))
    el.append(HRFlowable(width='100%', thickness=1, color=BORDER))
    el.append(Spacer(1, 20))

    # Gauge + grade + summary
    overall = data['overall_score']
    grade   = score_grade(overall)
    col     = score_color(overall)
    hex_col = col.hexval()[2:]

    gauge_cell   = ScoreGauge(overall, size=130)
    grade_para   = Paragraph(
        f'<font size="52" color="#{hex_col}"><b>{grade}</b></font>',
        ParagraphStyle('Grade', alignment=TA_CENTER, leading=60))
    summary_para = Paragraph(data['executive_summary'], STYLES['Body'])

    gauge_tbl = Table([[gauge_cell, grade_para, summary_para]],
                      colWidths=[150, 100, CONTENT_W - 250])
    gauge_tbl.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN',  (1,0), (1,0),  'CENTER'),
        ('LEFTPADDING',  (0,0), (0,0), 0),
        ('RIGHTPADDING', (0,0), (0,0), 12),
        ('RIGHTPADDING', (1,0), (1,0), 14),
    ]))
    el.append(gauge_tbl)
    el.append(Spacer(1, 20))
    el.append(HRFlowable(width='100%', thickness=1, color=BORDER))
    el.append(Spacer(1, 10))
    el.append(Paragraph(
        f"<font color='#{SECONDARY.hexval()[2:]}'>Pripremljeno za: </font>"
        f"<b>{data['brand_name']}</b>"
        f"<font color='#{SECONDARY.hexval()[2:]}'> · Generated by AI Marketing Suite</font>",
        S('BrandLine', fontSize=9)))
    el.append(PageBreak())
    return el


def scores_page(data):
    el = []
    el.append(Paragraph("Pregled Ocena po Kategorijama", STYLES['H2']))
    el.append(HRFlowable(width='100%', thickness=1, color=BORDER))
    el.append(Spacer(1, 14))

    cats   = data['categories']
    bar_w  = CONTENT_W * 0.48

    header_row = [[
        Paragraph('<b>Kategorija</b>',  STYLES['Label']),
        Paragraph('<b>Ocena</b>',       STYLES['Label']),
        Paragraph('<b>Progres</b>',     STYLES['Label']),
        Paragraph('<b>Težina</b>',      STYLES['Label']),
        Paragraph('<b>Status</b>',      STYLES['Label']),
    ]]
    rows = []
    for name, info in cats.items():
        s    = info['score']
        w    = info.get('weight', '')
        col  = score_color(s)
        hx   = col.hexval()[2:]
        if s >= 80:   status = 'Snažno'
        elif s >= 60: status = 'Solidno'
        elif s >= 40: status = 'Treba pažnje'
        else:         status = 'Kritično'

        d = Drawing(bar_w, 12)
        d.add(Rect(0, 2, bar_w,           8, fillColor=LIGHT_BG, strokeColor=None))
        d.add(Rect(0, 2, bar_w*(s/100),   8, fillColor=col,      strokeColor=None))

        rows.append([
            Paragraph(f'<b>{name}</b>', STYLES['Small']),
            Paragraph(f'<font color="#{hx}"><b>{s}</b></font>',
                      S('Num', fontSize=11, fontName='Helvetica-Bold', alignment=TA_CENTER)),
            d,
            Paragraph(w, STYLES['Small']),
            Paragraph(f'<font color="#{hx}"><b>{status}</b></font>',
                      S('Stat', fontSize=8.5)),
        ])

    col_widths = [165, 45, bar_w, 45, 90]
    tbl = Table(header_row + rows, colWidths=col_widths,
                rowHeights=[20] + [32] * len(rows))
    tbl.setStyle(TableStyle([
        ('BACKGROUND',   (0,0), (-1,0),  PRIMARY),
        ('TEXTCOLOR',    (0,0), (-1,0),  WHITE),
        ('FONTNAME',     (0,0), (-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',     (0,0), (-1,0),  8.5),
        ('ALIGN',        (0,0), (-1,0),  'CENTER'),
        ('VALIGN',       (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN',        (1,1), (1,-1),  'CENTER'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [WHITE, LIGHT_BG]),
        ('GRID',         (0,0), (-1,-1), 0.5, BORDER),
        ('TOPPADDING',   (0,0), (-1,-1), 5),
        ('BOTTOMPADDING',(0,0), (-1,-1), 5),
        ('LEFTPADDING',  (0,0), (-1,-1), 8),
    ]))
    el.append(tbl)
    el.append(PageBreak())
    return el


def findings_page(data):
    el = []
    el.append(Paragraph("Ključni Nalazi", STYLES['H2']))
    el.append(HRFlowable(width='100%', thickness=1, color=BORDER))
    el.append(Spacer(1, 12))

    SEV_COLORS = {
        'Critical': DANGER,
        'High':     HIGHLIGHT,
        'Medium':   WARNING,
        'Low':      ACCENT,
    }
    header = [[
        Paragraph('<b>Ozbiljnost</b>', STYLES['Label']),
        Paragraph('<b>Nalaz</b>',      STYLES['Label']),
    ]]
    rows = []
    for f in data['findings']:
        sev = f['severity']
        col = SEV_COLORS.get(sev, SECONDARY)
        hx  = col.hexval()[2:]
        rows.append([
            Paragraph(f'<font color="#{hx}"><b>{sev}</b></font>',
                      S('Sev', fontSize=8.5, fontName='Helvetica-Bold', alignment=TA_CENTER)),
            Paragraph(f['finding'], STYLES['FindTxt']),
        ])

    tbl = Table(header + rows, colWidths=[82, CONTENT_W - 82])
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),  (-1,0),  PRIMARY),
        ('TEXTCOLOR',     (0,0),  (-1,0),  WHITE),
        ('FONTNAME',      (0,0),  (-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0),  (-1,0),  8.5),
        ('ALIGN',         (0,0),  (-1,0),  'CENTER'),
        ('VALIGN',        (0,0),  (-1,-1), 'TOP'),
        ('ALIGN',         (0,1),  (0,-1),  'CENTER'),
        ('ROWBACKGROUNDS',(0,1),  (-1,-1), [WHITE, LIGHT_BG]),
        ('GRID',          (0,0),  (-1,-1), 0.5, BORDER),
        ('TOPPADDING',    (0,0),  (-1,-1), 8),
        ('BOTTOMPADDING', (0,0),  (-1,-1), 8),
        ('LEFTPADDING',   (0,0),  (-1,-1), 10),
    ]))
    el.append(tbl)
    el.append(PageBreak())
    return el


def action_plan_page(data):
    el = []
    el.append(Paragraph("Prioritetni Akcioni Plan", STYLES['H2']))
    el.append(HRFlowable(width='100%', thickness=1, color=BORDER))
    el.append(Spacer(1, 14))

    sections = [
        ('🔴  Odmah — Ova Nedelja',            data.get('quick_wins', []),  DANGER,   LIGHT_BG),
        ('🟠  Kratkoročno — 1 do 3 Meseca',    data.get('medium_term', []), HIGHLIGHT, WHITE),
        ('🟡  Strateški — 3 do 6 Meseci',      data.get('strategic', []),   SUCCESS,  LIGHT_BG),
    ]

    for title, items, col, bg in sections:
        if not items:
            continue

        hdr = Table([[Paragraph(f'<b>{title}</b>',
                                S('AH', fontSize=10, fontName='Helvetica-Bold', textColor=WHITE))]],
                    colWidths=[CONTENT_W])
        hdr.setStyle(TableStyle([
            ('BACKGROUND',    (0,0), (-1,-1), col),
            ('TOPPADDING',    (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 8),
            ('LEFTPADDING',   (0,0), (-1,-1), 14),
        ]))
        el.append(hdr)

        item_rows = []
        for i, item in enumerate(items, 1):
            item_rows.append([
                Paragraph(f'<font color="#{col.hexval()[2:]}"><b>{i}.</b></font>',
                          S('Num', fontSize=10, fontName='Helvetica-Bold', alignment=TA_CENTER)),
                Paragraph(item, STYLES['Body']),
            ])

        item_tbl = Table(item_rows, colWidths=[28, CONTENT_W - 28])
        item_tbl.setStyle(TableStyle([
            ('BACKGROUND',    (0,0), (-1,-1), bg),
            ('VALIGN',        (0,0), (-1,-1), 'TOP'),
            ('ALIGN',         (0,0), (0,-1),  'CENTER'),
            ('TOPPADDING',    (0,0), (-1,-1), 7),
            ('BOTTOMPADDING', (0,0), (-1,-1), 7),
            ('LEFTPADDING',   (0,0), (0,-1),  10),
            ('LEFTPADDING',   (1,0), (1,-1),  8),
            ('LINEBELOW',     (0,0), (-1,-2), 0.5, BORDER),
        ]))
        el.append(item_tbl)
        el.append(Spacer(1, 12))

    el.append(PageBreak())
    return el


def competitors_page(data):
    comps = data.get('competitors')
    if not comps:
        return []

    el = []
    el.append(Paragraph("Konkurentska Analiza", STYLES['H2']))
    el.append(HRFlowable(width='100%', thickness=1, color=BORDER))
    el.append(Spacer(1, 12))

    brand   = data['brand_name']
    fields  = ['Pozicioniranje', 'Cene', 'Socijalni Dokaz', 'Sadržaj']
    keys    = ['positioning', 'pricing', 'social_proof', 'content']
    n_comps = len(comps)
    col_w   = CONTENT_W / (n_comps + 2)

    header_row = [Paragraph('<b>Kategorija</b>', STYLES['Label']),
                  Paragraph(f'<b>{brand}</b>',   STYLES['Label'])]
    for c in comps:
        header_row.append(Paragraph(f'<b>{c["name"]}</b>', STYLES['Label']))

    rows = [header_row]
    brand_vals = data.get('brand_values', {})
    for field, key in zip(fields, keys):
        row = [Paragraph(f'<b>{field}</b>', STYLES['Small']),
               Paragraph(brand_vals.get(key, '—'), STYLES['Small'])]
        for c in comps:
            row.append(Paragraph(c.get(key, '—'), STYLES['Small']))
        rows.append(row)

    tbl = Table(rows, colWidths=[col_w * 1.5] + [col_w] * (n_comps + 1))
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  PRIMARY),
        ('TEXTCOLOR',     (0,0), (-1,0),  WHITE),
        ('BACKGROUND',    (1,1), (1,-1),  colors.HexColor('#EDF2FF')),
        ('FONTNAME',      (0,0), (-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1), 8.5),
        ('ROWBACKGROUNDS',(0,1), (0,-1),  [LIGHT_BG]),
        ('GRID',          (0,0), (-1,-1), 0.5, BORDER),
        ('TOPPADDING',    (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING',   (0,0), (-1,-1), 8),
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
    ]))
    el.append(tbl)
    el.append(PageBreak())
    return el


def methodology_page(data):
    el = []
    el.append(Paragraph("Metodologija", STYLES['H2']))
    el.append(HRFlowable(width='100%', thickness=1, color=BORDER))
    el.append(Spacer(1, 12))

    el.append(Paragraph(
        "Ovaj izveštaj je generisan od strane <b>AI Marketing Suite</b> — sistema višestrukih "
        "specijalizovanih agenata koji pokriva SEO, analitiku, copywriting, social media, "
        "CRO, paid ads i strategiju. Svaka ocena je zasnovana na verifikovanim podacima "
        "i industrijskim standardima za lokalne B2C brendove u Srbiji.",
        STYLES['Body']))
    el.append(Spacer(1, 10))
    el.append(Paragraph("<b>Kategorije, Težine i Kriterijumi:</b>", STYLES['H3']))

    cats = data['categories']
    meth_rows = [['Kategorija', 'Težina', 'Kriterijum ocenjivanja']]
    criteria_map = data.get('methodology_criteria', {})
    for name, info in cats.items():
        meth_rows.append([
            name,
            info.get('weight', ''),
            criteria_map.get(name, '80+: Odlično · 60-79: Solidno · 40-59: Treba pažnje · <40: Kritično')
        ])

    tbl = Table(meth_rows, colWidths=[165, 50, CONTENT_W - 215])
    tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  PRIMARY),
        ('TEXTCOLOR',     (0,0), (-1,0),  WHITE),
        ('FONTNAME',      (0,0), (-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1), 8.5),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [WHITE, LIGHT_BG]),
        ('GRID',          (0,0), (-1,-1), 0.5, BORDER),
        ('TOPPADDING',    (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING',   (0,0), (-1,-1), 8),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
    ]))
    el.append(tbl)
    el.append(Spacer(1, 28))
    el.append(HRFlowable(width='100%', thickness=1, color=BORDER))
    el.append(Spacer(1, 8))
    el.append(Paragraph(
        f"Generated by AI Marketing Suite for Claude Code  ·  "
        f"{data['url']}  ·  {data['date']}",
        STYLES['Footer']))
    return el


# ── Main ───────────────────────────────────────────────────────────────────────

def generate_report(data, output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=2*cm,  bottomMargin=2*cm,
    )
    story = []
    story += cover_page(data)
    story += scores_page(data)
    story += findings_page(data)
    story += action_plan_page(data)
    story += competitors_page(data)
    story += methodology_page(data)
    doc.build(story)
    print(f"PDF generisan: {output_path}")


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        with open(sys.argv[1], encoding='utf-8') as f:
            data = json.load(f)
        output = sys.argv[2] if len(sys.argv) >= 3 else 'MARKETING-REPORT-output.pdf'
    else:
        print("Usage: python generate_pdf_report.py <data.json> <output.pdf>")
        sys.exit(1)
    generate_report(data, output)
