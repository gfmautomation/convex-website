"""Build the Convex draft site.

Outputs:
  ../site/          plain multi-page static site (drop-in replacement for the current GitHub Pages repo)
  ../preview.html   single-file clickable preview of every page (for review and sharing)
Run:  python3 build.py
"""
import base64
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from common import APP_LOGIN, APP_REGISTER, SITE, strip_tags  # noqa: E402
import pages_main, pages_types, pages_misc  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = ROOT
TERMS_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "terms-source.html")

PAGES = (pages_main.PAGES + pages_types.PAGES
         + [pages_misc.PRICING, pages_misc.FAQ, pages_misc.CONTACT, pages_misc.terms_page(TERMS_SRC), pages_misc.NOTFOUND])

NAV = [("how-it-works.html", "How it works", "how"),
       ("contracts-we-review.html", "Contracts", "contracts"),
       ("purchaser-profiles.html", "Purchaser lenses", "lens"),
       ("why-convex.html", "Why Convex", "why"),
       ("pricing.html", "Pricing", "pricing"),
       ("faq.html", "FAQs", "faq")]

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">')


def header(active):
    cur = ' aria-current="page"'
    links = "".join(
        f'<li><a href="{h}" data-nav="{k}"{cur if k == active else ""}>{t}</a></li>' for h, t, k in NAV)
    return f'''<header class="header"><div class="wrap nav">
<a class="logo" href="index.html" aria-label="Convex home"><img src="convex_logo.png" alt="Convex" width="520" height="380"></a>
<button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links"><span></span><span></span><span></span></button>
<ul class="nav-links" id="nav-links">{links}
<li><a class="btn btn-sm btn-ghost-light" href="{APP_LOGIN}">Sign in</a></li>
<li><a class="btn btn-sm" href="{APP_REGISTER}">Start trial</a></li></ul>
</div></header>'''


FOOTER = f'''<footer class="footer"><div class="wrap">
<div class="footer-grid">
  <div><img src="convex_logo.png" alt="Convex" width="520" height="380"><p>Review Smarter. Close Faster.</p>
  <p style="margin-top:.8rem">AI contract review for NSW conveyancers and property lawyers.</p></div>
  <div><h4>Product</h4><ul><li><a href="how-it-works.html">How it works</a></li><li><a href="purchaser-profiles.html">Purchaser lenses</a></li>
  <li><a href="why-convex.html">Why Convex</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="faq.html">FAQs</a></li></ul></div>
  <div><h4>Contracts</h4><ul><li><a href="nsw-residential-contract-review.html">Residential</a></li><li><a href="strata-contract-review.html">Strata</a></li>
  <li><a href="off-the-plan-contract-review.html">Off-the-plan</a></li><li><a href="unregistered-land-contract-review.html">Unregistered land</a></li>
  <li><a href="house-and-land-contract-review.html">House and land</a></li><li><a href="commercial-contract-review.html">Commercial</a></li></ul></div>
  <div><h4>Contact</h4><ul><li><a href="contact.html">Book a demo</a></li><li><a href="mailto:info@convex.au">info@convex.au</a></li>
  <li><a href="tel:+61406522627">0406 522 627</a></li><li><a href="{APP_LOGIN}">Sign in</a></li></ul></div>
</div>
<div class="footer-bottom"><p>&copy; 2026 Convex Legal Pty Ltd ABN 87 692 237 577. Convex is a support tool for legal professionals and does not provide legal advice.</p>
<p><a href="terms-and-conditions.html">Terms and conditions</a></p></div>
</div></footer>'''


def url_of(p):
    return SITE + "/" + ("" if p["file"] == "index.html" else p["file"])


