# Article JSON-LD — za svih ~30 blog postova (ručno ubacivanje)

**Datum:** 11. jun 2026.
**Kako:** Za svaki post otvori njegovu **Custom Schema** polje (isti način kao za service strane) i nalepi pripadajući blok. Naslov, opis, slika i datumi (`datePublished` / `dateModified`) su **povučeni sa vašeg sajta** — tačni su.
**Napomena:** post `sve-istine-o-laserskoj-epilaciji` već ima Article — nije u listi.
**Posle ubacivanja:** proveri post na validator.schema.org (mora da prikaže `Article`), pa GSC → Request indexing.

---

### 1. Da li je serum zaista potreban? - odgovori
`https://sensiskinstudio.com/da-li-je-serum-zaista-potreban/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Da li je serum zaista potreban? - odgovori",
  "description": "Da li serum zaista treba? Saznajte razliku između seruma i kreme, kada i kako se nanosi i zašto je bitan korak u rutini.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2023/02/47395f213efac32a626e841ad2a0f1ae.jpeg",
  "datePublished": "2023-02-15T12:57:10+00:00",
  "dateModified": "2026-06-10T22:43:19+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/da-li-je-serum-zaista-potreban/" }
}
```

### 2. Hemijski pilinzi - kako funkcionišu i da li su bezbedni
`https://sensiskinstudio.com/da-li-vas-plase-hemijski-pilinzi/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hemijski pilinzi - kako funkcionišu i da li su bezbedni",
  "description": "Da li vas plaše hemijski pilinzi? Saznajte kako funkcionišu, šta se dešava na koži i zašto su bezbedni.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/12/Sensi-skin-hemijski-pilinzi.jpg",
  "datePublished": "2022-12-06T11:06:14+00:00",
  "dateModified": "2026-06-10T22:57:03+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/da-li-vas-plase-hemijski-pilinzi/" }
}
```

### 3. Dermalux LED terapija - za koga i koliko tretmana
`https://sensiskinstudio.com/dermalux-led-terapija-kao-resenje-problema/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Dermalux LED terapija - za koga i koliko tretmana",
  "description": "DERMALUX LED terapija kao rešenje za problematičnu, aknoznu i reaktivnu kožu — kako svetlost leči i koliko tretmana treba.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2024/04/DermaluxFlexLifestyle01-1024x.jpg-e1712072858641.webp",
  "datePublished": "2024-04-02T15:49:18+00:00",
  "dateModified": "2026-06-10T22:46:52+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/dermalux-led-terapija-kao-resenje-problema/" }
}
```

### 4. Dermatolog ili estetičar - kome se obratiti?
`https://sensiskinstudio.com/dermatolog-ili-esteticar/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Dermatolog ili estetičar - kome se obratiti?",
  "description": "Kome da se obratite - dermatologu ili kozmetičaru-estetičaru? Razlike u ulogi i kada je ko pravi izbor.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/10/IMG-9649-scaled-1.jpg",
  "datePublished": "2022-10-14T12:14:58+00:00",
  "dateModified": "2026-06-10T22:59:18+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/dermatolog-ili-esteticar/" }
}
```

### 5. Faktori rasta u borbi protiv starenja kože
`https://sensiskinstudio.com/faktori-rasta-u-borbi-protiv-starenja-koze/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Faktori rasta u borbi protiv starenja kože",
  "description": "Šta su faktori rasta u kozmetologiji i kako pomažu kolagenu i elastinu? EGF, FGF, IGF i primena u tretmanima.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/08/IMG-9509-1-scaled-1.jpg",
  "datePublished": "2023-01-31T11:48:13+00:00",
  "dateModified": "2026-06-10T22:52:24+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/faktori-rasta-u-borbi-protiv-starenja-koze/" }
}
```

