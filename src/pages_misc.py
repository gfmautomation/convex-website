import re
from common import *

# ---------------------------------------------------------------- PRICING
TOPUP = 29
FEATURES = [
    "All contract types",
    "All purchaser lens packs",
    "Traffic light report",
    "Client-ready letter in Word and PDF",
    "Custom letterhead branding",
    "Bulk contract uploads",
    "OCR for scanned PDFs",
    "Email and phone support",
]
PLANS = [
    ("Small", "For solo practitioners", 145, 1560, 5, "About 1 review a week. Suits a sole practitioner, or a lawyer who does conveyancing alongside other work.",
     FEATURES, False),
    ("Medium", "For growing practices", 595, 6370, 20, "About 1 review every business day. Suits a busy practitioner or a small conveyancing team.",
     FEATURES, True),
    ("Large", "For high-volume firms", 1495, 14995, 50, "2 to 3 reviews every business day. Suits a firm with several people running contract reviews.",
     FEATURES, False),
]


def _plans():
    out = []
    for name, for_, m, y, cr, suits, feats, featured in PLANS:
        pill = '<span class="pill">Most popular</span>' if featured else ""
        li = "".join(f"<li>{f}</li>" for f in feats)
        out.append(f'''<div class="plan{' featured' if featured else ''}">{pill}<h3>{name}</h3><p class="for">{for_}</p>
<p class="price" data-monthly="{m}" data-yearly="{y}">$<span class="amt">{m:,}</span><span class="per">/month</span></p>
<p class="price-note" data-note-monthly="Billed monthly" data-note-yearly="Billed once a year, {cr*12} credits issued upfront">Billed monthly</p>
<div class="credits"><b>{cr}</b><span>reviews a month</span></div>
<p class="suits">{suits}</p>
<ul>{li}</ul><a class="btn" href="{APP_REGISTER}">Start your trial</a></div>''')
    return "".join(out)


CREDIT_STEPS = f'''<ol class="steps credit-steps">
  <li><h3>Your allowance arrives</h3><p>At the start of each billing month you receive your plan's credits: 5, 20 or 50. On a yearly plan the full year's credits (60, 240 or 600) arrive upfront and can be used at any pace across the year.</p></li>
  <li><h3>1 review uses 1 credit</h3><p>The traffic light report and client letter are included. A review that fails to complete is generally not charged.</p></li>
  <li><h3>Top up in a busy month</h3><p>Buy extra credits at ${TOPUP} each, from 1 to 100 at a time, from your billing page. They are added to your balance straight away.</p></li>
  <li><h3>Unused credits expire</h3><p>Credits do not roll over. When your next billing period starts, any remaining credits, including top-ups, expire and a fresh allowance is issued.</p></li>
</ol>'''

price_faqs = [
    ("What is a credit?",
     "1 credit runs 1 contract review. The traffic light report and client letter for that review are included and do not use further credits."),
    ("Do unused credits roll over to the next month?",
     "No. Credits expire at the start of each new billing period, when your fresh allowance is issued. This applies to plan credits, trial credits and top-up credits. On a yearly plan, credits last for the whole year and expire at renewal."),
    ("What if I run out of credits before the month ends?",
     f"Buy top-up credits from your billing page at ${TOPUP} each, from 1 to 100 at a time. They are available immediately and expire at your next billing date, like plan credits. If you regularly top up, moving to the next plan is usually simpler."),
    ("Which plan should I choose?",
     "Choose by your usual monthly volume of contract reviews. Small suits about 1 review a week, Medium about 1 every business day, and Large 2 to 3 every business day. You can change plans as your volume changes."),
    ("Does every plan include every contract type and lens?",
     "Yes. Residential, strata, off-the-plan, unregistered land, house and land and commercial reviews, and every purchaser lens, are available on every plan."),
    ("How does the trial work?",
     "First-time subscribers receive a 7-day trial with 5 trial credits. At the end of the trial your plan starts and the full credit allowance is issued. Cancel before the trial ends and you are not charged."),
    ("How do yearly plans work?",
     "You pay once a year at a lower price than 12 monthly payments, and the full year's credits are issued upfront, so a quiet month followed by a busy one does not cost you anything."),
    ("Can I change plans or cancel?",
     "Yes. Plan changes usually take effect from the next billing period. Cancellation takes effect at the end of the current billing period, and you can keep using your credits until then."),
    ("How is payment taken?",
     "Payments are processed securely by Stripe. Prices are in Australian dollars and the amount confirmed at checkout applies."),
]

