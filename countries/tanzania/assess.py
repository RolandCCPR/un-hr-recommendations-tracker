"""United Republic of Tanzania — implementation assessment of its 3rd-cycle (2021,
A/HRC/49/15) UPR recommendations, graded against the 4th-cycle documentation
(session 53): National Report A/HRC/WG.6/53/TZA/1, OHCHR Compilation /2 and
Stakeholders' Summary /3.

    python scripts/run_assess.py tanzania

First pass for expert review. Quotes are verbatim from the three documents.
Events after the 29 October 2025 general elections (internet shutdown, reports
of lethal force, arrests) are documented by special procedures and
stakeholders; the State rejects the allegations (Compilation, paras 10-11, 19-20).
"""

from __future__ import annotations

from recommendations.models import Grade

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

# theme -> (grade, action_summary, rationale, [(org, doc "1"|"2"|"3", para, quote)])
CLUSTERS = {
    "Ratification of & accession to international instruments": (
        C, "Ratify outstanding international instruments (CAT, ICPPED, ICRMW and others)",
        "The National Report states that Tanzania is yet to ratify the "
        "instruments recommended and continues legal and policy "
        "consultations; stakeholders confirm that CAT, ICPPED and others "
        "remain unratified.",
        [
            ("United Republic of Tanzania", "1", "13", "The URT is yet to ratify the international human rights instruments recommended during the 3rd cycle of UPR"),
            ("Stakeholders", "3", "3", "the United Republic of Tanzania had yet to ratify CAT"),
        ],
    ),
    "Freedom of opinion and expression & access to information": (
        E, "Protect freedom of expression, journalists, human rights defenders and activists",
        "The State acknowledges an internet disruption after the 29 October "
        "2025 elections, a regulator shut down more than 80,000 websites and "
        "accounts in May 2025, and special procedures and stakeholders report "
        "arrests of journalists, opposition figures and activists, enforced "
        "disappearances and lethal force; the State rejects the allegations. "
        "Contrary measures outweigh the 2022 lifting of the rally ban and the "
        "revoked newspaper suspensions.",
        [
            ("United Republic of Tanzania", "2", "20", "the Internet disruption following the events of 29 October 2025 had been a temporary measure"),
            ("ERF", "3", "29", "the Communications Regulatory Authority had shut down more than 80 000 websites, social media accounts, blogs, and online platforms"),
            ("JS7", "3", "12", "reported cases of enforced disappearances, arbitrary detention, torture and extrajudicial killing of political actors, activists, journalists and protesters before, during, and after the October 2025 elections"),
        ],
    ),
    "Right to education": (
        B, "Expand access to inclusive, quality education",
        "Education financing rose from TZS 5.6 to 6.3 trillion, 472 primary and "
        "386 secondary schools and 42 special and inclusive schools were built "
        "and a Re-Entry Guideline (2022) returned 13,272 students; UNCT and "
        "UNESCO note infrastructure, quality and legislative gaps.",
        [
            ("United Republic of Tanzania", "1", "101", "budget allocations increasing from TZS 5.6 trillion in 2022/23 to TZS 6.3 trillion in 2025/26"),
            ("United Republic of Tanzania", "1", "104", "the Re-Entry Guideline of 2022, which enabled 13,272 students to return to school"),
            ("UNESCO", "2", "35", "enact legislation to make pre-primary education free and compulsory for at least one year and to guarantee at least 12 years of free primary and secondary education"),
        ],
    ),
    "National Human Rights Action Plans (or specific areas) / implementation plans": (
        B, "Implement national action plans (GBV, trafficking, albinism)",
        "The Second National Plan of Action to End Violence Against Women and "
        "Children (2024/25-2028/29), NATIP III and the National Action Plan "
        "for Persons with Albinism (2024/25-2028/29) were adopted; the UN "
        "country team finds implementation partial.",
        [
            ("United Republic of Tanzania", "1", "27", "establishment of 550 new GBV Desks in markets, transport hubs, and other public areas across 19 regions, increasing the total number of GBV desks to 788 nationwide"),
            ("United Republic of Tanzania", "1", "36", "the National Action Plan for the Rights and Welfare of Persons with Albinism (2024/25–2028/29) was developed"),
        ],
    ),
    "Equality & non-discrimination": (
        B, "Combat discrimination against persons with albinism, women and persons affected by leprosy",
        "Tanzania adopted the National Action Plan for Persons with Albinism, "
        "extended social protection and sunscreen supply to persons with "
        "albinism, runs leprosy screening and women hold 39.3% of "
        "Parliament; attacks, stigma and legal gaps persist.",
        [
            ("United Republic of Tanzania", "1", "58", "71 criminal cases involving attacks against persons with albinism were prosecuted, of which 68 involved trafficking in body parts and 34 cases resulted in convictions"),
            ("United Republic of Tanzania", "1", "22", "women's representation in Parliament increased to 39.3% in 2025"),
            ("United Nations country team", "2", "12", "fully implement the judgment of the African Court on Human and Peoples’ Rights"),
        ],
    ),
    "Right to health": (
        B, "Expand health financing, infrastructure and access to care",
        "Health financing rose from TZS 1.31 to 3.104 trillion, facilities "
        "increased from 8,458 to 10,044, maternal mortality fell from 197 to "
        "104 per 100,000 live births; UNCT finds rural access and workforce "
        "gaps.",
        [
            ("United Republic of Tanzania", "1", "93", "Health financing increased from TZS 1.31 trillion in 2024/25 to TZS 3.104 trillion in 2025/26"),
            ("United Republic of Tanzania", "1", "96", "Maternal mortality declined from 197 deaths per 100,000 live births in 2022 to 104 in 2026"),
            ("United Nations country team", "2", "30", "accelerate equitable access to healthcare, particularly in underserved areas"),
        ],
    ),
    "Violence against women": (
        B, "Prevent and respond to violence against women and children",
        "The Second National Plan of Action (2024/25-2028/29) established 788 "
        "GBV desks, and 5,562 GBV convictions were recorded; GERG and JS30 "
        "note the lack of comprehensive GBV legislation.",
        [
            ("United Republic of Tanzania", "1", "27", "establishment of 550 new GBV Desks in markets, transport hubs, and other public areas across 19 regions, increasing the total number of GBV desks to 788 nationwide"),
            ("United Republic of Tanzania", "1", "29", "resulting in 5,562 convictions (60%) and 3,771 acquittals (40%)"),
            ("JS30", "3", "65", "there was no comprehensive legislation on gender-based violence"),
        ],
    ),
    "Children: definition": (
        C, "Raise the minimum age of marriage to 18 and amend the Law of Marriage Act",
        "Amendments to the Law of Marriage Act are only 'under consultation'; "
        "the High Court ordered the amendment in 2016, upheld on appeal, and "
        "the UN country team finds the recommendations not implemented.",
        [
            ("United Republic of Tanzania", "1", "26", "Amendment of the Law of Marriage Act, Cap. 29, are under consultation as part of broader legal reforms"),
            ("United Nations country team", "2", "47", "had not implemented the recommendations it had supported at its previous review on amending the Law of Marriage Act (1971) to raise the minimum age of marriage for girls to 18 years"),
        ],
    ),
    "Death penalty": (
        C, "Abolish the death penalty or adopt a formal moratorium",
        "Tanzania maintains a de facto moratorium (no execution since 1994) "
        "but the mandatory death penalty remains in the Penal Code and no "
        "formal moratorium or awareness campaign has followed.",
        [
            ("United Republic of Tanzania", "1", "64", "The URT maintained its de facto moratorium on the death penalty, and no executions have been carried out since 1994"),
            ("JS28", "3", "11", "the mandatory death penalty for the murder and treason as prescribed in the Penal Code required reform"),
            ("United Nations country team", "2", "9", "expressed concern about the lack of implementation of those commitments"),
        ],
    ),
    "Legal & institutional reform": (
        B, "Strengthen legal protection of vulnerable groups, including persons with albinism",
        "Tanzania adopted the National Action Plan for Persons with Albinism and "
        "prosecuted 71 attack cases; protection of sexual minorities is "
        "not addressed.",
        [
            ("United Republic of Tanzania", "1", "58", "71 criminal cases involving attacks against persons with albinism were prosecuted, of which 68 involved trafficking in body parts and 34 cases resulted in convictions"),
            ("United Nations country team", "2", "55", "criminalization of consensual same-sex relations"),
        ],
    ),
    "Constitutional & legislative framework": (
        C, "Enact legislation on sexual and gender-based violence and decriminalise same-sex relations",
        "Consensual same-sex relations remain criminalised in mainland "
        "Tanzania and Zanzibar and no comprehensive law on sexual and "
        "gender-based violence exists.",
        [
            ("JS4", "3", "79", "consensual same-sex relations remained criminalized under the laws of mainland Tanzania"),
            ("JS30", "3", "65", "there was no comprehensive legislation on gender-based violence"),
        ],
    ),
    "Liberty & security of the person": (
        B, "Protect persons with albinism and fight female genital mutilation",
        "A National Action Plan on Persons with Albinism (2024/25-2028/29) was "
        "established, 71 attack cases prosecuted (34 convictions) and a "
        "National Multisectoral Strategy to End FGM (2025/26-2029/30) "
        "adopted; JS1 reports continued attacks and killings.",
        [
            ("United Republic of Tanzania", "1", "58", "71 criminal cases involving attacks against persons with albinism were prosecuted, of which 68 involved trafficking in body parts and 34 cases resulted in convictions"),
            ("United Republic of Tanzania", "1", "55", "adopted the National Multisectoral Strategy to End Female Genital Mutilation (2025/26–2029/30)"),
            ("JS1", "3", "14", "reported attacks and killings of persons with albinism and the inadequate protection systems for them"),
        ],
    ),
    "Sexual & gender-based violence": (
        B, "Combat female genital mutilation and gender-based violence",
        "A National Multisectoral Strategy to End FGM (2025/26-2029/30) was "
        "adopted, prevalence fell from 10% to about 5% and GBV desks expanded; "
        "JS2 notes that criminal liability is limited to custodians.",
        [
            ("United Republic of Tanzania", "1", "55", "adopted the National Multisectoral Strategy to End Female Genital Mutilation (2025/26–2029/30)"),
            ("JS2", "3", "66", "restricted criminal liability to parents, guardians, or other custodial figures"),
        ],
    ),
    "Administration of justice & fair trial": (
        B, "Strengthen the judiciary and access to justice",
        "Case backlog fell from 10% to 5%, 26 High Court sub-registries and an "
        "e-Case Management System were established and the Mama Samia Legal "
        "Aid Campaign reached 7.9 million people; the UN country team and JS17 "
        "report lack of judicial independence and presidential powers over "
        "judges.",
        [
            ("United Republic of Tanzania", "1", "41", "case backlog declined from 10% in 2022 to 5% in 2023"),
            ("United Republic of Tanzania", "1", "44", "provided legal aid awareness, advice and representation to a total of 7,885,295 people"),
            ("United Nations country team", "2", "15", "expressed concern about the lack of judicial independence"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        B, "Prevent trafficking in persons and protect victims",
        "NATIP III (2021-2024), a Multi-Agency Task Force (2022), anti-trafficking "
        "secretariats and 7 safe houses were established; UNCT finds limited "
        "prosecutions and no explicit prohibition on trafficking in body parts.",
        [
            ("United Republic of Tanzania", "1", "56", "establishment of a Multi-Agency Task Force in 2022 to support coordinated investigation and prosecution of trafficking offences"),
            ("United Republic of Tanzania", "1", "57", "establishment of 7 safe houses and referral systems in Mainland Tanzania"),
            ("United Nations country team", "2", "25", "limited prosecutions, weak data systems and the absence of provisions explicitly prohibiting trafficking in body parts"),
        ],
    ),
    "Discrimination against women": (
        B, "Combat discrimination against women and girls",
        "A National Gender and Women Development Policy (2023), a National "
        "Women Access to Justice Strategy and a Gender Equality Strategy "
        "2022-2027 were adopted; customary law still disadvantages women.",
        [
            ("United Republic of Tanzania", "1", "23", "the National Gender and Women Development Policy of 2023"),
            ("JS10", "3", "10", "the coexistence of parallel legal systems created ambiguity and perpetuated discrimination against women"),
        ],
    ),
    "Children: protection against exploitation": (
        B, "Prevent child labour and sexual abuse of children",
        "A National Action Plan on the Elimination of Child Labour (2025/26-2029/30) "
        "was adopted and child labour fell from 33.8% to 25.4%; JS10 reports it "
        "remains widespread.",
        [
            ("United Republic of Tanzania", "1", "32", "These interventions contributed to reducing child labour from 33.8% to 25.4% in 2024"),
            ("JS10", "3", "41", "child labour had remained widespread, particularly in agriculture, fishing, mining, and domestic work"),
        ],
    ),
    "Right to peaceful assembly": (
        E, "Ensure freedom of assembly and a safe environment for parties, media and civil society",
        "Special procedures and stakeholders report restriction of opposition "
        "rallies, disqualification of opposition candidates, the October 2025 "
        "internet shutdown and arrests; the State rejects the allegations.",
        [
            ("JS21", "3", "36", "the Authorities had systematically restricted opposition rallies and had curtailed the movement of members of opposition parties"),
            ("Special procedure mandate holders", "2", "23", "had reportedly resulted in the disqualification of opposition candidates during the nomination process"),
            ("United Republic of Tanzania", "2", "20", "the Internet disruption following the events of 29 October 2025 had been a temporary measure"),
        ],
    ),
    "Cooperation & Follow up with Treaty Bodies": (
        B, "Submit reports to treaty bodies",
        "Tanzania is finalising overdue reports to CRPD and CEDAW and hosted an "
        "OHCHR treaty-body reporting workshop (October 2024).",
        [
            ("United Republic of Tanzania", "1", "17", "The URT is finalising its State Party Report om the Convention on the Rights of Persons with Disabilities and the Convention on the Elimination of All Forms of Discrimination Against Women"),
            ("United Republic of Tanzania", "1", "16", "from 1–3 October 2024 jointly hosted with the Office of the High Commissioner for Human Rights"),
        ],
    ),
    "Right to development": (
        B, "Implement national development plans and gender mainstreaming",
        "The Third National Five-Year Development Plan concluded and Vision "
        "2050 was launched (July 2026); the National Gender and Women "
        "Development Policy and its strategy mainstream gender in planning.",
        [
            ("United Republic of Tanzania", "1", "65", "The URT successfully concluded implementation of Tanzania Development Vision 2025 through the Third National Five-Year Development Plan (2021/22–2025/26)"),
            ("United Republic of Tanzania", "1", "9", "On 17 July, 2026 the National Development Agenda Vision 2050 was officially launched"),
        ],
    ),
    "Access to justice & remedy": (
        B, "Promote access to justice and legal aid",
        "The Mama Samia Legal Aid Campaign provided legal aid to 7.9 million "
        "people, 446 laws were translated into Kiswahili and a toll-free "
        "legal call centre was launched (2024); JS28 reports limited access "
        "for the indigent.",
        [
            ("United Republic of Tanzania", "1", "44", "provided legal aid awareness, advice and representation to a total of 7,885,295 people"),
            ("JS28", "3", "19", "Despite the Legal Aid Act, 2017, only a few indigent accused had received assistance"),
        ],
    ),
    "Cooperation with human rights mechanisms & requests for technical assistance": (
        B, "Engage with OHCHR and cooperate with UN mechanisms",
        "Tanzania hosted an OHCHR treaty-body reporting workshop (October 2024) "
        "and received an African Commission visit; the UN country team finds "
        "cooperation with special procedures not implemented.",
        [
            ("United Republic of Tanzania", "1", "16", "from 1–3 October 2024 jointly hosted with the Office of the High Commissioner for Human Rights"),
            ("United Nations country team", "2", "2", "the State had not issued a standing invitation to the special procedures"),
        ],
    ),
    "Human rights & poverty": (
        B, "Reduce poverty, including among persons with albinism",
        "National poverty fell from 26.4% (2020) to 24.9% (2025), TASAF "
        "reached 1.36 million households and interest-free loans were "
        "extended to persons with disabilities including albinism.",
        [
            ("United Republic of Tanzania", "1", "66", "national basic needs poverty rate declined from 26.4% in 2020 to 24.9% in 2025"),
            ("United Republic of Tanzania", "1", "85", "TASAF benefited a total of 1.36 million households with 5,195,605 beneficiaries"),
        ],
    ),
    "Right to participate in public affairs & right to vote": (
        B, "Electoral reform and election observation",
        "Electoral laws were amended (2024), 164 CSOs were accredited for voter "
        "education and 12 international observer missions attended the 2025 "
        "elections; SADC found the elections fell short of its principles and "
        "special procedures raised questions on the electoral commission's "
        "independence.",
        [
            ("United Republic of Tanzania", "1", "62", "12 international observer missions comprising 135 observers observed the elections"),
            ("JS7", "3", "35", "found that the elections had fallen short of its principles and guidelines"),
            ("United Nations country team", "2", "21", "expressed concern about the independence and impartiality of the Independent National Electoral Commission"),
        ],
    ),
    "Land & property rights": (
        C, "Equal inheritance and customary-law reform for women",
        "Customary and religious laws continue to disadvantage women in "
        "inheritance; the National Land Policy was revised in 2025.",
        [
            ("JS10", "3", "10", "Customary and religious laws influenced matters such as inheritance and property rights, which disadvantaged women"),
        ],
    ),
    "Cooperation & Follow up with Special Procedures": (
        C, "Extend a standing invitation to special procedures",
        "The UN country team and stakeholders confirm that no standing "
        "invitation was issued and visit requests were not granted.",
        [
            ("United Nations country team", "2", "2", "the State had not issued a standing invitation to the special procedures"),
        ],
    ),
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)": (
        C, "Strengthen the fight against torture and ill-treatment; prohibit corporal punishment",
        "The UN country team finds the torture recommendation not implemented, "
        "JS15 reports ongoing risks in police custody and corporal punishment "
        "remains lawful.",
        [
            ("JS15", "3", "13", "ongoing risks of torture and ill-treatment in police custody"),
            ("JS10", "3", "70", "corporal punishment remained lawful and widely practices in homes and schools"),
        ],
    ),
    "Right to social security": (
        B, "Advance social protection",
        "A National Social Security Policy (2023) was adopted, TASAF reached "
        "1.36 million households and informal-sector coverage expanded; UNCT "
        "notes domestic workers and persons with leprosy are not covered.",
        [
            ("United Republic of Tanzania", "1", "84", "the National Social Security Policy of 2023"),
            ("United Nations country team", "2", "27", "the existing social protection programmes did not adequately cover all vulnerable groups"),
        ],
    ),
    "Safe drinking water & sanitation": (
        B, "Improve drinking water and sanitation in rural areas",
        "WSDP III completed 1,373 rural projects and raised rural access to "
        "85.2%; UNCT notes disparities in rural and informal settlements.",
        [
            ("United Republic of Tanzania", "1", "91", "increased access to water in rural areas to 85.2%, and 92.5 % in urban areas"),
            ("United Nations country team", "2", "29", "disparities in access to water in rural and informal settlements"),
        ],
    ),
    "Human rights education, trainings & awareness raising": (
        B, "Human rights training and awareness-raising",
        "Awareness programmes reached 21 million people and constitutional "
        "modules entered school curricula; JS14 notes no specific "
        "programme for public officials.",
        [
            ("United Republic of Tanzania", "1", "106", "awareness programs reached out to 21,109,573 people, including law enforcement officials, journalists, and trade unionists"),
            ("JS14", "3", "8", "there was no specific national programme for comprehensive human rights education for public service officials and students"),
        ],
    ),
    "Cooperation & follow up with the Universal Periodic Review (UPR)": (
        B, "Implement accepted UPR recommendations",
        "A national mechanism coordinates follow-up; the second National Human "
        "Rights Action Plan is still at finalisation stage.",
        [
            ("United Republic of Tanzania", "1", "18", "the draft NHRAP, which is currently at the finalisation stage"),
        ],
    ),
    "Rule of law & impunity": (
        C, "Investigate attacks on journalists and defenders; combat impunity",
        "A Presidential Commission of Inquiry (November 2025) and a Criminal "
        "Investigation Commission (May 2026) were set up on the post-election "
        "unrest, but stakeholders report reprisals and structural impunity.",
        [
            ("United Republic of Tanzania", "1", "7", "a Presidential Commission of Inquiry was established on 18 November, 2025 to examine the unrest that occurred during and after the General Elections"),
            ("JS27", "3", "24", "accountability for police abuses had remained severely undermined by a combination of political interference and structural conflicts of interest"),
        ],
    ),
    "Arbitrary arrest & detention": (
        B, "Investigate arbitrary arrests and ensure fair hearings",
        "Decision to Charge Guidelines (2023) and DPP Guidelines No. 2 of 2024 "
        "strengthened prosecutorial safeguards, and a Commission of Inquiry on "
        "the post-election unrest was created; special procedures report "
        "arbitrary arrests of protesters and opposition leaders.",
        [
            ("United Republic of Tanzania", "1", "48", "The Decision to Charge Guidelines (2023) and Director of Public Prosecutions Guidelines No. 2 of 2024 strengthened investigation standards"),
            ("United Nations country team", "2", "16", "arrests of an opposition leader during a public rally and of several young people in the aftermath of the October 2025 elections"),
        ],
    ),
    "Freedom of association": (
        B, "Amend media, political-party and communications laws",
        "The Media Services, Political Parties, Statistics and Electronic and "
        "Postal Communications Acts were amended (R.E. 2023); stakeholders "
        "consider that restrictions remain.",
        [
            ("United Republic of Tanzania", "1", "51", "These reforms removed criminal defamation provisions and strengthened safeguards for editorial independence, professional standards, and responsible media practice"),
            ("JS3", "3", "29", "licensing requirements and content restrictions"),
        ],
    ),
    "Human rights & climate change": (
        A, "Participation of women, children, persons with disabilities and local communities in climate frameworks",
        "The UN country team considers the recommendation fully implemented.",
        [
            ("United Nations country team", "2", "42", "The country team considered that it had fully implemented that recommendation"),
        ],
    ),
    "Conditions of detention": (
        B, "Reform the prison system",
        "5,923 inmates were pardoned (2025), parole and community service "
        "orders were expanded and e-courts reach 81 prisons; JS28 describes "
        "prison conditions as deplorable.",
        [
            ("United Republic of Tanzania", "1", "46", "5,923 inmates received a Presidential pardon in 2025"),
            ("JS28", "3", "16", "the conditions in prisons as deplorable"),
        ],
    ),
    "Good governance & corruption": (
        B, "Tackle corruption",
        "A 4th Strategy and Action Plan of the National Anti-Corruption Strategy "
        "(2023-2030) was developed, procurement and audit laws were revised "
        "and Tanzania left the FATF grey list (June 2025); UNCT finds the "
        "recommendation partially implemented.",
        [
            ("United Republic of Tanzania", "1", "75", "developed the 4th SAP of the NACSAP (2023-2030)"),
            ("United Republic of Tanzania", "1", "77", "grey list effective June 13, 2025"),
        ],
    ),
    "Rights related to marriage & family": (
        B, "Marriage registration",
        "Marriage registration services are administered by RITA and amendments "
        "to the Law of Marriage Act are under consultation.",
        [
            ("United Republic of Tanzania", "1", "26", "continued strengthening of the civil registration system, including marriage registration services administered by RITA"),
        ],
    ),
    "Right to adequate housing": (
        B, "Improve access to adequate housing, water and sanitation",
        "Housing construction loans reached 31% of loans (TZS 659.3 billion) "
        "and the Zanzibar Housing Corporation built 144 units; UNCT finds "
        "partial implementation.",
        [
            ("United Republic of Tanzania", "1", "89", "accessible housing construction loans, which reached 31% of loans worth TZS 659.3 billion"),
        ],
    ),
    "Sexual & reproductive health and rights": (
        A, "Prenatal and postnatal health rights of women",
        "The UN country team considers the recommendation fully implemented.",
        [
            ("United Nations country team", "2", "31", "had fully implemented the recommendation to strengthen measures to safeguard the health rights of women, particularly on issues relating to prenatal and postnatal care"),
        ],
    ),
    "Persons with disabilities: definition, general principles": (
        B, "Empower persons with disabilities",
        "The Persons with Disabilities Policy was revised (2023), a National "
        "Assistive Technology Strategy 2024-2027 launched and interest-free "
        "loans extended; UNCT finds partial implementation.",
        [
            ("United Republic of Tanzania", "1", "34", "the Person with Disabilities Policy of 2004 was revised in 2023"),
            ("United Republic of Tanzania", "1", "35", "launched the National Assistive Technology Strategy (2024-2027) on 3rd December, 2024"),
        ],
    ),
    "Rights related to name, identity & nationality": (
        A, "Birth registration for all children",
        "The UN country team considers the recommendation fully implemented, "
        "noting legal reforms and a nationwide simplified registration for "
        "children under 5.",
        [
            ("United Nations country team", "2", "57", "The country team considered that the United Republic of Tanzania had fully implemented the recommendation"),
        ],
    ),
    "Budget & resources (for human rights implementation)": (
        B, "Adequate resources for health and education",
        "Health financing rose from TZS 1.31 to 3.104 trillion and education "
        "financing from TZS 5.6 to 6.3 trillion.",
        [
            ("United Republic of Tanzania", "1", "93", "Health financing increased from TZS 1.31 trillion in 2024/25 to TZS 3.104 trillion in 2025/26"),
            ("United Republic of Tanzania", "1", "101", "budget allocations increasing from TZS 5.6 trillion in 2022/23 to TZS 6.3 trillion in 2025/26"),
        ],
    ),
    "Advancement of women": (
        B, "Protect the rights of women, children and persons with disabilities",
        "Gender, child-protection and disability policies were adopted and "
        "expanded.",
        [
            ("United Republic of Tanzania", "1", "23", "the National Gender and Women Development Policy of 2023"),
        ],
    ),
    "Persons with disabilities: accessibility, mobility": (
        B, "Accessibility of public places and transport",
        "New courts, health facilities and schools incorporate ramps and "
        "accessible toilets, and accessibility regulations for public "
        "transport apply.",
        [
            ("United Republic of Tanzania", "1", "40", "newly constructed courts, Integrated Justice Centres, health facilities, schools and other public buildings incorporated ramps, accessible toilets and other universal accessibility features"),
        ],
    ),
    "Refugees & asylum seekers": (
        B, "Protect refugee claimants and ensure voluntary repatriation",
        "Tanzania hosts 164,901 refugees with UNHCR; the UN country team recommendations "
        "that non-refoulement be respected in the Burundi tripartite "
        "repatriation.",
        [
            ("United Republic of Tanzania", "1", "63", "Tanzania hosted 164,901 refugees in partnership with UNHCR and their country of origin"),
            ("United Nations country team", "2", "56", "comply with the principle of non-refoulement in the implementation of the tripartite agreement on the repatriation of Burundian refugees"),
        ],
    ),
    "Indigenous peoples": (
        E, "Clarify land rights and safeguard indigenous culture and livelihoods",
        "Tanzania states that no group is recognised as indigenous and denies "
        "the allegations of eviction; special procedures and stakeholders report "
        "forced evictions in Ngorongoro and Ruaha: a position contrary to the "
        "recommendation.",
        [
            ("United Republic of Tanzania", "2", "54", "no special group or community in the country was recognized as indigenous"),
            ("JS18", "3", "76", "planned eviction of pastoralists from at least 25 villages in Ngorongoro Division"),
        ],
    ),
    "Private life & privacy": (
        D, "Ban invasive anal examinations of LGBTI persons",
        "The documents contain no information on this recommendation.", [],
    ),
}

