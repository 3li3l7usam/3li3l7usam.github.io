# -*- coding: utf-8 -*-
# Static site generator for Ali Alhusam's portfolio website.
# usage: python3 gen.py <out_dir> [--preview]
import sys, os, json, html, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *

OUT = sys.argv[1]
PREVIEW = '--preview' in sys.argv
SRC = os.path.dirname(os.path.abspath(__file__))
META = json.load(open(os.path.join(OUT, 'assets/img/meta.json')))
E = lambda s: html.escape(s, quote=True)
BY = {p['slug']: p for p in PROJECTS}
CATNAME = dict(CATS)
# Astoria (the brand face) comes from Ali's Adobe Fonts web kit 'svo2ffi' (domains: 3li3l7usam.github.io, localhost);
# Alegreya Sans from Google Fonts is only the fallback where the kit is not allowed to load
FONT = '<link rel="preconnect" href="https://use.typekit.net" crossorigin><link rel="stylesheet" href="https://use.typekit.net/svo2ffi.css">' + '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya+Sans:wght@300;400;500;700;800&amp;display=swap">'
LENIS = 'https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js'
# motion is opt-in: scripts add it, reduced-motion users never get it, and it falls away if site.js does not arrive
BOOT = ("<script>(function(d){if(!matchMedia('(prefers-reduced-motion: reduce)').matches)d.classList.add('motion');"
        "setTimeout(function(){if(!window.__aa)d.classList.remove('motion')},3500)})(document.documentElement)</script>")
USED = set()
HERO_IMG = ('hero/portrait.webp', 'hero/portrait.m.webp')

def base(rel): return os.path.splitext(rel)[0]
def full(rel, up=''): USED.add(base(rel) + '.webp'); return up + 'assets/img/' + base(rel) + '.webp'
def thumb(rel, up=''): USED.add(base(rel) + '.t.webp'); return up + 'assets/img/' + base(rel) + '.t.webp'
def size(rel):
    w, h = META[rel]; return w, h
def tsize(rel):
    w, h = size(rel); s = min(1, 760 / max(w, h)); return round(w * s), round(h * s)
def is_plate(p, rel):
    return p.get('plate') or any(k in rel for k in ('RM_Wordmark', 'ND_Sticker', 'RQ_Logo'))
def split(text):
    """words wrapped for the line-by-line rise; the heading keeps its plain text for assistive tech"""
    return ' '.join(f'<span class="w"><span style="--i: {i}">{E(w)}</span></span>' for i, w in enumerate(text.split()))
def vt(slug): return f'view-transition-name: p-{slug}'

def head(title, desc, up=''):
    return (f'<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            f'<title>{E(title)}</title><meta name="claude:viewport-fit-sides" content="cover"><meta name="description" content="{E(desc)}">'
            f'<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta name="theme-color" content="#231F20">'
            f'{BOOT}{FONT}<link rel="stylesheet" href="{up}assets/site.css">')

def site_header(up=''):
    home = up + 'index.html' if up else ''
    links = [('Work', '#work'), ('Behind the scenes', '#bts'), ('Process', '#process'), ('About', '#about'), ('Contact', '#contact')]
    nav = ''.join(f'<a href="{home}{h}">{t}</a>' for t, h in links)
    return (f'<div id="top"></div><a class="skip" href="#main">Skip to content</a><header class="site-head"><div class="wrap">'
            f'<a class="brand" href="{up}index.html">Ali Alhusam</a><nav class="nav" aria-label="Sections">{nav}</nav></div>'
            f'<span class="progress" aria-hidden="true"></span></header>')

def contact_band():
    c = CONTACT
    items = [f'<li class="rv" style="--d: 0"><small>Email</small><div class="val">{E(c["email"])}</div><button class="copy" type="button" data-copy="{E(c["email"])}">Copy email</button></li>',
             f'<li class="rv" style="--d: 1"><small>Phone</small><div class="val">{E(c["phone"])}</div><button class="copy" type="button" data-copy="{E(c["phone"])}">Copy number</button></li>',
             f'<li class="rv" style="--d: 2"><small>Behance</small><div class="val"><a href="{c["behance"]}" target="_blank" rel="noopener">behance.net/3li3l7usam</a></div></li>']
    if c.get('linkedin'):
        items.append(f'<li class="rv" style="--d: 3"><small>LinkedIn</small><div class="val"><a href="{c["linkedin"]}" target="_blank" rel="noopener">Ali Alhusam</a></div></li>')
    return (f'<section class="contact" id="contact" aria-labelledby="contact-h"><div class="wrap"><span class="mark" aria-hidden="true"></span>'
            f'<h2 id="contact-h" class="split" aria-label="Let’s create what’s next.">{split("Let’s create what’s next.")}</h2><ul class="contact-list">{"".join(items)}</ul></div></section>'
            f'<footer class="site-foot"><div class="wrap"><span>© 2026 Ali Alhusam</span><span>Senior graphic designer</span><a class="to-top" href="#top">Back to top</a></div></footer>')

