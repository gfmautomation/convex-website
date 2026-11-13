from common import *

ALL_TYPES = [
    ("nsw-residential-contract-review.html", "Established residential"),
    ("strata-contract-review.html", "Strata"),
    ("off-the-plan-contract-review.html", "Off-the-plan"),
    ("unregistered-land-contract-review.html", "Unregistered land"),
    ("house-and-land-contract-review.html", "House and land"),
    ("commercial-contract-review.html", "Commercial"),
]


def type_page(file, title, desc, crumb, h1, lead, eyebrow, cards, docs, lens_rows, faqs, cta_title):
    grid = '<div class="grid g3">' + "".join(card(i, t, x) for i, t, x in cards) + '</div>'
    others = [(h, t) for h, t in ALL_TYPES if h != file]
    body = (phero(f'<a href="contracts-we-review.html">Contracts we review</a><span>/</span>{crumb}', h1, lead, eyebrow)
            + section(head("What Convex checks", f"What Convex looks for in {crumb.lower()} contracts") + grid)
            + section('<div class="split" style="align-items:start"><div>'
                      + head("Documents", "What Convex reads",
                             "Convex reviews the contract together with the documents attached to it.")
                      + '</div><div>' + checks(docs) + '</div></div>', "alt")
            + section(head("Purchaser lens", "Framed for the buyer",
                           "The same contract means different things to an owner-occupier, an investor, an SMSF and a developer. Convex frames the review and the letter for the buyer you select.")
                      + '<p><a href="purchaser-profiles.html">How purchaser lens packs work &rarr;</a></p>')
            + section(head("Questions", f"{crumb} contract review FAQs") + '<div class="narrow">' + faq(faqs) + '</div>', "alt")
            + section(xsell("Other contract types", others + [("contracts-we-review.html", "All contracts and documents")]), "tight")
            + cta_band(cta_title))
    return dict(file=file, nav="contracts", title=title, desc=desc, faqs=faqs, crumb=crumb,
                parent=("contracts-we-review.html", "Contracts we review"), body=body)


RES = type_page(
    "nsw-residential-contract-review.html",
    "NSW Residential Contract Review Software for Conveyancers | Convex",
    "AI review of NSW residential contracts for sale: special conditions, title, s10.7 planning certificate, prescribed documents and tenancies, with a traffic light report and client letter.",
    "Established residential",
    "AI review of NSW residential contracts for sale",
    "For established houses, townhouses, duplexes and villas on Torrens title, vacant or tenanted. Convex reviews the Law Society and REINSW contract, the vendor's special conditions and every document attached.",
    "Established residential",
    [
        ("pen", "Special conditions", "Early deposit release, reduced deposits and deposit bonds, notice to complete periods, penalty interest, vendor rescission rights and clauses excluding the purchaser's claims."),
        ("file", "Front page and particulars", "Parties, price, deposit, completion period, inclusions and exclusions, whether cooling-off applies or a 66W certificate is proposed, and which edition of the contract is used."),
        ("map", "Title and plans", "Whether the vendor is the registered proprietor, and the mortgages, caveats, easements, covenants and 88B restrictions recorded on title."),
        ("building", "Planning certificate", "Zoning and permitted use, heritage, flood, bushfire, contamination, road widening and acquisition affectations from the s10.7 certificate."),
        ("stack", "Prescribed documents", "Whether the documents required for the contract appear to be attached. A missing prescribed document can give the purchaser a right to rescind."),
        ("key", "Tenancies", "Residential tenancy agreements: parties, rent, term, bond, and whether the property is sold with vacant possession or subject to the tenancy."),
    ],
    ["<strong>The contract:</strong> front page, printed conditions and special conditions",
     "<strong>Title search</strong> and the title plan",
     "<strong>Section 88B instrument</strong> and dealings creating easements or covenants",
     "<strong>Section 10.7 planning certificate</strong>",
     "<strong>Sewer service diagram</strong>",
     "<strong>Swimming pool</strong> certificate of compliance or non-compliance",
     "<strong>Occupation certificates</strong> and building approvals included in the pack",
     "<strong>Home building insurance</strong> or owner-builder documents where included",
     "<strong>Residential tenancy agreement</strong> where the property is tenanted"],
    [("Owner-occupier", "A sale subject to a periodic tenancy is headlined red: the client cannot move in on settlement."),
     ("Investor - own name", "The same tenancy is confirmed and the letter focuses on rent, bond transfer and adjustments."),
     ("First home buyer", "Cooling-off, the deposit and finance timing are explained in fuller, plainer language."),
     ("Develop: yes", "Minimum lot size, 88B building restrictions and heritage controls move to the top for a knockdown rebuild or subdivision.")],
    [("Does Convex tell me which prescribed documents are missing?",
      "Convex checks the pack against the documents that should be attached for that type of property and flags any that appear to be missing, with the consequence for the purchaser."),
     ("Which edition of the contract does Convex support?",
      "Convex reads any edition of the Law Society and REINSW contract for the sale and purchase of land, and flags where an earlier edition appears to have been used."),
     ("Can Convex review a tenanted property?",
      "Yes. Convex reads the residential tenancy agreement and explains the tenancy's effect for the buyer."),
     ("Does Convex review building and pest reports?",
      "No. Convex reviews the contract and the documents attached to it. Building and pest reports are outside its scope."),
     ("How long does a residential review take?",
      "Usually 3 to 5 minutes from upload.")],
    "Review your next residential contract with Convex")

