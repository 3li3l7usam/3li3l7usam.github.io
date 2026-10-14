# Ali Alhusam — portfolio website

Static site served by GitHub Pages at https://3li3l7usam.github.io/

- `index.html` — home: selected work, all work, behind the scenes, process and AI toolkit, about, contact
- `work/` — one page per project
- `assets/` — stylesheet, script and images (WebP)
- `_build/` — the generator. Edit `data.py` (projects, feedback quotes, contact) and run
  `python3 gen.py <site folder>` with the images in `<site folder>/assets/img/` and their `meta.json`.

Client feedback stays hidden until the quotes in `data.py` are filled in.