LIGHTBOX = ('<dialog class="lb" id="lb" aria-label="Image viewer"><div class="lb-inner"><img alt="">'
            '<div class="lb-bar"><span class="lb-count"></span><div><button class="prev" type="button">Previous</button>'
            '<button class="next-img" type="button">Next</button><button class="close" type="button">Close</button></div></div></div></dialog>')

def doc(title, desc, body, up='', preview_page=False, cls=''):
    scripts = f'<script src="{LENIS}" defer></script><script src="{up}assets/site.js" defer></script>'
    if preview_page:  # artifact page: the publisher adds the document skeleton, so the body class is set by script
        return head(title, desc, up) + f'<script>document.body.className="{cls}"</script>' + body + scripts
    return (f'<!doctype html><html lang="en"><head>{head(title, desc, up)}</head><body class="{cls}">{body}{scripts}</body></html>')

def window(rel, label, up='', alt=''):
    w, h = size(rel)
    return (f'<div class="window"><div class="window-bar"><i></i><i></i><i></i><span>{E(label)}</span></div>'
            f'<div class="pane"><img src="{full(rel, up)}" width="{w}" height="{h}" alt="{E(alt)}" loading="lazy" data-full="{full(rel, up)}"></div></div>')

def section_head(id_, title, text, extra=''):
    return (f'<div class="section-head"><h2 id="{id_}" class="split" aria-label="{E(title)}">{split(title)}</h2>'
            f'<div class="rv"><p>{text}</p>{extra}</div></div>')

# ------------------------------------------------------------------ home
NODES = [('national-day-96', '1 / span 6', '0px', '02_National_Day_96/ND_Screen_Wide_Triple.jpg', '16 / 9'),
         ('altanfeethi-chauffeur', '8 / span 3', '72px', '01_Altanfeethi_Chauffeur/AC_Rome.jpg', '1 / 1'),
         ('electricity-friend', '2 / span 4', '24px', '19_Saudi_Energy/SE_Poster_Be_The_Hero.jpg', '3 / 4'),
         ('saudifood-show-2026', '7 / span 6', '0px', '03_Saudifood_2026/mockups_hd/SF_Final_VIP_Wall.jpg', '16 / 9'),
         ('campaign-key-visuals', '1 / span 4', '40px', '13_Social_Media/SM_Watan_Story.jpg', '1 / 1'),
         ('ramadan-1447', '6 / span 3', '0px', '04_Ramadan_1447/RM_Greeting_Minister.jpg', '4 / 5'),
         ('new-horizons', '9 / span 4', '96px', '12_Presentations/PR_Mockup_Horizons.jpg', '16 / 9')]

def name_markup():
    out, i = [], 0
    for word in ('Ali', 'Alhusam'):
        chars = ''
        for ch in word:
            chars += f'<span class="ch" style="--i: {i}">{ch}</span>'; i += 1
        out.append(f'<span class="name-line">{chars}</span>')
    return ' '.join(out)