STRATA = type_page(
    "strata-contract-review.html",
    "Strata Contract Review NSW | AI Review for Conveyancers | Convex",
    "AI review of NSW strata contracts for units and townhouses: by-laws, strata plan, exclusive use, levies, special levies and defect clauses, tailored to the buyer.",
    "Strata",
    "AI review of NSW strata contracts",
    "For units, townhouses and villas in a registered strata scheme. Convex reviews the contract together with the strata plan, by-laws and strata disclosures, and flags what matters for the particular buyer.",
    "Strata",
    [
        ("building", "Strata plan and the lot", "Lot number, unit entitlement, and whether car spaces and storage are part of the lot, exclusive use common property, or only a licence."),
        ("file", "By-laws", "Pets, renovations, short-term letting, parking, smoking and exclusive use by-laws, with any unusual obligations on the owner."),
        ("pie", "Levies and special levies", "How levies and special levies are adjusted, and special conditions that shift levies raised before completion to the purchaser."),
        ("shield", "Defects and remediation", "Acknowledgements about building defects, cladding, rectification orders or remediation works, and clauses limiting the purchaser's claims."),
        ("stack", "Strata disclosures", "Strata renewal proposals, strata development contracts and other disclosures that must accompany a strata contract."),
        ("pen", "Special conditions", "Every special condition reviewed, as for any residential contract."),
    ],
    ["<strong>The contract</strong> and special conditions",
     "<strong>Strata plan</strong> and title search for the lot",
     "<strong>By-laws</strong>, including exclusive use and special privilege by-laws",
     "<strong>Section 10.7 planning certificate</strong>",
     "<strong>Strata renewal and strata development contract</strong> disclosures where attached",
     "<strong>Residential tenancy agreement</strong> where tenanted"],
    [("Downsizer", "By-laws on pets and renovations, and levies, are brought to the front for a client moving into strata for the first time."),
     ("Investor - own name", "Short-term letting by-laws, the tenancy and levy adjustments are prioritised."),
     ("First home buyer", "Unit entitlement, levies and car space arrangements are explained in plain language."),
     ("Upgrading or moving", "Renovation by-laws and any works the owners corporation has planned are headlined.")],
    [("Does Convex review strata inspection reports?",
      "No. Convex reviews the contract and the strata documents attached to it. A strata inspection report from the owners corporation's records is a separate document and remains recommended."),
     ("Can Convex tell whether a car space is on title?",
      "Convex reads the strata plan and by-laws in the pack and reports whether the car space appears to be part of the lot, exclusive use common property, or neither."),
     ("Is off-the-plan strata covered here?",
      'Off-the-plan strata has its own checks, including the disclosure statement and sunset date. See <a href="off-the-plan-contract-review.html">off-the-plan contract review</a>.'),
     ("Does the lens change a strata review?",
      "Yes. A strata review is framed differently for a downsizer moving in than for an investor.")],
    "Review your next strata contract with Convex")