PRICING = dict(
    file="pricing.html", nav="pricing",
    title="Convex Pricing | Contract Review Plans, Credits and Top-ups",
    desc="Convex plans for NSW conveyancers and property lawyers: 5, 20 or 50 contract reviews a month, monthly or yearly, top-up credits when you need them, and a 7-day trial.",
    faqs=price_faqs, crumb="Pricing",
    body=phero("Pricing", "Plans built around your monthly volume",
               "Every plan includes every contract type and every purchaser lens. Choose the number of reviews you usually run each month, pay monthly or yearly, and top up in a busy month.")
    + f'''<section class="section alt" data-pricing><div class="wrap">
<div class="billing" role="group" aria-label="Billing period">
  <span class="lbl lbl-m active">Monthly</span>
  <label class="switch"><input type="checkbox" id="billing-toggle" data-billing-toggle aria-label="Show yearly prices"><span class="slider"></span></label>
  <span class="lbl lbl-y">Yearly</span><span class="save">Save with yearly billing</span>
</div>
<div class="plans">{_plans()}</div>
<p class="fine">Prices in Australian dollars. 7-day trial with 5 review credits for first-time subscribers. Top-up credits ${TOPUP} each.</p>
</div></section>'''
    + section(head("How credits work", "Credits, top-ups and expiry",
                   "Each plan gives you a monthly allowance of review credits. Here is how they arrive, how they are used, and when they expire.") + CREDIT_STEPS)
    + section(head("Worked examples", "What a month looks like")
              + '<div class="grid g3">'
              + card("", "A quiet month on Small", "A solo practitioner runs 4 reviews. 1 credit is left unused and expires at the next billing date, when 5 new credits arrive.")
              + card("", "A busy month on Medium", "A practice runs 24 reviews. It uses its 20 credits and buys 4 top-ups at $29 each, which expire at the next billing date if unused.")
              + card("", "A yearly plan on Large", "A firm pays once for the year and receives 600 credits upfront. It runs 30 reviews in January and 70 in March without buying top-ups.")
              + '</div>', "alt")
    + section(head("Questions", "Billing and credits") + '<div class="narrow">' + faq(price_faqs) + '</div>')
    + section(xsell("Related pages", [("how-it-works.html", "How it works"), ("why-convex.html", "Why Convex"), ("faq.html", "All FAQs"), ("terms-and-conditions.html", "Terms and conditions")]), "tight alt")
    + cta_band("Talk to us about a firm-wide plan", "Need more than 50 reviews a month, or several teams? We can tailor a plan.")
)

