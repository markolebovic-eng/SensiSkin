// Reusable PDF-export pipeline for client reports (see SKILL.md section 4).
//
// Usage:
//   node build-pdf-report.js <path-to-report.html> <path-to-output.pdf> [--verify <dir>]
//
// What it does, in order:
//   1. Loads the report HTML in a real (non-CLI) Chrome via puppeteer-core, pointed at
//      the machine's existing Chrome install (no bundled-Chromium download needed).
//   2. Waits for Paged.js (must be loaded via <script src="https://unpkg.com/pagedjs/...">
//      in the HTML itself) to finish laying the document out into .pagedjs_page divs.
//   3. Injects the visible footer bar into ONLY the last page, absolutely positioned to
//      span the full page width and sit flush with the true bottom edge — this is the
//      part that cannot be done with CSS alone (see SKILL.md 4d for why).
//   4. Exports the PDF via page.pdf(), which faithfully captures that already-paginated,
//      already-finished DOM state.
//   5. Optionally (--verify <dir>), screenshots every .pagedjs_page individually so you
//      can actually look at each page before telling the owner it's done (SKILL.md 4e).
//
// Requires: puppeteer-core installed somewhere reachable (npm install --prefix <dir>
// puppeteer-core --no-save works fine in a scratch directory — no need to add it to
// the client project's own package.json).
//
// The source HTML's .footer element must stay `display:none` in its own stylesheet —
// this script reads its innerHTML and re-injects a *copy* of it as `.final-footer-bar`
// on the last page only. Do not remove the source .footer element from the HTML.

const puppeteer = require('puppeteer-core');
const path = require('path');

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

async function main() {
  const [, , htmlPathArg, pdfPathArg, verifyFlag, verifyDirArg] = process.argv;
  if (!htmlPathArg || !pdfPathArg) {
    console.error('Usage: node build-pdf-report.js <report.html> <output.pdf> [--verify <dir>]');
    process.exit(1);
  }
  const doVerify = verifyFlag === '--verify';
  const verifyDir = doVerify ? verifyDirArg : null;

  const htmlUrl = htmlPathArg.startsWith('file://')
    ? htmlPathArg
    : 'file:///' + htmlPathArg.replace(/\\/g, '/');

  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: 'new',
    args: ['--no-sandbox'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 1600 });

  await page.goto(htmlUrl, { waitUntil: 'networkidle0', timeout: 60000 });
  await page.waitForSelector('.pagedjs_pages', { timeout: 30000 });
  await new Promise((r) => setTimeout(r, 1500)); // let Paged.js finish settling

  const injectResult = await page.evaluate(() => {
    const pages = document.querySelectorAll('.pagedjs_page');
    const last = pages[pages.length - 1];
    if (!last) return { ok: false, reason: 'no .pagedjs_page elements found' };
    const sourceFooter = document.querySelector('.footer');
    if (!sourceFooter) return { ok: false, reason: 'no .footer source element found' };

    if (getComputedStyle(last).position === 'static') {
      last.style.position = 'relative';
    }
    const bar = document.createElement('div');
    bar.className = 'final-footer-bar';
    bar.innerHTML = sourceFooter.innerHTML;
    bar.style.position = 'absolute';
    bar.style.left = '0';
    bar.style.right = '0';
    bar.style.bottom = '0';
    bar.style.width = '100%';
    last.appendChild(bar);

    const r = bar.getBoundingClientRect();
    return {
      ok: true,
      pageCount: pages.length,
      barRect: { x: r.x, y: r.y, width: r.width, height: r.height, bottom: r.bottom },
      lastPageBottom: last.getBoundingClientRect().bottom,
    };
  });

  console.log('footer injection result:', JSON.stringify(injectResult, null, 2));
  if (!injectResult.ok) {
    await browser.close();
    process.exit(1);
  }

  const pdfPath = pdfPathArg;
  await page.pdf({
    path: pdfPath,
    printBackground: true,
    preferCSSPageSize: true,
    margin: { top: 0, bottom: 0, left: 0, right: 0 },
  });
  console.log('PDF written to', pdfPath);

  if (doVerify && verifyDir) {
    const pages = await page.$$('.pagedjs_page');
    for (let i = 0; i < pages.length; i++) {
      const box = await pages[i].boundingBox();
      const outPath = path.join(verifyDir, `verify-page-${i + 1}.png`);
      await page.screenshot({ path: outPath, clip: box });
      console.log('wrote', outPath);
    }
  }

  await browser.close();
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