OTP = type_page(
    "off-the-plan-contract-review.html",
    "Off-the-Plan Contract Review NSW | Sunset Clauses and Disclosure | Convex",
    "AI review of NSW off-the-plan contracts: disclosure statement, draft strata plan and by-laws, sunset date, material changes, deposit and completion mechanics.",
    "Off-the-plan",
    "AI review of NSW off-the-plan contracts",
    "Off-the-plan contracts carry risks an established sale does not: the building does not exist yet, the plan can change, and completion depends on registration. Convex reviews the contract with its disclosure statement and draft documents.",
    "Off-the-plan strata",
    [
        ("file", "Disclosure statement", "Whether a disclosure statement and the required draft documents are attached, and whether they are consistent with the contract."),
        ("clock", "Sunset date", "The sunset date, how it can be extended, and the vendor's rights to rescind, compared with the limits that apply to residential off-the-plan contracts."),
        ("pen", "Changes to the plan", "Clauses allowing the vendor to vary the plan, the lot, the finishes or the by-laws, and the purchaser's rights when a material change is notified."),
        ("pie", "Deposit", "Deposit amount, instalments, deposit bonds and guarantees, and where and how the deposit is held until completion."),
        ("building", "Completion", "How completion is triggered by registration of the plan, the notice period, and any delay, interest or holding costs."),
        ("shield", "Developer protections", "Restrictions on caveats, on-selling, assignment and marketing, nomination fees and clauses limiting claims for defects."),
    ],
    ["<strong>The contract</strong> and special conditions",
     "<strong>Disclosure statement</strong>",
     "<strong>Draft strata plan</strong> and plan of the proposed lot",
     "<strong>Draft by-laws</strong> and any proposed strata development contract",
     "<strong>Schedule of finishes</strong> and inclusions",
     "<strong>Title search</strong> for the parent lot",
     "<strong>Section 10.7 planning certificate</strong> and development consent where attached"],
    [("First home buyer", "The sunset date, deposit and cooling-off are explained in plain terms, with how long the client may wait to complete."),
     ("Investor - own name", "Restrictions on on-selling or assignment before completion and any rental guarantee terms are prioritised."),
     ("Investor - SMSF", "Deposit bond and finance timing against an unknown completion date are brought forward for the fund's lender and adviser."),
     ("Downsizer", "The draft by-laws, finishes and changes the vendor may make to the lot are headlined.")],
    [("What is the cooling-off period for an off-the-plan contract?",
      "Residential off-the-plan contracts in NSW have a longer cooling-off period than an established sale. Convex confirms whether a cooling-off period applies and whether a waiver is proposed."),
     ("Does Convex compare the disclosure statement with the contract?",
      "Yes. Convex reads both and flags inconsistencies, for example a different number of car spaces or a different sunset date."),
     ("Does Convex review off-the-plan houses or land lots?",
      'Proposed Torrens lots are covered on the <a href="unregistered-land-contract-review.html">unregistered land</a> page. House and land packages are covered on the <a href="house-and-land-contract-review.html">house and land</a> page.'),
     ("Does Convex check the finishes schedule against the marketing material?",
      "Convex reads the finishes schedule attached to the contract. Marketing brochures are not part of the contract and are not reviewed.")],
    "Review your next off-the-plan contract with Convex")