# ---------------------------------------------------------------- FAQ
FAQ_CATS = [
    ("about", "About Convex", [
        ("What is Convex?",
         "Convex is an AI contract review platform for NSW conveyancers and property lawyers. Enter the matter details, choose the purchaser lens and upload the contract. Convex returns a traffic light report and a client-ready letter in Word and PDF."),
        ("Who is Convex for?",
         "Licensed conveyancers, property lawyers and law firms acting for buyers of NSW property. It is used by solo practitioners through to high-volume firms."),
        ("Can a buyer use Convex directly?",
         "No. Convex is built for professionals who review the output and advise the client. Buyers should engage a conveyancer or lawyer, many of whom use Convex."),
        ("Who built Convex?",
         "Convex was designed by Zohra Ali, a NSW property lawyer admitted in 2015 and Principal of Corporate Legal, working with a team of software engineers. Corporate Legal uses Convex on its own contract reviews."),
        ("Is Convex part of Corporate Legal?",
         "No. Convex is operated by Convex Legal Pty Ltd, a separate company. Corporate Legal is a subscriber that uses Convex on its own files, which is how the platform is tested on real matters every week."),
        ("Can Corporate Legal see my documents or clients?",
         "No. Corporate Legal has no access to other subscribers' accounts, documents or client details. Access by Convex personnel is limited to support and troubleshooting, and is logged."),
        ("How is Convex different from other AI contract review tools?",
         'Convex tailors each review to the buyer through purchaser lens packs, covers residential and commercial contracts in one platform, reads the whole contract pack, and explains each issue in a client-ready letter framed for the buyer. See <a href="why-convex.html">Why Convex</a>.'),
    ]),
    ("contracts", "Contracts and documents", [
        ("Which contract types can Convex review?",
         "Established residential, existing strata, off-the-plan strata, unregistered land, the land contract in a house and land package, and commercial contracts of sale in NSW."),
        ("Does Convex review the building contract in a house and land package?",
         "No. Convex reviews the land contract and notes where it depends on the building contract. The building contract itself is outside scope."),
        ("Which documents does Convex read?",
         "The contract and special conditions, title search and plans, 88B instruments, the s10.7 planning certificate, sewer diagram, pool certificates, occupation certificates, home building insurance, strata and off-the-plan documents, and tenancy agreements and leases attached to the contract."),
        ("Does Convex identify the contract type automatically?",
         "Yes. If Convex cannot tell, it asks you."),
        ("Does Convex flag missing prescribed documents?",
         "Yes. Convex checks the pack against the documents that should be attached and flags any that appear to be missing, with the consequence for the buyer."),
        ("Which edition of the contract does Convex support?",
         "Any edition of the Law Society and REINSW contract for the sale and purchase of land. Convex flags where an earlier edition appears to have been used."),
        ("What file types can I upload?",
         "PDF files, including scanned PDFs, which are read with built-in OCR."),
        ("Can I upload several contracts at once?",
         "Yes. You can upload several contracts at once on every plan."),
        ("What does Convex not review?",
         "Building contracts, business sale contracts, standalone leases, strata inspection reports, building and pest reports, and contracts for property outside NSW."),
    ]),
    ("lens", "Purchaser lens packs", [
        ("What is a purchaser lens?",
         "A lens tells Convex who is buying and what they intend to do with the property. It changes what is prioritised in the review and how the letter is framed."),
        ("Which lenses are available?",
         "<ul><li><strong>Owner-occupier:</strong> upgrading or moving, downsizing, or first home buyer.</li><li><strong>Investor:</strong> own name, trust, or SMSF.</li><li><strong>Development:</strong> a yes or no option that can be combined with any profile.</li><li><strong>Not sure yet:</strong> a balanced default for either choice when the buyer's plans are not settled.</li></ul>"),
        ("What if I do not know the buyer's plans yet?",
         "Use the Not sure yet option. Convex applies a balanced default: the review is framed for a general purchaser, and anything whose significance depends on how the buyer will use the property is flagged so you can confirm it with the client. If their plans become clear later, run the contract again under the right profile."),
        ("Why is Convex built around purchaser lenses?",
         "Because that is how a property lawyer reviews a contract. The first question is always what the client is buying for. A generic review treats every buyer the same, so the letter either buries the client in risks that do not apply to them or underplays the ones that do. Convex asks that first question, the way you would."),
        ("Why not simply flag every risk as red, to be safe?",
         "A letter where everything is urgent is a letter clients stop reading. The risks that matter get lost among the ones that do not, and the reviewing lawyer spends time rewriting. Framing the review for the buyer keeps every item in the report while putting what matters to this client first."),
        ("How does the lens reduce editing time?",
         "Most edits to a generic review letter are about relevance: deleting what does not apply and expanding what does. Because the letter is already framed for the buyer, those edits are largely done before you open it."),
        ("What if I choose the wrong lens?",
         "Run the contract again under the correct profile. If you are unsure at the start, choosing \"Not sure yet\" gives a balanced review rather than one framed for the wrong buyer."),
        ("Does a lens remove anything from the review?",
         "No. Every clause is reviewed under every lens. The lens changes how items are rated and explained for the buyer."),
        ("Can the same clause be scored differently for different buyers?",
         "Yes. A sale subject to a tenancy is red for a family intending to move in and usually green for an investor."),
        ("Does the SMSF lens give superannuation advice?",
         "No. It flags contract terms relevant to an SMSF purchase for you and the fund's adviser. Superannuation compliance advice is outside scope."),
        ("Do lenses work on commercial contracts?",
         "Yes. The same profiles and the development option apply to commercial reviews."),
    ]),
    ("output", "Reports and letters", [
        ("What is the traffic light report?",
         "A list of every finding, scored green, amber or red with a short reason, so you can read the most significant items first."),
        ("What do green, amber and red mean?",
         "<ul><li><strong>Green:</strong> standard or low-risk for this buyer.</li><li><strong>Amber:</strong> needs explaining to the client or a question to the vendor.</li><li><strong>Red:</strong> shifts risk or cost to the buyer, or typically warrants negotiation before exchange.</li></ul>The rating reflects the purchaser lens you select."),
        ("What happens when Convex is unsure?",
         "It flags the item for your review and explains why."),
        ("Can I edit the client letter?",
         "Yes. The letter downloads in Word as well as PDF. It is written to be sent with minimal edits, and you can add any firm-specific wording you like."),
        ("Does the letter include my matter number and client details?",
         "Yes. The matter number and client names you enter at the start populate your letterhead and the letter. Once the Smokeball and Clio integrations are live, these will be pulled from the matter automatically."),
        ("Does the letter suggest amendments?",
         "Today the letter explains the legal implication of each issue for the buyer. Suggested amendments are coming soon: they will appear in italics under each issue for ease of reference, with a separate amendments list you can download and send to the vendor's solicitor. You decide which to adopt."),
        ("Can I use my own letterhead?",
         "Yes. Custom letterhead branding is included on every plan."),
        ("How do I get the letter to my client?",
         "Download it in Word or PDF and send it the way you usually do, then save it to the matter in your practice management system. The Smokeball and Clio integrations will save it back to the matter automatically once released."),
        ("How long does a review take?",
         "Usually 3 to 5 minutes, including long contracts and scanned PDFs."),
    ]),
    ("accuracy", "Accuracy and professional responsibility", [
        ("Is Convex accurate enough for legal work?",
         "Convex is designed by a practising property lawyer and refined on real contracts every week. You remain responsible for checking the output before advising your client."),
        ("Does Convex replace my review?",
         "No. Convex reads, flags and drafts. You review, advise and decide."),
        ("Does Convex provide legal advice?",
         'No. Convex is a support tool for professionals and does not provide legal advice or create a solicitor-client relationship. See the <a href="terms-and-conditions.html">Terms and Conditions</a>.'),
        ("How much time will Convex save?",
         "Convex can reduce contract review time by up to 80%. The saving depends on the contract and how much you add to the letter."),
    ]),
    ("security", "Security and confidentiality", [
        ("Where is my data stored?",
         "On Amazon Web Services in the Sydney region, with access controlled through AWS identity and access management."),
        ("Who can see my uploaded documents?",
         "You and your team. Authorised Convex personnel may access documents only for support or troubleshooting, and that access is limited and logged."),
        ("Is my data used to train Convex?",
         'Uploaded documents are processed to produce your review and, in de-identified form, to improve the reliability of the system. See the <a href="terms-and-conditions.html">Terms and Conditions</a>.'),
        ("Can I delete my documents?",
         "Yes. Documents stay in your account until you delete them. Keep your own records to meet any retention obligations that apply to you."),
    ]),
    ("billing", "Pricing and billing", [
        ("How much does Convex cost?",
         'Small is $145 a month for 5 reviews, Medium $595 a month for 20 reviews, and Large $1,495 a month for 50 reviews. Yearly billing is also available. See <a href="pricing.html">Pricing</a>.'),
        ("Is there a free trial?",
         "Yes. First-time subscribers receive a 7-day trial with 5 review credits."),
        ("Do unused credits roll over?",
         "No. Remaining credits expire at the start of each new billing period, when a fresh allowance is issued. On a yearly plan the full year's credits are issued upfront and last until renewal."),
        ("Can I buy extra credits?",
         "Yes. Top-up credits cost $29 each and can be bought 1 to 100 at a time while your subscription is active. They expire at your next billing date."),
        ("Can I cancel at any time?",
         "Yes. Cancellation takes effect at the end of the current billing period."),
    ]),
    ("roadmap", "Integrations and roadmap", [
        ("Does Convex integrate with Smokeball or Clio?",
         "Integrations with Smokeball and Clio are in development. They will pull the matter number and client details from the matter and save the finished letter back to it. Existing subscribers will be told as soon as they are available."),
        ("When will Convex cover Victoria and Queensland?",
         "Victoria and Queensland are next on the roadmap. Contact us to be told when they launch."),
        ("Will Convex accept Word documents?",
         "Word document upload is planned. PDF, including scanned PDF, is supported now."),
    ]),
    ("start", "Getting started", [
        ("Do I need technical experience?",
         "No. Enter the matter details, choose the lens, upload the PDF and Convex does the rest. There is no setup or training required."),
        ("Do I need to change how I review contracts?",
         "No. Convex follows the order you already work in, and produces a letter you can send with minimal edits."),
        ("Can my whole team use Convex?",
         "Yes. The Large plan includes a team-ready workflow. Contact us about firm-wide plans."),
        ("Can I see a demo first?",
         'Yes. <a href="contact.html">Book a demo</a> and we will walk you through a review.'),
    ]),
]


