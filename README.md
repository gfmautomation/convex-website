# convex-website (draft v2 - September 2026)

Proposed replacement for www.convex.au. Plain HTML, CSS and JS, same stack as the current site, so it deploys to GitHub Pages exactly as before (CNAME kept).

## Pages

| File | Purpose | Main search target |
|---|---|---|
| index.html | Home | AI contract review NSW conveyancers |
| how-it-works.html | 5-step walkthrough, traffic light scale | how AI contract review works |
| purchaser-profiles.html | Purchaser lens packs (interactive) | contract review for investors / SMSF / first home buyers |
| why-convex.html | Comparison and differentiators | best AI contract review tool |
| contracts-we-review.html | Hub: contract types and documents read | - |
| nsw-residential-contract-review.html | Established residential | NSW contract review software |
| strata-contract-review.html | Strata | strata contract review NSW |
| off-the-plan-contract-review.html | Off-the-plan strata | off the plan contract review NSW |
| unregistered-land-contract-review.html | Proposed lots | unregistered land contract review |
| house-and-land-contract-review.html | Land contract in H&L packages | house and land contract review |
| commercial-contract-review.html | Commercial / industrial | commercial property contract review NSW |
| pricing.html | Plans, toggle, billing FAQs | Convex pricing |
| faq.html | 45+ FAQs, searchable, 9 topics | - |
| contact.html | Demo request form (same Formspree endpoint) | - |
| terms-and-conditions.html | Existing terms, unchanged text | - |
| 404.html | Not found | - |

Also: sitemap.xml, robots.txt, favicon.png.

## SEO built in

- Unique title and meta description on every page, canonical URLs, Open Graph tags
- JSON-LD: Organization + SoftwareApplication (home), BreadcrumbList (all inner pages), FAQPage (every page with FAQs, generated from the same source as the visible FAQs so they cannot drift)
- One H1 per page, internal cross-links between every contract-type page

## Behaviour (main.js)

- Mobile menu
- Pricing toggle: prices read from data attributes, so the on-screen figure and the toggle can no longer disagree (fixes the $590/$595 and $1,395/$1,495 bug on the live site)
- FAQ search filter
- Purchaser lens picker (illustrative)
- Contact form posts to Formspree via fetch

## Source

The pages are generated from Python source (`src/`) so the header, footer and FAQ schema stay consistent. To regenerate: `python3 src/build.py`. Editing the generated HTML directly also works if the source is not kept.
