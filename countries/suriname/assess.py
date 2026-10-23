"""Suriname — implementation assessment of its 3rd-cycle (2021, A/HRC/49/6)
UPR recommendations, graded against the 4th-cycle documentation (session 53):
National Report A/HRC/WG.6/53/SUR/1, OHCHR Compilation /2 and Stakeholders'
Summary /3.

    python scripts/run_assess.py suriname

First pass for expert review. Quotes are verbatim from the three documents.
"""

from __future__ import annotations

from recommendations.models import Grade

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

# theme -> (grade, action_summary, rationale, [(org, doc "1"|"2"|"3", para, quote)])
CLUSTERS = {
    "Ratification of & accession to international instruments": (
        C, "Ratify outstanding treaties and optional protocols",
        "Suriname acceded to the Convention against Torture on 16 November 2021, "
        "but is still only 'considering' accession to OP-CAT, OP-CEDAW, "
        "OP-CRPD, OP-ICESCR and the Second Optional Protocol; ICPPED and ICRMW "
        "remain unratified.",
        [
            ("Suriname", "1", "7", "OPCAT, OP-CEDAW, OP-CRPD and OP-ICESCR. The relevant national assessments, consultations and preparatory processes are ongoing"),
            ("Committee on the Elimination of Racial Discrimination", "2", "2", "encouraged Suriname to consider ratifying the International Convention on the Protection of the Rights of All Migrant Workers and Members of Their Families and the International Convention for the Protection of All Persons from Enforced Disappearance"),
        ],
    ),
    "Sexual & gender-based violence": (
        B, "Combat gender-based and domestic violence",
        "Suriname adopted the Act on Violence and Sexual Harassment in "
        "Employment (2022), implements the Gender Vision Policy 2021-2035, "
        "trains first responders and opened a specialised victim hearing room "
        "(March 2026); implementation of the 2009 Domestic Violence Act is "
        "weak, shelter capacity is insufficient and the 2022 Act excludes "
        "public servants.",
        [
            ("Suriname", "1", "26", "the Equal Treatment in Employment Act (S.B. 2022 no. 137) and the Act on Violence and Sexual Harassment in Employment (S.B. 2022 no. 136)"),
            ("Suriname", "1", "45", "a specialized hearing room was put into operation at the De Nieuwe Grond police station for the reception and questioning of victims of domestic and gender-based violence"),
            ("Human Rights Committee", "2", "73", "regretted the reportedly weak implementation of its legislative framework"),
            ("JS6", "3", "70", "existing capacity was insufficient, with victims regularly being turned away"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        C, "Establish and operationalise a national human rights institution",
        "The draft National Human Rights Institute Act is still in "
        "pre-parliamentary consultation, with an intended completion date of "
        "November 2026; no institution exists.",
        [
            ("Suriname", "1", "7", "The draft National Human Rights Institute Act is in the final pre-parliamentary consultation phase, with an intended completion date of end November 2026"),
            ("JS6", "3", "9", "Suriname had persistently failed to establish and operationalize an independent national human rights institution"),
        ],
    ),
    "Sexual & reproductive health and rights": (
        B, "Reduce maternal mortality and expand sexual and reproductive health services",
        "Suriname introduced the SIP Plus perinatal information system (2024-2025), "
        "the Maternal and Perinatal Death Surveillance model, the SRHR Policy "
        "2020-2030 and has integrated comprehensive sexuality education into the "
        "curriculum; maternal mortality remains high.",
        [
            ("Suriname", "1", "82", "The introduction and nationwide scaling-up of the SIP Plus perinatal information system in 2024 and 2025"),
            ("JS6", "3", "46", "Suriname had reduced maternal mortality over time, but the level remained high"),
        ],
    ),
    "Children: definition": (
        B, "Strengthen child-protection systems and legislation",
        "The Children's Ombudsperson Act (2025), the lowering of the age of "
        "majority to 18 and equal status for all children in the new Civil Code "
        "advance child protection; the Ombudsman institute is not yet "
        "operational and corporal punishment is not prohibited in all settings.",
        [
            ("Suriname", "1", "60", "provides for the establishment of the Children’s Ombudsman Institute Suriname (KOI)"),
            ("United Nations country team", "2", "18", "it was not yet operational, its bureau had not been staffed"),
            ("Suriname", "1", "61", "the statutory age of majority has been lowered de jure from 21 to 18 years"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        B, "Prevent and combat human trafficking",
        "A National Action Plan on Human Trafficking (2021-2025), a "
        "specialised police TIP unit and a strengthened National Referral "
        "Mechanism are in place and Suriname is Tier 1; convictions remain low.",
        [
            ("Suriname", "1", "53", "supported by the National Action Plan on Human Trafficking (2021–2025)"),
            ("Suriname", "1", "55", "the National Referral Mechanism was further strengthened for the identification, referral and protection of victims of human trafficking"),
            ("ECLJ", "3", "26", "the number of convictions remained low"),
        ],
    ),
    "Right to education": (
        B, "Improve access to quality education, especially in the interior",
        "Suriname adopted the National Education Policy Plan 2024-2031, a "
        "Multilingual Education Programme 2025-2030, school feeding, subsidised "
        "transport and a 2025 inclusive education protocol; dropout in the "
        "interior averages 21% and teacher and infrastructure gaps persist.",
        [
            ("Suriname", "1", "71", "the National Education Policy Plan Suriname 2024–2031 (NOBS)"),
            ("Suriname", "1", "75", "the de facto school dropout in the interior, which averages 21 per cent"),
            ("United Nations country team", "2", "61", "Access to quality education remained limited, especially in the rainforest and for marginalized communities and children with disabilities"),
        ],
    ),
    "Death penalty": (
        A, "Abolish the death penalty",
        "The death penalty was abolished in the Penal Code (2015) and in the "
        "Military Criminal Code (2021); the Second Optional Protocol remains unratified.",
        [
            ("Suriname", "1", "7", "the amendment of the Military Criminal Code (S.B. 2021 no. 117), by which the death penalty was abolished"),
            ("United Nations country team", "2", "5", "Suriname had abolished the death penalty in the Penal Code in 2015 and in the Military Penal Code in 2021"),
        ],
    ),
    "Equality & non-discrimination": (
        B, "Strengthen non-discrimination legislation",
        "The Equal Treatment in Employment Act (2022) and the Act on Violence "
        "and Sexual Harassment in Employment (2022) were adopted; there is no "
        "comprehensive anti-discrimination law and no legislation on sexual "
        "orientation or gender identity.",
        [
            ("Suriname", "1", "26", "Suriname has strengthened the legal framework on non-discrimination in the labour market"),
            ("Committee on the Elimination of Racial Discrimination", "2", "12", "prioritize the drafting and adoption of a comprehensive anti-discrimination law"),
        ],
    ),
    "Human rights & poverty": (
        B, "Strengthen social protection and combat poverty",
        "The National Social Protection Strategy 2024-2030, the Moni Karta "
        "cash-transfer system and a Multisectoral Early Childhood Development "
        "Policy 2025-2035 were adopted; multidimensional poverty remains widespread.",
        [
            ("Suriname", "1", "85", "the National Social Protection Strategy (NSPS) 2024–2030"),
            ("Suriname", "1", "86", "In 2024, cash transfers reached 133,560 beneficiaries"),
            ("JS6", "3", "37", "multidimensional poverty in Suriname affected up to 73% of large households"),
        ],
    ),
    "Cooperation & Follow up with Special Procedures": (
        C, "Extend a standing invitation to special procedures",
        "No standing invitation has been extended; the UN country team recommends considering one.",
        [("United Nations country team", "2", "10", "recommended that Suriname consider issuing a standing invitation to the special procedure mandate holders")],
    ),
    "Right to an adequate standard of living": (
        B, "Recognise Indigenous and tribal peoples' rights",
        "Suriname launched a Land Rights Project 2026-2030 with UNDP, received "
        "a national FPIC protocol (October 2025) and the National Assembly "
        "approved the Act on the Protection of Residential and Living Areas of "
        "Indigenous and Tribal Peoples; the Collective Rights Act is still a draft.",
        [
            ("Suriname", "1", "96", "the Act on the Protection of the Residential and Living Areas of Indigenous and Tribal Peoples has been approved by the National Assembly"),
            ("Suriname", "1", "95", "formally handed over the national FPIC protocol to the Government on 14 October 2025"),
            ("Human Rights Committee", "2", "96", "to expedite the adoption, within a clear time frame, of the draft law on the collective rights of Indigenous and tribal peoples"),
        ],
    ),
    "Right to health": (
        B, "Improve access to essential health services and mental health",
        "The Healthcare Facilities Readiness Initiative (June 2026), the "
        "Medical Mission for the interior, malaria-free certification (2025) "
        "and the National Mental Health Strategy 2025-2030 advance access; "
        "rural access, workforce and referral gaps remain.",
        [
            ("Suriname", "1", "79", "on 25 June 2026 the State launched the large-scale Healthcare Facilities Readiness Initiative"),
            ("Suriname", "1", "80", "in 2025 the country was officially certified malaria-free by the World Health Organization"),
            ("UNICEF", "2", "57", "access to primary healthcare in remote areas was undermined by shortages of medical personnel"),
        ],
    ),
    "Violence against women": (
        B, "Eliminate violence against women",
        "The 2022 Act and the Gender Vision Policy are in place and training "
        "is provided; violence remains highly prevalent.",
        [("Human Rights Committee", "2", "73", "was concerned by the continued high prevalence of violence against women in Suriname")],
    ),
    "Human rights & climate change": (
        B, "Climate adaptation and participation",
        "Suriname implements its National Adaptation Plan 2020-2030 and updated NDCs.",
        [("Suriname", "1", "108", "Climate and adaptation policy is anchored in the National Adaptation Plan (NAP 2020–2030)")],
    ),
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)": (
        B, "Investigate police ill-treatment and excessive force",
        "Training on public-order maintenance and community-oriented policing "
        "was introduced and the police Personnel Investigation Department "
        "oversees use of force; civil society reports no prosecutions and "
        "calls for an independent oversight body.",
        [
            ("Suriname", "1", "38", "Since 2025, the KPS has systematically moved to a community-oriented policing approach"),
            ("JS6", "3", "13", "recommended that Suriname establish an independent oversight mechanism to investigate allegations of police misconduct"),
        ],
    ),
    "Conditions of detention": (
        B, "Improve prison and detention conditions",
        "The Penitentiary Institutions and Remand Centres Act and Decree "
        "(2023), a Central Resocialization Department (2025), new case managers "
        "and a forensic observation facility improve conditions; international "
        "bodies still call for improvements, notably at Santa Boma prison.",
        [
            ("Suriname", "1", "42", "the Penitentiary Institutions and Remand Centres Act (S.B. 2023 no. 147) and the Penitentiary Decree (S.B. 2023 no. 148)"),
            ("Working Group of Experts on People of African Descent", "2", "29", "enhance its efforts to improve the conditions in places of deprivation of liberty"),
        ],
    ),
    "Advancement of women": (
        B, "Promote gender equality and women's participation",
        "The Gender Vision Policy Document 2021-2035 guides training of first "
        "responders and officials; negative gender stereotypes and low "
        "representation persist.",
        [("Suriname", "1", "27", "the Gender Vision Policy Document 2021–2035 and the SRHR Policy 2020–2030 are being implemented")],
    ),
    "Rights related to marriage & family": (
        B, "Support the family through social policies",
        "The new Civil Code (in force May 2025) strengthened the legal position of families and children.",
        [("Suriname", "1", "87", "The legal position of citizens and families has been further strengthened by the new Civil Code (S.B. 2024 no. 164), in force since 1 May 2025")],
    ),
    "Persons with disabilities: independence, inclusion": (
        B, "Disability inclusion legislation and inclusive education",
        "The General Act for Persons with Disabilities was introduced in the "
        "National Assembly (June 2024), a National Policy Plan 2025-2030 was "
        "adopted and an inclusive education protocol issued; accessibility "
        "barriers persist.",
        [
            ("Suriname", "1", "66", "the formal member’s bill for the General Act for Persons with Disabilities (AWMB) was submitted to the National Assembly"),
            ("Suriname", "1", "67", "the National Policy Plan for Persons with Disabilities Suriname 2025–2030"),
        ],
    ),
    "Persons with disabilities: definition, general principles": (
        B, "Comprehensive legislation to protect persons with disabilities",
        "The General Act for Persons with Disabilities is before the National Assembly.",
        [("Suriname", "1", "66", "the formal member’s bill for the General Act for Persons with Disabilities (AWMB) was submitted to the National Assembly")],
    ),
    "Children: protection against exploitation": (
        C, "Eradicate child labour and economic exploitation of children",
        "The ILO continues to request measures on child labour and hazardous "
        "work in mining, and the compulsory-education age (12) lies below the "
        "minimum employment age (16).",
        [("JS6", "3", "28", "The compulsory education age (12 years) did not extend to the minimum age for employment (16 years)")],
    ),
    "Cooperation with international organizations": (
        B, "Implement the judgments of the Inter-American Court of Human Rights",
        "Suriname recognises remaining constitutional challenges in implementing "
        "the Moiwana, Saramaka and Kaliña and Lokono judgments; the Human Rights "
        "Committee finds them only partially implemented.",
        [
            ("Suriname", "1", "7", "recognizes the remaining constitutional challenges in the full de jure implementation of the standing judgments of the Inter-American Court of Human Rights"),
            ("Human Rights Committee", "2", "11", "had been only partially implemented"),
        ],
    ),
    "National Mechanisms for Reporting & Follow-up (NMRF)": (
        B, "Establish a national mechanism for implementation, reporting and follow-up",
        "The Human Rights Bureau of the Ministry of Justice and Police "
        "coordinates reporting with ministry focal points and a National "
        "Recommendations Tracking Database.",
        [
            ("Suriname", "1", "10", "take place under the central direction of the Human Rights Bureau of the Ministry of Justice and Police"),
            ("Suriname", "1", "11", "the National Recommendations Tracking Database (NRTD)"),
        ],
    ),
    "Right to development": (
        B, "Implement the Nairobi Summit commitments",
        "The SRHR Policy 2020-2030 and perinatal reforms implement the commitments.",
        [("Suriname", "1", "27", "the SRHR Policy 2020–2030 are being implemented")],
    ),
    "Human rights & the environment": (
        B, "Mitigate mercury and mining pollution",
        "The National Environmental Authority is operational and Suriname "
        "implements the Minamata Convention through a 2021-2025 action plan "
        "for small-scale gold mining; contamination persists in the interior.",
        [
            ("Suriname", "1", "108", "Suriname implements the Minamata Convention on Mercury through the NAP-ASGM (2021–2025)"),
            ("Committee on the Elimination of Racial Discrimination", "2", "69", "reports of ongoing pollution – mercury and other toxics – on land and in rivers"),
        ],
    ),
    "Safe drinking water & sanitation": (
        B, "Expand water, sanitation and hygiene programmes",
        "UN WASH installed 118 rainwater tanks in 57 villages and a "
        "project for 26 rural communities is being implemented; less than 40% "
        "of people in the interior have safe drinking water.",
        [
            ("Suriname", "1", "109", "the installation of automated surface-water treatment systems and 118 rainwater tanks in 57 villages has been realized through the UN WASH programs"),
            ("Suriname", "1", "109", "currently less than 40% of the population in the interior has structural access to safe drinking water"),
        ],
    ),
    "Discrimination against women": (
        B, "Adopt legislation on equal treatment of women and men",
        "The Equal Treatment in Employment Act (2022) was adopted; the ILO "
        "continues to ask for comprehensive legislation covering all grounds.",
        [("ILO Committee of Experts", "2", "48", "reiterated its request to Suriname to adopt as soon as possible comprehensive legislation that")],
    ),
    "Rule of law & impunity": (
        B, "Platform to protect the rights of Indigenous and tribal peoples",
        "Consultations with traditional authorities, the FPIC protocol and an "
        "inter-ministerial commission were launched.",
        [("Suriname", "1", "95", "an interministerial commission is currently studying modalities to integrate this protocol as a formal guideline for consultations in the interior")],
    ),
    "Right to participate in public affairs & right to vote": (
        B, "Meaningful participation of Indigenous peoples",
        "A national FPIC protocol was handed over and consultation trajectories were held in 2026.",
        [("Suriname", "1", "24", "In 2026, the Ministry of ROS and UNDP carried out consultation and capacity trajectories in the interior")],
    ),
    "Labour rights and right to work": (
        B, "Deepen measures for an adequate standard of living and decent work",
        "The Decent Work Country Programme 2023-2026 and a revised Labour Act (2023) were implemented.",
        [("Suriname", "1", "88", "The Decent Work Country Program (DWCP) 2023–2026 promotes employment")],
    ),
    "Land & property rights": (
        B, "Enact a law to demarcate Indigenous lands",
        "The Collective Rights Act is still before the National Assembly; the "
        "Act on the Protection of Residential and Living Areas was approved "
        "pending promulgation and a Land Rights Project was launched.",
        [("Suriname", "1", "94", "the draft Act on the Collective Rights of Indigenous and Tribal Peoples (initiated in 2019, with renewed parliamentary treatment in 2023–2025)")],
    ),
    "Rights related to name, identity & nationality": (
        D, "Review gender identity policies",
        "The documents contain no information on this ask.", [],
    ),
}

KEYWORDS = [
    # --- ratification-cluster specifics ---
    (r"Convention against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment", A,
     "Ratify the Convention against Torture",
     "Suriname acceded to the Convention against Torture on 16 November 2021.",
     [("Suriname", "1", "7", "On 16 November 2021, Suriname acceded to the Convention against Torture")]),
    (r"Optional Protocol to the Convention against Torture|OPCAT|OP-CAT", C,
     "Ratify OP-CAT",
     "Suriname is only considering accession to the OP-CAT.",
     [("Suriname", "1", "7", "OPCAT, OP-CEDAW, OP-CRPD and OP-ICESCR. The relevant national assessments, consultations and preparatory processes are ongoing"),
      ("Human Rights Committee", "2", "3", "recommended that Suriname consider ratifying the Optional Protocol to the Convention against Torture")]),
    (r"Second Optional Protocol", C,
     "Ratify the Second Optional Protocol (abolition)",
     "Ratification remains pending although the death penalty has been abolished.",
     [("United Nations country team", "2", "5", "ratification of the Second Optional Protocol to the International Covenant on Civil and Political Rights, aiming at the abolition of the death penalty, remained pending")]),
    (r"Optional Protocol to the Convention on the Rights of the Child on the (involvement|sale)|armed conflict|sale of children", A,
     "Ratify the Optional Protocols to the CRC on armed conflict and sale of children",
     "Suriname is a party to OP-CRC-AC and OP-CRC-SC.",
     [("Suriname", "1", "9", "including the optional protocols OP-ICCPR, OP2-ICCPR, OP-CRC-AC and OP-CRC-SC")]),
    (r"Enforced Disappearance", C,
     "Ratify the Convention on Enforced Disappearance",
     "No ratification is reported.",
     [("Committee on the Elimination of Racial Discrimination", "2", "2", "encouraged Suriname to consider ratifying the International Convention on the Protection of the Rights of All Migrant Workers and Members of Their Families and the International Convention for the Protection of All Persons from Enforced Disappearance")]),
    (r"Optional Protocol to the Convention on the Elimination of All Forms of Discrimination|OP-CEDAW", C,
     "Ratify OP-CEDAW",
     "Ratification is in the pre-parliamentary preparatory phase.",
     [("Suriname", "1", "9", "Ratification of OPCAT, OP-CEDAW and OP-CRPD is currently in the preparliamentary preparatory phase")]),
    (r"Optional Protocol to the International Covenant on Economic, Social and Cultural", C,
     "Ratify OP-ICESCR",
     "UNESCO recommends ratification; Suriname is considering accession.",
     [("UNESCO", "2", "4", "recommended that Suriname ratify the Optional Protocol to the International Covenant on Economic, Social and Cultural Rights")]),
    (r"United Nations Educational, Scientific and Cultural Organization Conv|UNESCO", C,
     "Ratify the UNESCO Convention against Discrimination in Education",
     "UNESCO recommends ratification; none is reported.",
     [("UNESCO", "2", "9", "recommended that Suriname ratify the Convention against Discrimination in Education")]),
    (r"Genocide", C,
     "Ratify the Genocide Convention",
     "A civil-society submission recommends ratification; none is reported.",
     [("CGNK", "3", "6", "recommended that Suriname ratify the Convention on the Prevention and the Punishment of the crime of Genocide")]),
    (r"Declaration on Children, Youth and Climate Action", D,
     "Sign the Declaration on Children, Youth and Climate Action",
     "The documents contain no information on this ask.", []),
    (r"Request technical support from OHCHR", B,
     "Request OHCHR technical support",
     "Suriname cooperates strategically with OHCHR, UNDP, UNICEF and other partners in capacity-strengthening.",
     [("Suriname", "1", "6", "the State cooperated strategically with international partners, including OHCHR, UNDP, UNICEF, UNFPA, IOM and PAHO, in support of capacity-strengthening and data validation")]),
    (r"Increase efforts to ratify the main international human rights instruments|main international treaties on human rights that are still pending|Prioritize the parliamentary debates", C,
     "Ratify pending core instruments",
     "Suriname reports that ratification of the remaining protocols is only at the preparatory phase.",
     [("Suriname", "1", "9", "Ratification of OPCAT, OP-CEDAW and OP-CRPD is currently in the preparliamentary preparatory phase")]),
    # --- violence ---
    (r"shelters", D,
     "Shelters for victims of gender-based violence",
     "The documents report insufficient shelter capacity and no new shelters; the State does not describe measures on shelters.",
     [("JS6", "3", "70", "existing capacity was insufficient, with victims regularly being turned away")]),
    # --- children ---
    (r"corporal punishment", C,
     "Prohibit corporal punishment in all settings",
     "The State describes elimination of corporal punishment in education only; the Human Rights Committee asks that parents' corporal punishment also be prohibited in the Civil Code.",
     [("Human Rights Committee", "2", "85", "prohibiting corporal punishment by parents in the draft New Civil Code")]),
    (r"child, early and forced marriage|child marriage", C,
     "Eliminate child, early and forced marriage",
     "UNESCO asks that the minimum age of marriage be 18 without exception; the State only states that customary law cannot override national law.",
     [("UNESCO", "2", "87", "amend its legislation to ensure that the minimum age of marriage was 18 years old without exception")]),
    # --- trafficking ---
    (r"Enforce the Penal Code more effectively", C,
     "Prosecute traffickers more effectively",
     "Convictions remain low.",
     [("Human Rights Committee", "2", "44", "the low number of convictions for trafficking in persons")]),
    # --- abortion ---
    (r"Decriminalize abortion", D,
     "Decriminalise abortion", "The documents contain no information on abortion.", []),
    # --- LGBT ---
    (r"discrimination against lesbian, gay|sexual orientation|legislation that specifically addresses discrimination", C,
     "Legislate against discrimination based on sexual orientation and gender identity",
     "No such legislation exists; the 2023 LGBTQ+ Needs Assessment only identified priorities.",
     [("Suriname", "1", "27", "The Suriname LGBTQ+ Needs Assessment Report (2023) contributed to identifying priorities on inclusion and nondiscrimination")]),
    (r"Make article 80 of the Civil Code gender neutral", D,
     "Make article 80 of the Civil Code gender neutral",
     "The documents contain no information on this ask.", []),
    # --- child poverty ---
    (r"child poverty", B,
     "National plan against child poverty",
     "A General Child Allowance supports about 96,500 children and a Multisectoral Early Childhood Development Policy 2025-2035 was adopted.",
     [("Suriname", "1", "86", "the General Child Allowance supports approximately 96,500 children")]),
    # --- inclusive education / multilingual ---
    (r"multilingual", B,
     "Multilingual approach to education",
     "The Multilingual Education Program 2025-2030 was ratified in 2024 and piloted in Galibi; scale-up faces barriers.",
     [("Suriname", "1", "74", "the Multilingual Education Program 2025–2030 was formally ratified in October 2024")]),
    # --- child labour ---
    (r"Eradicate child labour", C,
     "Eradicate child labour",
     "The ILO continues to request measures including on hazardous work in mining.",
     [("ILO Committee of Experts", "2", "84", "to ensure that no child was engaged in hazardous work in mining")]),
    (r"economically exploited", B,
     "Protect children from economic exploitation",
     "The Youth Information Unit runs prevention programmes and the Labour Act was revised in 2023.",
     [("Suriname", "1", "64", "the Youth Information Unit of the Suriname Police Force continuously carries out prevention and awareness programs")]),
    (r"Take further steps to ensure the meaningful participation of indigenous", B,
     "Meaningful participation of Indigenous peoples",
     "A national FPIC protocol was handed over and consultations were held.",
     [("Suriname", "1", "95", "formally handed over the national FPIC protocol to the Government on 14 October 2025")]),
    (r"^Step up efforts to abolish the death penalty through the revision of the Military Penal Code", B,
     "Abolish the death penalty in the Military Penal Code and ratify the Second Optional Protocol",
     "The Military Criminal Code was amended in 2021 to abolish the death penalty, but the Second Optional Protocol remains unratified.",
     [("Suriname", "1", "7", "the amendment of the Military Criminal Code (S.B. 2021 no. 117), by which the death penalty was abolished"),
      ("United Nations country team", "2", "5", "ratification of the Second Optional Protocol to the International Covenant on Civil and Political Rights, aiming at the abolition of the death penalty, remained pending")]),
]

FALLBACK = (
    D, "Miscellaneous",
    "No rule matched and the evidence base contains no specific information on this recommendation.",
    [],
)
