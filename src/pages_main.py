from common import *

# ---------------------------------------------------------------- HOME
HERO_REPORT = report(
    "Sample traffic light report",
    "8 Example Avenue, Kellyville NSW - established house, tenanted",
    "Investor - SMSF | Develop: No",
    [("r", 2, "Red"), ("a", 4, "Amber"), ("g", 13, "Green")],
    [
        ("r", "Special condition 32", "Deposit released to the vendor before settlement"),
        ("r", "Special condition 38", "Directors to personally guarantee the purchaser"),
        ("a", "Tenancy agreement", "Periodic tenancy at $640 per week"),
        ("a", "Planning certificate", "Flood-related development controls apply"),
        ("g", "Title search", "Vendor matches the registered proprietor"),
    ],
    "Illustrative example. Each item is explained in plain English in the client letter.")

COVERS = """<div class="covers">
  <div><span class="covers-lbl">Every NSW contract type</span>
  <p>Residential and commercial, established and off-the-plan, strata, unregistered land and house and land.</p></div>
  <div><span class="covers-lbl">Every kind of buyer</span>
  <p>Owner-occupiers, first home buyers, investors, trusts, SMSFs and developers, with a balanced default when the buyer's plans are not yet known.</p></div>
</div>"""

LENS_DEMO = """
<div class="grid g2">
  <div class="card">
    <span class="tag">Same clause</span>
    <h3>"The purchaser takes title subject to the existing periodic tenancy."</h3>
    <ul class="plain">
      <li><strong>Owner-occupier:</strong> <span class="dot r"></span> Red. The client cannot move in on settlement. Vacant possession is not being given, and ending the tenancy depends on the notice rules for the tenant.</li>
      <li><strong>Investor:</strong> <span class="dot g"></span> Green. An income-producing tenancy continues from day 1. The letter confirms the rent, bond transfer and adjustments instead.</li>
    </ul>
  </div>
  <div class="card">
    <span class="tag">Same certificate</span>
    <h3>Planning certificate shows zone R2 Low Density Residential with a minimum lot size of 450 m&sup2;.</h3>
    <ul class="plain">
      <li><strong>Not developing:</strong> <span class="dot g"></span> Green. Noted for completeness. Nothing in the zoning restricts ordinary residential use.</li>
      <li><strong>Intending to develop:</strong> <span class="dot a"></span> Amber. On a 600 m&sup2; lot the minimum lot size prevents a Torrens subdivision into 2 lots. The letter explains the constraint so the client can take planning advice before exchange.</li>
    </ul>
  </div>
</div>"""

FOUNDER = """<div class="founder">
  <div class="founder-id"><div class="avatar" aria-hidden="true">ZA</div><div><b>Zohra Ali</b><span>Principal, Corporate Legal<br>Admitted as a lawyer in 2015</span></div></div>
  <div class="founder-text">
    <span class="eyebrow">Built and used in practice</span>
    <h2>Designed by a property lawyer who uses it on her own files</h2>
    <p>Convex was designed by Zohra Ali, a NSW property lawyer with more than 10 years in conveyancing and the Principal of Corporate Legal. Convex reflects the standard she applies to her own clients' contracts.</p>
    <p>Corporate Legal runs its contract reviews through Convex. The platform is tested on real matters every week, not only in a lab.</p>
  </div>
</div>"""

FOUNDER_STATS = stats([("10+ years", "in NSW property law"), ("190+", "reviews run at Corporate Legal"),
                       ("13,700+", "contract pages reviewed"), ("200+", "Google reviews for Corporate Legal")])

THOROUGH = '<div class="grid g3">' + "".join([
    card("stack", "Every document, not just the special conditions", "Title, planning certificate, plans and prescribed documents are all reviewed, because many issues never appear in the special conditions."),
    card("lens", "Inconsistencies surfaced", "Where one document in the contract does not line up with another, Convex brings it to your attention."),
    card("clock", "The same standard at 5pm on a Friday", "Every page is read, every time. Convex does not skim a 90-page contract because the day has run long."),
    card("lights", "Nothing assumed", "Anything Convex cannot confirm is standard is flagged for your review, with the reason."),
    card("scale", "Built from practice", "Designed by a practising property lawyer and refined on real contracts every week."),
    card("people", "Framed for the buyer", "The letter reads as advice for this client rather than a list of every possible risk."),
]) + '</div>'