def schema(p):
    blocks = []
    if p["file"] == "index.html":
        blocks.append({"@context": "https://schema.org", "@type": "Organization", "name": "Convex",
                       "legalName": "Convex Legal Pty Ltd", "url": SITE + "/", "logo": SITE + "/convex_logo.png",
                       "email": "info@convex.au", "telephone": "+61406522627", "areaServed": "New South Wales, Australia"})
        blocks.append({"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Convex",
                       "applicationCategory": "BusinessApplication", "operatingSystem": "Web",
                       "description": p["desc"], "url": SITE + "/",
                       "offers": {"@type": "AggregateOffer", "priceCurrency": "AUD", "lowPrice": "145", "highPrice": "1495", "offerCount": "3"}})
    elif p["file"] != "404.html":
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
        if p.get("parent"):
            items.append({"@type": "ListItem", "position": 2, "name": p["parent"][1], "item": SITE + "/" + p["parent"][0]})
        items.append({"@type": "ListItem", "position": len(items) + 1, "name": p.get("crumb", p["title"]), "item": url_of(p)})
        blocks.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})
    if p.get("faqs"):
        blocks.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in p["faqs"]]})
    return "".join(f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>' for b in blocks)


def clean(s):
    return s.replace("—", "-").replace("–", "-")


def render(p):
    robots = '<meta name="robots" content="noindex">' if p.get("noindex") else ""
    return clean(f'''<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p["title"]}</title>
<meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{url_of(p)}">{robots}
<meta property="og:type" content="website"><meta property="og:site_name" content="Convex">
<meta property="og:title" content="{p["title"]}"><meta property="og:description" content="{p["desc"]}">
<meta property="og:url" content="{url_of(p)}"><meta property="og:image" content="{SITE}/convex_logo.png">
<meta name="twitter:card" content="summary">
<link rel="icon" type="image/png" href="favicon.png">
{FONTS}
<link rel="stylesheet" href="styles.css">
{schema(p)}
</head>
<body>
{header(p["nav"])}
<main id="main">{p["body"]}</main>
{FOOTER}
<script src="main.js"></script>
</body>
</html>
''')


def build_site():
    for p in PAGES:
        with open(os.path.join(OUT, p["file"]), "w", encoding="utf-8") as f:
            f.write(render(p))
    urls = "".join(f"<url><loc>{url_of(p)}</loc><lastmod>2026-09-23</lastmod></url>"
                   for p in PAGES if not p.get("noindex"))
    open(os.path.join(OUT, "sitemap.xml"), "w").write(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")


# ------------------------------------------------------------------ preview bundle
def data_uri(fn):
    mime = {"png": "image/png", "webp": "image/webp"}[fn.rsplit(".", 1)[1]]
    return f"data:{mime};base64," + base64.b64encode(open(os.path.join(OUT, fn), "rb").read()).decode()


def slug(fn):
    return fn[:-5]


def preview_links(html):
    html = re.sub(r'href="([a-z0-9-]+)\.html(#[a-z0-9-]+)?"', lambda m: f'href="#{m.group(1)}"', html)
    for img in ["convex_logo.png", "stressed_lawyer.webp", "Conveyancer_winning_with_Convex.webp"]:
        html = html.replace(f'src="{img}"', f'src="{data_uri(img)}"')
    html = re.sub(r'<div class="video"><iframe[^>]*></iframe></div>',
                  '<div class="video"><a class="video-link" href="https://www.youtube.com/watch?v=FOdhpSK5-Bo" target="_blank" rel="noopener">'
                  '<span><span class="play"><svg width="28" height="28" viewBox="0 0 24 24" fill="#012B27"><path d="M8 5v14l11-7z"/></svg></span>'
                  'Watch the demo on YouTube</span></a></div>', html)
    html = html.replace("data-ajax>", 'data-ajax data-preview="1">')
    return html


PREVIEW_CSS = """
.header{top:env(safe-area-inset-top,0px)}
.draftbar{background:#FFF7CC;color:#3D3200;font-size:.85rem;border-bottom:1px solid #E8D98A}
.draftbar .wrap{display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap;padding-block:.5rem}
.draftbar select{font:inherit;padding:.3rem .5rem;border-radius:6px;border:1px solid #D9C97A;background:#fff;color:#012B27;max-width:100%}
"""

ROUTER = """
(function(){
  var pages=[].slice.call(document.querySelectorAll('.pg'));
  var ids=pages.map(function(p){return p.dataset.page});
  var sel=document.getElementById('pg-select');
  function show(id){
    pages.forEach(function(p){p.hidden=p.dataset.page!==id});
    var pg=document.querySelector('.pg[data-page="'+id+'"]');
    var nav=pg?pg.dataset.nav:'';
    document.querySelectorAll('[data-nav]').forEach(function(a){
      if(a.dataset.nav===nav)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});
    if(sel)sel.value=id;
    document.title=(pg&&pg.dataset.title)||document.title;
    window.scrollTo(0,0);
  }
  var current='index';
  function route(){
    var h=(location.hash||'').slice(1);
    if(!h){current='index';show(current);return;}
    if(ids.indexOf(h)!==-1){current=h;show(h);return;}
    var el=document.getElementById(h);
    if(el){el.scrollIntoView();}
  }
  window.addEventListener('hashchange',route);
  if(sel)sel.addEventListener('change',function(){location.hash=sel.value;});
  route();
})();
"""


def build_preview():
    css = open(os.path.join(OUT, "styles.css"), encoding="utf-8").read()
    js = open(os.path.join(OUT, "main.js"), encoding="utf-8").read()
    opts = "".join(f'<option value="{slug(p["file"])}">{p.get("crumb", "Home" if p["file"] == "index.html" else p["title"])}</option>'
                   for p in PAGES)
    body = "".join(
        f'<div class="pg" data-page="{slug(p["file"])}" data-nav="{p["nav"]}" data-title="{clean(p["title"])}"'
        f'{"" if p["file"] == "index.html" else " hidden"}>{p["body"]}</div>' for p in PAGES)
    html = f'''<title>Convex Website Draft</title>
{FONTS}
<style>{css}{PREVIEW_CSS}</style>
<div class="draftbar"><div class="wrap"><span><strong>Draft for review:</strong> proposed replacement for convex.au. Not live. Links to the app open the real app.</span>
<label>Jump to page <select id="pg-select">{opts}</select></label></div></div>
{header("home")}
<main id="main">{body}</main>
{FOOTER}
<script>{js}</script>
<script>{ROUTER}</script>
'''
    html = clean(preview_links(html))
    open(os.path.join(ROOT, "preview.html"), "w", encoding="utf-8").write(html)
    return len(html)


if __name__ == "__main__":
    build_site()
    n = build_preview()
    print(f"built {len(PAGES)} pages; preview {n/1024:.0f} KB")