### 6. Gubitak kose i androgena alopecija - uzroci i tretmani
`https://sensiskinstudio.com/gubitak-kose-i-androgena-alopecija/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Gubitak kose i androgena alopecija - uzroci i tretmani",
  "description": "Zašto dolazi do gubitka kose i šta je androgena alopecija? Uzroci, simptomi i metode lečenja.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/06/socked-woman-drag-fallen-hair-from-brush-pink-background-isolated-girlhair-fall-out-problem-scaled-1.jpg",
  "datePublished": "2022-06-27T11:53:11+00:00",
  "dateModified": "2026-06-10T23:07:06+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/gubitak-kose-i-androgena-alopecija/" }
}
```

### 7. Jesenji režim nege kože - vodič za jesen
`https://sensiskinstudio.com/jesenji-rezim-nege/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Jesenji režim nege kože - vodič za jesen",
  "description": "Kako prilagoditi rutinu nege kože jesenjem periodu? SPF, retinol, hidratacija i tretmani preporučeni za jesen.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/09/IMG-4180-scaled-1.jpg",
  "datePublished": "2022-09-19T12:28:02+00:00",
  "dateModified": "2026-06-10T23:00:04+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/jesenji-rezim-nege/" }
}
```

### 8. Koraci unapredjene nege lica - serumi, maske, piling
`https://sensiskinstudio.com/koraci-unapredjene-nege-lica/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Koraci unapredjene nege lica - serumi, maske, piling",
  "description": "Dodajte serume, maske i piling u svoju rutinu nege lica. Vodič za pravilnu primenu i redosled preparata.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2023/03/IMG_9560-scaled-1.jpg",
  "datePublished": "2023-03-24T21:42:09+00:00",
  "dateModified": "2026-06-10T22:50:58+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/koraci-unapredjene-nege-lica/" }
}
```

### 9. Leto i promene na koži - prva pomoć i tretmani
`https://sensiskinstudio.com/leto-i-promene-na-kozi/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Leto i promene na koži - prva pomoć i tretmani",
  "description": "Kako sunce menja kožu i koji tretmani pomažu obnovi kože posle letovanja? LED terapija, Mesojet i Karboksi terapija.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2024/08/Common-summer-skin-problems-and-how-to-treat-them-mobilehome.jpg.webp",
  "datePublished": "2024-08-02T15:11:51+00:00",
  "dateModified": "2026-06-10T22:46:35+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/leto-i-promene-na-kozi/" }
}
```

### 10. Melazma - uzroci, simptomi i tretman
`https://sensiskinstudio.com/melazma/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Melazma - uzroci, simptomi i tretman",
  "description": "Šta je melazma, kako nastaje i kako se leči? Stručni saveti i pregled profesionalnih tretmana za hiperpigmentaciju kože.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/09/hiperpigment-600x460-2.jpg",
  "datePublished": "2022-09-24T17:19:37+00:00",
  "dateModified": "2026-06-10T22:42:58+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/melazma/" }
}
```

### 11. Menopauza i nega kože - promene i rešenja
`https://sensiskinstudio.com/menopauza-i-pravilna-nega-koze/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Menopauza i nega kože - promene i rešenja",
  "description": "Kako menopauza utiče na kožu i koji su pravi kozmetički preparati i tretmani za žene u menopauzi?",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/06/beautiful-middle-aged-woman-posing-lingerie-body-positive-beauty-photoshooting-scaled-1.jpg",
  "datePublished": "2022-06-20T09:57:50+00:00",
  "dateModified": "2026-06-10T23:06:29+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/menopauza-i-pravilna-nega-koze/" }
}
```

### 12. Nega lica: šta je do kozmetičara, a šta do vas?
`https://sensiskinstudio.com/nega-lica-sta-je-u-rukama-kozmeticara-a-sta-je-do-vas/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Nega lica: šta je do kozmetičara, a šta do vas?",
  "description": "Koji deo nege kože obezbeđuje kozmetičar, a šta je vaša odgovornost? Saveti o peškiru, šminci i higijeni.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/08/IMG-9503-scaled-1.jpg",
  "datePublished": "2022-08-02T19:08:29+00:00",
  "dateModified": "2026-06-10T22:45:02+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/nega-lica-sta-je-u-rukama-kozmeticara-a-sta-je-do-vas/" }
}
```