CALC = """<div class="calc" data-calc>
  <div class="calc-in">
    <fieldset><legend>Contract type</legend><div class="seg">
      <label><input type="radio" name="ctype" value="est" checked><span>Established</span></label>
      <label><input type="radio" name="ctype" value="otp"><span>Off-the-plan</span></label></div></fieldset>
    <label for="calc-rate">Your hourly rate ($)<input id="calc-rate" type="number" min="0" step="10" value="400" data-k="rate"></label>
    <label for="calc-hours">Hours for a manual review<input id="calc-hours" type="number" min="0" step="0.25" value="1" data-k="hours"></label>
    <label for="calc-fee">Fee you charge for the review ($)<input id="calc-fee" type="number" min="0" step="10" value="250" data-k="fee"></label>
    <label for="calc-n">Reviews a month<input id="calc-n" type="number" min="1" step="1" value="10" data-k="n"></label>
  </div>
  <div class="calc-out" aria-live="polite">
    <table><thead><tr><th></th><th>Manual</th><th>With Convex</th></tr></thead><tbody>
      <tr><th scope="row">Your time per review</th><td data-o="t1"></td><td data-o="t2"></td></tr>
      <tr><th scope="row">Cost of that time</th><td data-o="c1"></td><td data-o="c2"></td></tr>
      <tr><th scope="row">Convex credit</th><td>-</td><td data-o="cr"></td></tr>
      <tr><th scope="row">Fee received</th><td data-o="f1"></td><td data-o="f2"></td></tr>
      <tr class="tot"><th scope="row">Margin per review</th><td data-o="m1"></td><td data-o="m2"></td></tr>
      <tr class="tot"><th scope="row">Margin per month</th><td data-o="mm1"></td><td data-o="mm2"></td></tr>
    </tbody></table>
    <p class="calc-note"><b data-o="save"></b> better off and <b data-o="hrs"></b> hours back each month. Assumes checking a Convex review takes 20% of the manual time (the up to 80% saving) and a credit costs about $30.</p>
  </div>
</div>"""

home_faqs = [
    ("What is Convex?",
     "Convex is an AI contract review platform for NSW conveyancers and property lawyers. Enter the matter details, choose the purchaser lens and upload the contract. Convex returns a green, amber and red traffic light report and a client-ready letter in Word and PDF."),
    ("Which NSW contracts can Convex review?",
     "Established residential, existing strata, off-the-plan strata, unregistered land, the land contract in a house and land package, and commercial contracts of sale. The building contract in a house and land package is not reviewed."),
    ("What is a purchaser lens?",
     "A lens tells Convex who the buyer is and what they intend to do with the property: owner-occupier (upgrader, downsizer or first home buyer), investor (own name, trust or SMSF), and whether they intend to develop. If you do not know yet, choose \"Not sure yet\" and Convex applies a balanced default. Every clause is still reviewed. The lens decides what is prioritised and how the letter is framed."),
    ("Who built Convex?",
     "Zohra Ali, a NSW property lawyer admitted in 2015 and Principal of Corporate Legal, designed Convex with a team of software engineers. Corporate Legal uses Convex on its own contract reviews."),
    ("How long does a review take?",
     "Usually 3 to 5 minutes from upload, including long contracts and scanned PDFs."),
    ("Can I try it first?",
     "Yes. New subscribers receive a 7-day trial with 5 review credits."),
]