LAND = type_page(
    "unregistered-land-contract-review.html",
    "Unregistered Land Contract Review NSW | Proposed Lots | Convex",
    "AI review of NSW contracts for unregistered land: draft deposited plan, draft 88B instrument, design guidelines, building covenants, registration and sunset dates.",
    "Unregistered land",
    "AI review of contracts for unregistered land in NSW",
    "For proposed lots in a draft deposited plan, usually in a new estate. Convex reviews the contract with the draft plan, the draft 88B instrument and the estate's design requirements.",
    "Proposed Torrens lots",
    [
        ("map", "Draft deposited plan", "Lot number, area and dimensions, and clauses allowing the final lot to differ from the draft within a tolerance."),
        ("file", "Draft 88B instrument", "Proposed easements, restrictions on use and positive covenants, including building envelopes, materials, fencing and retaining walls."),
        ("house", "Design guidelines", "Developer approval of house plans, minimum dwelling size, facade and landscaping requirements, and any bond or approval fee."),
        ("clock", "Building timeframes", "Covenants to start or finish building within a period, and any buy-back or penalty if they are not met."),
        ("building", "Registration and sunset", "The expected registration date, the sunset date, the vendor's rights to rescind, and the period to complete after notice of registration."),
        ("shield", "Services and site", "Road access, services, bushfire and flood affectations, and conditions about the state of the land at completion."),
    ],
    ["<strong>The contract</strong> and special conditions",
     "<strong>Draft deposited plan</strong>",
     "<strong>Draft section 88B instrument</strong>",
     "<strong>Estate design guidelines</strong> where attached",
     "<strong>Title search</strong> for the parent lot",
     "<strong>Section 10.7 planning certificate</strong> for the parent lot"],
    [("First home buyer", "The time to registration, the deposit and building timeframes are explained, as these drive when the client can move in."),
     ("Develop: yes", "Restrictions on dual occupancy, secondary dwellings or further subdivision in the 88B instrument are headlined."),
     ("Investor - SMSF", "Items about building on vacant land are flagged for the fund's adviser, as borrowing to improve land raises separate questions."),
     ("Upgrading or moving", "Design guidelines and approval requirements that affect the home the client wants to build are brought forward.")],
    [("Does Convex review the building contract?",
      'No. Convex reviews the land contract only. See <a href="house-and-land-contract-review.html">house and land contract review</a>.'),
     ("Does Convex read estate design guidelines?",
      "Yes, where they are attached to the contract or referred to in the 88B instrument and included in the pack."),
     ("Can Convex tell me when the lot will register?",
      "Convex reports the dates and notice periods in the contract. It cannot predict when the plan will actually register."),
     ("Is off-the-plan strata covered here?",
      'No. Off-the-plan strata is covered on the <a href="off-the-plan-contract-review.html">off-the-plan</a> page.')],
    "Review your next land contract with Convex")

HL = type_page(
    "house-and-land-contract-review.html",
    "House and Land Package Contract Review NSW | Land Contract | Convex",
    "AI review of the land contract in a NSW house and land package, including links to the builder, design approvals, registration and timing. The building contract is not reviewed.",
    "House and land",
    "AI review of the land contract in a house and land package",
    "In a house and land package the buyer usually signs 2 contracts: one for the land and a separate building contract. Convex reviews the land contract and flags where it depends on the build. The building contract is outside its scope.",
    "House and land packages",
    [
        ("key", "Links to the builder", "Conditions requiring a nominated builder, making the land contract conditional on a building contract, or allowing the vendor to rescind if the build does not proceed."),
        ("clock", "Timing", "Land completion dates against the likely start of construction, and any holding costs or penalties if the build is delayed."),
        ("house", "Design approvals", "Developer approval of plans, design guidelines and building covenants that the builder must also satisfy."),
        ("map", "Registered or unregistered", "Whether the land is already registered, and if not, the draft plan, 88B instrument and sunset date."),
        ("pie", "Deposit and price", "The land deposit and any package pricing or rebates referred to in the land contract."),
        ("pen", "Special conditions", "Every special condition in the land contract reviewed."),
    ],
    ["<strong>The land contract</strong> and special conditions",
     "<strong>Title search</strong>, or the draft deposited plan for an unregistered lot",
     "<strong>Section 88B instrument</strong> or draft instrument",
     "<strong>Design guidelines</strong> where attached",
     "<strong>Section 10.7 planning certificate</strong>",
     "<strong>Not reviewed:</strong> the building contract, plans and specifications"],
    [("First home buyer", "The 2-contract structure and the timing between land completion and construction are explained plainly."),
     ("Investor - own name", "Rental guarantees and the time before the property can earn income are brought forward."),
     ("Investor - SMSF", "The link between the land and the build is flagged for the fund's adviser, as borrowing to build raises separate questions."),
     ("Upgrading or moving", "Timing is compared with the client's need to sell or leave their current home.")],
    [("Why doesn't Convex review the building contract?",
      "Building contracts are a different kind of document with their own statutory framework and industry forms. Convex focuses on the land contract so that part of the package is reviewed in depth."),
     ("Should I upload the building contract with the land contract?",
      "Upload the land contract and its annexures only. If the land contract refers to the building contract, Convex notes the reference so you can review the 2 together."),
     ("Does Convex cover house and land packages on registered land?",
      "Yes. The land can be registered or unregistered."),
     ("Is there a separate fee for house and land reviews?",
      "No. A house and land review uses 1 credit, the same as any other review.")],
    "Review your next house and land package with Convex")