### 13. Obuzdati se i ne dirati akne - kako to uspeti?
`https://sensiskinstudio.com/obuzdati-se-i-ne-dirati-akne-kako/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Obuzdati se i ne dirati akne - kako to uspeti?",
  "description": "Zašto je diranje akni štetno i šta da radite umesto toga? Saveti i SOS gel kao rešenje za problematičnu kožu.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2023/01/kako-ne-dirati-akne-001.jpg",
  "datePublished": "2023-01-17T10:15:37+00:00",
  "dateModified": "2026-06-10T22:53:09+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/obuzdati-se-i-ne-dirati-akne-kako/" }
}
```

### 14. Osnovna beauty rutina - jutarnja i večernja nega
`https://sensiskinstudio.com/osnovni-koraci-svakodnevne-beauty-rutine/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Osnovna beauty rutina - jutarnja i večernja nega",
  "description": "Koji su obavezni koraci jutarnje i večernje nege lica? Stručni vodič za osnovu koja daje vidljive rezultate.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/09/IMG-9576-scaled-1.jpg",
  "datePublished": "2023-03-21T09:26:09+00:00",
  "dateModified": "2026-06-10T22:51:45+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/osnovni-koraci-svakodnevne-beauty-rutine/" }
}
```

### 15. Perutanje kože - uzroci i rešenja
`https://sensiskinstudio.com/perutanje-koze/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Perutanje kože - uzroci i rešenja",
  "description": "Najčešći uzroci perutanja kože i efikasna rešenja za kućnu negu i profesionalne tretmane u Sensi Skin.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/10/dry-cosmetic-makeup-powder-is-female-face-beauty-treatment-concept-girl-makes-makeup-1-scaled-1.jpg",
  "datePublished": "2022-10-31T12:58:50+00:00",
  "dateModified": "2026-06-10T22:57:49+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/perutanje-koze/" }
}
```

### 16. Osetljivost kože zimi - uzroci i tretmani
`https://sensiskinstudio.com/pojava-osetljivosti-koze-tokom-zimskih-dana/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Osetljivost kože zimi - uzroci i tretmani",
  "description": "Koji su znaci zimske osetljivosti kože, šta odmah uraditi i koji profesionalni tretmani vraćaju kožnu barijeru? Saveti Sensi Skin.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/12/pojava-osetljivosti-koze-tokom-zimskih-dana-001.jpg",
  "datePublished": "2022-12-28T07:48:59+00:00",
  "dateModified": "2026-06-10T22:56:21+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/pojava-osetljivosti-koze-tokom-zimskih-dana/" }
}
```

### 17. Posledice starenja na koži - prevencija i tretmani
`https://sensiskinstudio.com/posledice-starenja-na-kozi/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Posledice starenja na koži - prevencija i tretmani",
  "description": "Koji su prvi znaci starenja kože i koji tretmani ih usporavaju? Stručni vodič Sensi Skin centra za anti-age negu.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2023/11/paketi-jesen-zima-001.jpg",
  "datePublished": "2024-01-10T09:08:44+00:00",
  "dateModified": "2026-06-10T22:47:32+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/posledice-starenja-na-kozi/" }
}
```

### 18. Pravilna dnevna rutina za negu kože lica
`https://sensiskinstudio.com/pravilna-dnevna-rutina-za-negu-koze-lica/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Pravilna dnevna rutina za negu kože lica",
  "description": "Koji su koraci pravilne dnevne rutine za negu kože lica? Čišćenje, serum, krema i profesionalni tretmani.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/06/pexels-ron-lach-8131568-scaled-1.jpg",
  "datePublished": "2022-06-09T12:07:52+00:00",
  "dateModified": "2026-06-10T23:08:19+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/pravilna-dnevna-rutina-za-negu-koze-lica/" }
}
```