def _faq_page_body():
    nav = "".join(f'<a href="#{cid}">{name}</a>' for cid, name, _ in FAQ_CATS)
    groups = "".join(
        f'<div class="faq-group" id="{cid}"><h2 class="faq-cat">{name}</h2>{faq(items)}</div>' for cid, name, items in FAQ_CATS)
    return f'''<section class="section"><div class="wrap faq-layout" data-faq-scope>
<nav class="faq-nav" aria-label="FAQ topics">{nav}</nav>
<div><label for="faq-q" class="eyebrow" style="display:block">Search the FAQs</label>
<input id="faq-q" class="faq-search" type="search" placeholder="For example: sunset date, SMSF, credits" data-faq-search>
<p class="faq-empty" hidden>No questions match that search. <a href="contact.html">Ask us directly</a>.</p>
{groups}</div></div></section>'''


ALL_FAQS = [qa for _, _, items in FAQ_CATS for qa in items]

FAQ = dict(
    file="faq.html", nav="faq",
    title="Convex FAQs | AI Contract Review for NSW Conveyancers",
    desc="Answers about Convex: contract types, documents reviewed, purchaser lens packs, traffic light scoring, client letters, security, pricing, integrations and the roadmap.",
    faqs=ALL_FAQS, crumb="FAQs",
    body=phero("FAQs", "Frequently asked questions",
               "Everything about how Convex reviews NSW contracts, what it covers, and how billing works. Search, or jump to a topic.")
    + _faq_page_body() + cta_band("Still have a question?", "We are happy to walk you through a review on a contract of your choice.")
)