def home():
    big, small = HERO_IMG
    USED.update(HERO_IMG)
    hero = (f'<section class="hero" aria-label="Introduction"><div class="hero-stage"><div class="hero-dots" aria-hidden="true"></div>'
            f'<h1 class="name" aria-label="Ali Alhusam">{name_markup()}</h1>'
            f'<figure class="portrait"><img src="assets/img/{big}" srcset="assets/img/{small} 630w, assets/img/{big} 1099w" sizes="(max-width: 700px) 100vw, 52vh" '
            f'width="1099" height="1500" alt="Portrait of Ali Alhusam" fetchpriority="high" draggable="false"></figure>'
            f'<div class="name-front" aria-hidden="true"><div class="name">{name_markup()}</div></div>'
            f'</div>'
            f'<div class="hero-foot wrap"><p class="lede">Senior graphic designer. <span>Brand identity, campaigns and AI-driven visuals for government entities and leading enterprises, since 2018.</span></p>'
            f'</div></section>')
    nodes = ''
    for i, (slug, col, mt, rel, ar) in enumerate(NODES):
        p = BY[slug]
        nodes += (f'<a class="node" href="work/{slug}.html" draggable="false" data-cursor="Open" style="--col: {col}; --mt: {mt}; --i: {i}">'
                  f'<span class="port in" aria-hidden="true"></span><span class="port out" aria-hidden="true"></span>'
                  f'<span class="node-head"><b>{E(p["title"])}</b><small>{E(p["client"].split(",")[0])}</small></span>'
                  f'<span class="shot"><img src="{thumb(rel)}" srcset="{thumb(rel)} 760w, {full(rel)} 2000w" sizes="(max-width: 900px) 100vw, 50vw" alt="" style="aspect-ratio: {ar}" loading="lazy" draggable="false"></span></a>')
    selected = (f'<section class="section wrap" id="selected" aria-labelledby="sel-h">'
                + section_head('sel-h', 'Selected work', 'Seven projects for MODON, Saudi Energy, the Ministry of Industry and Altanfeethi, linked the way they move on a Magnific Spaces canvas.',
                               '<p class="hint">Drag the nodes. The wires follow.</p>')
                + f'<div class="canvas"><svg class="wires" aria-hidden="true"></svg>{nodes}</div></section>')
    counts = {k: sum(1 for p in PROJECTS if p['cat'] == k) for k, _ in CATS}
    chips = f'<button class="chip" type="button" data-cat="all" aria-pressed="true">All<span>{len(PROJECTS)}</span></button>' + ''.join(
        f'<button class="chip" type="button" data-cat="{k}" aria-pressed="false">{E(n)}<span>{counts[k]}</span></button>' for k, n in CATS)
    cards = ''
    for i, p in enumerate(PROJECTS):
        tw, th = tsize(p['cover'])
        ai = '<span class="ai">AI</span>' if p.get('ai') else ''
        cards += (f'<a class="card rv{" plate" if p.get("plate") else ""}" href="work/{p["slug"]}.html" data-cat="{p["cat"]}" data-cursor="View" style="--d: {i % 5}">'
                  f'<span class="shot"><img src="{thumb(p["cover"])}" width="{tw}" height="{th}" alt="" loading="lazy" style="{vt(p["slug"])}"></span>'
                  f'<span><b>{E(p["title"])}</b>{ai}<small>{E(p["client"])}</small></span></a>')
    work = (f'<section class="section wrap" id="work" aria-labelledby="work-h">'
            + section_head('work-h', 'All work', 'Campaigns, event themes, presentations and social content, plus earlier identity, editorial and packaging work.')
            + f'<div class="filters rv" role="group" aria-label="Filter projects">{chips}</div><div class="grid">{cards}</div></section>')
    figs = ''
    for i, (key, slug) in enumerate((('ND', 'national-day-96'), ('SE', 'electricity-friend'), ('SF', 'saudifood-show-2026'))):
        b = BTS[key]; p = BY[slug]
        figs += (f'<figure class="rv" style="--d: {i}">{window(b["img"], b["window"], alt="Magnific Spaces canvas for " + p["title"])}'
                 f'<figcaption><span>{E(b["title"])}. {E(b["steps"][1][1])}</span><a href="work/{slug}.html">See {E(p["title"])}</a></figcaption></figure>')
    bts = (f'<section class="section wrap" id="bts" aria-labelledby="bts-h">'
           + section_head('bts-h', 'Behind the scenes', 'The real canvases: references, generations and finished designs side by side, the way each campaign was built in Magnific Spaces.')
           + f'<div class="bts-grid">{figs}</div></section>')
    steps = ''.join(f'<li class="rv" style="--d: {i + 2}"><h3>{E(t)}</h3><p class="tools">{E(tools)}</p><p>{E(d)}</p></li>' for i, (t, tools, d) in enumerate(PROCESS))
    kit = ''.join(f'<div class="rv" style="--d: {i}"><dt>{E(stage)}</dt><dd><b>{E(tools)}</b><span>{E(d)}</span></dd></div>' for i, (stage, tools, d) in enumerate(TOOLKIT))
    process = (f'<section class="section wrap" id="process" aria-labelledby="proc-h">'
               + section_head('proc-h', 'How I work with AI', 'Five steps and one rule: AI speeds up the making, never the thinking. Every image is directed, chosen and finished by hand.')
               + f'<ol class="steps">{steps}</ol><dl class="toolkit" aria-label="Toolkit by stage">{kit}</dl></section>')
    def logo(n, hidden=False):
        w, h = size('00_Clients/' + n + '.png')
        alt = '' if hidden else E(n.replace('_white', '').replace('_', ' ').title())
        return f'<img src="{full("00_Clients/" + n + ".png")}" alt="{alt}" loading="lazy" width="{w}" height="{h}">'
    sets = (f'<div class="marquee-set">{"".join(logo(n) for n in CLIENT_LOGOS)}</div>'
            f'<div class="marquee-set" aria-hidden="true">{"".join(logo(n, True) for n in CLIENT_LOGOS)}</div>')
    about = (f'<section class="section wrap" id="about" aria-labelledby="about-h">'
             f'<div class="section-head"><h2 id="about-h" class="split" aria-label="About">{split("About")}</h2><p></p></div>'
             f'<div class="about"><p class="bio rv">I design identities, campaigns and presentations for government entities and leading enterprises in Saudi Arabia. '
             f'I bring AI into every stage of the work, from the first idea to the final file, so campaign visuals arrive faster without losing control of the brand.</p>'
             f'<p class="since rv" style="--d: 2">Designing since<b>2018</b></p></div>'
             f'<div class="marquee rv" aria-label="Selected clients"><div class="marquee-track">{sets}</div></div></section>')
    filled = [f for f in FEEDBACK if f['quote'].strip()]
    fb = ''
    if filled or PREVIEW:
        items = filled or FEEDBACK
        figs = ''
        for i, f in enumerate(items):
            ph = not f['quote'].strip()
            q = f['quote'] or 'Client quote goes here: one or two sentences on the result and on working together.'
            who = f['name'] or 'Name'
            role = f['role'] or 'Title, organisation'
            figs += (f'<figure class="rv {"placeholder" if ph else ""}" style="--d: {i}"><blockquote>{E(q)}</blockquote>'
                     f'<figcaption><b>{E(who)}</b>{E(role)}, {E(f["project"])}</figcaption></figure>')
        note = 'Placeholders for now. This section stays hidden on the live site until the quotes are in.' if not filled else ''
        fb = (f'<section class="section wrap" id="feedback" aria-labelledby="fb-h">' + section_head('fb-h', 'In their words', note)
              + f'<div class="quotes">{figs}</div></section>')
    body = site_header() + f'<main id="main">{hero}{selected}{work}{bts}{process}{about}{fb}</main>' + contact_band() + LIGHTBOX + '<div class="cursor" aria-hidden="true"><span></span></div>'
    desc = 'Portfolio of Ali Alhusam, senior graphic designer: campaigns, event themes, presentations and AI-driven visuals for MODON, Saudi Energy, the Ministry of Industry and Altanfeethi.'
    return doc('Ali Alhusam', desc, body, cls='home'), doc('Ali Alhusam', desc, body, preview_page=True, cls='home')