### 19. Nega predela oko očiju - koža kapaka i podočnjaci
`https://sensiskinstudio.com/predeo-oko-ociju-kako-negovati-ovu-osetljvu-regiju/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Nega predela oko očiju - koža kapaka i podočnjaci",
  "description": "Kako negovati osetljivu kožu oko očiju? Uzroci podočnjaka, pravi preparati i profesionalni tretmani.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/07/close-up-beauty-portrait-topless-woman-with-perfect-skin-natural-make-up-with-anti-aging-cream-dots-moisturize-firm-skin-eyes-scaled-1.jpg",
  "datePublished": "2022-07-18T11:24:02+00:00",
  "dateModified": "2026-06-10T23:05:29+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/predeo-oko-ociju-kako-negovati-ovu-osetljvu-regiju/" }
}
```

### 20. Promene na koži od sunca - fleke i hiperpigmentacija
`https://sensiskinstudio.com/promene-na-kozi-kao-posledica-suncanja/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Promene na koži od sunca - fleke i hiperpigmentacija",
  "description": "Kako sunce uzrokuje hiperpigmentaciju i fleke na licu? Uzroci, tipovi i efikasni tretmani za uklanjanje.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/08/IMG-9442-scaled-1.jpg",
  "datePublished": "2022-08-22T13:58:14+00:00",
  "dateModified": "2026-06-10T23:03:14+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/promene-na-kozi-kao-posledica-suncanja/" }
}
```

### 21. Prva pomoć koži u hladnim danima - zimska nega
`https://sensiskinstudio.com/prva-pomoc-kozi-u-hladnim-danima/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Prva pomoć koži u hladnim danima - zimska nega",
  "description": "Kako obnoviti kožnu barijeru tokom zime? Korak-po-korak vodič za hladne dane i preporučeni tretmani u Sensi Skin.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2023/12/5A5A5087-Edit-scaled-1.jpg",
  "datePublished": "2023-12-04T15:33:34+00:00",
  "dateModified": "2026-06-10T22:48:29+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/prva-pomoc-kozi-u-hladnim-danima/" }
}
```

### 22. Rozacea - simptomi, uzroci i nega kože
`https://sensiskinstudio.com/rozacea-kako-da-ublazite-simptome/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Rozacea - simptomi, uzroci i nega kože",
  "description": "Šta je rozacea, koji su simptomi i kako da ublažite crvenilo i iritaciju? Stručni saveti i profesionalni tretmani.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/09/closeup-view-eye-cheek-young-woman-suffering-from-red-blotchy-cheeks-blushing-caucasian-girl-with-green-teal-eyes-copy-space-left-1-scaled-1.jpg",
  "datePublished": "2022-09-09T11:26:34+00:00",
  "dateModified": "2026-06-10T23:01:43+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/rozacea-kako-da-ublazite-simptome/" }
}
```

### 23. Sinergija estetskih procedura i tretmana lica
`https://sensiskinstudio.com/sinergija-estetskih-procedura-i-tretmana-lica/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Sinergija estetskih procedura i tretmana lica",
  "description": "Kako kombinovati injekcione estetske procedure sa tretmanima lica? Šta se sme, šta ne i koliko treba čekati.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2023/05/IMG-9471-scaled-1.jpg",
  "datePublished": "2023-05-09T17:50:34+00:00",
  "dateModified": "2026-06-10T22:49:14+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/sinergija-estetskih-procedura-i-tretmana-lica/" }
}
```

