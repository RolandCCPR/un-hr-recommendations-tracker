"""Eswatini — implementation assessment of its 3rd-cycle (2021, A/HRC/49/6)
UPR recommendations, graded against the 4th-cycle documentation (session 53):
National Report A/HRC/WG.6/53/SWZ/1, OHCHR Compilation /2 and Stakeholders'
Summary /3.

    python scripts/run_assess.py eswatini

First pass for expert review. Quotes are verbatim from the three documents.
The National Report states (para 2) that recommendations on gender-based
violence, water and sanitation and inclusive education were reported in the
mid-term report and are not repeated; that report was not reviewed here.
"""

from __future__ import annotations

from recommendations.models import Grade

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

# theme -> (grade, action_summary, rationale, [(org, doc "1"|"2"|"3", para, quote)])
CLUSTERS = {
    "Ratification of & accession to international instruments": (
        C, "Ratify outstanding international instruments",
        "The National Report states that ratification of OP-CAT, OP-CEDAW and "
        "the Genocide Convention 'remain under active consideration'; no "
        "ratification is reported and Amnesty confirms the instruments are "
        "unratified.",
        [
            ("Eswatini", "1", "10", "ratification and accession to outstanding treaties remain under active consideration within the national consultative framework"),
            ("Amnesty International", "3", "2", "Eswatini had still not ratified OP-CAT, the ICCPR-OP 2, the OP-CEDAW, and the ICRMW"),
        ],
    ),
    "Violence against women": (
        B, "Combat violence against women and implement the Sexual Offences and Domestic Violence Act",
        "Eswatini adopted a GBV Coordination Mechanism, trained frontline "
        "responders, expanded one-stop centres and runs five (privately "
        "operated) safe houses; the UN country team and civil society report "
        "persistently high GBV and weak enforcement.",
        [
            ("Eswatini", "1", "58", "The DPMO has adopted a formalised Gender-Based Violence (GBV) Coordination Mechanism"),
            ("Eswatini", "1", "64", "five safe houses are operational across the country, all of which are privately operated"),
            ("United Nations country team", "2", "80", "high rates of gender-based violence persisted due to weak enforcement, cultural barriers and limited funding"),
        ],
    ),
    "Sexual & gender-based violence": (
        B, "Strengthen multisectoral response to gender-based violence",
        "A multisectoral coordination structure, one-stop centres, referral "
        "pathways, specialised courts and training for responders exist; "
        "SNL reports a 91% case withdrawal rate in Lubombo.",
        [
            ("Eswatini", "1", "60", "Victim support services have been expanded through the establishment of one-stop centres and referral pathways"),
            ("SNL", "3", "92", "the 91% case withdrawal rate documented in Lubombo"),
        ],
    ),
    "Equality & non-discrimination": (
        B, "Combat discrimination and violence against persons with albinism and people living with HIV",
        "The National Disability Plan of Action 2024-2028, the Persons with "
        "Disabilities Act, awareness days and skin-health clinics protect "
        "persons with albinism, and the HIV Stigma Index is run; JS1 reports "
        "persisting barriers and low access to remedies.",
        [
            ("Eswatini", "1", "25", "the National Disability Plan of Action (NDPA) 2024–2028"),
            ("JS1", "3", "17", "persons with albinism continued to experience significant barriers to the enjoyment of their fundamental rights"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        B, "Establish an independent national human rights institution in line with the Paris Principles",
        "The Commission on Human Rights and Public Administration Bill 2025 was "
        "introduced in Parliament (March 2026), but the Commission still lacks "
        "full independence and the Bill has gaps.",
        [
            ("Eswatini", "1", "15", "The Government is expediting efforts towards the enactment of the Commission on Human Rights and Public Administration Bill 2025"),
            ("El Hak", "3", "14", "still lacked full functional and financial independence"),
        ],
    ),
    "Freedom of opinion and expression & access to information": (
        C, "Protect freedom of expression, association and assembly",
        "The National Report cites the Constitution and the Sibaya dialogue "
        "(2023) and states that no one is targeted; the UN country team and "
        "ICJ report that the Sedition, Terrorism and Public Order Acts are "
        "used to restrict dissent and internet services are shut down during "
        "protests.",
        [
            ("Eswatini", "1", "46", "Eswatini provides a safe environment for exercising civic space rights, with no individuals targeted"),
            ("United Nations country team", "2", "34", "restricted debate and dissent through broad discretionary powers and criminal sanctions"),
            ("El Hak", "3", "70", "Eswatini recurrently resorted to completely shutting down internet services to block information during protests"),
        ],
    ),
    "Right to education": (
        B, "Improve access to quality education, retention and completion",
        "Eswatini is implementing the Education Sector Strategic Plan 2022-2034 "
        "and competency-based curriculum reform, school feeding reaches "
        "355,478 learners and the primary dropout rate fell from 6.5% to "
        "4.8%; free secondary education is not yet provided.",
        [
            ("Eswatini", "1", "105", "Education Sector Strategic Plan (ESSP) 2022–2034"),
            ("Eswatini", "1", "117", "a reduction in the national primary school dropout rate from 6.5% to 4.8%"),
            ("Eswatini", "1", "114", "Due to resource constraints, Eswatini is not yet ready to provide free secondary education"),
        ],
    ),
    "Right to health": (
        B, "Strengthen health services and HIV response",
        "Eswatini provides free long-acting PrEP, runs the HIV Stigma Index and "
        "adopted an NCD and mental health plan 2024-2028; life expectancy "
        "rose from 58.2 to 64.5 years; the Committee on the Rights of the Child "
        "notes scarce rural facilities and medicine stock-outs.",
        [
            ("Eswatini", "1", "90", "life expectancy rates have increased to 64.5 years (2026) for both sexes combined from 58.2 years in 2021"),
            ("Eswatini", "1", "91", "National Non Communicable Diseases, Injuries and Mental Health (NCDIMH) Sector operational plan 2024-2028"),
            ("Committee on the Rights of the Child", "2", "62", "remained concerned about the scarcity of healthcare facilities, particularly in rural areas"),
        ],
    ),
    "Sexual & reproductive health and rights": (
        B, "Reduce maternal mortality and improve sexual and reproductive health",
        "The SRMNCAH&N Strategy 2024-2028 rolled out emergency obstetric care "
        "to all maternity facilities and skilled birth attendance rose to "
        "93.4%; UNFPA notes maternal mortality remains high.",
        [
            ("Eswatini", "1", "101", "Sexual Reproductive Maternal & Newborn Child, Adolescent Health & Nutrition (SRMNCAH&N) Strategy (2024–2028)"),
            ("UNFPA", "2", "65", "maternal mortality remained high"),
        ],
    ),
    "Discrimination against women": (
        B, "Align legislation with CEDAW and combat gender stereotypes",
        "All ministries were directed to review legislation for CEDAW "
        "compliance under the Programme of Action and ILO Conventions 100 and "
        "111 were ratified; the Family Law Bills have not been enacted and "
        "customary law still entrenches inequality.",
        [
            ("Eswatini", "1", "22", "all government ministries are directed to review their respective pieces of legislation to promote the objects and purposes of CEDAW"),
            ("Eswatini", "1", "24", "Eswatini ratified ILO Conventions Nos. 100 and 111"),
            ("United Nations country team", "2", "79", "customary law entrenched gender inequality in inheritance and property rights"),
        ],
    ),
    "Right to participate in public affairs & right to vote": (
        C, "Allow political parties and reform the electoral system",
        "The National Report describes only the Elections and Boundaries "
        "Commission and civic education; political parties remain banned and "
        "the People's United Democratic Movement was designated a terrorist "
        "organisation.",
        [
            ("Eswatini", "1", "52", "The Elections and Boundaries Commission (EBC) is established by Section 90 of the Constitution and the Elections and Boundaries Commission Act No. 3 of 2013"),
            ("JS6", "3", "72", "the continued legal and practical ban on political parties exemplified Eswatini’s entrenched resistance to pluralism"),
            ("JS6", "3", "73", "the political formation the People’s United Democratic Movement had been designated as a terrorist organization by the authorities"),
        ],
    ),
    "Death penalty": (
        C, "Abolish the death penalty or adopt a moratorium",
        "The National Report is silent; JS5 recommends abolition and a de jure "
        "moratorium, indicating the penalty remains in law.",
        [
            ("JS5", "3", "24", "recommended that Eswatini abolish the death penalty"),
        ],
    ),
    "Right to peaceful assembly": (
        C, "Ensure the right to peaceful assembly and investigate violations",
        "The State's review of the June 2021 unrest found no unlawful conduct "
        "by police; the UN country team reports excessive force against "
        "peaceful assemblies and stalled investigations.",
        [
            ("Eswatini", "1", "39", "The outcome of these reviews did not reveal evidence of unlawful conduct on the part of police officers in the discharge of their duties"),
            ("United Nations country team", "2", "39", "participants in peaceful assemblies had been met with excessive force, arbitrary arrests, prolonged detention and serious injuries"),
        ],
    ),
    "Human rights & poverty": (
        B, "Reduce poverty, especially in rural areas",
        "The national poverty rate fell from 58.9% to 53.5%; the Regional "
        "Development Fund, the Agricultural Development Fund and youth funds "
        "were launched.",
        [
            ("Eswatini", "1", "74", "national poverty rate declined from 58.9% (2016/17) to 53.5%"),
            ("Eswatini", "1", "76", "the Regional Development Fund (RDF) supported 107 agricultural projects to enhance productivity and food security"),
        ],
    ),
    "Participation of women in political & public life": (
        B, "Increase women's participation in decision-making",
        "Women hold 29% of parliamentary seats after the 2023 elections "
        "(four elected under the Election of Women Members Act 2018) and 25% "
        "of Cabinet.",
        [
            ("Eswatini", "1", "54", "women holding 29 per cent of seats in the Parliament, with 25% held in the Cabinet"),
        ],
    ),
    "Persons with disabilities: definition, general principles": (
        B, "Protect the rights and education of persons with disabilities",
        "The National Disability Advisory Council was established (2023), the "
        "NDPA 2024-2028 adopted and disability grant beneficiaries rose to "
        "17,193; the UN country team notes accessibility gaps and a "
        "resourcing need.",
        [
            ("Eswatini", "1", "9", "The establishment of the National Disability Advisory Council in 2023"),
            ("Eswatini", "1", "73", "The Disability Grant beneficiaries increased from 5 019 in 2021 to 17,193 in 2025"),
            ("United Nations country team", "2", "97", "accessibility gaps persisted in buildings, transport and information"),
        ],
    ),
    "Advancement of women": (
        B, "Women's economic empowerment and shelters",
        "A National MSME Policy 2024-2029 and the Citizen Economic "
        "Empowerment Act 2023 support women's enterprises; shelters remain "
        "privately operated.",
        [
            ("Eswatini", "1", "65", "The National MSME Policy 2024–2029 promotes the formalisation of informal enterprises"),
            ("Eswatini", "1", "64", "the Government is making efforts to establish a state-owned gender-based violence shelter"),
        ],
    ),
    "Human rights defenders": (
        C, "Protect human rights defenders, journalists and activists",
        "The National Report says no one is targeted; investigations into the "
        "killing of lawyer Thulani Maseko have stalled and Eswatini has no "
        "legal framework for the protection of defenders.",
        [
            ("Eswatini", "1", "46", "Eswatini provides a safe environment for exercising civic space rights, with no individuals targeted"),
            ("United Nations country team", "2", "24", "investigations had stalled in relation to the perpetrators of the 2021–2023 violence in which protestors, including a prominent human rights lawyer, had been killed"),
            ("JS5", "3", "66", "Eswatini did not have a comprehensive legal framework for the protection of human rights defenders"),
        ],
    ),
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)": (
        C, "Investigate torture and deaths in custody; adopt a torture law",
        "Eswatini has no specific torture law and relies on internal "
        "complaints units (38 complaints against police, 2021-2025); JS3 and "
        "Amnesty report alleged torture of detainees held for political "
        "expression.",
        [
            ("Eswatini", "1", "32", "Eswatini does not have a specific torture law"),
            ("JS3", "3", "25", "incidents of alleged torture and other cruel, inhuman or degrading treatment of detainees, particularly of those held for expressing political opinions or linked to protest activity"),
        ],
    ),
    "Human rights & counter-terrorism": (
        E, "Reform or repeal the Suppression of Terrorism Act and the Sedition and Subversive Activities Act",
        "The Prime Minister, as appellant, obtained an August 2024 Supreme "
        "Court judgment upholding both Acts and the National Report cites it "
        "as affirming that rights are subject to lawful limitations; no "
        "reform was undertaken and the Acts continue to be applied against "
        "dissent: a position contrary to the recommendation.",
        [
            ("Eswatini", "1", "47", "the Supreme Court upheld the Sedition and Subversive Activities Act 46 of 1938 and Suppression of Terrorism Act 3 of 2028 as consistent with constitutional guarantees"),
            ("Amnesty International", "3", "38", "Eswatini had neither taken adequate steps to bring the Suppression of Terrorism Act into line with international standards"),
            ("United Nations country team", "2", "18", "the Suppression of Terrorism Act, 2008, was applied in ways that conflated terrorism with political dissent"),
        ],
    ),
    "Conditions of detention": (
        B, "Improve prison conditions and reduce overcrowding",
        "Matsapha Correctional Centre is being refurbished, extra-mural "
        "employment and non-custodial sentences were expanded and more than "
        "400 offenders were released by mercy in 2025; facilities hold 4,458 "
        "inmates for 3,090 places.",
        [
            ("Eswatini", "1", "40", "Matsapha Correctional Centre is undergoing major refurbishment"),
            ("Eswatini", "1", "41", "in 2025 the Prerogative of Mercy released more than 400 offenders"),
            ("Eswatini", "1", "127", "correctional facilities continue to operate at capacity significantly exceeding approved limits"),
        ],
    ),
    "Administration of justice & fair trial": (
        B, "Reform the judiciary and strengthen its independence",
        "The Judicial Service Commission was reconstituted by Legal Notice "
        "(2025) and additional judges and magistrates were appointed; ICJ and "
        "El Hak report executive interference and low public confidence.",
        [
            ("Eswatini", "1", "18", "members of the Judicial Service Commission were appointed through Legal Notice of 2025"),
            ("ICJ", "3", "40", "public confidence in the judiciary in Eswatini was very low"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        B, "Resource the anti-trafficking plan and task force",
        "A National Strategic Framework and Action Plan 2019-2023 was funded "
        "and the multi-agency Task Force strengthened with a Protection "
        "Committee and Tripartite Mechanism.",
        [
            ("Eswatini", "1", "50", "implement the National Strategic Framework and Action Plan to Combat People Trafficking 2019-2023"),
            ("Eswatini", "1", "51", "The Task Force against Trafficking in Persons has been strengthened through enhanced multi-agency coordination"),
        ],
    ),
    "Safe drinking water & sanitation": (
        B, "Improve access to safe drinking water and sanitation",
        "The National Report refers water and sanitation to Eswatini's mid-term "
        "report, which records rural water schemes, a solar-powered pump "
        "pilot, disability-accessible water facilities and a sanitation "
        "project; the proportion with safely managed drinking water rose from "
        "75% to 81.2% (2022-2023). The Committee on the Rights of the Child "
        "notes children in informal settlements without water.",
        [
            ("Eswatini", "M", "36", "The proportion of the national population which has access to safely managed clean drinking water increased from 75% in 2022 to 81.2% in 2023"),
            ("Eswatini", "M", "37", "introducing solar- powered pumps as a renewable energy solution"),
            ("Eswatini", "M", "38", "New facility designs now accommodate persons with disabilities (PWDs)"),
            ("Committee on the Rights of the Child", "2", "61", "many children lived in informal settlements without access to water or sanitation"),
        ],
    ),
    "Scope of international obligations": (
        B, "Domesticate international instruments and align the human rights framework",
        "Eswatini enacted the Computer Crime and Data Protection Acts (2022), "
        "the Disaster Risk Management Act (2025) and the Legal Aid Act (2025), "
        "and received Commonwealth support on domestication.",
        [
            ("Eswatini", "1", "12", "Eswatini further received technical assistance from the Commonwealth on better cooperation with international human rights mechanisms, domestication of treaties"),
        ],
    ),
    "Children: family environment & alternative care": (
        C, "Prohibit corporal punishment in all settings",
        "Corporal punishment remains lawful in the home, alternative care, "
        "day care, schools and penal institutions.",
        [
            ("Committee on the Rights of the Child", "2", "17", "was seriously concerned that corporal punishment was still lawful in the home, in alternative care settings, in day care, in schools and in penal institutions"),
        ],
    ),
    "Cooperation & Follow up with Special Procedures": (
        D, "Extend a standing invitation to special procedures",
        "The documents contain no information on this recommendation.", [],
    ),
    "Children: definition": (
        C, "Raise the minimum age of marriage to 18",
        "The Marriages Bill 8 of 2022 has not been enacted; the Committee on "
        "the Rights of the Child urges its adoption.",
        [
            ("Eswatini", "1", "23", "the Government has prioritised the enactment of a suite of Family Law Bills"),
            ("Committee on the Rights of the Child", "2", "89", "urged Eswatini to revise its legislation, including by amending the Marriage Act and adopting the marriage bill, in order to ensure that the minimum age of marriage was established at 18 for both girls and boys"),
        ],
    ),
    "Cooperation with human rights mechanisms & requests for technical assistance": (
        A, "Engage with human rights mechanisms and request OHCHR technical support",
        "Eswatini received OHCHR and UNCO technical assistance for its NMRF, "
        "hosted the African Commission and the African Committee of Experts on "
        "the Rights of the Child and benefited from the UPR Voluntary Fund.",
        [
            ("Eswatini", "1", "11", "Eswatini received technical assistance from the OHCHR in collaboration with the UNCO to strengthen its capacity to deliver on its mandate"),
            ("Eswatini", "1", "13", "hosted a Promotion Mission of the African Committee of Experts on the Rights and Welfare of the Child in July 2023, the African Commission on Human and Peoples' Rights in July 2025"),
        ],
    ),
    "National Human Rights Action Plans (or specific areas) / implementation plans": (
        B, "Adopt national strategies and plans",
        "A National Strategy and Plan of Action on Positive Parenting 2023-2027 "
        "and the Government Programme of Action and National Development "
        "Plan 2023-2028 were adopted.",
        [
            ("Eswatini", "1", "125", "National Strategy and Plan of Action on Positive Parenting 2023–2027"),
        ],
    ),
    "Cooperation & Follow up with Treaty Bodies": (
        B, "Submit reports to treaty bodies",
        "Eswatini submitted its outstanding initial reports under ICESCR and "
        "CAT and is working on the CERD periodic report.",
        [
            ("Eswatini", "1", "11", "Submitted outstanding initial reports under the ICESCR and CAT and is currently working on the periodic report on CERD"),
        ],
    ),
    "Legal & institutional reform": (
        B, "Strengthen national human rights mechanisms through the proposed law",
        "The Commission on Human Rights and Public Administration Bill was "
        "introduced in Parliament in March 2026.",
        [
            ("Eswatini", "1", "15", "The Bills were introduced for debate in Parliament in March 2026 and April 2025, respectively."),
        ],
    ),
    "Business & Human Rights": (
        D, "National action plan on human rights, including business",
        "The documents contain no information on this recommendation.", [],
    ),
    "Human rights & climate change": (
        A, "Participation of women, children, persons with disabilities and local communities in climate frameworks",
        "NDC 3.0 sets dedicated targets for women, youth and persons with "
        "disabilities in climate governance bodies, a youth consultation forum "
        "was held and the Disaster Risk Management Act (2025) was enacted "
        "through multi-sectoral consultation.",
        [
            ("Eswatini", "1", "29", "3.0 adopts an inclusivity and Just Transition approach, with dedicated targets for women, youth, and PWDs in climate governance bodies"),
            ("Eswatini", "1", "30", "The Disaster Risk Management Act 16 of 2025 was enacted through multi-sectoral stakeholder consultations"),
        ],
    ),
    "Good governance & corruption": (
        C, "Fund the Anti-Corruption Commission",
        "The National Report states that efforts to mobilise adequate "
        "resources 'remain ongoing'; JS3 reports no significant arrests and no "
        "whistleblower protection law.",
        [
            ("Eswatini", "1", "20", "efforts to mobilise adequate resources remain ongoing"),
            ("JS3", "3", "53", "no significant arrests had been made, signalling a persistent lack of political will to empower the Anti-Corruption Commission"),
        ],
    ),
    "Right to social security": (
        B, "Strengthen social protection floors",
        "The Social Security Inquiry tool (2024/25), the Eswatini National "
        "Pension Fund Bill (2025) and increased grants extend protection; "
        "only 29% of the population is covered.",
        [
            ("Eswatini", "1", "69", "the Eswatini National Pension Fund (ENPF) Bill, introducing a comprehensive National Pension Scheme"),
            ("United Nations country team", "2", "57", "social protection coverage remained limited, with only 29% of the population covered"),
        ],
    ),
    "Right to an adequate standard of living": (
        B, "Promote social policies for the most vulnerable",
        "Elderly and disability grants were increased, food assistance reached "
        "263,090 people and a decent shelter programme built 204 houses.",
        [
            ("Eswatini", "1", "73", "Elderly Grant increased by 20 per cent from E500 (USD31.25) to E600 (USD37.50) per month"),
        ],
    ),
    "2030 Agenda & other voluntary commitments": (
        B, "Implement human rights mechanisms' recommendations related to the SDGs",
        "Recommendations were aligned with the SDGs, the National Development "
        "Plan and the Government Programme of Action, and Eswatini presented "
        "its third Voluntary National Review (July 2025).",
        [
            ("Eswatini", "1", "14", "Eswatini aligned the recommendations emanating from the human rights mechanisms with the relevant Sustainable Development Goals"),
        ],
    ),
    "Data collection & research": (
        B, "Strengthen national data systems",
        "A revised Statistics Bill and the ESDS 2026-2028 were prepared and "
        "phase 1 of the 2027 census was completed.",
        [
            ("Eswatini", "1", "82", "adopted the Eswatini Strategy for the Development of Statistics (ESDS) 2026-2028"),
        ],
    ),
    "Rule of law & impunity": (
        C, "Fight impunity of security forces",
        "The State's internal reviews of the June 2021 unrest found no "
        "unlawful police conduct; the UN country team and Amnesty report "
        "stalled investigations and impunity.",
        [
            ("Eswatini", "1", "39", "The outcome of these reviews did not reveal evidence of unlawful conduct on the part of police officers in the discharge of their duties"),
            ("Amnesty International", "3", "43", "failures to investigate unlawful killings such as the killing of human rights lawyer Thulani Maseko"),
        ],
    ),
    "Arbitrary arrest & detention": (
        C, "Combat arbitrary arrests and guarantee fair trials",
        "The National Report cites existing constitutional and procedural "
        "guarantees; the UN country team reports prolonged pre-trial detention "
        "under the Terrorism Act and Amnesty reports limited judicial oversight.",
        [
            ("Eswatini", "1", "45", "Section 16 of the Constitution prohibits arbitrary arrest and detention"),
            ("United Nations country team", "2", "19", "persons charged under that Act had reportedly been subjected to prolonged pretrial detention"),
        ],
    ),
    "Economic, social & cultural rights - general measures of implementation": (
        B, "Implement economic and social development programmes",
        "The Government Programme of Action, National Development Plan "
        "2023-2028 and regional agricultural funds target disparities.",
        [
            ("Eswatini", "1", "75", "The NDP prioritises poverty reduction, food security, and inclusive economic growth"),
        ],
    ),
    "Land & property rights": (
        B, "Agricultural productivity and women's access to land",
        "The Regional Development Fund and Agricultural Development Fund "
        "financed 107 projects (60% women beneficiaries); JS3 notes dual "
        "tenure still restricts women's land rights.",
        [
            ("Eswatini", "1", "76", "the Regional Development Fund (RDF) supported 107 agricultural projects to enhance productivity and food security"),
            ("JS3", "3", "93", "dual tenure (Title Deed Land and Swazi Nation Land) and customary allocation practices continued to restrict women’s tenure rights"),
        ],
    ),
    "Rights related to name, identity & nationality": (
        C, "Equal rights of mothers and fathers to transmit nationality",
        "No reform is reported; the UN country team recommends amending "
        "section 43 of the Constitution and the Citizenship Act.",
        [
            ("United Nations country team", "2", "111", "amend section 43 of the Constitution on citizenship by birth and the Citizenship Act, 1992, to remove gender-discriminatory provisions"),
        ],
    ),
}

KEYWORDS = [
    # --- ratification specifics ---
    (r"Convention relating to the Status of Stateless Persons", D,
     "Ratify the statelessness conventions",
     "The documents contain no information on this recommendation.", []),
    # --- LGBTI ---
    (r"same-sex|sexual orientation|gender identity|lesbian, gay|homosexual", C,
     "Decriminalise same-sex relations and prohibit discrimination based on sexual orientation and gender identity",
     "The National Report says equality before the law applies to all and denies any case of abuse on these grounds; colonial-era common-law offences still criminalise same-sex conduct and there is no anti-discrimination law covering these grounds.",
     [("Eswatini", "1", "28", "There have been no reported cases of people being violated or abused on the basis of their sexual orientation"),
      ("JS8", "3", "98", "consensual same-sex conduct remained effectively criminalized in Eswatini through the continued existence of colonial-era common law offences"),
      ("JS8", "3", "97", "there was no comprehensive anti-discrimination legislation explicitly prohibiting discrimination based on sexual orientation and gender identity")]),
    (r"^Take the necessary steps to combat discrimination and violence against women and children, and on the basis of sexual", B,
     "Combat discrimination and violence against women and children (and on grounds of sexual orientation)",
     "Measures on violence against women and children exist; nothing is reported on sexual orientation and gender identity.",
     [("Eswatini", "1", "58", "The DPMO has adopted a formalised Gender-Based Violence (GBV) Coordination Mechanism"),
      ("Eswatini", "1", "28", "There have been no reported cases of people being violated or abused on the basis of their sexual orientation")]),
    # --- women's legal reform ---
    (r"^(Establish the legal framework for the domestication|Make further efforts to bring the legislation into compliance|Take action to align all laws|Ensure that the national legislation is in line)", C,
     "Domesticate CEDAW and align family and succession laws",
     "CEDAW is not incorporated into domestic law and the Marriages Bill 8 of 2022 and Matrimonial Property Bill 9 of 2022 are still not enacted; the Government itself requests support for the Family Law Bills.",
     [("Eswatini", "1", "21", "While CEDAW has not yet been fully incorporated into domestic law, the Government is progressively aligning national laws with the Convention’s provisions"),
      ("Eswatini", "1", "128", "The Government requires technical and financial support for the full operationalisation of the Legal Aid Act, the Commission on Human Rights and Public Administration Bill, and the comprehensive Family Law Bills")]),
    (r"^Review the Constitution and law on nationality", C,
     "Review nationality laws to guarantee women equal rights",
     "No reform is reported; the UN country team recommends amending section 43 of the Constitution and the Citizenship Act.",
     [("United Nations country team", "2", "111", "amend section 43 of the Constitution on citizenship by birth and the Citizenship Act, 1992, to remove gender-discriminatory provisions")]),
    # --- freedom of expression / terrorism acts ---
    (r"^Repeal the 1938 Sedition and Subversive Activities Act", E,
     "Repeal the 1938 Sedition and Subversive Activities Act",
     "The Supreme Court upheld the Act and the Suppression of Terrorism Act in August 2024 and Eswatini cites the judgment as affirming that rights are subject to lawful limitations; the Act continues to be applied against dissent.",
     [("Eswatini", "1", "47", "the Supreme Court upheld the Sedition and Subversive Activities Act 46 of 1938 and Suppression of Terrorism Act 3 of 2028 as consistent with constitutional guarantees"),
      ("United Nations country team", "2", "34", "restricted debate and dissent through broad discretionary powers and criminal sanctions")]),
    (r"^Withdraw all criminal charges brought against human rights defenders", E,
     "Withdraw charges against defenders under the Suppression of Terrorism Act and repeal the Act",
     "The Act was upheld by the Supreme Court (August 2024) and continues to be used; Amnesty and El Hak call for charges to be dropped.",
     [("Eswatini", "1", "47", "the Supreme Court upheld the Sedition and Subversive Activities Act 46 of 1938 and Suppression of Terrorism Act 3 of 2028 as consistent with constitutional guarantees"),
      ("Amnesty International", "3", "58", "withdraw all charges brought solely under the Suppression of Terrorism Act that related to the peaceful exercise of the rights to freedom of expression, association and peaceful assembly")]),
    (r"^Immediately end law enforcement violence", E,
     "End law enforcement violence against peaceful assemblies",
     "The ILO reports that more than 80 people were reported to have lost their lives in police crackdowns on protests in 2022-2023 and the UN country team reports excessive force against peaceful assemblies; the State maintains the force used was necessary and proportionate.",
     [("ILO Committee of Experts", "2", "52", "more than 80 people were reported to have lost their lives because of police crackdowns on protests"),
      ("Eswatini", "1", "39", "The outcome of these reviews did not reveal evidence of unlawful conduct on the part of police officers in the discharge of their duties")]),
    (r"^(Take steps to prevent excessive use of force|Enter into a genuine, inclusive and comprehensive dialogue|Create an environment that facilitates inclusive, productive dialogue)", B,
     "Dialogue with demonstrators and prevention of excessive force",
     "Eswatini convened the Sibaya national dialogue (23 October-3 November 2023), trained more than 2,000 security personnel on lawful use of force and 353 police officers with CHRPA; investigations of the 2021 unrest were internal and the UN country team reports ongoing excessive force.",
     [("Eswatini", "1", "48", "Eswatini convened Sibaya on 23 October–3 November 2023, a national dialogue that is inclusive of all stakeholders, including those critical of the Government policies and actions"),
      ("Eswatini", "1", "16", "The CHRPA trained more than 2,000 security personnel on human rights-compliant policing"),
      ("United Nations country team", "2", "39", "participants in peaceful assemblies had been met with excessive force, arbitrary arrests, prolonged detention and serious injuries")]),
    (r"^Investigate allegations of human rights violations by security forces against protesters", C,
     "Investigate violations by security forces against protesters in 2021 and ensure accountability",
     "The State's internal reviews found no unlawful conduct; the UN country team reports that investigations have stalled and ICJ and Amnesty call for an independent mechanism.",
     [("Eswatini", "1", "38", "the REPS undertook internal investigations and reviews of incidents involving the use of force during the unrest"),
      ("United Nations country team", "2", "24", "investigations had stalled in relation to the perpetrators of the 2021–2023 violence in which protestors, including a prominent human rights lawyer, had been killed")]),
    # --- torture ---
    (r"^(Accede to the Optional Protocol to the Convention against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment and take|Ensure that impartial investigations are carried out, that the perpetrators are prosecuted and that human rights training)", B,
     "Prevent torture by law enforcement: training and complaints",
     "CHRPA trained more than 2,000 security personnel, the Police Academy trained 353 officers and 1,189 officers received human-rights refresher courses; OP-CAT is still not ratified and investigations are internal.",
     [("Eswatini", "1", "16", "The CHRPA trained more than 2,000 security personnel on human rights-compliant policing"),
      ("Eswatini", "1", "36", "1,189 officers received refresher courses with human rights components"),
      ("Amnesty International", "3", "2", "Eswatini had still not ratified OP-CAT, the ICCPR-OP 2, the OP-CEDAW, and the ICRMW")]),
    # --- death penalty ---
    (r"^Strengthen awareness-raising campaigns and public debates on the death penalty", D,
     "Awareness-raising and public debate on the death penalty",
     "The documents contain no information on this recommendation.", []),
    # --- education ---
    (r"COVID-19 pandemic", A,
     "Maintain access to education during the COVID-19 pandemic",
     "Radio, television, print and blended learning reached about 70% of enrolled learners, all public schools reopened under health protocols and a Learning Passport platform was introduced.",
     [("Eswatini", "1", "111", "These interventions reached approximately 70 % of enrolled learners"),
      ("Eswatini", "1", "112", "MoET introduced the Learning Passport, a digital platform providing continuous access to curriculum-based learning during emergencies")]),
    (r"menstrual hygiene", D,
     "Menstrual hygiene management to combat school dropout",
     "The documents contain no information on this recommendation.", []),
    (r"free education from the eighth|compulsory free education up to|free education policy at the secondary", C,
     "Introduce free secondary education",
     "The National Report states that Eswatini is not yet ready to provide free secondary education; a task team is studying standardised fees.",
     [("Eswatini", "1", "114", "Due to resource constraints, Eswatini is not yet ready to provide free secondary education"),
      ("Eswatini", "1", "118", "MOET commissioned an Education Sector Transformation Task Team to develop innovative means for standardising secondary school fees")]),
    # --- SRHR ---
    (r"Decriminalize abortion|Repeal laws that do not allow safe abortions|comprehensive sexuality education", C,
     "Decriminalise abortion and provide comprehensive sexuality education",
     "The National Report states that abortion is not criminalised in cases of rape, incest, fetal malformation or risk to health or life, without citing a legal change; the CRC recommends comprehensive sexuality education in the compulsory curriculum.",
     [("Eswatini", "1", "104", "Eswatini does not criminalise abortion in cases of rape, incest, serious fetal malformation, or risks to the health or life of the pregnant woman"),
      ("Committee on the Rights of the Child", "2", "69", "ensure that comprehensive sexual and reproductive health education was part of the compulsory school curriculum")]),
    # --- children ---
    (r"^Finalize the approval process for the national strategy and the action plan on positive parenting", A,
     "Approve the national strategy and plan of action on positive parenting",
     "The National Strategy and Plan of Action on Positive Parenting 2023-2027 is the national roadmap and is being implemented.",
     [("Eswatini", "1", "125", "National Strategy and Plan of Action on Positive Parenting 2023–2027")]),
    (r"^(Continue to ensure the full protection of young girls against harmful practices and forced marriages|Take further measures to prevent early and forced marriages)", B,
     "Prevent forced and child marriage",
     "Civil registration officials were trained to detect forced and child marriages, customary-marriage observers (umgijimi) check age and consent, and child marriage is prohibited by the Children's Protection and Welfare Act 2012; the minimum age of marriage is not yet 18.",
     [("Eswatini", "1", "122", "has trained officials to detect potential forced or child marriages during the registration process of marriages"),
      ("Eswatini", "1", "124", "child marriage is explicitly prohibited under the Children’s Protection and Welfare Act of 2012")]),
    (r"^Centre recovery efforts", B,
     "Child-protection systems and free education",
     "Additional social workers and community child protection committees were deployed and free primary education guaranteed; the CRC finds no integrated child protection system.",
     [("Eswatini", "1", "120", "The DPMO has reinforced additional social workers and community child protection committees")]),
    # --- participation ---
    (r"^Strengthen the participation of young people in political decision-making", B,
     "Youth participation in political decision-making",
     "The Elections and Boundaries Commission runs civic and voter education for young people through social media and national events.",
     [("Eswatini", "1", "53", "thereby expanding access to information, particularly among young people")]),
    # --- NHRI-related ---
    (r"^Include human rights in the work of the commission to reform legislation", B,
     "Human rights in the law reform commission's work",
     "The Law Reform Unit updated statutes (2023-2025) and researched constitutional provisions on estates and succession.",
     [("Eswatini", "1", "17", "The Law Reform Unit has updated and revised statutes for the period 2023–2025")]),
]

FALLBACK = (D, "No information on this recommendation",
            "The documents contain no information on this recommendation.", [])