# ------------------------------------------------------------------ project pages
def rows(images, plate=lambda rel: False, target=3.3):
    out, cur, s = [], [], 0
    for rel in images:
        w, h = size(rel); ar = 1.6 if plate(rel) else w / h  # marks sit on a fixed 16:10 plate
        if ar >= 2.2:
            if cur: out.append((cur, s)); cur, s = [], 0
            out.append(([(rel, ar)], ar)); continue
        cur.append((rel, ar)); s += ar
        if s >= target: out.append((cur, s)); cur, s = [], 0
    if cur: out.append((cur, s))
    return out

def project(i):
    p = PROJECTS[i]; up = '../'
    facts = ''.join(f'<div><dt>{E(k)}</dt><dd>{E(v)}</dd></div>' for k, v in p['facts'])
    top = (f'<div class="wrap"><nav class="crumbs rv" aria-label="Breadcrumb"><a href="../index.html#work">All work</a> / {E(CATNAME[p["cat"]])}</nav>'
           f'<header class="p-head"><h1 class="split" aria-label="{E(p["title"])}">{split(p["title"])}</h1><p class="sub rv" style="--d: 3">{E(p["sub"])}</p></header>'
           f'<div class="p-intro"><p class="summary rv" style="--d: 4">{E(p["summary"])}</p><dl class="facts rv" style="--d: 5">{facts}</dl></div>')
    named = False
    if p.get('hero'):
        w, h = size(p['hero'])
        top += (f'<figure class="p-hero"><img src="{full(p["hero"], up)}" width="{w}" height="{h}" alt="{E(p["title"])}, key visual" '
                f'data-full="{full(p["hero"], up)}" style="{vt(p["slug"])}"></figure>')
        named = True
    brief = ''
    if p.get('brief'):
        hd, obj, idea, vd = BRIEFS[p['brief']]
        brief = (f'<section class="brief" aria-labelledby="brief-h"><h2 id="brief-h" class="split" aria-label="{E(hd)}">{split(hd)}</h2><dl>'
                 f'<div class="rv" style="--d: 1"><dt>The objective</dt><dd>{E(obj)}</dd></div><div class="rv" style="--d: 2"><dt>The idea</dt><dd>{E(idea)}</dd></div>'
                 f'<div class="rv" style="--d: 3"><dt>Visual direction</dt><dd>{E(vd)}</dd></div></dl></section>')
    gal = ''
    n = 0
    for items, s in rows([r for r in p['images'] if r != p.get('hero')], lambda rel: is_plate(p, rel)):
        figs = ''
        for k, (rel, ar) in enumerate(items):
            n += 1
            w, h = size(rel)
            style = '' if named else f' style="{vt(p["slug"])}"'
            cls = ' '.join(c for c in (('plate' if is_plate(p, rel) else ''), ('wide' if ar >= 1.2 else ''), ('' if not named else 'rv-img')) if c)
            named = True
            figs += (f'<figure class="{cls}" style="flex: {ar:.4f} 1 0%; aspect-ratio: {ar:.4f}; --d: {k}">'
                     f'<img src="{thumb(rel, up)}" srcset="{thumb(rel, up)} 760w, {full(rel, up)} 2000w" sizes="(max-width: 700px) 50vw, 40vw" '
                     f'width="{w}" height="{h}" alt="{E(p["title"])}, image {n}" loading="lazy" data-full="{full(rel, up)}"{style}></figure>')
        if s < 3.25 and not (len(items) == 1 and items[0][1] >= 2.2):  # short row: keep its height, leave the rest empty
            figs += f'<span class="spacer" style="flex: {max(3.3 - s, 0.01):.4f} 1 0%"></span>'
        gal += f'<div class="g-row">{figs}</div>'
    gallery = f'<section class="gallery" aria-label="Project images">{gal}</section>'
    bts = ''
    if p.get('bts'):
        b = BTS[p['bts']]
        steps = ''.join(f'<li><b>{E(t)}</b><span>{E(d)}</span></li>' for t, d in b['steps'])
        bts = (f'<section class="p-bts" aria-labelledby="pbts-h"><div class="rv">{window(b["img"], b["window"], up, "Magnific Spaces canvas for " + p["title"])}</div>'
               f'<div class="rv" style="--d: 2"><p class="label">Behind the scenes</p><h2 id="pbts-h">{E(b["title"])}</h2><ol>{steps}</ol></div></section>')
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    nav = (f'<a class="next" href="{nxt["slug"]}.html" data-cursor="Next"><small><span>Next project</span><span>{(i + 2 - 1) % len(PROJECTS) + 1:02d} / {len(PROJECTS)}</span></small>'
           f'<b>{E(nxt["title"])}</b><img class="peek" src="{thumb(nxt["cover"], up)}" alt="" loading="lazy"></a></div>')
    body = site_header(up) + f'<main id="main" class="page">{top}{brief}{gallery}{bts}{nav}</main>{LIGHTBOX}' + contact_band() + '<div class="cursor" aria-hidden="true"><span></span></div>'
    return doc(f'{p["title"]} · Ali Alhusam', p['summary'], body, up, cls='project')

# ------------------------------------------------------------------ write
os.makedirs(os.path.join(OUT, 'work'), exist_ok=True)
idx, idx_prev = home()
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(idx)
if PREVIEW: open(os.path.join(OUT, '_preview_page.html'), 'w', encoding='utf-8').write(idx_prev)
for i, p in enumerate(PROJECTS):
    open(os.path.join(OUT, 'work', p['slug'] + '.html'), 'w', encoding='utf-8').write(project(i))
shutil.copy(os.path.join(SRC, 'site.css'), os.path.join(OUT, 'assets/site.css'))
shutil.copy(os.path.join(SRC, 'site.js'), os.path.join(OUT, 'assets/site.js'))
json.dump(sorted(USED), open(os.path.join(OUT, '_used.json'), 'w'), indent=0)
missing = [u for u in USED if not os.path.exists(os.path.join(OUT, 'assets/img', u))]
print('pages', 1 + len(PROJECTS), 'images used', len(USED), 'missing', missing)