### 24. Beauty kofer za letovanje - šta spakovati
`https://sensiskinstudio.com/sta-cete-spakovati-u-svoj-beauty-kofer/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Beauty kofer za letovanje - šta spakovati",
  "description": "Koji preparati su neophodni za letnji beauty kofer? Saveti za negu lica, tela i kose na odmoru.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/07/bag-with-cosmetics-copy-space-scaled-1.jpg",
  "datePublished": "2022-07-07T08:25:35+00:00",
  "dateModified": "2026-06-10T23:04:39+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/sta-cete-spakovati-u-svoj-beauty-kofer/" }
}
```

### 25. Štetnost solarijuma - zašto je opasno
`https://sensiskinstudio.com/stetnost-solarijuma/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Štetnost solarijuma - zašto je opasno",
  "description": "Zašto je solarijum štetan za kožu i organizam? UV zračenje, rizik od melanoma i bezbedne alternative.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/06/solarium-g197d97170-1920.jpg",
  "datePublished": "2022-06-14T11:54:12+00:00",
  "dateModified": "2026-06-10T23:07:43+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/stetnost-solarijuma/" }
}
```

### 26. Tipovi i stanje kože - u čemu je razlika?
`https://sensiskinstudio.com/tipovi-i-stanje-koze-u-cemu-je-razlika-i-kako-da-ih-odredite/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Tipovi i stanje kože - u čemu je razlika?",
  "description": "Kako da razlikujete tip kože od stanja kože i zašto je ta razlika važna za pravilnu negu? Stručni vodič.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/08/IMG-9498-1-scaled-1.jpg",
  "datePublished": "2022-08-30T12:12:22+00:00",
  "dateModified": "2026-06-10T23:02:33+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/tipovi-i-stanje-koze-u-cemu-je-razlika-i-kako-da-ih-odredite/" }
}
```

### 27. Tretmani lica pre i posle letovanja - saveti
`https://sensiskinstudio.com/tretmani-lica-sta-primeniti-pre-a-sta-posle-letnjeg-odmora/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Tretmani lica pre i posle letovanja - saveti",
  "description": "Koji tretmani lica su preporučeni pre letovanja i koji posle? Stručni saveti kozmetičara za pripremu i obnovu kože.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/08/IMG-9532-scaled-1.jpg",
  "datePublished": "2022-08-10T10:50:12+00:00",
  "dateModified": "2026-06-10T22:44:23+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/tretmani-lica-sta-primeniti-pre-a-sta-posle-letnjeg-odmora/" }
}
```

### 28. Uticaj kiseonika na kožu - oksigenacija kože
`https://sensiskinstudio.com/uticaj-kiseonika-na-kozu/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Uticaj kiseonika na kožu - oksigenacija kože",
  "description": "Zašto koža stari brže kada joj nedostaje kiseonik i kako CO2 tretman vraća svežinu i sijaj koži.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/11/paket-001.jpg",
  "datePublished": "2023-04-26T17:05:30+00:00",
  "dateModified": "2026-06-10T22:50:15+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/uticaj-kiseonika-na-kozu/" }
}
```

### 29. Vrste akni - tipovi i razlike
`https://sensiskinstudio.com/vrste-akni/`

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Vrste akni - tipovi i razlike",
  "description": "Koje su vrste akni i čime se razlikuju? Od komedona do nodulo-cistične akne - stručni vodič za pravilno tretiranje.",
  "image": "https://sensiskinstudio.com/wp-content/uploads/2022/08/young-woman-with-acne-problem-color-scaled-1.jpg",
  "datePublished": "2022-08-19T09:10:31+00:00",
  "dateModified": "2026-06-10T23:03:56+00:00",
  "author": { "@type": "Person", "name": "Nataša Burka", "url": "https://sensiskinstudio.com/kozmetoloski-centar-sensi-skin/" },
  "publisher": { "@type": "Organization", "name": "Sensi Skin", "logo": { "@type": "ImageObject", "url": "https://sensiskinstudio.com/wp-content/uploads/2026/03/sensi-skin-logo-001.webp" } },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://sensiskinstudio.com/vrste-akni/" }
}
```
