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
Run from the repo root. It regenerates `index.html`, `work.html` and `work/*.html` and copies `_build/site.css` and
`_build/site.js` into `assets/`. Edit the files in `_build/`, never the generated copies.

- `_build/data.py`: all content (projects, briefs, behind-the-scenes, step-by-step boards in `STEPS`, the home page's
  sketch-to-render strip in `FLOW`, toolkit, process, client logos, feedback, contact)
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
- Home is calm and light (Ali asked for a home that is not loud): a short intro with the name, the portrait and two
  buttons, a "See the work" band, the sketch-to-final process, about and contact. No project grid on the home page.
- The work lives on its own page, `work.html` (filters, all projects, behind-the-scenes canvases); "Work" in the menu
  and the home page buttons lead there.
- Project pages with an entry in `STEPS` show a "Step by step" board: sketch, then generation or 3D, then the final.
  Sketches are crude phone photos of notebook doodles, on purpose.
- Motion: Lenis smooth scroll, reveals on scroll, cursor label on work, page transitions between pages. Everything
  respects `prefers-reduced-motion`. The node canvas code in `site.js` is unused since v4.

## Content rules
- Never write "art director" anywhere.
- No company names in Ali's bio.
- The feedback section stays hidden until real quotes are filled in `FEEDBACK` in `data.py`.
- Contact shows email, phone (Ali chose to keep it public) and Behance; LinkedIn appears once its URL is set in `CONTACT`.

## Still open
- Client feedback quotes (quote, name, title, project).
- LinkedIn URL.
- Behind-the-scenes canvas for Altanfeethi Chauffeur (to be built in Magnific Spaces), then add it as `BTS['AC']`.
- Booth sources: Blender files in Ali's Downloads (`القرية/output/v1`, `شركة الاجور/OUTPUT/Blender/..._v5_FINAL`);
  the outline and clay passes in `Links/22_Booths` were rendered from them.