KEYWORDS = [
    # --- ratification ---
    (r"Convention on the Rights of Persons with Disabilities", B,
     "Implement the Convention on the Rights of Persons with Disabilities",
     "Tanzania is a party and is finalising its first report; the Persons with Disabilities Policy was revised and an assistive technology strategy launched.",
     [("United Republic of Tanzania", "1", "17", "The URT is finalising its State Party Report om the Convention on the Rights of Persons with Disabilities"),
      ("United Republic of Tanzania", "1", "34", "the Person with Disabilities Policy of 2004 was revised in 2023")]),
    (r"^Establish a moratorium (on the death penalty with a view to its eventual abolition|on executions with a view to abolishing)", B,
     "Establish a moratorium on executions",
     "Tanzania maintains a de facto moratorium (no execution since 1994) which it has not formalised.",
     [("United Republic of Tanzania", "1", "64", "The URT maintained its de facto moratorium on the death penalty, and no executions have been carried out since 1994"),
      ("JS28", "3", "11", "As no executions had been carried out since 1994, a de facto moratorium appeared to be in place")]),
    # --- freedom of expression: law reform vs practice ---
    (r"^Increase investment in the construction of communication facilities", A,
     "Invest in communication infrastructure in rural areas",
     "Tanzania built 10,787 communication towers, extended the fibre-optic backbone to 15,167 km and raised internet penetration from 25% to 85.3%.",
     [("United Republic of Tanzania", "1", "54", "expanded the national fibre optic backbone to 15,167 kilometres"),
      ("United Republic of Tanzania", "1", "54", "Internet penetration increased from 25% (15.6 million users) to 85.3% (58.1 million users) by December 2025")]),
    (r"^(Amend the Media Services Act of 2016|Promote freedom of the media by ensuring full compliance|Repeal or amend laws unreasonably restricting|Amend the domestic legal framework|Amend the Media Services Act, the Political Parties Act|Review legislation, including the Cybercrimes Act|Ensure, through dialogue and technical support|Repeal or amend national legislation that restricts civil society|Amend or repeal aspects of the Political Parties Act|Repeal or amend all laws that are not in conformity|Guarantee freedom of assembly, association, expression and press freedom for members|Ensure that the laws governing the right to freedom of peaceful assembly)", B,
     "Amend laws restricting freedom of expression, assembly and association",
     "The Media Services, Access to Information, Cybercrimes, Political Parties, Statistics and Electronic and Postal Communications Acts were amended (R.E. 2023), removing criminal defamation provisions, and the political-rally ban was lifted (2022-2023); stakeholders consider that licensing and content restrictions remain.",
     [("United Republic of Tanzania", "1", "51", "These reforms removed criminal defamation provisions and strengthened safeguards for editorial independence, professional standards, and responsible media practice"),
      ("United Republic of Tanzania", "1", "4", "Its recommendations led to lifting the ban on political party rallies"),
      ("JS3", "3", "29", "licensing requirements and content restrictions")]),
    (r"^Protect freedom of expression, freedom of peaceful assembly and freedom of association, bring laws", C,
     "Protect freedom of expression and assembly; reform restrictive laws and combat impunity",
     "Some laws were amended but attacks on journalists and defenders remain unaddressed; UNCT considers the recommendations on freedoms not implemented.",
     [("United Nations country team", "2", "17", "The country team considered those recommendations not to have been implemented"),
      ("United Republic of Tanzania", "1", "51", "These reforms removed criminal defamation provisions and strengthened safeguards for editorial independence, professional standards, and responsible media practice")]),
    # --- education: pregnant girls ---
    (r"^(Refrain from imposing a ban on pregnant girls|End its policy of expelling pregnant schoolgirls)", A,
     "End the ban on pregnant girls attending school",
     "Education Circular No. 2 of 2021 lifted the ban on pregnant schoolgirls and adolescent mothers may return after childbirth; a Re-Entry Guideline (2022) returned 13,272 students.",
     [("UNESCO", "2", "39", "the ban on pregnant schoolgirls had been lifted in both mainstream schools and alternative learning pathways and adolescent mothers were allowed to return to education after childbirth"),
      ("United Republic of Tanzania", "1", "104", "the Re-Entry Guideline of 2022, which enabled 13,272 students to return to school")]),
    (r"pregnant girls|pregnant schoolgirls|pregnant|young mothers", B,
     "Re-entry to education for pregnant girls and young mothers",
     "Education Circular No. 2 of 2021 and a Re-Entry Guideline (2022) allow return after childbirth (13,272 returned); JS2 notes restrictive provisions, discretion of schools and no measure against pregnancy tests.",
     [("United Republic of Tanzania", "1", "104", "the Re-Entry Guideline of 2022, which enabled 13,272 students to return to school"),
      ("JS2", "3", "59", "existing laws and policies neither adequately addressed, nor sufficiently facilitated, their re-entry into the education system")]),
    (r"^(Refrain from imposing a ban on pregnant girls|End its policy of expelling pregnant schoolgirls)", A,
     "End the ban on pregnant girls attending school",
     "Education Circular No. 2 of 2021 lifted the ban on pregnant schoolgirls and adolescent mothers may return after childbirth; a Re-Entry Guideline (2022) returned 13,272 students.",
     [("UNESCO", "2", "39", "the ban on pregnant schoolgirls had been lifted in both mainstream schools and alternative learning pathways and adolescent mothers were allowed to return to education after childbirth"),
      ("United Republic of Tanzania", "1", "104", "the Re-Entry Guideline of 2022, which enabled 13,272 students to return to school")]),
    # --- plans ---
    (r"^(Approve the implementation of the national human rights action plan|Expedite ongoing efforts aimed at the early finalization|Accelerate the adoption of the overdue|Enhance the national infrastructure for the effective implementation of the national human rights action plan|Expedite the adoption of the second national human rights action plan)", C,
     "Adopt and implement the second National Human Rights Action Plan",
     "The second plan has been drafted since 2017-2018 and is only 'at the finalisation stage'; JS26 reports the 2018-2022 plan expired without implementation.",
     [("United Republic of Tanzania", "1", "18", "the draft NHRAP, which is currently at the finalisation stage"),
      ("JS26", "3", "7", "the National Human Rights Action Plan (2018-2022) had expired without implementation")]),
    (r"^Adopt a national strategy and action plan for the prevention of radicalization", C,
     "Adopt a national strategy against radicalisation and violent extremism",
     "JS7 reports that no such strategy and plan has been published.",
     [("JS7", "3", "17", "no such strategy and plan had been published")]),
    # --- LGBTI ---
    (r"sexual orientation|LGBTQI|same-sex|sexual minorities|lesbian, gay", C,
     "Decriminalise same-sex relations and protect LGBTI persons",
     "Consensual same-sex relations remain criminalised in mainland Tanzania and Zanzibar; JS4 reports deregistration of 14 organisations serving LGBTI persons and no measurable progress on violence against LGBTI persons.",
     [("United Nations country team", "2", "55", "criminalization of consensual same-sex relations"),
      ("JS4", "3", "32", "the Authorities had deregistered 14 organizations that had provided health and support services to LGBTI persons")]),
    (r"^Respect the right to confidentiality and dignity of LGBTI", D,
     "Ban invasive anal examinations of LGBTI persons",
     "The documents contain no information on this recommendation.", []),
    # --- violence/marriage ---
    (r"^Enact a comprehensive law on sexual and gender-based violence|^Step up efforts on the legislative front", C,
     "Enact comprehensive legislation on gender-based violence",
     "JS30 notes there is no comprehensive legislation on gender-based violence and the framework is fragmented; JS14 notes no definition of marital rape.",
     [("JS30", "3", "65", "there was no comprehensive legislation on gender-based violence"),
      ("JS14", "3", "65", "the absence of definitions of “marital rape” and “family violence” in national policy")]),
    (r"Law of Marriage Act|minimum (legal )?age of marriage|outlaw all forms of child marriage|^Continue to combat the phenomena of child, early and forced marriage", C,
     "Amend the Law of Marriage Act and raise the minimum age of marriage to 18",
     "Amendment is only 'under consultation'; the High Court ordered it in 2016 and JS2 notes the Act still allows girls to marry at 14.",
     [("United Republic of Tanzania", "1", "26", "Amendment of the Law of Marriage Act, Cap. 29, are under consultation as part of broader legal reforms"),
      ("JS2", "3", "69", "the Law of Marriage Act, which allowed girls as young as 14 years of age to marry, had not been amended")]),
    (r"^(Strengthen the policies and the legal framework to ensure marriage registration|Promote the elimination of discrimination against women and girls|Enhance the protection of girls and women of all ages from the practice of female genital|Adopt legislative and policy measures to combat all forms of discrimination)", B,
     "Combat child marriage, FGM and discrimination against women",
     "FGM prevalence fell from 10% to about 5% under national strategies, marriage registration was digitalised through RITA and pregnant girls may return to school; the Law of Marriage Act has not been amended.",
     [("United Republic of Tanzania", "1", "55", "adopted the National Multisectoral Strategy to End Female Genital Mutilation (2025/26–2029/30)"),
      ("United Republic of Tanzania", "1", "26", "continued strengthening of the civil registration system, including marriage registration services administered by RITA")]),
    (r"corporal punishment", C,
     "Prohibit corporal punishment",
     "Corporal punishment remains lawful in schools and homes.",
     [("UNESCO", "2", "49", "recommended legally proscribing corporal punishment in education settings"),
      ("JS10", "3", "70", "corporal punishment remained lawful and widely practices in homes and schools")]),
    (r"^Continue to protect the rights of children through the strengthening of protective policies", B,
     "Protect children's rights",
     "Child helpline, online-protection campaign, child justice strategy, child labour action plan and fee-free basic education were implemented; legislation on marriage and corporal punishment is unchanged.",
     [("United Republic of Tanzania", "1", "30", "National Child Online Protection Campaign in all 26 regions of Mainland Tanzania")]),
    # --- death penalty ---
    (r"^Strengthen awareness-raising campaigns on the death penalty", C,
     "Awareness campaigns and public debates on the death penalty",
     "The UN country team expresses concern about the lack of implementation of this commitment.",
     [("United Nations country team", "2", "9", "expressed concern about the lack of implementation of those commitments")]),
    # --- inheritance/land ---
    (r"rights in matters of inheritance, succession and land", B,
     "Women's inheritance and land rights",
     "The National Land Policy was revised in 2025 and women land-right holders rose from 28.5% to 35%; customary inheritance rules persist.",
     [("United Republic of Tanzania", "1", "22", "the proportion of women land-right holders rose from 28.5% in 2020 to 35.0% in 2025"),
      ("JS10", "3", "10", "Customary and religious laws influenced matters such as inheritance and property rights, which disadvantaged women")]),
    (r"^Revoke customary laws that undermine women", C,
     "Revoke discriminatory customary laws on women's land rights",
     "CHRAGG recommends repeal of the 1963 Local Customary Law Declaration Order; no repeal is reported.",
     [("CHRAGG", "3", "2", "Repeal The Customary Law (Declaration) Order (GN. No. 436/1963) (No.4)")]),
    # --- older persons ---
    (r"older persons", A,
     "Protect the rights of older persons",
     "The Elder Persons Matters Act No. 2 of 2020 and the revised National Ageing Policy apply; the UN country team considers the recommendation implemented.",
     [("United Republic of Tanzania", "1", "88", "Elder Persons Matters Act No. 2 of 2020"),
      ("United Nations country team", "2", "50", "had implemented the relevant recommendation it had supported at the previous review")]),
    # --- health ---
    (r"^Strengthen HIV-prevention programmes aimed at young people", B,
     "Expand HIV prevention among young people",
     "The National HIV Prevention Road Map (2023/24-2026/27) expands youth-friendly services; the UN country team calls to expand youth-focused HIV prevention.",
     [("United Republic of Tanzania", "1", "99", "National HIV Prevention Road Map (2023/24–2026/27)")]),
    # --- justice / detention ---
    (r"^(End illegal pretrial detention|Review the legislation on the automatic denial of bail|Ensure access to justice, including by addressing the use of non-bailable offences)", C,
     "End unlawful pre-trial detention and review non-bailable offences",
     "ERF reports a significantly high number of persons in prolonged pre-trial detention and JS17 reports that over 1,700 persons were held for non-bailable offences after the October 2025 elections.",
     [("ERF", "3", "21", "a significantly high number of persons had been held in pro-longed pre-trial detention"),
      ("JS17", "3", "22", "over 1,700 persons had reportedly been held under investigation for non-bailable offences")]),
    (r"^Improve further the independence of the judicial system and its impartial attitude towards the lesbian", C,
     "Judicial independence and impartiality towards LGBTI persons",
     "JS17 reports extensive presidential powers over judicial appointments and removal; criminalisation continues.",
     [("JS17", "3", "18", "conferred on the Presidency extensive powers in relation to judicial appointments, tenure and removal")]),
    (r"^Take steps to promptly and effectively investigate and provide information on cases of arbitrary arrest", B,
     "Investigate arbitrary arrest and detention of political opponents and activists",
     "A Presidential Commission of Inquiry (November 2025) and a Criminal Investigation Commission (May 2026) were set up on the post-election unrest; the State rejects allegations of arbitrary arrests.",
     [("United Republic of Tanzania", "1", "7", "a Presidential Commission of Inquiry was established on 18 November, 2025 to examine the unrest that occurred during and after the General Elections"),
      ("United Republic of Tanzania", "2", "11", "It rejected the allegations of widespread arbitrary arrests and detentions")]),
    (r"^Conduct full and impartial investigations of all threats and attacks against and killings of journalists", C,
     "Investigate attacks and killings of journalists and defenders",
     "A Commission of Inquiry was created on the post-election unrest but reprisals against defenders and lawyers are reported.",
     [("United Republic of Tanzania", "1", "7", "a Presidential Commission of Inquiry was established on 18 November, 2025 to examine the unrest that occurred during and after the General Elections"),
      ("JS17", "3", "23", "reprisals against lawyers involved with human rights causes or associated with opposition political parties")]),
    (r"^Take all necessary measures to combat impunity for the crimes of enforced disappearance and human trafficking", B,
     "Combat impunity for enforced disappearance and human trafficking",
     "Anti-trafficking prosecutions and a Multi-Agency Task Force exist; enforced disappearances reported after the October 2025 elections are denied by the State.",
     [("United Republic of Tanzania", "1", "56", "establishment of a Multi-Agency Task Force in 2022 to support coordinated investigation and prosecution of trafficking offences"),
      ("JS7", "3", "12", "reported cases of enforced disappearances, arbitrary detention, torture and extrajudicial killing of political actors, activists, journalists and protesters before, during, and after the October 2025 elections")]),
    # --- trafficking ---
    (r"^Review the legislative framework and ensure that it sufficiently addresses trafficking in body parts", C,
     "Address trafficking in body parts in legislation",
     "The UN country team notes the absence of provisions explicitly prohibiting trafficking in body parts.",
     [("United Nations country team", "2", "25", "the absence of provisions explicitly prohibiting trafficking in body parts")]),
    # --- special procedures / cooperation ---
    (r"^Continue cooperation with the Human Rights Council and its mechanisms, including the special procedures", C,
     "Cooperate with Human Rights Council mechanisms, including special procedures",
     "The UN country team considers cooperation with special procedures not implemented; visit requests by three Special Rapporteurs were not granted.",
     [("United Nations country team", "2", "2", "the State had not issued a standing invitation to the special procedures or granted the requests for visits")]),
    # --- participation / elections ---
    (r"^Ensure a safe and enabling environment for political parties", E,
     "Ensure a safe and enabling environment for political parties, civil society and defenders",
     "Opposition rallies were restricted, opposition candidates disqualified and the 29 October 2025 elections followed by an internet shutdown and reports of lethal force; the State rejects the allegations.",
     [("JS21", "3", "36", "the Authorities had systematically restricted opposition rallies and had curtailed the movement of members of opposition parties"),
      ("Special procedure mandate holders", "2", "23", "had reportedly resulted in the disqualification of opposition candidates during the nomination process")]),
    # --- NGOs ---
    (r"^Amend the Non-Governmental Organizations Act \(Amendments\) Regulation 2018", C,
     "Amend the NGO regulations in line with international standards",
     "JS5 and JS21 report broad registration discretion and burdensome compliance; 14 LGBTI-serving organisations were deregistered.",
     [("JS5", "3", "32", "granted the Authorities broad discretion to deny registration or impose restrictions on organizations")]),
    # --- other ---
    (r"^Implement the national action plan for persons with albinism", B,
     "Implement the national action plan for persons with albinism",
     "The National Action Plan for Persons with Albinism (2024/25-2028/29) was adopted and 71 attack cases were prosecuted; the UN country team calls for stronger implementation and for the African Court judgment to be implemented.",
     [("United Republic of Tanzania", "1", "36", "the National Action Plan for the Rights and Welfare of Persons with Albinism (2024/25–2028/29) was developed"),
      ("United Nations country team", "2", "12", "fully implement the judgment of the African Court on Human and Peoples’ Rights")]),
    (r"^Clarify land rights and safeguard indigenous culture", E,
     "Clarify land rights and safeguard indigenous culture and livelihoods",
     "Tanzania states that no group is recognised as indigenous; special procedures and stakeholders report forced evictions in Ngorongoro and Ruaha.",
     [("United Republic of Tanzania", "2", "54", "no special group or community in the country was recognized as indigenous"),
      ("JS18", "3", "76", "planned eviction of pastoralists from at least 25 villages in Ngorongoro Division")]),
]

FALLBACK = (D, "No information on this recommendation",
            "The documents contain no information on this recommendation.", [])