COMM = type_page(
    "commercial-contract-review.html",
    "Commercial Property Contract Review NSW | AI for Property Lawyers | Convex",
    "AI review of NSW commercial contracts of sale: GST and going concern, leases and tenancy schedules, permitted use, adjustments and vendor warranties, tailored to the buyer.",
    "Commercial",
    "AI review of NSW commercial property contracts",
    "For offices, shops, industrial units, warehouses, mixed-use buildings and development sites, whether sold vacant or tenanted. Convex reviews the contract, the vendor's annexures and any leases attached.",
    "Commercial and industrial",
    [
        ("pie", "GST", "Whether the price is GST inclusive or exclusive, going concern and margin scheme conditions, and what happens if a going concern supply is not achieved."),
        ("key", "Leases", "Tenancy schedules and leases attached: rent, term, options, reviews, security and bank guarantees, and assignment of the landlord's interest."),
        ("building", "Permitted use", "Zoning and permitted use from the s10.7 certificate, compared with the buyer's intended use or the tenant's use."),
        ("pen", "Special conditions", "As-is clauses, limits on the purchaser's claims, vendor warranties, and conditions typical of commercial sales."),
        ("stack", "Adjustments", "Outgoings, land tax and rent adjustments, arrears and incentives owed to tenants at completion."),
        ("shield", "Building and site", "Fire safety, environmental and contamination matters, and development consents disclosed in the pack."),
    ],
    ["<strong>The contract</strong> and special conditions",
     "<strong>Title search</strong>, plans and 88B instruments",
     "<strong>Section 10.7 planning certificate</strong>",
     "<strong>Leases</strong>, tenancy schedules and disclosure statements attached to the contract",
     "<strong>Strata plan and by-laws</strong> for commercial strata lots",
     "<strong>Development consents</strong> and fire safety documents where included"],
    [("Owner-occupier", "Vacant possession, fit-out and whether the zoning permits the client's business use are headlined."),
     ("Investor - own name or trust", "Lease terms, rent, security and GST treatment of a going concern sale are prioritised."),
     ("Investor - SMSF", "Leases to related parties and business real property questions are flagged for the fund's adviser."),
     ("Develop: yes", "Zoning, height and floor space controls, consents and site affectations move to the top.")],
    [("Is there a cooling-off period for a commercial contract?",
      "Cooling-off applies to residential property in NSW. Convex confirms the position for the contract and notes any condition that affects it."),
     ("Does Convex review standalone commercial leases?",
      "No. Convex reads leases attached to a contract of sale as part of that review. It does not review a lease on its own."),
     ("Does Convex review business sale contracts?",
      "No. Convex reviews contracts for the sale of land. Contracts for the sale of a business are outside its scope."),
     ("Does Convex give GST advice?",
      "Convex explains how the contract deals with GST and flags inconsistencies, such as a going concern clause with no lease attached. Tax advice remains with the client's accountant.")],
    "Review your next commercial contract with Convex")

