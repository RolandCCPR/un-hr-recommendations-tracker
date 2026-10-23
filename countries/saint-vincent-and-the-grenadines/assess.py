"""Saint Vincent and the Grenadines — implementation assessment of its 3rd-cycle
(2021, A/HRC/49/10) UPR recommendations, graded against the 4th-cycle
documentation (session 53): OHCHR Compilation A/HRC/WG.6/53/VCT/2 and
Stakeholders' Summary /3. The National Report (/1) was not yet available at
the time of assessment, so the evidence on the State's own measures is thin.

    python scripts/run_assess.py saint-vincent-and-the-grenadines

First pass for expert review. Quotes are verbatim from the documents.
"""

from __future__ import annotations

from recommendations.models import Grade

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

# theme -> (grade, action_summary, rationale, [(org, doc "1"|"2"|"3", para, quote)])
CLUSTERS = {
    "Ratification of & accession to international instruments": (
        C, "Ratify outstanding treaties and optional protocols",
        "The country has ratified the major core treaties but not ICPPED, the "
        "Second Optional Protocol to the ICCPR, OP-CAT, OP-CEDAW, OP-ICESCR, "
        "OP-CRC on communications or the American Convention; no ratification "
        "in the review period is reported.",
        [
            ("United Nations subregional team in Barbados", "2", "3", "had not ratified the Second Optional Protocol to the International Covenant on Civil and Political Rights"),
            ("JS1", "3", "2", "had not yet ratified several important treaties, including the International Convention for the Protection of All Persons from Enforced Disappearances"),
        ],
    ),
    "Equality & non-discrimination": (
        C, "Adopt comprehensive anti-discrimination legislation",
        "The Constitution covers only six grounds and no comprehensive "
        "anti-discrimination law has been adopted; consensual same-sex conduct "
        "remains criminalised under sections 146 and 148 of the Criminal Code.",
        [
            ("United Nations subregional team", "2", "12", "the legal framework in Saint Vincent and the Grenadines still lacked explicit protections against discrimination based on sexual orientation or gender identity, and that no comprehensive anti-discrimination legislation had been adopted"),
            ("Three submissions", "3", "52", "consensual samesex conduct was criminalized under sections 146 and 148 of the Penal Code"),
        ],
    ),
    "Sexual & gender-based violence": (
        B, "Combat sexual and gender-based violence",
        "A National Task Force on Gender-Based Violence was launched in 2024 "
        "and anti-violence campaigns run; however the Sexual Offences Bill has "
        "been pending for over five years and marital rape, sexual harassment "
        "and domestic violence are not criminal offences.",
        [
            ("United Nations subregional team", "2", "51", "in 2024 the country had launched the National Task Force on Gender-Based Violence"),
            ("JS1", "3", "40", "had been working for over 5 years on a Sexual Offences Bill to update laws in relation to sexual offences under the Criminal Code, but that the bill was still pending"),
        ],
    ),
    "Death penalty": (
        C, "Establish a formal moratorium and abolish the death penalty",
        "A de facto moratorium on executions has been observed since 1995 "
        "but the death penalty is retained, one person remains on death row "
        "and the country votes against the UN moratorium resolution.",
        [
            ("JS4", "3", "11", "had observed a de facto moratorium on executions since 1995 and that one person remained on death row"),
            ("JS4", "3", "11", "had consistently voted against the United Nations General Assembly resolution calling for a global moratorium on the death penalty"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        C, "Establish a Paris-Principles national human rights institution",
        "No independent institution exists and the feasibility study accepted "
        "in the previous cycle has not been carried out; the recommendation "
        "has been repeated in the 2011, 2016 and 2021 cycles.",
        [
            ("JS5", "3", "5", "the State did not have an independent national human rights institution and had not conducted the feasibility study"),
            ("Special Rapporteur on environment", "2", "11", "a recommendation made during the 2011, 2016 and 2021 universal periodic review cycles"),
        ],
    ),
    "Human rights & climate change": (
        B, "Climate policy, adaptation and disaster risk management",
        "The country implements a national climate change policy, climate "
        "strategy and national adaptation plan and the Special Rapporteur was "
        "impressed by its progress; vulnerability remains extreme.",
        [
            ("Special Rapporteur on environment", "2", "45", "pursuant to its national climate change policy, national climate strategy and implementation plan, and national adaptation plan"),
            ("Special Rapporteur on environment", "2", "46", "was impressed by the progress made by Saint Vincent and the Grenadines on many fronts"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        B, "Combat trafficking in persons",
        "The Prevention of Trafficking in Persons Act was amended in 2023 and a "
        "National Action Plan 2021-2025 adopted, but no victim has been "
        "identified since the last review and prosecutions are lacking.",
        [
            ("ILO Committee of Experts", "2", "20", "had been amended in 2023 in regard to the penalties for offences"),
            ("United Nations subregional team", "2", "21", "had adopted a National Action Plan to Combat Trafficking in Persons, for 2021–2025"),
            ("ECLJ", "3", "21", "failure to identify a single victim of human trafficking since the last universal periodic review"),
        ],
    ),
    "Right to education": (
        B, "Strengthen the education system",
        "Education is free and compulsory to age 16 with high literacy and "
        "enrolment; secondary retention, pregnant students and inclusive "
        "education remain gaps.",
        [
            ("CCI", "3", "31", "provided free and compulsory education for children aged 5 to 16 years, covering primary and secondary levels"),
            ("CCI", "3", "31", "declined at the secondary level, reflecting challenges in retention and completion"),
        ],
    ),
    "Right to an adequate standard of living": (
        B, "Poverty reduction and social protection",
        "The Zero Hunger Trust Fund and expanded social protection (with "
        "UNICEF) responded to the 2021 volcanic eruption and COVID-19; about 30% "
        "of the population lived below the poverty line.",
        [
            ("Special Rapporteur on environment", "2", "31", "commended the Zero Hunger Trust Fund, which provided nutritional and financial support to vulnerable children and older persons"),
            ("UNICEF", "2", "30", "the Ministry of National Mobilization had partnered with UNICEF to temporarily expand and strengthen the social protection system"),
        ],
    ),
    "Children: definition": (
        B, "Child poverty and child rights legislation",
        "A National Child Protection Policy has been implemented since 2020, "
        "but corporal punishment remains lawful in schools and at home.",
        [
            ("United Nations subregional team", "2", "53", "had progressively implemented the National Child Protection Policy"),
            ("UNESCO", "2", "54", "the Education Act of 2006 authorized the use of corporal punishment in schools"),
        ],
    ),
    "Children: protection against exploitation": (
        B, "Protect children from violence and sexual exploitation",
        "The National Child Protection Policy provides a multisectoral "
        "framework; sexual abuse of children persists and hazardous-work "
        "legislation lags.",
        [
            ("United Nations subregional team", "2", "53", "a coordinated, multi-sectoral framework for prevention of abuse, neglect, exploitation and violence against children"),
            ("CCI", "3", "46", "reports of sexual abuse and exploitation of children persisted"),
        ],
    ),
    "Cooperation with human rights mechanisms & requests for technical assistance": (
        B, "Seek OHCHR and regional technical assistance",
        "The country sought technical assistance to strengthen reporting and "
        "implementation, with UN-supported capacity-building since 2021, and an "
        "OHCHR Regional Office for the Caribbean was established in 2024.",
        [
            ("United Nations subregional team", "2", "6", "had sought technical assistance to strengthen national reporting capacity and the implementation of treaty body recommendations"),
            ("OHCHR", "2", "9", "In 2024, the OHCHR Regional Office for the Caribbean was established"),
        ],
    ),
    "Cooperation & Follow up with Special Procedures": (
        B, "Standing invitation to special procedures",
        "No standing invitation is reported, but the Special Rapporteur on "
        "the environment visited, the first visit by an independent expert in "
        "almost ten years.",
        [
            ("Special Rapporteur on environment", "2", "8", "his visit was the first in almost 10 years by an independent expert appointed by the Human Rights Council"),
        ],
    ),
    "Rights related to marriage & family": (
        C, "Raise the minimum age of marriage to 18",
        "The Marriage Act still allows marriage with parental consent at 15 "
        "for girls and 16 for boys.",
        [
            ("JS1", "3", "18", "the minimum age of marriage with parental consent was 15 for girls and 16 for boys"),
            ("UNESCO", "2", "19", "amend its legislation to ensure that the minimum age of marriage was 18 years, without exceptions"),
        ],
    ),
    "Violence against women": (
        B, "Strengthen the response to violence against women",
        "A 2024 GBV task force, the Domestic Violence Act 2015 and "
        "anti-violence campaigns exist; underreporting and limited victim "
        "support persist.",
        [
            ("United Nations subregional team", "2", "51", "limited resources for victim support services"),
            ("ICAAD", "3", "42", "Gender Affairs undertook antiviolence campaigns in schools, clinics and communities"),
        ],
    ),
    "Support to victims & witnesses": (
        D, "Support and referral services for victims",
        "The documents contain no specific information on this ask.", [],
    ),
    "Migrants": (
        D, "Access of migrants to services and decriminalisation of irregular entry",
        "The documents contain no information on this ask.", [],
    ),
    "Conditions of detention": (
        B, "Improve prison and detention conditions",
        "The new Belle Isle facility is a significant improvement, but the "
        "older Kingstown prison remains overcrowded and inadequate.",
        [
            ("United Nations subregional team", "2", "13", "the newer Belle Isle detention facility represented a significant improvement in detention infrastructure"),
            ("United Nations subregional team", "2", "13", "the older Kingstown prison reportedly continued to face structural limitations"),
        ],
    ),
    "Right to health": (
        D, "Strengthen the national health system",
        "The documents contain no specific information on measures on this ask.", [],
    ),
    "Labour rights and right to work": (
        C, "Legislate against sexual harassment and employment discrimination",
        "The Employment Relations (Prevention of Sexual Harassment) Bill has "
        "been drafted but not adopted and there is no framework prohibiting "
        "discrimination in employment.",
        [
            ("JS1", "3", "22", "an Employment Relations (Prevention of Sexual Harassment) Bill had been drafted but not yet adopted"),
            ("ILO Committee of Experts", "2", "22", "urged the Government to adopt without further delay an effective framework prohibiting direct and indirect discrimination on all grounds"),
        ],
    ),
    "Constitutional & legislative framework": (
        B, "Bring legislation into line with international obligations",
        "Recent legislation (Domestic Violence Act 2015, 2023 trafficking "
        "amendments) advances alignment, but the Constitution does not "
        "guarantee economic, social, cultural and environmental rights.",
        [
            ("Special Rapporteur on environment", "2", "10", "economic, social, cultural and environmental rights were not guaranteed in the Constitution"),
        ],
    ),
    "Legal & institutional reform": (
        D, "Create appropriate legislative and institutional conditions",
        "The documents contain no information on this ask.", [],
    ),
    "Right to social security": (
        B, "Promote and protect social security",
        "Social protection was expanded after the 2021 eruption.",
        [("UNICEF", "2", "30", "the Ministry of National Mobilization had partnered with UNICEF to temporarily expand and strengthen the social protection system")],
    ),
    "Human rights & poverty": (
        B, "Poverty eradication through social welfare policies",
        "Social welfare programmes (Zero Hunger Trust Fund) are in place; poverty remains significant.",
        [("Special Rapporteur on environment", "2", "31", "commended the Zero Hunger Trust Fund")],
    ),
    "Persons with disabilities: independence, inclusion": (
        C, "Inclusion of persons with disabilities",
        "A comprehensive Disability Bill has been pending for several years.",
        [("JS1", "3", "48", "had had a comprehensive Disability Bill for several years")],
    ),
    "Persons with disabilities: accessibility, mobility": (
        D, "Accessibility of public buildings and transport",
        "The documents contain no information on this ask.", [],
    ),
    "National Mechanisms for Reporting & Follow-up (NMRF)": (
        B, "National mechanism for monitoring and reporting",
        "The National Human Rights Monitoring and Reporting Mechanism was "
        "established in the Ministry of Foreign Affairs to coordinate "
        "implementation, monitoring and reporting of accepted recommendations.",
        [("JS1", "3", "7", "established the National Human Rights Monitoring and Reporting Mechanism in the Ministry of Foreign Affairs")],
    ),
    "Economic & political crisis, natural disasters or other emergencies": (
        B, "Protect the population in emergencies",
        "The State, with UNICEF, expanded social protection and food support "
        "after the 2021 La Soufrière eruption.",
        [("Special Rapporteur on environment", "2", "31", "programmes such as the Love Box, whereby the Government purchased food from farmers needing markets, then donated the food to families displaced for months by the volcanic eruption")],
    ),
    "Liberty & security of the person": (
        D, "Human-rights-centred reform of law enforcement",
        "The documents contain no information on this ask.", [],
    ),
    "Freedom of association": (
        D, "Freedom of association and assembly",
        "The documents contain no information on this ask.", [],
    ),
}

KEYWORDS = [
    # --- ratification-cluster specifics ---
    (r"Hague|Intercountry Adoption", D,
     "Ratify the Hague Intercountry Adoption Convention",
     "The documents contain no information on this ask.", []),
    (r"American Convention", C,
     "Ratify the American Convention on Human Rights",
     "The country has ratified very few OAS human rights treaties; the Special Rapporteur encouraged it to join the inter-American system.",
     [("Special Rapporteur on environment", "2", "5", "encouraged Saint Vincent and the Grenadines to join the inter-American human rights system by becoming a Party to the American Convention on Human Rights")]),
    # --- death penalty specifics ---
    (r"Continue the moratorium on the death penalty", A,
     "Continue the de facto moratorium",
     "A de facto moratorium on executions has been observed since 1995.",
     [("JS4", "3", "11", "had observed a de facto moratorium on executions since 1995")]),
    (r"Maintain the de facto moratorium", B,
     "Maintain the moratorium and commute the last death sentence",
     "The moratorium is maintained but one person remains on death row.",
     [("JS4", "3", "11", "one person remained on death row")]),
    (r"awareness-raising campaign|public awareness campaign|public debates on the topic", D,
     "Awareness-raising on the death penalty",
     "The documents contain no information on awareness-raising on the death penalty.", []),
    # --- SGBV specifics ---
    (r"marital rape|sexual harassment|sexual offences legislation|strengthen laws against sexual crimes|Include domestic violence as a criminal offence|violence as a criminal offence", C,
     "Criminalise marital rape, sexual harassment and domestic violence",
     "The Sexual Offences Bill has been pending for over five years; the Employment Relations (Prevention of Sexual Harassment) Bill is not adopted and domestic violence is treated as a civil matter.",
     [("JS1", "3", "40", "had not implemented the recommendations from the previous universal periodic review related to explicitly making marital rape a crime and enacting a sexual harassment bill"),
      ("JS1", "3", "39", "under the 2015 Domestic Violence Act, domestic violence was treated as a civil matter and not a crime")]),
    (r"public awareness campaigns to end gender-based violence", B,
     "Public awareness campaigns against gender-based violence",
     "Gender Affairs ran anti-violence campaigns in schools, clinics and communities in 2024.",
     [("ICAAD", "3", "42", "Gender Affairs undertook antiviolence campaigns in schools, clinics and communities")]),
    (r"safe and functional institution for victims|creation of an institution for victims|Establish facilities and institutions where victims", C,
     "Establish facilities for victims of violence",
     "Crisis housing exists but access is restricted to those with a court protection order, and victim support services lack resources.",
     [("ICAAD", "3", "44", "improve access to government-established crisis and emergency housing for gender-based violence and domestic violence victims by removing any requirement")]),
    # --- trafficking specifics ---
    (r"Amend the Prevention of Trafficking in Persons Act", A,
     "Amend the Trafficking Act to ensure proportionate penalties",
     "The Act was amended in 2023 to enact stricter penalties.",
     [("ECLJ", "3", "20", "in 2023 Saint Vincent and the Grenadines had amended the Prevention of Trafficking in Persons Act to enact stricter penalties for individuals convicted of human trafficking")]),
    (r"investigate and prosecute|prosecution of perpetrators|Improve the capacity of officials", C,
     "Investigate and prosecute trafficking",
     "There is a decade-long lack of prosecutions and the Anti-Trafficking Unit is underfunded.",
     [("ECLJ", "3", "20", "a decade-long lack of prosecutions and insufficient services for victims")]),
    # --- education specifics ---
    (r"minimum age of work to 16", C,
     "Align the minimum age for work with compulsory schooling",
     "The minimum age for work remains 14 while compulsory schooling lasts to 16.",
     [("ILO Committee of Experts", "2", "40", "the minimum age for work or employment was 14 years and that the age of completion of compulsory education (set at 16 years under the Education Act of 2006) continued to be higher")]),
    (r"retention and re-integration of school-age|special education needs|children with disabilities|inclusive education", D,
     "Retention of pregnant students and inclusive education",
     "The documents contain no specific information on measures on this ask.", []),
    (r"family life education curriculum|comprehensive sexuality education", B,
     "Revise family life and comprehensive sexuality education",
     "The regional CSEC Social Studies syllabus was revised in 2023 to include sexual orientation and gender identity content; the Health and Family Life Education programme has not been revised to the international guidance.",
     [("JS1; JS5", "3", "34", "revised in 2023 to include content addressing issues related to sexual orientation and gender identity")]),
    # --- children ---
    (r"corporal punishment", C,
     "Prohibit corporal punishment",
     "The Education Act authorises corporal punishment in schools and it is lawful at home as 'reasonable punishment'.",
     [("UNESCO", "2", "54", "the Education Act of 2006 authorized the use of corporal punishment in schools"),
      ("CCI", "3", "45", "legally permitted under the concept of 'reasonable punishment'")]),
    (r"sale, sexual|prostitution", D,
     "Legal protection of children from sale and sexual exploitation",
     "The documents contain no information on this ask.", []),
    # --- other ---
    (r"standing invitation", B,
     "Standing invitation to special procedures",
     "No standing invitation is reported, but the Special Rapporteur on the environment visited.",
     [("Special Rapporteur on environment", "2", "8", "his visit was the first in almost 10 years by an independent expert appointed by the Human Rights Council")]),
    (r"Reform the labour code", C,
     "Prohibit sexual harassment in the labour code",
     "The draft Employment Relations (Prevention of Sexual Harassment) Bill has not been adopted.",
     [("JS1", "3", "22", "an Employment Relations (Prevention of Sexual Harassment) Bill had been drafted but not yet adopted")]),
    (r"awareness campaigns aimed at address", D,
     "Awareness campaigns against discrimination",
     "The documents contain no information on this ask.", []),
    (r"Continue taking measures against discrimination in all forms", C,
     "Continue measures against discrimination",
     "No comprehensive anti-discrimination legislation has been adopted.",
     [("United Nations subregional team", "2", "12", "no comprehensive anti-discrimination legislation had been adopted")]),
    (r"HIV/AIDS", D,
     "Anti-discrimination protection for people with HIV", "The documents contain no information on this ask.", []),
]

FALLBACK = (
    D, "Miscellaneous",
    "No rule matched and the evidence base contains no specific information on this recommendation.",
    [],
)