HOME = dict(
    file="index.html", nav="home",
    title="Convex | AI Contract Review for NSW Conveyancers and Property Lawyers",
    desc="AI contract review for NSW conveyancers and lawyers. Residential, strata, off-the-plan, unregistered land, house and land and commercial contracts, reviewed through your client's purchaser profile.",
    faqs=home_faqs,
    body=f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">AI contract review for NSW conveyancers and property lawyers</span>
      <h1>Every NSW contract, reviewed through <em>your client's</em> lens.</h1>
      <p class="lead">Convex reads the contract and every document attached to it, scores each issue green, amber or red, and drafts a client-ready letter framed for the buyer in front of you.</p>
      <div class="btn-row">
        <a class="btn" href="{APP_REGISTER}">Start your 7-day trial</a>
        <a class="btn btn-ghost-light" href="how-it-works.html">See how it works</a>
      </div>
      {COVERS}
    </div>
    {HERO_REPORT}
  </div>
</section>

{section(FOUNDER + FOUNDER_STATS, "tight founder-band")}

{section(head("Contract types", "One platform for every NSW contract you review",
  "Convex covers the residential and commercial contracts a NSW property practice sees every week.")
 + '<div class="grid g3">'
 + link_card("nsw-residential-contract-review.html", "house", "Established residential", "Houses, townhouses, duplexes and vacant or tenanted homes on Torrens title.")
 + link_card("strata-contract-review.html", "building", "Strata", "Existing units and townhouses in a registered strata scheme, including by-laws and levies.")
 + link_card("off-the-plan-contract-review.html", "crane", "Off-the-plan", "Proposed strata lots with a disclosure statement, draft plan, sunset date and finishes schedule.")
 + link_card("unregistered-land-contract-review.html", "map", "Unregistered land", "Proposed lots in a draft deposited plan, including design guidelines and draft 88B instruments.")
 + link_card("house-and-land-contract-review.html", "key", "House and land", "The land contract in a house and land package. The building contract is outside scope.")
 + link_card("commercial-contract-review.html", "store", "Commercial", "Office, retail, industrial and mixed-use property, including GST, leases and permitted use.")
 + '</div>')}

{section(head("Purchaser lens packs", "The same contract means different things to different buyers",
  "A standard review scores a clause the same way for every client. Convex asks who is buying and why, and frames the review to match. Here is how 2 common items change with the lens.")
 + LENS_DEMO
 + '<p style="margin-top:2rem"><a class="btn" href="purchaser-profiles.html">Explore the purchaser lens packs</a></p>', "ink")}

{section(head("Thoroughness", "Built to be more thorough, not just faster",
  "Speed is the by-product. The point of Convex is a review you would put your name to, on every contract, whoever is reviewing it and whatever time of day it is.") + THOROUGH, "alt")}

{section(head("The economics", "Make contract reviews profitable again",
  "Pre-purchase contract reviews in NSW are commonly offered free, or for a small fixed fee - often around $100 for an established contract and $200 for off-the-plan. Done properly by hand, a review costs more in time than it earns. Convex turns it into work you can charge for, and profit from.")
 + '<div class="split" style="align-items:start"><div>'
 + checks(["<strong>The fee:</strong> the review is priced as a loss leader, so every hour spent on it is paid for by the conveyance that may follow.",
           "<strong>The time:</strong> a thorough manual review of a standard contract commonly takes 1 to 1.5 hours, and an off-the-plan contract 2 hours or more. At $400 an hour, that is $400 to $800 of time for a fee of $0 to $200.",
           "<strong>The lost lead:</strong> if the client is outbid or walks away, the time is never recovered.",
           "<strong>The risk:</strong> conveyancing and property work is the largest single source of professional negligence notifications to Lawcover. A rushed review is where things are missed.",
           "<strong>The opportunity:</strong> a thorough review on your letterhead, ready the same day, is a service worth charging for. At $250 a review and $400 an hour, a 1-hour manual review loses $150. With Convex, 12 minutes of checking makes $140."])
 + '<p style="margin-top:1.25rem">Change the figures in the calculator to match your practice.</p>'
 + '</div><div>' + CALC + '</div></div>')}

{section(head("What you receive", "A client-ready review, not a first draft")
 + '<div class="grid g4">'
 + card("lights", "Traffic light report", "Every finding scored green, amber or red with a short reason, so you read the reds first.")
 + card("letter", "Client-ready letter", "Your letterhead, matter number and client details already in place. Every issue explained in plain English, so minimal edits are needed.")
 + card("file", "Word and PDF", "Download the letter in Word and PDF and save it to the matter in your practice management system.")
 + card("pen", 'Suggested amendments <span class="soon">Coming soon</span>', "Suggested amendments in italics under each issue, plus a separate amendments list to download and send to the vendor's solicitor.")
 + '</div>', "alt")}

{section(head("How it works", "From matter to client letter in 4 steps", "", True)
 + '''<ol class="steps">
  <li><h3>Enter the matter</h3><p>Add your matter number and client names. They populate the letterhead, so use the same number as your practice management system.</p></li>
  <li><h3>Choose the lens</h3><p>Select the purchaser profile and whether your client intends to develop. Not sure yet? Convex applies a balanced default.</p></li>
  <li><h3>Upload the contract</h3><p>Drop in the contract PDF. Scanned documents are read with OCR. The review is ready in 3 to 5 minutes.</p></li>
  <li><h3>Review and send</h3><p>Check the report and letter, make sure you are happy with it, and send it to your client with minimal edits.</p></li>
</ol>
<p style="text-align:center;margin-top:2.5rem"><a class="btn btn-ghost" href="how-it-works.html">The full walkthrough</a></p>''')}

{section(head("Demo", "See Convex in action", "A short walkthrough of the platform.", True)
 + '<div class="narrow" style="margin:0 auto"><div class="video"><iframe src="https://www.youtube-nocookie.com/embed/FOdhpSK5-Bo" title="Convex demo" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe></div></div>', "alt", "demo")}

{section(head("Pricing", "Plans built around your monthly volume", "Every plan includes every contract type and every purchaser lens. Need more in a busy month? Top up at the same rate per review.", True)
 + '''<div class="grid g3" style="max-width:960px;margin:0 auto">
  <div class="card" style="text-align:center"><h3>Small</h3><p>About 1 review a week</p><p class="price">$145<span class="per">/month</span></p><p><strong>5</strong> reviews a month<br>or <strong>60</strong> a year</p></div>
  <div class="card" style="text-align:center;border:2px solid var(--emerald)"><h3>Medium</h3><p>About 1 review every business day</p><p class="price">$595<span class="per">/month</span></p><p><strong>25</strong> reviews a month<br>or <strong>300</strong> a year</p></div>
  <div class="card" style="text-align:center"><h3>Large</h3><p>2 to 3 reviews every business day</p><p class="price">$1,495<span class="per">/month</span></p><p><strong>50</strong> reviews a month<br>or <strong>600</strong> a year</p></div>
</div>
<p style="text-align:center;margin-top:2rem"><a class="btn btn-ghost" href="pricing.html">Plans, credits and top-ups explained</a></p>''')}

{section(head("On the roadmap", "What is coming next")
 + '<div class="grid g4">'
 + card("plug", 'Smokeball and Clio <span class="soon">Coming soon</span>', "Matter number and client details pulled from the matter, and the finished letter saved straight back to it.")
 + card("pen", 'Suggested amendments <span class="soon">Coming soon</span>', "Italic amendment suggestions in the letter and a downloadable amendments list.")
 + card("map", 'Victoria <span class="soon">Coming soon</span>', "Contracts of sale and section 32 vendor statements.")
 + card("map", 'Queensland <span class="soon">Coming soon</span>', "Contracts and the seller disclosure regime.")
 + '</div>', "alt")}

{section(head("FAQs", "Common questions", "", True)
 + '<div class="narrow" style="margin:0 auto">' + faq(home_faqs)
 + '<p style="text-align:center;margin-top:2rem"><a class="btn btn-ghost" href="faq.html">All FAQs</a></p></div>')}

{cta_band()}
""")

# ---------------------------------------------------------------- HOW IT WORKS
how_faqs = [
    ("What should I upload?",
     "The contract for sale as issued by the vendor's solicitor or agent, with its annexures: special conditions, title search, plans, s10.7 planning certificate, sewer diagram, 88B instrument, strata or off-the-plan documents and any tenancy agreement or lease. Convex reviews everything attached."),
    ("Why do I enter the matter number and client names?",
     "They populate the letterhead and the letter, so the output is ready to send. Use the same matter number as your practice management system so the letter files against the right matter. Once the Smokeball and Clio integrations are live, these details will be pulled through automatically."),
    ("Does Convex work out the contract type itself?",
     "Yes. Convex recognises the type of contract it is reading. If it cannot, it tells you."),
    ("What if Convex is unsure about a clause?",
     "It flags the clause for your review and says why."),
    ("How do I get the letter to my client?",
     "Download the letter in Word or PDF and send it the way you usually do. Save a copy to the matter in your practice management system. The Smokeball and Clio integrations will save it back to the matter automatically once they are released."),
]

HOW = dict(
    file="how-it-works.html", nav="how",
    title="How Convex Works | NSW Contract Review in 5 Steps",
    desc="How Convex reviews a NSW contract of sale: enter the matter, choose the purchaser lens, upload the contract, and receive a traffic light report and client-ready letter in Word and PDF.",
    faqs=how_faqs, crumb="How it works",
    body=phero("How it works", "How a Convex review works",
               "A Convex review follows the same order you would: set up the matter, understand the buyer, read every document in the contract against their circumstances, then put the findings into a letter ready to send.")
    + section(head("Demo", "See Convex in action", "A short walkthrough of the platform.", True)
      + '<div class="narrow" style="margin:0 auto"><div class="video"><iframe src="https://www.youtube-nocookie.com/embed/rUPKEoJ_Ag0" title="Convex demo" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe></div></div>', "alt", "demo")
    + section('''<ol class="detail-steps">
<li><div><h3>Enter the matter details</h3>
<p>Add the matter number and your client's names. These populate your letterhead and the letter itself. Use the same matter number as your practice management system so the letter files against the right matter.</p>
<p>Once the Smokeball and Clio integrations are released <span class="soon">Coming soon</span>, the matter number and client details will be pulled through from the matter automatically.</p></div></li>
<li><div><h3>Choose the purchaser lens</h3>
<p>Tell Convex who is buying and what they intend to do:</p>
<ul><li><strong>Owner-occupier:</strong> upgrading or moving, downsizing, or a first home buyer.</li>
<li><strong>Investor:</strong> buying in their own name, through a trust, or through an SMSF.</li>
<li><strong>Development:</strong> whether the client intends to develop, subdivide or rebuild.</li>
<li><strong>Not sure yet:</strong> if the client has not decided, Convex applies a balanced default and flags the items worth confirming with them.</li></ul>
<p>The letter is framed for that buyer. Nothing is left out of the review. <a href="purchaser-profiles.html">More about purchaser lenses</a>.</p></div></li>
<li><div><h3>Upload the contract</h3>
<p>Upload the contract PDF as you received it, with its annexures. Scanned pages are read with OCR. Several contracts can be uploaded at once.</p></div></li>
<li><div><h3>Convex reviews the whole contract</h3>
<p>Convex recognises the type of contract it is reading and reviews the contract together with every document attached to it, including the title, plans, planning certificate and prescribed documents. Each finding is scored for the buyer you selected.</p></div></li>
<li><div><h3>Review, download and send</h3>
<p>Within 3 to 5 minutes you have a traffic light report with the reds first, and a client-ready letter on your letterhead that explains every issue in plain English. Review it, make sure you are happy with it, and send it to your client with minimal edits.</p>
<p>Download the letter in Word and PDF and save it to the matter in your practice management system.</p></div></li>
</ol>''')
    + section(head("The traffic light scale", "What green, amber and red mean")
      + '<div class="grid g3">'
      + '<div class="card"><span class="dot g" style="margin-bottom:.8rem"></span><h3>Green</h3><p>Standard or low-risk for this buyer. Included in the letter for completeness.</p></div>'
      + '<div class="card"><span class="dot a" style="margin-bottom:.8rem"></span><h3>Amber</h3><p>Needs explaining to the client, or may need a question to the vendor before exchange.</p></div>'
      + '<div class="card"><span class="dot r" style="margin-bottom:.8rem"></span><h3>Red</h3><p>Shifts risk or cost to the buyer, or is unusual enough that it typically warrants negotiation or amendment before exchange.</p></div>'
      + '</div><p class="disc">Scores reflect the purchaser lens you select. A clause can be green for one buyer and red for another.</p>', "alt")
    + section(head("Questions", "About the process") + '<div class="narrow">' + faq(how_faqs) + '</div>')
    + section(xsell("Related pages", [("purchaser-profiles.html", "Purchaser lens packs"), ("contracts-we-review.html", "Contracts and documents we review"), ("pricing.html", "Pricing"), ("faq.html", "All FAQs")]), "tight alt")
    + cta_band()
)

# ---------------------------------------------------------------- PURCHASER PROFILES
lens_faqs = [
    ("Does a lens hide risks from the review?",
     "No. Every clause and document is reviewed under every lens. The lens changes how each item is rated for the buyer and how the letter explains it."),
    ("What if I do not know the buyer's plans yet?",
     "Use the Not sure yet option. Convex applies a balanced default: the review is framed for a general purchaser, and anything whose significance depends on how the buyer will use the property is flagged so you can confirm it with the client. If their plans become clear later, run the contract again under the right profile."),
    ("Can I use more than one lens on the same contract?",
     "Select the profile that matches your client when you upload. If the client's plans change, for example they decide to develop, run the contract again under the new profile."),
    ("Does the SMSF lens give superannuation advice?",
     "No. It frames the contract review for a fund buyer. Compliance with superannuation law remains a matter for the fund's accountant or licensed adviser."),
    ("Does the first home buyer lens work out duty concessions?",
     "No. The lens explains the contract in plainer terms. Eligibility for duty concessions and grants depends on the buyer's circumstances and should be checked separately."),
    ("Do lenses apply to commercial contracts?",
     "Yes. An owner-occupier buying premises for their own business, an investor buying a tenanted asset, an SMSF buying business real property and a developer buying a site each receive a commercial review framed for them."),
]

def lens_card(title, who, outcome):
    return f'<div class="card lens-card"><h4>{title}</h4><p>{who}</p><p style="margin-top:.6rem;color:var(--text)">{outcome}</p></div>'


LENSES = dict(
    file="purchaser-profiles.html", nav="lens",
    title="Purchaser Lens Packs | Contract Review Tailored to the Buyer | Convex",
    desc="Convex tailors each NSW contract review to the buyer: owner-occupier, first home buyer, downsizer, investor in own name, trust or SMSF, and whether they intend to develop.",
    faqs=lens_faqs, crumb="Purchaser lens packs",
    body=phero("Purchaser lens packs", "A contract review that knows who is buying",
               "A periodic tenancy is a problem for a family moving in and an asset for an investor. A minimum lot size is irrelevant to one buyer and decisive for another. Convex lens packs frame the review and the letter for the client in front of you.")
    + section('<div class="split" style="align-items:start"><div>'
              + head("How a lens works", "Chosen once, at the start")
              + checks(["<strong>Every clause is still reviewed:</strong> the lens changes emphasis, never coverage.",
                        "<strong>The rating fits the buyer:</strong> the same clause can be green for one client and red for another.",
                        "<strong>The letter speaks to the client:</strong> explanations are written for that buyer's situation, not a generic purchaser.",
                        "<strong>Development is a separate switch:</strong> any profile can be combined with an intention to develop, subdivide or rebuild.",
                        "<strong>Not sure yet is an option:</strong> if the buyer's plans are not settled, Convex applies a balanced default."])
              + '</div><div>' + LENS_DEMO.replace('grid g2', 'grid') + '</div></div>')
    + section('<div class="lens-group">' + head("Owner-occupiers", "Buying a home to live in")
              + '<div class="grid g3">'
              + lens_card("Upgrading or moving", "Clients selling one home and buying the next.", "The letter reads for someone who needs to move in, on time.")
              + lens_card("Downsizing", "Clients moving to a smaller home, often into strata for the first time.", "The letter reads for someone choosing how they will live day to day.")
              + lens_card("First home buyer", "Clients buying for the first time.", "The letter explains the contract more fully, in plainer language.")
              + '</div></div><div class="lens-group" style="margin-bottom:0">' + head("Investors", "Buying to hold for income or growth")
              + '<div class="grid g3">'
              + lens_card("Own name", "Individuals buying an investment property personally.", "The letter reads for someone buying an income-producing asset.")
              + lens_card("Trust", "Purchases through a discretionary or unit trust.", "The letter reads for a trustee buyer, not an individual.")
              + lens_card("SMSF", "Purchases by a self-managed super fund.", "The letter reads for a fund buyer and flags matters for the fund's adviser.")
              + '</div></div><div class="lens-group" style="margin:3rem 0 0">' + head("Not sure yet", "When the buyer's plans are not settled")
              + '<div class="grid g2">'
              + lens_card("Purchaser: not sure yet", "Clients who have not decided whether they will live in the property or rent it out, or who are still deciding how to hold it.", "Convex applies a balanced default. The letter is framed for a general purchaser, and items whose significance depends on the buyer's plans are flagged for you to confirm.")
              + lens_card("Develop: not sure yet", "Clients who may develop, subdivide or rebuild but have not decided.", "Planning and title matters that would affect a future project are flagged, without treating the purchase as a development.")
              + '</div></div>', "alt")
    + section(head("Development", "Intending to develop, subdivide or rebuild?",
                   "Any profile can be combined with the development option. The same contract then reads very differently: what is a footnote for a home buyer can decide whether a project works.")
              + '<p><a href="contact.html">See it on a contract of your choice in a demo &rarr;</a></p>')
    + section(head("Questions", "About purchaser lenses") + '<div class="narrow">' + faq(lens_faqs) + '</div>', "alt")
    + section(xsell("Related pages", [("how-it-works.html", "How it works"), ("contracts-we-review.html", "Contracts we review"), ("why-convex.html", "Why Convex"), ("faq.html", "All FAQs")]), "tight")
    + cta_band("See the lens in action on your next contract")
)

# ---------------------------------------------------------------- WHY CONVEX
ASK_ROWS = [
    ("Is it built for NSW conveyancing, or adapted from a general tool?",
     "Contract structure, printed conditions and prescribed documents differ between states. A general tool has to guess.",
     "Built for NSW contracts from the start."),
    ("Does it change the review for different buyers?",
     "A clause that suits an investor can be a serious problem for a family moving in.",
     "Yes. Purchaser lens packs for owner-occupiers, first home buyers, investors, trusts, SMSFs and developers, plus a balanced default when the buyer's plans are not yet known."),
    ("Does it cover commercial and off-the-plan contracts?",
     "Many firms review a mix of contract types. Using a different process for each costs time.",
     "Yes. Established, strata, off-the-plan, unregistered land, house and land and commercial."),
    ("Does it read the whole pack or only the special conditions?",
     "Many issues sit in the title, the planning certificate or a lease, not in the special conditions.",
     "The contract and every document attached to it."),
    ("Who designed it?",
     "A tool designed without conveyancing practice tends to flag the wrong things.",
     "Zohra Ali, a practising NSW property lawyer and Principal of Corporate Legal, who uses Convex on her own files."),
    ("What does it do when it is unsure?",
     "A tool that guesses green creates the risk it was meant to remove.",
     "Flags it for your review, with the reason."),
    ("Does it help with amendments?",
     "Finding the problem is half the job. The other half is fixing it before exchange.",
     "Each issue is explained with its legal implication. Suggested amendments in italics and a downloadable amendments list are coming soon."),
    ("Where is my client data stored?",
     "Contracts contain personal and financial information.",
     "Amazon Web Services, Sydney region, with access controls and encryption."),
]


def _ask_table():
    rows = "".join(f"<tr><th scope='row'>{q}</th><td>{w}</td><td>{c}</td></tr>" for q, w, c in ASK_ROWS)
    return (f'<div class="table-wrap"><table class="compare"><thead><tr><th>Question</th><th>Why it matters</th>'
            f'<th>Convex</th></tr></thead><tbody>{rows}</tbody></table></div>')


CHAT_ROWS = [
    ("Knows the NSW printed conditions", "Only what is in its general training", "Built for the NSW contract of sale"),
    ("Consistent output", "Varies with how the question is asked", "The same structure, scale and letter format every time"),
    ("Reads long scanned packs", "Often truncates or skips pages", "Reads the whole contract, including scanned pages"),
    ("Client-ready letter", "You format it yourself", "Your letterhead, matter number and client details, in Word and PDF"),
    ("Confidentiality", "Depends on the tool and settings", "Stored in Sydney under Convex's data terms"),
]


def _chat_table():
    rows = "".join(f"<tr><th scope='row'>{a}</th><td>{b}</td><td>{c}</td></tr>" for a, b, c in CHAT_ROWS)
    return (f'<div class="table-wrap"><table class="compare"><thead><tr><th></th><th>General-purpose AI chat</th>'
            f'<th>Convex</th></tr></thead><tbody>{rows}</tbody></table></div>')


WHY = dict(
    file="why-convex.html", nav="why",
    title="Why Convex | How Convex Compares to Other AI Contract Review Tools",
    desc="What sets Convex apart from other AI contract review tools: purchaser lens packs, residential and commercial coverage, whole-pack review, and designed by a practising NSW property lawyer.",
    crumb="Why Convex",
    body=phero("Why Convex", "What to look for in an AI contract review tool",
               "There are now several AI tools that read contracts of sale. They differ in who built them, what they read, and whether the output is something you would put your name to. These are the questions worth asking, with Convex's answers.")
    + section(head("Questions to ask", "8 questions to ask any AI contract review tool") + _ask_table())
    + section(head("What makes Convex different", "The 4 things we built Convex around")
              + '<div class="grid g2">'
              + card("lens", "The buyer, not just the contract", "Convex is built around purchaser lens packs. The review and letter are framed for an owner-occupier, first home buyer, downsizer, investor, trust, SMSF or developer, so clients are not buried in risks that do not apply to them and the ones that do are not missed.")
              + card("stack", "Every contract type you handle", "Residential, strata, off-the-plan, unregistered land, house and land and commercial contracts are all covered in the one subscription, so the whole team uses the same process.")
              + card("scale", "Built from practice", "Convex was designed by Zohra Ali, a practising NSW property lawyer, and is used on Corporate Legal's own files every week. Anything it cannot confirm is flagged for your review.")
              + card("pen", 'From issue to amendment <span class="soon">Coming soon</span>', "Today Convex explains the legal implication of every issue for the buyer. Next, it will suggest an amendment in italics under each issue for ease of reference, with a separate amendments list you can download and send to the vendor's solicitor. You decide what to adopt.")
              + '</div>', "alt")
    + section('<div class="founder">' + FOUNDER.split('<div class="founder">',1)[1] + FOUNDER_STATS, "alt")
    + section(head("Thoroughness", "Built to be more thorough, not just faster",
                   "An AI review is only as good as the legal judgement built into it.") + THOROUGH)
    + section(head("Compared with AI chat", "Why not paste the contract into a chatbot?",
                   "General-purpose AI chat tools are capable, but they are not a review process.") + _chat_table())
    + section(head("Time back", "Reduce review time by up to 80%",
                   "Convex completes its review in 3 to 5 minutes. Your time goes into checking the reds and ambers, adding your advice and speaking with the client.")
              + checks(["<strong>Friday rushes:</strong> upload several contracts at once and work through the reports in order of risk.",
                        "<strong>Referral partners:</strong> turn around buyer's agent and broker referrals the same day.",
                        "<strong>Capacity:</strong> take on more matters without adding staff."]), "ink")
    + section(xsell("Related pages", [("purchaser-profiles.html", "Purchaser lens packs"), ("contracts-we-review.html", "Contracts we review"), ("pricing.html", "Pricing"), ("contact.html", "Book a demo")]), "tight alt")
    + cta_band()
)

PAGES = [HOME, HOW, LENSES, WHY]