DOC_ROWS = [
    ("Contract front page", "Parties, price, deposit, completion period, inclusions, cooling-off and contract edition"),
    ("Special conditions", "Every special condition, rated for the buyer"),
    ("Title search and plans", "Registered proprietor, mortgages, caveats, easements and covenants"),
    ("Section 88B instrument", "Restrictions on use, positive covenants and building controls"),
    ("Section 10.7 planning certificate", "Zoning, permitted use, heritage, flood, bushfire, contamination and acquisition"),
    ("Sewer service diagram", "Whether it is attached and relevant to the lot"),
    ("Swimming pool certificates", "Certificate of compliance or non-compliance and what follows for the buyer"),
    ("Occupation certificates and approvals", "Certificates included in the pack and their relevance to the improvements"),
    ("Home building insurance", "Insurance or owner-builder documents where they apply"),
    ("Strata plan and by-laws", "Lot, unit entitlement, car spaces, exclusive use and by-law obligations"),
    ("Off-the-plan disclosure statement", "Consistency with the contract, draft plan, draft by-laws and finishes"),
    ("Tenancy agreements and leases", "Rent, term, options, bond or security and assignment"),
]

_doc_rows = "".join(f"<tr><th scope='row'>{a}</th><td>{b}</td></tr>" for a, b in DOC_ROWS)

HUB = dict(
    file="contracts-we-review.html", nav="contracts",
    title="Contracts and Documents Convex Reviews | NSW Residential and Commercial",
    desc="Every NSW contract type Convex reviews - established residential, strata, off-the-plan, unregistered land, house and land and commercial - and the documents in the pack it reads.",
    crumb="Contracts we review",
    body=phero("Contracts we review", "NSW contracts and documents Convex reviews",
               "Convex covers the residential and commercial contracts a NSW property practice sees every week, and reads the whole pack attached to each one.")
    + section(head("Contract types", "Choose a contract type") + '<div class="grid g3">'
              + link_card("nsw-residential-contract-review.html", "house", "Established residential", "Houses, townhouses, duplexes and villas on Torrens title, vacant or tenanted.")
              + link_card("strata-contract-review.html", "building", "Strata", "Existing units and townhouses: strata plan, by-laws, levies and defect clauses.")
              + link_card("off-the-plan-contract-review.html", "crane", "Off-the-plan", "Disclosure statements, sunset dates, changes to the plan and deposit terms.")
              + link_card("unregistered-land-contract-review.html", "map", "Unregistered land", "Draft deposited plans, draft 88B instruments and design guidelines.")
              + link_card("house-and-land-contract-review.html", "key", "House and land", "The land contract and its links to the build. Building contracts are excluded.")
              + link_card("commercial-contract-review.html", "store", "Commercial", "GST, leases, permitted use and adjustments for commercial and industrial property.")
              + '</div>')
    + section(head("Documents", "What Convex reads in the pack", "Convex reviews the contract together with every document attached to it.")
              + f'<div class="table-wrap"><table class="compare"><thead><tr><th>Document</th><th>What it covers</th></tr></thead><tbody>{_doc_rows}</tbody></table></div>', "alt")
    + section('<div class="grid g2"><div>' + head("Out of scope", "What Convex does not review")
              + checks(["Building contracts, including the build side of a house and land package",
                        "Contracts for the sale of a business",
                        "Standalone leases not attached to a contract of sale",
                        "Strata inspection reports and building and pest reports",
                        "Contracts for property outside NSW"])
              + '</div><div>' + head("Coming soon", "Next states")
              + checks(['<strong>Victoria:</strong> contracts of sale and section 32 vendor statements <span class="soon">Coming soon</span>',
                        '<strong>Queensland:</strong> contracts and the seller disclosure regime <span class="soon">Coming soon</span>'])
              + '</div></div>')
    + cta_band()
)

PAGES = [HUB, RES, STRATA, OTP, LAND, HL, COMM]
