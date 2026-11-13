"""Shared building blocks for the Convex site build."""
import html as _html
import re

APP_REGISTER = "https://app.convex.au/auth/register"
APP_LOGIN = "https://app.convex.au/auth/login"
SITE = "https://www.convex.au"

_I = {
    "file": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6M9 17h4"/>',
    "house": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-5h4v5"/>',
    "building": '<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2"/>',
    "crane": '<path d="M4 21h10"/><path d="M7 21V4l10 3"/><path d="M7 7h12"/><path d="M17 7v5"/><rect x="15" y="12" width="4" height="3"/>',
    "map": '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
    "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M15 8l2 2"/>',
    "store": '<path d="M4 9l1.5-5h13L20 9"/><path d="M4 9h16v2a3 3 0 0 1-5.3 2 3 3 0 0 1-5.4 0A3 3 0 0 1 4 11z"/><path d="M5 13v8h14v-8"/>',
    "lens": '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/><path d="M8.5 11l1.8 1.8L14 9.2"/>',
    "lights": '<rect x="8" y="2" width="8" height="20" rx="4"/><circle cx="12" cy="7" r="1.6"/><circle cx="12" cy="12" r="1.6"/><circle cx="12" cy="17" r="1.6"/>',
    "letter": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "stack": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    "scale": '<path d="M12 3v18M7 21h10"/><path d="M5 7h14"/><path d="M5 7l-3 6a3 3 0 0 0 6 0zM19 7l-3 6a3 3 0 0 0 6 0z"/>',
    "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-4.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "plug": '<path d="M9 2v5M15 2v5"/><path d="M6 7h12v4a6 6 0 0 1-12 0z"/><path d="M12 17v5"/>',
    "send": '<path d="M22 2L11 13"/><path d="M22 2l-7 20-4-9-9-4z"/>',
    "people": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.5a5 5 0 0 1 5.5 5"/>',
    "pen": '<path d="M4 20l4-1 11-11-3-3L5 16z"/><path d="M14 6l3 3"/>',
    "pie": '<path d="M12 3v9h9"/><circle cx="12" cy="12" r="9"/>',
    "trust": '<path d="M12 3l9 4H3z"/><path d="M5 10v8M9.5 10v8M14.5 10v8M19 10v8"/><path d="M3 21h18"/>',
    "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    "down": '<path d="M12 4v14M6 12l6 6 6-6"/>',
    "up": '<path d="M12 20V6M6 12l6-6 6 6"/>',
}


def icon(name):
    return ('<div class="ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' + _I[name] + '</svg></div>')


def card(ic, title, text, extra=""):
    return f'<div class="card">{icon(ic) if ic else ""}<h3>{title}</h3><p>{text}</p>{extra}</div>'


def link_card(href, ic, title, text, more="Read more"):
    return (f'<a class="card" href="{href}">{icon(ic) if ic else ""}<h3>{title}</h3><p>{text}</p>'
            f'<span class="more">{more} &rarr;</span></a>')


def head(eyebrow, title, lead="", ctr=False):
    e = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    l = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<div class="head{" ctr" if ctr else ""}">{e}<h2>{title}</h2>{l}</div>'


def section(inner, cls="", sid=""):
    i = f' id="{sid}"' if sid else ""
    return f'<section class="section {cls}"{i}><div class="wrap">{inner}</div></section>'


def phero(crumb, h1, lead, eyebrow=""):
    e = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    return (f'<section class="phero"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb">'
            f'<a href="index.html">Home</a><span>/</span>{crumb}</nav>{e}<h1>{h1}</h1>'
            f'<p class="lead">{lead}</p></div></section>')


def faq(items):
    out = ['<div class="faq">']
    for q, a in items:
        out.append(f'<details><summary>{q}</summary><div class="a">{a}</div></details>')
    out.append('</div>')
    return "".join(out)


def xsell(label, links):
    a = "".join(f'<a href="{h}">{t}</a>' for h, t in links)
    return f'<div class="xsell"><b>{label}</b><div class="xlinks">{a}</div></div>'


def cta_band(title="Run your next NSW contract review through Convex",
             text="7-day trial with 5 review credits. Cancel any time before the trial ends."):
    return (f'<section class="cta-band"><div class="wrap cta-inner"><div><h2>{title}</h2><p>{text}</p></div>'
            f'<div class="btn-row"><a class="btn" href="{APP_REGISTER}">Start your trial</a>'
            f'<a class="btn btn-ghost" href="contact.html">Book a demo</a></div></div></section>')


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def strip_tags(s):
    s = re.sub(r"<li>", " - ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = _html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def report(title, sub, lens, tally, rows, foot="Illustrative example only. Not advice on any real property."):
    t = "".join(f'<div><span class="dot {k}"></span><b>{n}</b> {lbl}</div>' for k, n, lbl in tally)
    names = {"r": "Red", "a": "Amber", "g": "Green"}
    r = "".join(
        f'<li><span class="dot {k}" aria-label="{names[k]}"></span><span class="t">{tt}</span><span class="ref">{ref}</span></li>'
        for k, ref, tt in rows)
    return (f'<div class="report" role="figure" aria-label="Sample Convex traffic light report">'
            f'<div class="report-top"><b>{title}</b><small>{sub}</small><span class="lens-chip">{lens}</span></div>'
            f'<div class="report-tally">{t}</div><ol>{r}</ol><div class="report-foot">{foot}</div></div>')


def stats(items):
    return '<div class="stats">' + "".join(f'<div><b>{n}</b><span>{l}</span></div>' for n, l in items) + '</div>'