# ---------------------------------------------------------------- CONTACT
CONTACT = dict(
    file="contact.html", nav="contact",
    title="Contact Convex | Book a Demo",
    desc="Book a Convex demo or ask a question about AI contract review for NSW conveyancers and property lawyers.",
    crumb="Contact",
    body=phero("Contact", "Book a demo or ask a question",
               "Tell us a little about your practice and we will be in touch within 1 business day.")
    + section('''<div class="split" style="align-items:start">
<form class="form card" action="https://formspree.io/f/xovnrlaj" method="POST" data-ajax>
  <div class="row2"><label for="c-name">Full name<input id="c-name" name="name" required autocomplete="name"></label>
  <label for="c-email">Email<input id="c-email" type="email" name="email" required autocomplete="email"></label></div>
  <div class="row2"><label for="c-phone">Phone<input id="c-phone" type="tel" name="phone" autocomplete="tel"></label>
  <label for="c-firm">Firm name<input id="c-firm" name="firm" autocomplete="organization"></label></div>
  <div class="row2"><label for="c-role">Your role<select id="c-role" name="business" required>
    <option value="">Select</option><option value="conveyancer">Conveyancer</option><option value="property-lawyer">Property lawyer</option>
    <option value="principal">Principal or practice manager</option><option value="other">Other</option></select></label>
  <label for="c-vol">Contract reviews a month<select id="c-vol" name="volume">
    <option value="">Select</option><option>Up to 5</option><option>6 to 20</option><option>21 to 50</option><option>More than 50</option></select></label></div>
  <label for="c-msg">How can we help?<textarea id="c-msg" name="message" placeholder="For example: a demo on an off-the-plan contract"></textarea></label>
  <button class="btn" type="submit">Send</button>
  <p class="form-status" aria-live="polite"></p>
</form>
<div class="contact-side">
  <div class="card"><h3>Email</h3><p><a href="mailto:info@convex.au">info@convex.au</a></p></div>
  <div class="card"><h3>Phone</h3><p><a href="tel:+61406522627">0406 522 627</a></p></div>
  <div class="card"><h3>Already a subscriber?</h3><p><a href="''' + APP_LOGIN + '''">Sign in to Convex</a></p></div>
</div></div>''')
)

# ---------------------------------------------------------------- TERMS
def _terms_body(src_path):
    raw = open(src_path, encoding="utf-8").read()
    raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    hdr = re.search(r'<div class="terms-header">(.*?)</div>\s*<div class="terms-content">', raw, re.S).group(1)
    hdr = re.sub(r"<h1>.*?</h1>", "", hdr, flags=re.S)
    content = re.search(r'<div class="terms-content">(.*?)<div class="last-updated">', raw, re.S).group(1)
    return (phero("Terms and conditions", "Terms of Use", "Convex Legal Pty Ltd (ABN 87 692 237 577).")
            + section(f'<div class="prose terms-content">{hdr}{content}</div>'))


def terms_page(src_path):
    return dict(file="terms-and-conditions.html", nav="", title="Terms of Use | Convex",
                desc="Terms of use for the Convex AI contract review platform.", crumb="Terms and conditions",
                body=_terms_body(src_path))


NOTFOUND = dict(
    file="404.html", nav="", title="Page not found | Convex", desc="This page could not be found.", noindex=True,
    body=f'''<section class="section nf"><div class="wrap"><div class="code">404</div><h1 style="margin:1rem 0">Page not found</h1>
<p class="lead" style="margin:0 auto 2rem">The page you were looking for has moved or does not exist.</p>
<div class="btn-row" style="justify-content:center"><a class="btn" href="index.html">Go to the home page</a><a class="btn btn-ghost" href="faq.html">Read the FAQs</a></div></div></section>''')
