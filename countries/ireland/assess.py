"""Ireland — implementation assessment of its 3rd-cycle (2021, A/HRC/49/15)
UPR recommendations, graded against the 4th-cycle documentation (session 53):
National Report A/HRC/WG.6/53/IRL/1, OHCHR Compilation /2 and Stakeholders'
Summary /3.

    python scripts/run_assess.py ireland

First pass for expert review. Quotes are verbatim from the three documents.
"""

from __future__ import annotations

from recommendations.models import Grade

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

# theme -> (grade, action_summary, rationale, [(org, doc "1"|"2"|"3", para, quote)])
CLUSTERS = {
    "Equality & non-discrimination": (
        B, "Combat racism, hate speech and hate crime and strengthen protection from discrimination",
        "Ireland launched the National Action Plan Against Racism 2023-2027 "
        "(March 2023), appointed a Special Rapporteur on Racial Equality "
        "(July 2024), enacted the Criminal Justice (Hate Offences) Act 2024 "
        "and the National LGBTIQ+ Inclusion Strategy II (2025); IHREC reports "
        "that hate speech reform was dropped, leaving the 1989 Incitement to "
        "Hatred Act in place, and hate crime is rising.",
        [
            ("Ireland", "1", "19", "was launched on 21 March 2023, the UN International Day for the Elimination of Racial Discrimination"),
            ("Ireland", "1", "24", "provides for increased penalties where certain offences are motivated by hatred"),
            ("IHREC", "3", "3", "hate speech reform had been dropped from the legislative agenda, leaving the ineffective Prohibition of Incitement to Hatred Act 1989 in place"),
        ],
    ),
    "Ratification of & accession to international instruments": (
        C, "Ratify outstanding international instruments",
        "Ireland acceded to the Optional Protocol to the CRPD (October 2024) "
        "and is preparing OPCAT and the OP on the sale of children, but "
        "ICPPED and OP-ICESCR are not ratified and Ireland has no plans to "
        "sign the Migrant Workers Convention.",
        [
            ("Ireland", "1", "10", "Ireland intends to ratify the International Convention for the Protection of All Persons from Enforced Disappearance (ICPPED) as soon as practicable"),
            ("Ireland", "1", "10", "the question of ratification remains under consideration by Government"),
        ],
    ),
    "Discrimination against women": (
        B, "Close the gender pay gap and promote gender equality",
        "Ireland launched the National Strategy for Women and Girls 2025-2030, "
        "the Gender Pay Gap Information Act 2021 and portal, the Work Life "
        "Balance Act 2023 and expanded childcare funding to €1.48 billion; "
        "the 2024 referendum on Article 41.2 was defeated and CEDAW notes a "
        "9.6% pay gap.",
        [
            ("Ireland", "1", "27", "was launched in November 2025"),
            ("Ireland", "1", "34", "Gender pay gap reporting is being delivered on a phased basis"),
            ("Committee on the Elimination of Discrimination against Women", "2", "33", "persistent gender pay gap of 9.6 per cent and a gender pension gap of 36 per cent"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        B, "Prevent and combat human trafficking and protect victims",
        "The Third National Action Plan 2023-2027 was launched (November 2023) "
        "and the Criminal Law (Sexual Offences and Human Trafficking) Act "
        "2024 enacted; CEDAW notes low prosecution and conviction rates and "
        "gaps in victim identification.",
        [
            ("Ireland", "1", "56", "launched in November 2023"),
            ("Committee on the Elimination of Discrimination against Women", "2", "29", "persistently low prosecution and conviction rates"),
        ],
    ),
    "Members of minorities": (
        B, "Inclusion of Travellers and Roma",
        "The National Traveller and Roma Inclusion Strategy II 2024-2028 was "
        "approved (July 2024) with a Steering Committee, annual report and "
        "Education Strategy; over €160 million funded Traveller accommodation, "
        "while only 96 units were built in 2019-2024 according to the Traveller "
        "Movement.",
        [
            ("Ireland", "1", "38", "were approved by Government and announced in July 2024"),
            ("Ireland", "1", "39", "Between 2020 and 2025, over €160 million was drawn down by local authorities for Traveller-specific accommodation"),
            ("Council of Europe", "3", "53", "Travellers and Roma continued to face structural anti-Traveller racism and antigypsyism, including over-policing"),
        ],
    ),
    "Constitutional & legislative framework": (
        B, "Implement CRPD legislation, electoral and technology legislation",
        "The Assisted Decision-Making (Capacity) Act 2015 was fully "
        "commenced (April 2023), the Mental Health Act 2026 enacted and a "
        "review of the Disability Act launched; the Equality (Miscellaneous "
        "Provisions) Bill 2024 is not yet enacted and ICERD is not "
        "incorporated.",
        [
            ("Ireland", "1", "48", "full commencement of the Assisted Decision-Making (Capacity) Act 2015 in April 2023"),
            ("Committee on the Elimination of Discrimination against Women", "2", "7", "noted with concern that the equality (miscellaneous provisions) bill of 2024 had not been enacted"),
        ],
    ),
    "Sexual & gender-based violence": (
        B, "Strengthen the response to domestic, sexual and gender-based violence",
        "Ireland launched the Third National Strategy (2022-2026), created the "
        "statutory agency Cuan (January 2024), increased DSGBV funding to almost "
        "€80 million and created offences of stalking and non-fatal "
        "strangulation; CEDAW notes there is no femicide offence and IHREC "
        "reports rising demand.",
        [
            ("Ireland", "1", "51", "was launched in June 2022 and is implemented through action plans"),
            ("Ireland", "1", "53", "created standalone offences of stalking and non-fatal strangulation, strengthened harassment law"),
            ("Committee on the Elimination of Discrimination against Women", "2", "48", "the absence of legislation criminalizing femicide, familicide and domestic homicide"),
        ],
    ),
    "Conditions of detention": (
        B, "Reduce prison overcrowding and improve conditions",
        "A Prison Overcrowding Response Group (2023), €527 million capital "
        "investment and 232 new spaces were delivered, and Mandela Rules "
        "safeguards on solitary confinement introduced; prisons still operate "
        "at 124% of capacity.",
        [
            ("Ireland", "1", "60", "as of 10 March 2026, the system was operating at 124% of total maximum capacity"),
            ("Ireland", "1", "60", "Since 2024, 232 new spaces have been constructed"),
            ("IPRT", "3", "21", "5,850 people in custody against a bed capacity of 4,736"),
        ],
    ),
    "Right to adequate housing": (
        B, "Address homelessness and the affordability of housing",
        "Delivering Homes, Building Communities 2025-2030 was published and 36,284 "
        "homes were completed in 2025; IHREC reports that the housing crisis has "
        "worsened since 2021 and homelessness figures have doubled.",
        [
            ("Ireland", "1", "68", "In 2025, 36,284 homes were completed"),
            ("IHREC", "3", "5", "Ireland's housing crisis had significantly worsened since 2021, with homelessness figures doubling"),
        ],
    ),
    "Sexual & reproductive health and rights": (
        B, "Remove barriers to reproductive health services",
        "A Free Contraception Scheme (2022), a National Sexual Health "
        "Strategy 2025-2035 and the Safe Access Zones Act 2024 were adopted; "
        "CEDAW and IHREC report that the recommendations of the 2023 review of "
        "the Termination of Pregnancy Act (including the three-day waiting "
        "period) were not implemented.",
        [
            ("Ireland", "1", "78", "was signed into law in May 2024 and commenced in October 2024"),
            ("Committee on the Elimination of Discrimination against Women", "2", "39", "failure to implement the recommendations of the 2023 independent review of the Health (Regulation of Termination of Pregnancy) Act of 2018"),
        ],
    ),
    "Persons with disabilities: independence, inclusion": (
        B, "Inclusion and rights of persons with disabilities",
        "The National Human Rights Strategy for Disabled People 2025-2030 was "
        "launched (September 2025) with a Delivery and Monitoring Committee, and "
        "the OP-CRPD was acceded to; IHREC reports a de facto policy of "
        "institutionalisation.",
        [
            ("Ireland", "1", "44", "launch of the National Human Rights Strategy for Disabled People 2025–2030"),
            ("IHREC", "3", "11", "a chronic lack of community-based supports and a de facto policy of institutionalisation"),
        ],
    ),
    "Racial discrimination": (
        B, "Eliminate racism, racist hate speech and racial profiling",
        "The National Action Plan Against Racism 2023-2027 and the Hate Offences "
        "Act 2024 were adopted and a Special Rapporteur appointed; racist hate "
        "speech provisions were omitted and racial profiling is only prohibited "
        "by policy.",
        [
            ("Ireland", "1", "21", "In July 2024, Dr Ebun Joseph was appointed Special Rapporteur on Racial Equality and Racism"),
            ("Ireland", "1", "25", "It prohibits racial profiling and unjustified use of diversity or minority grounds in informing policing policy or activity"),
            ("JS4", "3", "19", "widespread evidence of racial profiling, discriminatory conduct and inadequate cultural sensitivity by An Garda Síochána"),
        ],
    ),
    "Children: definition": (
        B, "Promote and protect children's rights",
        "Young Ireland (2023-2028), a National Child Poverty Target (3% by 2030), "
        "a Child Poverty and Well-being Programme Office and a participation "
        "action plan were adopted; child consistent poverty rose to 8.5% in 2024 "
        "(OCO).",
        [
            ("Ireland", "1", "81", "to reduce child consistent poverty to 3% or less by the end of 2030"),
            ("OCO", "3", "37", "8.5 per cent of children were living in consistent poverty in 2024, up from 4.8 per cent in 2023"),
        ],
    ),
    "Migrants": (
        B, "Protect migrants and promote their integration",
        "Ireland approved a Comprehensive Accommodation Strategy (March 2024) "
        "and plans a new National Migration and Integration Strategy (2026); "
        "the previous integration strategy ended in 2021 and 649 applicants "
        "were unaccommodated.",
        [
            ("Ireland", "1", "87", "the Government approved a Comprehensive Accommodation Strategy in March 2024"),
            ("Ireland", "1", "49", "the Programme for Government 2025 commits to developing a new National Migration and Integration Strategy"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        B, "Resource the Irish Human Rights and Equality Commission",
        "IHREC funding rose to €10.5 million (2026) and staff from 62 to 87, "
        "but CEDAW finds it not adequately resourced for its expanded mandate.",
        [
            ("Ireland", "1", "6", "It received €9.7 million in 2025 and has been allocated €10.5 million in 2026, while staffing increased from 62 in December 2020 to 87 in December 2025"),
            ("Committee on the Elimination of Discrimination against Women", "2", "9", "was not adequately resourced to effectively discharge its expanded mandate"),
        ],
    ),
    "Right to health": (
        B, "Resource the health system, mental health and intercultural health",
        "Sláintecare, record health spending (+112% 2012-2025) and Sharing the "
        "Vision 2020-2030 are in place and the Mental Health Act 2026 was "
        "enacted; IHREC notes Ireland remains an outlier without universal "
        "healthcare.",
        [
            ("Ireland", "1", "76", "total health expenditure rising by 112% between 2012 and 2025"),
            ("Ireland", "1", "79", "enacted in May 2026, provides for a more rights-based and person-centred approach"),
        ],
    ),
    "Right to education": (
        B, "Equitable access to quality education",
        "The DEIS Strategy to 2035 (March 2026), the free schoolbooks scheme, "
        "hot school meals in all primary schools (September 2025) and nearly "
        "1,450 new special classes widen access; the CRC notes persistent "
        "barriers for disadvantaged children and the free primary and "
        "post-primary guarantee is not legislated.",
        [
            ("Ireland", "1", "72", "published in March 2026"),
            ("Ireland", "1", "73", "Almost 1,450 new special classes have been sanctioned and sixteen new special schools established over the last four years"),
        ],
    ),
    "Refugees & asylum seekers": (
        B, "Protect refugees and asylum seekers",
        "The International Protection Act 2026 gives effect to the EU Pact and "
        "designates HIQA as the monitoring body for accommodation; UNHCR "
        "criticises provisions on child detention and family reunification and "
        "reports that about 90% of accommodation is not independently monitored.",
        [
            ("Ireland", "1", "89", "gives effect to the EU Migration and Asylum Pact, designates HIQA as the monitoring body for accommodation centres"),
            ("UNHCR", "2", "59", "approximately 90 per cent of accommodation settings neither independently monitored nor required to comply with the national standards as of late 2025"),
        ],
    ),
    "Administration of justice & fair trial": (
        B, "Reform the civil legal aid system",
        "An independent Review Group on civil legal aid was set up in June 2022 "
        "and reported in 2025; its recommendations are 'under consideration' "
        "and the Legal Aid Board warns the system risks collapse in 2026.",
        [
            ("Ireland", "1", "12", "An independent Review Group was established in June 2022 to examine the Civil Legal Aid Scheme"),
            ("JS9", "3", "17", "had not yet introduced substantive reforms"),
        ],
    ),
    "Violence against women": (
        B, "Eliminate violence against women and girls",
        "The Third National Strategy, Cuan and stalking and strangulation "
        "offences strengthened the response; CEDAW notes persistent GBV and "
        "the absence of a femicide offence.",
        [
            ("Ireland", "1", "52", "the dedicated statutory agency for DSGBV"),
            ("Committee on the Elimination of Discrimination against Women", "2", "48", "the absence of legislation criminalizing femicide, familicide and domestic homicide"),
        ],
    ),
    "Persons with disabilities: definition, general principles": (
        B, "Reform the legal and policy framework to meet CRPD standards",
        "Ireland acceded to the OP-CRPD, launched the 2025-2030 Strategy and "
        "reviews the Disability Act; the Assessment of Need system is under "
        "strain (20,000 children overdue).",
        [
            ("Ireland", "1", "47", "A public consultation to inform the review of the Disability Act 2005 was launched in June 2026"),
            ("AsIAm", "3", "52", "over 20,000 children overdue an assessment"),
        ],
    ),
    "Children: protection against exploitation": (
        B, "Protect children from sexual exploitation and abuse in institutions",
        "The Supports for Survivors of Residential Institutional Abuse Act 2025 "
        "provides supports to about 9,400 survivors; IHREC reports that no "
        "individual has been prosecuted for institutional abuse.",
        [
            ("Ireland", "1", "66", "was passed by the Oireachtas in July 2025"),
            ("IHREC", "3", "4", "no individual had been prosecuted for institutional abuse"),
        ],
    ),
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)": (
        B, "Strengthen safeguards against torture in prisons and institutions",
        "Human rights and prison oversight training is provided to prison "
        "recruits and Mandela Rules safeguards were introduced; the CPT reports "
        "deteriorating safety and conditions that may amount to inhuman or "
        "degrading treatment.",
        [
            ("Ireland", "1", "59", "Human rights training is provided to new recruits to the Irish Prison Service"),
            ("Council of Europe", "3", "21", "conditions that may amount to inhuman and degrading treatment"),
        ],
    ),
    "Business & Human Rights": (
        C, "Prevent harm by Irish companies abroad and adopt a second business and human rights action plan",
        "A second National Action Plan on Business and Human Rights is only "
        "'in development' (six years overdue); the Occupied Territories Bill was "
        "narrowed and the EU due diligence directive is to be transposed by July "
        "2028.",
        [
            ("Ireland", "1", "90", "committed to transposing the EU Corporate Sustainability Due Diligence Directive"),
            ("Stakeholders", "3", "46", "A second National Action Plan on Business and Human Rights was six years overdue"),
        ],
    ),
    "Human rights & the environment": (
        B, "Integrate human rights and environment in trade and investment",
        "Ireland supports sustainable-development provisions in EU trade "
        "agreements.",
        [
            ("Ireland", "1", "90", "Ireland promotes human rights, environmental protection and sustainable development through trade policy"),
        ],
    ),
    "Human rights & climate change": (
        B, "Climate action and participation of marginalised groups",
        "Climate Action Plan 2025, a National Adaptation Framework (2024) and the "
        "National Dialogue on Climate Action with women and disabled people "
        "were adopted; IHREC reports Ireland on track for only 23% emissions "
        "reductions against the legal 51% target.",
        [
            ("Ireland", "1", "92", "National Dialogue on Climate Action"),
            ("IHREC", "3", "9", "Ireland was on track to achieve only 23 per cent emissions reductions by 2030"),
        ],
    ),
    "Advancement of women": (
        B, "Strengthen the national machinery for women's advancement",
        "A National Strategy for Women and Girls 2025-2030 with a Monitoring "
        "Committee and Interdepartmental Committee was launched.",
        [
            ("Ireland", "1", "27", "was launched in November 2025"),
        ],
    ),
    "Right to an adequate standard of living": (
        B, "Equitable access to health, education and housing",
        "The Roadmap for Social Inclusion 2026-2030 (May 2026), the housing plan "
        "and expanded health and education supports address living standards.",
        [
            ("Ireland", "1", "50", "73 of its 81 commitments were delivered"),
        ],
    ),
    "Rights related to name, identity & nationality": (
        A, "Birth information and tracing for people in institutional care",
        "The Birth Information and Tracing Act 2022 is in force, with over "
        "18,100 information applications received; JS14 reports redaction of "
        "some records.",
        [
            ("Ireland", "1", "95", "established a right of access to birth certificates, birth and early life information"),
        ],
    ),
    "National Preventive Mechanism (NPM)": (
        B, "Designate a national preventive mechanism",
        "The General Scheme of the Inspection of Places of Detention Bill "
        "(June 2022) designates the Inspector of Prisons and IHREC; drafting "
        "continues with publication expected in 2026.",
        [
            ("Ireland", "1", "8", "The General Scheme of the Inspection of Places of Detention Bill was approved by Government in June 2022"),
            ("Ireland", "1", "8", "drafting work is underway with a view to publication later in 2026"),
        ],
    ),
    "Freedom of thought, conscience & religion": (
        B, "Choice of school types",
        "A Schools Reconfiguration for Diversity process and an action plan to "
        "increase multi-denominational primary schools are under way; the "
        "Human Rights Committee notes that more than half of secondary schools "
        "are under religious patronage.",
        [
            ("Ireland", "1", "71", "Ireland is taking forward a Schools Reconfiguration for Diversity process to increase multi-denominational primary provision"),
            ("Human Rights Committee", "2", "25", "more than half of secondary schools were under religious patronage"),
        ],
    ),
    "Freedom of association": (
        C, "Eliminate barriers and restrictions on civil society engagement, including by amending legislation",
        "Civil society concerns about the definition of 'political purposes' "
        "in the Electoral Act 1997 are only being examined, and the CESCR "
        "notes constraints on advocacy under the Charities Act 2009.",
        [
            ("Ireland", "1", "17", "are being examined as part of a review by An Coimisiún Toghcháin"),
            ("Committee on Economic, Social and Cultural Rights", "2", "21", "civil society faced constraints in engaging in political advocacy in the context of the Charities Act of 2009"),
        ],
    ),
    "Economic, social & cultural rights - general measures of implementation": (
        B, "Strengthen consultation mechanisms on economic, social and cultural rights",
        "A National Civic Forum, Public Participation Networks in each local "
        "authority area (over 18,000 groups) and a Human Rights Committee "
        "chaired by the Department of Foreign Affairs provide consultation.",
        [
            ("Ireland", "1", "14", "provides a mechanism for formal dialogue between the State and the community and voluntary sector"),
        ],
    ),
    "Children: juvenile justice": (
        B, "Implement the Youth Justice Strategy 2021-2027",
        "92 Youth Diversion Projects operate and youth justice funding almost "
        "doubled between 2020 and 2026; the CRC urges raising the age of "
        "criminal responsibility to 14.",
        [
            ("Ireland", "1", "84", "There are 92 Youth Diversion Projects and four Targeted Youth Diversion Projects operating nationwide"),
        ],
    ),
    "Inter-State cooperation and assistance": (
        D, "Avoid contributing to violations from unilateral coercive measures",
        "The documents contain no information on this ask.", [],
    ),
    "Rights related to marriage & family": (
        B, "Policies to support the family",
        "Childcare funding rose to €1.48 billion, parental leave was extended and "
        "a National Childcare Scheme operates.",
        [
            ("Ireland", "1", "30", "allocation for Early Learning and Childcare increasing from approximately €638 million in 2021 to €1.48 billion in Budget 2026"),
        ],
    ),
    "National Mechanisms for Reporting & Follow-up (NMRF)": (
        D, "Permanent national mechanism for implementation, reporting and follow-up",
        "The documents contain no information on this ask.", [],
    ),
}

KEYWORDS = [
    # --- ratification ---
    (r"Optional Protocol to the Convention on the Rights of Persons with Disabilities", A,
     "Ratify the Optional Protocol to the Convention on the Rights of Persons with Disabilities",
     "Ireland acceded to the OP-CRPD on 31 October 2024 (in force 30 November 2024).",
     [("Ireland", "1", "7", "Ireland acceded to the Optional Protocol to the United Nations Convention on the Rights of Persons with Disabilities (UNCRPD) on 31 October 2024")]),
    (r"Optional Protocol to the Convention on the Rights of the Child on the sale", B,
     "Ratify the Optional Protocol to the CRC on the sale of children",
     "Ireland states that legislative barriers have been addressed (2017 and 2024 Acts) and it will proceed with the remaining steps; ratification is still pending.",
     [("Ireland", "1", "9", "Ireland will now proceed with the remaining steps required for ratification, subject to Government approval"),
      ("OCO", "3", "13", "the delay in ratifying the OP-CRC-SC")]),
    (r"Optional Protocol to the Convention against Torture", B,
     "Ratify the Optional Protocol to the Convention against Torture and designate a national preventive mechanism",
     "The General Scheme of the Inspection of Places of Detention Bill was approved by Government in June 2022; drafting continues for publication in 2026 and ratification awaits it. IHREC is designated coordinating body of the NPM.",
     [("Ireland", "1", "8", "The General Scheme of the Inspection of Places of Detention Bill was approved by Government in June 2022"),
      ("Ireland", "1", "8", "drafting work is underway with a view to publication later in 2026")]),
    (r"^(Sign and ratify|Consider ratifying|Consider the possibility of ratifying|Ratify) the International Convention on the Protection of the Rights of All Migrant Workers", E,
     "Ratify the Convention on the Rights of All Migrant Workers",
     "Ireland states that it has not signed the Convention and that there are currently no plans to sign or ratify it.",
     [("Ireland", "1", "10", "While there are currently no plans to sign or ratify the ICRMW, the position remains under review")]),
    # --- racism / hate ---
    (r"^(Develop a new national action plan against racism|Adopt a national action plan against racism|Develop a national action plan against racism|Finalize and fully implement the national action plan against racism)|national action plan against racism with clear indicators, deadlines and resources", A,
     "Adopt and implement a national action plan against racism",
     "The National Action Plan Against Racism 2023-2027 was launched on 21 March 2023 and is overseen by a Special Rapporteur and an Advisory Committee, with annual reports; the 2026 Special Rapporteur report identifies remaining gaps.",
     [("Ireland", "1", "19", "was launched on 21 March 2023, the UN International Day for the Elimination of Racial Discrimination"),
      ("Ireland", "1", "21", "In July 2024, Dr Ebun Joseph was appointed Special Rapporteur on Racial Equality and Racism")]),
    (r"International Holocaust Remembrance Alliance", A,
     "Adopt the IHRA working definition of antisemitism",
     "Ireland endorsed the IHRA working definition in January 2025.",
     [("Ireland", "1", "23", "Ireland endorsed the International Holocaust Remembrance Alliance (IHRA) working definition of antisemitism in January of 2025")]),
    (r"^Amend the Prohibition of Incitement to Hatred Act 1989", C,
     "Amend the Prohibition of Incitement to Hatred Act 1989",
     "The 1989 Act remains in force and IHREC reports that hate speech reform was dropped from the legislative agenda.",
     [("IHREC", "3", "3", "hate speech reform had been dropped from the legislative agenda, leaving the ineffective Prohibition of Incitement to Hatred Act 1989 in place")]),
    (r"ban on racial profiling|legislation that prohibits the use of racial profiling|introduce legislation prohibiting ethnic profiling|prohibiting controls based on ethnic profiling", C,
     "Legislate against racial and ethnic profiling and establish an independent complaints mechanism",
     "An Garda Síochána prohibits racial profiling by policy only, there is no legislative ban and the Garda Síochána (Powers) Bill 2026 lacks demographic data collection provisions.",
     [("Ireland", "1", "25", "It prohibits racial profiling and unjustified use of diversity or minority grounds in informing policing policy or activity"),
      ("JS4", "3", "19", "widespread evidence of racial profiling, discriminatory conduct and inadequate cultural sensitivity by An Garda Síochána")]),
    (r"^Conduct impartial and independent investigations into the excessive use of violence by the security forces against people of African descent", D,
     "Investigate excessive use of violence by security forces against people of African descent",
     "The documents contain no information on this ask.", []),
    (r"Investigate cases of hate speech, including by politicians", C,
     "Investigate hate speech, including by politicians",
     "IHREC reports that hate crimes and incidents are rising with a chilling effect on political participation; the National Report gives no information on hate speech by politicians.",
     [("IHREC", "3", "3", "Hate crimes and incidents were on the rise, fuelled by far-right actors and online incitement, with a chilling effect on political participation")]),
    (r"Enact legislation to prohibit .conversion therap", C,
     "Prohibit conversion practices",
     "The Programme for Government 2025 only commits to advancing legislation; no bill is reported, and the Human Rights Committee reports continued practice.",
     [("Ireland", "1", "36", "The Programme for Government 2025 commits to advancing legislation to ban conversion practices"),
      ("Human Rights Committee", "2", "57", "reports of the continued practice of conversion therapy")]),
    (r"^Pursue its efforts to strengthen and increase national programmes for social inclusion", A,
     "Strengthen national programmes for social inclusion",
     "The Roadmap for Social Inclusion 2020-2025 delivered 73 of 81 commitments and a successor Roadmap 2026-2030 was published in May 2026.",
     [("Ireland", "1", "50", "73 of its 81 commitments were delivered"),
      ("Ireland", "1", "50", "was published in May 2026 following public consultation")]),
    # --- constitutional / legislative ---
    (r"International Convention on the Elimination of All Forms of Racial Discrimination", C,
     "Incorporate ICERD into domestic law",
     "No incorporation is reported; Ireland maintains that its dualist system does not require direct incorporation of treaties.",
     [("Human Rights Committee", "2", "6", "had not taken steps to incorporate the Covenant into the domestic legal order and had no intention to do so")]),
    (r"^Revise the law on the Irish Human Rights and Equality Commission", C,
     "Extend the IHREC's powers to all rights in the ICESCR",
     "No revision of the 2014 Act is reported; the CESCR reiterates its recommendation.",
     [("Committee on Economic, Social and Cultural Rights", "2", "9", "reviewing the Irish Human Rights and Equality Commission Act of 2014")]),
    (r"^(Consider expanding the mandate of the Irish Human Rights and Equality Commission|Expand the mandate of the national commission)", C,
     "Expand the IHREC's mandate to the prevention and prohibition of racial discrimination",
     "No expansion of the mandate is reported; the National Report refers only to IHREC's existing mandate to promote intercultural understanding.",
     [("Ireland", "1", "6", "IHREC also has a mandate under equality legislation to promote intercultural understanding")]),
    # --- women ---
    (r"^Encourage youth initiatives", D,
     "Youth initiatives on gender equality",
     "The documents contain no information on this ask.", []),
    (r"article 41 \(2\)|articles 40 and 41", B,
     "Amend Article 41.2 of the Constitution",
     "The Government put a constitutional amendment to a referendum in 2024 proposing to delete Article 41.2; it was defeated and CEDAW recommends a new referendum.",
     [("Committee on the Elimination of Discrimination against Women", "2", "5", "the 2024 constitutional referendum proposing to delete article 41.2 of the Constitution and replace it with gender-neutral language about care had been defeated")]),
    (r"Magdalene laundries", B,
     "Investigate and redress ill-treatment of women in the Magdalene laundries",
     "Ireland pays redress through the Magdalen Restorative Justice Ex Gratia Scheme (€33.4 million to 834 applicants) and reviewed the scheme in March 2026; the Human Rights Committee and IHREC report impunity and no prosecutions.",
     [("Ireland", "1", "65", "€33.4 million has been paid in lump sum awards to 834 applicants"),
      ("Human Rights Committee", "2", "16", "remained concerned about the climate of impunity")]),
    # --- trafficking ---
    (r"reinstate a dedicated anti-trafficking unit", B,
     "National action plan on modern slavery and a dedicated anti-trafficking unit",
     "A Third National Action Plan 2023-2027 was launched; JS1 recommends a costed, time-bound framework.",
     [("Ireland", "1", "56", "launched in November 2023"),
      ("JS1", "3", "28", "develop a costed, time-bound implementation framework")]),
    # --- minorities ---
    (r"^(Finalize its next Traveller and Roma inclusion strategy|Ensure that the new national Traveller and Roma integration strategy|Develop specific programmes that address the vulnerabilities of the Roma|Continue applying the current National Traveller and Roma Inclusion Strategy beyond 2021)", A,
     "Adopt and implement the next National Traveller and Roma Inclusion Strategy",
     "NTRIS II 2024-2028 and its first Action Plan 2024-2026 were approved in July 2024, with a stronger Roma focus, a Steering Committee, a Traveller and Roma Forum and an annual report (2025).",
     [("Ireland", "1", "38", "were approved by Government and announced in July 2024"),
      ("Ireland", "1", "40", "places a stronger focus on Roma inclusion than its predecessor")]),
    (r"^Promote the enactment of legislation that facilitates the integration of ethnic minority groups", C,
     "Enact legislation to integrate ethnic minority groups",
     "The previous Migrant Integration Strategy ended in 2021 and a new strategy is only expected in 2026; no legislation is reported.",
     [("Ireland", "1", "49", "The previous Migrant Integration Strategy concluded in 2021")]),
    # --- violence ---
    (r"^Finalize the adoption of the third national strategy on domestic, sexual and gender-based violence", A,
     "Adopt the third national strategy on domestic, sexual and gender-based violence",
     "The Third National Strategy (Zero Tolerance, 2022-2026) was launched in June 2022; a successor strategy 2027-2031 is under development.",
     [("Ireland", "1", "51", "was launched in June 2022 and is implemented through action plans")]),
    # --- detention ---
    (r"^Investigate thoroughly and impartially all cases of abuse of authority by prison staff", C,
     "Investigate abuse of authority by prison staff",
     "The CPT reports sharply increased allegations of severe abuse by staff and the National Report describes only oversight bodies and a new complaints system under development.",
     [("Council of Europe", "3", "21", "physical safety in male prisons had deteriorated sharply with increased allegations of severe abuse by staff"),
      ("Ireland", "1", "60", "Work is also underway to modernise Prison Visiting Committees")]),
    # --- SRHR ---
    (r"^Establish an action plan to ensure the access and availability of safe abortion services", C,
     "Action plan for safe abortion services",
     "No action plan is reported; IFPA and CEDAW report the O'Shea review recommendations were not implemented.",
     [("Committee on the Elimination of Discrimination against Women", "2", "39", "failure to implement the recommendations of the 2023 independent review of the Health (Regulation of Termination of Pregnancy) Act of 2018")]),
    # --- disabilities ---
    (r"^Develop a strategy to address the marginalization of people with disabilities", A,
     "Develop a strategy to address the marginalisation of people with disabilities",
     "The National Human Rights Strategy for Disabled People 2025-2030 (23 commitments, three programme plans) was launched in September 2025.",
     [("Ireland", "1", "44", "launch of the National Human Rights Strategy for Disabled People 2025–2030")]),
    # --- children / institutions ---
    (r"^Provide an apology for the serious violations suffered by mixed-race children", C,
     "Apologise and provide reparations to mixed-race children in institutions",
     "The 2026 Special Rapporteur report identifies gaps in recognition, justice and redress, and AMRI reports that mixed-race children continue to be denied adequate reparations.",
     [("AMRI", "3", "20", "continued to be denied adequate reparations as adults")]),
    (r"^Take further measures to promote the rights of the child, especially in its COVID-19 response", D,
     "Promote children's rights in the COVID-19 response",
     "The documents contain no information on this ask.", []),
    (r"^Sign the Declaration on Children, Youth and Climate Action", D,
     "Sign the Declaration on Children, Youth and Climate Action",
     "The documents contain no information on this ask.", []),
    (r"^Cease torture and other cruel or inhuman treatment of children in places of reform", C,
     "Prosecute abuse of children in reform and industrial schools",
     "Supports for survivors were legislated (2025) but IHREC reports that no individual has been prosecuted for institutional abuse.",
     [("IHREC", "3", "4", "no individual had been prosecuted for institutional abuse")]),
    # --- migrants / asylum ---
    (r"direct provision", C,
     "End direct provision and establish a new international protection support service",
     "The Government revisited the assumptions of the 2021 White Paper that was to end direct provision, adopted a Comprehensive Accommodation Strategy relying on emergency accommodation and is unable to offer accommodation to all single men; UNHCR reports about 90% of accommodation is not independently monitored.",
     [("Ireland", "1", "87", "required a review of the assumptions underpinning the White Paper to End Direct Provision"),
      ("Ireland", "1", "88", "IPAS remains unable to offer accommodation to all single male applicants")]),
    (r"^(Take further measures to protect and respect the rights of migrant workers|Adopt measures to improve the protection of refugees, migrants and asylum seekers by fully incorporating)", C,
     "Protect migrant workers and refugees in law",
     "Ireland says there are no plans to sign the ICRMW; the International Protection Act 2026 raises concerns for UNHCR on child detention and family reunification.",
     [("Ireland", "1", "10", "While there are currently no plans to sign or ratify the ICRMW, the position remains under review"),
      ("UNHCR", "2", "59", "provisions in the international protection bill of 2026 permitting the detention of children during the screening stage")]),
    # --- health ---
    (r"intersex children", D,
     "Health-care protocol for intersex children",
     "The documents contain no information on this ask; the Human Rights Committee asks that non-consensual sex assignment be prohibited.",
     []),
    # --- education ---
    (r"^(Consider introducing a legislative guarantee of free primary and secondary education|Fully implement the Education for Persons with Special Educational Needs Act 2004)", C,
     "Legislate free education and fully implement the EPSEN Act",
     "Free primary education is constitutional and free post-primary education is policy since 1967; UNESCO recommends legislating 12 years of free education and the CRC notes barriers for disadvantaged children and the use of special classes.",
     [("UNESCO", "2", "8", "guarantee in legislation at least 12 years of free primary and secondary education"),
      ("Committee on the Rights of the Child", "2", "41", "the establishment of special classes for children with disabilities")]),
    # --- civil legal aid ---
    (r"^Undertake a comprehensive and independent review of the legal aid system for civil cases", A,
     "Undertake a comprehensive and independent review of the civil legal aid system",
     "An independent Review Group on the Civil Legal Aid Scheme was established in June 2022 and reported in July 2025; reforms are still to follow.",
     [("Ireland", "1", "12", "An independent Review Group was established in June 2022 to examine the Civil Legal Aid Scheme"),
      ("JS9", "3", "17", "had undertaken an independent review of its civil legal aid scheme, published in July 2025")]),
    (r"^Broaden efforts to increase legal and financial aid", C,
     "Increase legal and financial aid for the vulnerable, migrants and asylum seekers",
     "The Review Group's recommendations are only 'under consideration'; waiting times reach 69 weeks and the Legal Aid Board warns of collapse in 2026.",
     [("JS9", "3", "17", "waiting times of up to 69 weeks for a first consultation"),
      ("Ireland", "1", "12", "are currently under consideration, taking into account findings from Ireland’s first national legal needs survey")]),
    # --- environment ---
    (r"^Recognize in its national legislation the right to a healthy, clean and sustainable environment", C,
     "Recognise the right to a healthy environment in national legislation",
     "No recognition is reported; IHREC recommends a constitutional referendum on environmental protection.",
     [("IHREC", "3", "9", "hold a referendum to amend the Constitution to include provisions on the protection of biodiversity and the environment")]),
]

FALLBACK = (D, "No information on this ask",
            "The documents contain no information on this ask.", [])
