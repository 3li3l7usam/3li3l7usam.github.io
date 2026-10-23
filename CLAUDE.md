# Ali Alhusam — portfolio website

Static portfolio site for Ali Alhusam, senior graphic designer (Saudi Arabia). Served by GitHub Pages from
`main` / root at https://3li3l7usam.github.io. Every push to `main` goes live within a minute or two.

## Working with Ali
- Ali writes in Arabic. Reply in Arabic.
- Ask before pushing to `main`: a push publishes to the public site.
- Never overwrite his originals on his Mac; save new versions instead.

## Build
```
python3 _build/gen.py .
```
Run from the repo root. It regenerates `index.html` and `work/*.html` and copies `_build/site.css` and
`_build/site.js` into `assets/`. Edit the files in `_build/`, never the generated copies.

- `_build/data.py`: all content (projects, briefs, behind-the-scenes, toolkit, process, client logos, feedback, contact)
- `_build/gen.py`: page templates and the gallery row layout
- `_build/site.css`, `_build/site.js`: styles and motion
- `assets/img/<folder>/<name>.webp` (full, max 2000 px) and `<name>.t.webp` (thumbnail, max 760 px);
  `assets/img/meta.json` holds every image's full size, keyed by its original path (`.jpg`/`.png`)
- `assets/img/hero/portrait*.webp`: the hero cutout (source: `Website_Photo/Ali_Alhusam_Website_Final.png` on Ali's Mac)

To add a project: export the images as above (both sizes) and add their sizes to `meta.json`, then add an entry
to `PROJECTS` in `data.py` and rebuild. The source images live on Ali's Mac in the portfolio's `Links/` folder;
`_work/web_assets.py` there produced the webp files and `meta.json`.

## Design rules
- One dark brand world: ink `#231F20`, white, lime `#D9F478` (lime only for connections, focus and the contact band).
- Type: Astoria from Ali's Adobe Fonts web kit `svo2ffi` (domains: 3li3l7usam.github.io, localhost), with Alegreya Sans
  as fallback. Never commit Astoria font files: the designer's licence (Alan Meeks) forbids redistributing them.
- Hero: name in two lines on the left, portrait on the right; the end of the surname slips behind the shoulder and
  continues as an outline (a masked copy of the name). The portrait stays a sensible size, never the largest element.
- Motion: Lenis smooth scroll, reveals on scroll, the Magnific-style node canvas (wires draw, signals travel, nodes
  drag), cursor label on work, page transitions between pages. Everything respects `prefers-reduced-motion`.

## Content rules
- Never write "art director" anywhere.
- No company names in Ali's bio.
- The feedback section stays hidden until real quotes are filled in `FEEDBACK` in `data.py`.
- Contact shows email, phone (Ali chose to keep it public) and Behance; LinkedIn appears once its URL is set in `CONTACT`.

## Still open
- Client feedback quotes (quote, name, title, project).
- LinkedIn URL.
- Behind-the-scenes canvas for Altanfeethi Chauffeur (to be built in Magnific Spaces), then add it as `BTS['AC']`.
- Link the site from the short printed profile (N2), which is built separately on Ali's Mac.
