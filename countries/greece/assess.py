"""Greece — implementation assessment of its 3rd-cycle (2021, A/HRC/49/5) UPR
recommendations, graded against the 4th-cycle documentation (session 53):
National Report A/HRC/WG.6/53/GRC/1, OHCHR Compilation /2 and Stakeholders'
Summary /3.

    python scripts/run_assess.py greece

First pass for expert review. Quotes are verbatim from the three documents.
"""

from __future__ import annotations

from recommendations.models import Grade

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

# theme -> (grade, action_summary, rationale, [(org, doc "1"|"2"|"3", para, quote)])
CLUSTERS = {
    "Racial discrimination": (
        B, "Combat racism, hate speech and hate crime",
        "Greece adopted a second National Action Plan against Racism and "
        "Intolerance (February 2026), created a Community-Oriented Policing "
        "Directorate with a Department for Combating Racism (Law 5187/2025) and "
        "extended the media regulator's remit to online platforms; CERD found "
        "implementation of the previous plan low and calls for stronger "
        "enforcement of article 82A and victim support.",
        [
            ("Greece", "1", "9", "adopted in February 2026 the second National Action Plan against Racism and Intolerance"),
            ("Greece", "1", "12", "Law 5187/2025 established the Community-Oriented Policing Directorate as a permanent institutional structure"),
            ("Committee on the Elimination of Racial Discrimination", "2", "16", "expressed concern about the low level of implementation of the National Action Plan against Racism and Intolerance, of 2020–2023"),
        ],
    ),
    "Administration of justice & fair trial": (
        C, "Investigate pushbacks, ensure individual assessment and access to asylum",
        "Greece describes a three-tier complaints system and a Fundamental "
        "Rights Officer, but the Human Rights Committee remains gravely "
        "concerned about pushbacks and questions the independence of the "
        "monitoring mechanisms; in July 2025 Greece suspended the registration "
        "of asylum applications of people arriving by sea.",
        [
            ("Greece", "1", "50", "Greece has put in place a three-tier system to address complaints"),
            ("Human Rights Committee", "2", "53", "remained gravely concerned about pushbacks of asylum-seekers, refugees and migrants at the country’s sea and land borders, in violation of the principle of non-refoulement"),
            ("Several submissions", "3", "35", "in July 2025, the submission of asylum applications by third-country nationals entering Greek territory by sea was suspended for a period of three months"),
        ],
    ),
    "Equality & non-discrimination": (
        B, "Strengthen non-discrimination policies and protection of minorities and LGBTIQ+ persons",
        "Greece enacted marriage equality (Law 5089/2024), banned conversion "
        "therapy (Law 4931/2022) and non-consensual interventions on intersex "
        "minors (Law 4958/2022), adopted a National LGBTIQ+ Equality Strategy "
        "2021-2025 and extended disciplinary sanctions for discrimination; "
        "discrimination, hate speech and weak implementation persist.",
        [
            ("Greece", "1", "15", "Law 5089/2024 on civil marriage equality represents a historic milestone, extending the right to marriage to same-sex couples"),
            ("Greece", "1", "21", "Law 5225/2025 amended the Civil Servants' Code to extend an existing disciplinary offense"),
            ("JS5", "3", "29", "LGBTIQ+ individuals in Greece continued to experience discrimination, harassment, and an alarming escalation in hate-motivated violence"),
        ],
    ),
    "Right to education": (
        B, "Inclusive and equal access to education",
        "Greece operates Reception Classes and School Annexes, Educational "
        "Priority Zones, unconditional enrolment of Roma children and a "
        "2025-2030 violence-prevention strategy; the CRC and OSCE-ODIHR note "
        "continued exclusion of Roma and migrant children and the Turkish "
        "minority's schools are not restored.",
        [
            ("Greece", "1", "98", "Dedicated structures, Reception School Annexes, after-hours Reception Units and Refugee Education Coordinators guarantee access to formal education for refugee and migrant children regardless of documentation status"),
            ("OSCE-ODIHR", "3", "26", "expressed concern about the alarming situation of Roma children being out of formal education"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        B, "Prevent and combat human trafficking",
        "Greece amended article 323A, runs a National Referral Mechanism "
        "(327 victims identified within Greece in 2025), is updating its "
        "National Action Plan and strengthened labour inspections; victim "
        "identification, resources and a permanent National Rapporteur remain gaps.",
        [
            ("Greece", "1", "61", "amendments to Article 323A of the Criminal Code, reflecting the full range of exploitation forms and introducing enhanced protections for minors"),
            ("Greece", "1", "63", "327 victims were identified as exploited within Greece"),
            ("TSA", "3", "15", "the Office of the National Rapporteur on Human Trafficking lacked sufficient means and remained headed by an interim rapporteur since 2021"),
        ],
    ),
    "Participation of women in political & public life": (
        B, "Increase women's political and public participation and employment",
        "A 40% candidate quota applies to all elections and the Gender "
        "Equality Observatory monitors it; women remain under 30% of elected "
        "bodies, and 2025 employment of women reached 62.3%.",
        [
            ("Greece", "1", "34", "The legislative framework mandates a minimum gender quota of 40% of candidates in parliamentary, European Parliament, municipal and regional elections"),
            ("Greece", "1", "34", "women remain significantly under-represented in elected bodies, particularly in leadership positions, where overall representation continues to fall below 30%"),
        ],
    ),
    "Conditions of detention": (
        B, "Improve conditions of detention and reduce overcrowding",
        "Law 4985/2022 created a judicial remedy on detention conditions, Law "
        "5187/2025 and Law 5282/2026 introduced electronic monitoring and "
        "community service and a 2025-2030 action plan was adopted; the CPT "
        "still calls for urgent improvements and a strategy to reduce the "
        "prison population.",
        [
            ("Greece", "1", "66", "Law 4985/2022 amended the Penitentiary Code to establish a judicial remedy enabling detainees to challenge their conditions of detention"),
            ("Greece", "1", "67", "Law 5282/2026 further introduced community service into the Penitentiary Code as an alternative to imprisonment"),
            ("European Committee for the Prevention of Torture", "3", "10", "recommended urgent improvements focusing on reducing cell occupancy, investing in maintenance, improving hygiene"),
        ],
    ),
    "Violence against women": (
        B, "Prevent and respond to violence against women",
        "Law 5172/2025 transposed the EU directive and criminalised stalking "
        "and cyber harassment, the 'Panic Button' app and 63 Domestic Violence "
        "Police Offices operate and a network of 65 facilities exists; "
        "shelter capacity is insufficient and femicide is not defined in law.",
        [
            ("Greece", "1", "39", "Law 5172/2025, transposing Directive (EU) 2024/1385, has reinforced the domestic violence protection framework"),
            ("Greece", "1", "40", "Operational Domestic Violence Police Offices have increased from 18 to 63"),
            ("Greece", "1", "38", "the Government acknowledges that shelter capacity is insufficient and is committed to expanding it"),
        ],
    ),
    "Right to an adequate standard of living": (
        B, "Social assistance, housing and living conditions",
        "Greece operates the Minimum Guaranteed Income programme, raised the "
        "minimum wage and launched a EUR 6.5 billion housing programme; "
        "conditions in pre-removal and reception facilities draw criticism.",
        [
            ("Greece", "1", "101", "The Minimum Guaranteed Income program provides financial assistance to extremely poor households and homeless individuals"),
            ("Greece", "1", "103", "A comprehensive 6.5-billion-euro program encompasses a rent rebate scheme"),
        ],
    ),
    "Discrimination against women": (
        B, "Institutional and policy framework on gender equality",
        "Law 4604/2019 and a new Ministry of Social Cohesion and Family "
        "Affairs frame gender equality, a National Action Plan 2026-2030 is "
        "being prepared and the Gender Equality Observatory collects data; "
        "CEDAW finds the laws of limited effectiveness.",
        [
            ("Greece", "1", "31", "Law 4604/2019 on the Promotion of Substantive Gender Equality mandates horizontal gender mainstreaming"),
            ("Committee on the Elimination of Discrimination against Women", "2", "41", "expressed concern about the limited effectiveness of the laws and policies to protect women’s rights"),
        ],
    ),
    "Labour rights and right to work": (
        B, "Eliminate the gender pay gap and labour discrimination",
        "Law 5316/2026 transposed the EU pay-transparency directive and Law "
        "5239/2025 requires workplace harassment policies; the unadjusted pay "
        "gap stands at 13.4%.",
        [
            ("Greece", "1", "37", "By Law 5316/2026 presented by the Ministry of Labor and Social Security and adopted in July 2026, EU Directive 2023/970 was transposed"),
            ("Greece", "1", "36", "the unadjusted gender pay gap stood at 13.4%"),
        ],
    ),
    "Ratification of & accession to international instruments": (
        C, "Ratify outstanding instruments",
        "The Committees recommend ratification of ICRMW, OP-ICESCR, OP-CRC-IC "
        "and the Domestic Workers Convention; Greece reports only the 2025 "
        "ratification of the Protocol to ILO Convention 29.",
        [
            ("Greece", "1", "5", "Greece ratified in 2025 the Protocol to ILO Convention 29"),
            ("Committee on the Rights of the Child; Committee on the Elimination of Discrimination against Women", "2", "2", "recommended that Greece ratify the Optional Protocol to the Convention on the Rights of the Child on a communications procedure"),
        ],
    ),
    "Legal & institutional reform": (
        B, "Strengthen migration and minority protection frameworks",
        "Greece consolidated its reception and asylum legal framework (Law "
        "4939/2022, Law 5307/2026), a Fundamental Rights Officer and a National "
        "Strategy for the Protection of Vulnerable Persons (June 2026); "
        "monitoring bodies' independence and pushbacks remain contested.",
        [
            ("Greece", "1", "51", "Law 4960/2022 established, within the Ministry of Migration and Asylum, the post of Fundamental Rights Officer"),
            ("Greece", "1", "57", "the GSVPIP adopted, after public consultation, the National Strategy for the Protection of Vulnerable Persons"),
        ],
    ),
    "Right to health": (
        B, "Improve access to health services",
        "Asylum seekers receive a provisional insurance and healthcare number, "
        "the Hippocrates programme screens new arrivals and Roma vaccination "
        "campaigns run; sanitation and mental-health policy gaps persist.",
        [
            ("Greece", "1", "104", "Asylum seekers benefit from a Provisional Insurance and Healthcare Number"),
            ("Greece", "1", "45", "Since July 2024, IOM's and partners’ Hippocrates program has provided medical and psychosocial screening"),
        ],
    ),
    "Children: definition": (
        B, "Promote child rights, child-centred budgeting and child poverty reduction",
        "Law 4837/2021 defined child abuse and created a national recording "
        "system, a 2025-2030 violence-prevention strategy was adopted and "
        "family benefits exist; the CRC asks for time-bound goals and a "
        "dedicated budget for the National Action Plan.",
        [
            ("Greece", "1", "88", "Law 4837/2021, which introduced statutory definitions of child abuse and established the National System for Recording and Monitoring relevant incidents"),
            ("Committee on the Rights of the Child", "2", "13", "recommended that Greece equip the National Action Plan with time-bound and measurable goals and a dedicated budget for its implementation"),
        ],
    ),
    "Freedom of thought, conscience & religion": (
        B, "Freedom of religion or belief and conscientious objection",
        "Law 5224/2025 regulates places of worship of all communities except the "
        "Orthodox Church, recognises Alevis and Law 5265/2026 revised the "
        "conscientious-objection procedure; alternative service remains "
        "longer than military service and the State remains involved in the "
        "selection of Muftis.",
        [
            ("Greece", "1", "76", "Law 5224/2025 strengthens the protection of freedom of worship"),
            ("JS6; JS7", "3", "7", "the punitive conditions of the alternatives to military service in Greece violated several human rights instruments"),
        ],
    ),
    "Freedom of association": (
        C, "Protect human rights defenders and humanitarian workers",
        "Law 5275/2026 simplified NGO registration but the Special Rapporteur "
        "on human rights defenders finds the registration regime "
        "discriminatory and reports a hostile environment and criminalisation "
        "of search-and-rescue work.",
        [
            ("Greece", "1", "58", "Law 5275/2026 limited the registration requirement to organizations receiving state or EU funding or operating within Ministry facilities"),
            ("Special Rapporteur on human rights defenders", "2", "25", "since 2019, human rights defenders and NGOs working in the field of migration had reported an increasingly hostile environment for their work"),
        ],
    ),
    "Persons with disabilities: definition, general principles": (
        B, "Inclusion of persons with disabilities and harmonisation with the CRPD",
        "Greece adopted a National Strategy for the Rights of Persons with "
        "Disabilities 2024-2030, created a National Accessibility Authority, "
        "reserved 12% of public recruitment, funded personal assistants and "
        "deinstitutionalisation (700 people moved).",
        [
            ("Greece", "1", "83", "National Strategy for the Rights of Persons with Disabilities 2024–2030 sets targets across accessibility, employment, education, health and independent living"),
            ("Greece", "1", "86", "Law 4765/2021 reserves 12% of annual public sector recruitment for individuals with a disability rate of at least 50%"),
        ],
    ),
    "National Human Rights Action Plans (or specific areas) / implementation plans": (
        B, "Implement national action plans",
        "The second National Action Plan against Racism and Intolerance was "
        "adopted after an evaluation of the 2020-2023 plan, which found "
        "fragmented implementation; the unaccompanied-minor relocation scheme "
        "relocated 1,368 minors.",
        [
            ("Greece", "1", "9", "Drawing on an evaluation of the previous 2020–2023 Plan, which identified fragmented implementation, weak inter-agency coordination and overreliance on project-based funding"),
            ("Greece", "1", "56", "1,368 minors of various nationalities were relocated to twelve EU Member States"),
        ],
    ),
    "Liberty & security of the person": (
        B, "Investigate excessive use of force and train law enforcement",
        "Greece reinforced the disciplinary framework in 2024 (removal of "
        "officers in serious cases), weekly referral of cases to the "
        "Ombudsman and large-scale police training (27,130 officers since "
        "2019); the Human Rights Committee remains gravely concerned about "
        "excessive and deadly force.",
        [
            ("Greece", "1", "69", "The 2024 reform of the disciplinary legislative framework reinforced these guarantees by providing for the removal from active service of uniformed officers involved in serious criminal or disciplinary offenses"),
            ("Human Rights Committee", "2", "20", "expressed grave concern about the use of excessive and deadly force by the police and other law enforcement officials"),
        ],
    ),
    "Persons with disabilities: accessibility, mobility": (
        B, "Accessibility of services for persons with disabilities",
        "Law 5023/2023 appointed accessibility officers in all courts and "
        "extended legal aid; Law 4997/2022 subsidises accessibility upgrades "
        "and accessibility offices are required in universities by 2026.",
        [
            ("Greece", "1", "87", "appointing accessibility officers in all courts, and granting direct legal aid irrespective of income"),
        ],
    ),
    "Freedom of opinion and expression & access to information": (
        B, "Decriminalise defamation and protect journalists",
        "Law 5090/2024 repealed article 362 (simple defamation), a Memorandum "
        "of Understanding and Task Force on journalists' safety exist and Law "
        "5253/2025 created a National Action Plan for the Safety of "
        "Journalists; OSCE-ODIHR asks that remaining criminal defamation and "
        "insult provisions be replaced by civil remedies.",
        [
            ("Greece", "1", "71", "Law 5090/2024 repealed Article 362 of the Criminal Code, eliminating the offense of simple defamation"),
            ("OSCE-ODIHR", "3", "12", "criminal provisions for defamation and insult be replaced by proportional civil remedies"),
        ],
    ),
    "Rights related to name, identity & nationality": (
        C, "Birth registration, asylum registration and recognition of minority identity",
        "Greece reports no new birth-registration measure; its national "
        "report states it recognises only a religious Muslim minority in "
        "Thrace; the asylum registration platform requires detention for up "
        "to 25 days.",
        [
            ("Greece", "1", "25", "Greece recognizes as a \"minority\" the religious Muslim Minority in Thrace, the status of which was established by the 1923 Treaty of Lausanne, on the basis of religion"),
            ("Committee on the Rights of the Child", "2", "60", "further facilitate access to birth registration procedures and identity documentation"),
        ],
    ),
    "Business & Human Rights": (
        D, "Business and human rights legislation and national action plan",
        "The documents contain no information on this ask.", [],
    ),
    "Human rights & climate change": (
        B, "Climate action and participation",
        "Greece adopted a National Climate Law (2022) with 55% and 80% "
        "reduction targets for 2030 and 2040, a National Adaptation Strategy "
        "and public online consultation of environmental legislation.",
        [
            ("Greece", "1", "107", "Greece implements its National Climate Law (Law 4936/2022), setting emissions reduction targets of -55% by 2030 and -80% by 2040"),
        ],
    ),
    "Rights related to marriage & family": (
        A, "Legal recognition of same-sex relationships and marriage",
        "Law 5089/2024 extended civil marriage to same-sex couples and "
        "recognises same-sex parents of children born abroad through assisted reproduction.",
        [
            ("Greece", "1", "15", "Law 5089/2024 on civil marriage equality represents a historic milestone, extending the right to marriage to same-sex couples"),
        ],
    ),
    "Human rights & poverty": (
        B, "National strategy for social integration and poverty reduction; child poverty",
        "Minimum Guaranteed Income and family benefits operate; JS2 asks that "
        "the National Strategy for Social Integration and Poverty Reduction be "
        "fully implemented and funded.",
        [
            ("Greece", "1", "89", "Financial protection for families with children is ensured through a range of incometargeted benefits"),
            ("JS2", "3", "11", "fully implement and adequately fund the National Strategy for Social Integration and Poverty Reduction"),
        ],
    ),
    "Persons with disabilities: independence, inclusion": (
        B, "Independent living and inclusion of persons with disabilities",
        "A Personal Assistant service assisted 1,100 people, 4,700 buildings "
        "received accessibility subsidies and more than 700 people moved to supported living.",
        [("Greece", "1", "85", "Law 4837/2021 established the Personal Assistant service for persons with disabilities")],
    ),
    "Children: family environment & alternative care": (
        B, "Deinstitutionalisation and guardianship",
        "Greece is transitioning to family-based care (foster-care platform, "
        "semi-autonomous living units) and launched a National Guardianship "
        "System for unaccompanied minors in 2024; the CRC finds children "
        "over-institutionalised.",
        [
            ("Greece", "1", "90", "Greece continues the transition to family-based models"),
            ("Committee on the Rights of the Child", "2", "46", "expressed concern about the overinstitutionalization of children deprived of parental care"),
        ],
    ),
    "Cooperation with international organizations": (
        B, "Cooperate with UNHCR and support migrant inclusion",
        "Greece cooperates with UNHCR, IOM and EUAA on reception and integration (HELIOS programme).",
        [("Greece", "1", "59", "The HELIOS program facilitates access to the labor market and delivers targeted interventions, including cultural mediation")],
    ),
    "National Preventive Mechanism (NPM)": (
        B, "Operational autonomy and resources of the national preventive mechanism",
        "The Ombudsperson is the NPM under OPCAT and the national "
        "investigation mechanism; the Human Rights Committee asks that its "
        "resources be adequate.",
        [("Greece", "1", "70", "The Greek Ombudsman functions both as the National Preventive Mechanism (NPM) under OPCAT and as the National Investigation Mechanism")],
    ),
    "Sexual & gender-based violence": (
        B, "Combat domestic violence",
        "Law 5172/2025 and the Panic Button app strengthened the domestic-violence framework.",
        [("Greece", "1", "39", "The \"Panic Button\" digital application")],
    ),
    "Economic, social & cultural rights - general measures of implementation": (
        B, "Protect rights of persons in vulnerable situations",
        "A new Ministry of Social Cohesion and Family Affairs and a "
        "multi-billion housing programme advance protection.",
        [("Greece", "1", "6", "The new Ministry of Social Cohesion and Family Affairs integrates policies on human rights, gender equality, child rights and vulnerable groups")],
    ),
    "Cooperation & Follow up with Treaty Bodies": (
        D, "Open, merit-based selection of treaty-body candidates",
        "The documents contain no information on this ask.", [],
    ),
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)": (
        B, "Prevent inhuman and degrading treatment",
        "Operational guidelines to all law enforcement and the Ombudsman "
        "mechanism exist; the Subcommittee on Prevention of Torture visited "
        "in October 2024 and the CPT calls for improvements.",
        [("Greece", "1", "68", "The prohibition of ill-treatment is further reinforced through operational guidelines issued to all law enforcement authorities")],
    ),
    "Access to justice & remedy": (
        B, "Access to justice for persons with disabilities",
        "Law 5023/2023 appointed accessibility officers in courts and granted direct legal aid.",
        [("Greece", "1", "87", "enhanced access to justice by eliminating discriminatory terminology from primary legislation, appointing accessibility officers in all courts, and granting direct legal aid irrespective of income")],
    ),
    "Budget & resources (for human rights implementation)": (
        C, "Adequate resources for implementing child rights policies",
        "The CRC recommends a dedicated budget for the National Action Plan "
        "on the Rights of the Child; none is reported.",
        [("Committee on the Rights of the Child", "2", "13", "recommended that Greece equip the National Action Plan with time-bound and measurable goals and a dedicated budget for its implementation")],
    ),
    "Advancement of women": (
        B, "Protect the rights of women and children",
        "Gender-equality and child-protection frameworks were strengthened.",
        [("Greece", "1", "31", "Within the Ministry of Social Cohesion and Family Affairs, created in 2023, the General Secretariat for Equality and Human Rights remains the lead body")],
    ),
    "Persons with disabilities: protecting the integrity of the person": (
        D, "End involuntary hospitalisation of persons with disabilities",
        "The documents contain no specific information on this ask.", [],
    ),
    "Cultural rights": (
        C, "Equal enjoyment of culture and use of minority languages",
        "The Turkish community of Western Thrace reports closure of its schools and curbs on its autonomy; no measure is reported.",
        [("ABTTF", "3", "24", "the temporary suspension and subsequent permanent closure of Turkish primary schools")],
    ),
    "Land & property rights": (
        C, "Conditions for Turkish Muslim communities in Western Thrace",
        "No measure is reported; the State recognises only a religious minority.",
        [("Greece", "1", "25", "Greece recognizes as a \"minority\" the religious Muslim Minority in Thrace")],
    ),
}

KEYWORDS = [
    # --- ratification-cluster specifics ---
    (r"Declaration on Children, Youth and Climate Action|article 14 of the International Convention on the Elimination of All Forms of Racial", D,
     "Sign the Declaration on Children, Youth and Climate Action / accept CERD article 14",
     "The documents contain no information on this ask.", []),
    # --- asylum access / non-refoulement (regression in 2025) ---
    (r"individual (consideration|assessment)|individual refugee|opportunity to obtain an individual|collective deportations|forcible eviction|principle of non-refoulement|breaches of the principle", E,
     "Ensure individual assessment of protection claims and stop collective returns",
     "In July 2025 Greece suspended the registration of asylum applications "
     "from people arriving by sea and provided for their return without "
     "registration, a measure contrary to these recommendations; the Human "
     "Rights Committee remains gravely concerned about pushbacks.",
     [("Several submissions", "3", "35", "the submission of asylum applications by third-country nationals entering Greek territory by sea was suspended for a period of three months. The suspension allowed the return, without registration"),
      ("Human Rights Committee", "2", "53", "remained gravely concerned about pushbacks of asylum-seekers, refugees and migrants at the country’s sea and land borders, in violation of the principle of non-refoulement")]),
    (r"^(?=.*(refugee|migrant|asylum|pushback|border)).*(investigat|complaints|mechanism to register|public enquiry|swift and independent)", C,
     "Investigate allegations of pushbacks and ill-treatment of migrants",
     "Greece reports a three-tier complaints system, but the Human Rights "
     "Committee asks that the independence and impartiality of monitoring "
     "mechanisms be affirmed and investigations be effective.",
     [("Greece", "1", "50", "every allegation of illtreatment, including alleged pushbacks, is investigated at internal and/or EU level"),
      ("Human Rights Committee", "2", "53", "affirm the independence and impartiality of the monitoring mechanisms involved in investigating violations of the human rights of migrants and asylumseekers at borders")]),
    (r"Ensure adequate reception and living conditions|Implement immediate measures for asylum seekers|humanitarian assistance|Ensure that migrant and asylum-seeking populations detained", B,
     "Reception and living conditions of asylum seekers",
     "Greece operates a modernised reception system (RIC, CCAC, Safe Areas, Hippocrates programme); the Human Rights Committee and CPT still request improved detention and reception conditions.",
     [("Greece", "1", "46", "Eight designated Safe Areas, supported by child protection personnel from NGOs and IOM")]),
    (r"children are not detained solely because", C,
     "Do not detain children solely for immigration status",
     "Greece reports safeguards for unaccompanied minors but the Human Rights Committee still calls for alternatives to detention.",
     [("Human Rights Committee", "2", "53", "provide effective alternatives to the detention of migrants and reduce the length and practice of such detentions")]),
    # --- religion / minorities ---
    (r"conscientious objection|conscientious objectors", C,
     "Recognise conscientious objection and alternative service",
     "Law 5265/2026 revised the review committee, but alternative service is longer than military service and civil society reports punitive conditions.",
     [("Greece", "1", "78", "Alternative service lasts 15 months, or, where reductions apply, 12, 9 or 5 months"),
      ("JS6; JS7", "3", "7", "the punitive conditions of the alternatives to military service in Greece violated several human rights instruments")]),
    (r"mosques|Turkish Muslim|Muslim communities", C,
     "Rights of the Turkish Muslim minority in Western Thrace",
     "Greece maintains that only a religious Muslim minority exists and Law 4964/2022 keeps State involvement in the selection of Muftis; the Turkish community asks that its schools and associations be restored.",
     [("ABTTF", "3", "25", "law No. 4964/2022 should be repealed, and the functioning of the mufti offices should be determined by the community itself")]),
    (r"ethnic identity", E,
     "Recognise the ethnic identity of the Turkish Muslim minority",
     "The National Report restates that Greece recognises only a religious minority, without reference to ethnic origin, which rejects the recommendation.",
     [("Greece", "1", "25", "Greece recognizes as a \"minority\" the religious Muslim Minority in Thrace, the status of which was established by the 1923 Treaty of Lausanne, on the basis of religion, without reference to the ethnic origin of its members")]),
    (r"establish and run their own schools", C,
     "Allow the Turkish minority to run its own schools",
     "The Turkish community reports closure of its primary schools and restrictions on school boards; no measure is reported.",
     [("ABTTF", "3", "24", "the temporary suspension and subsequent permanent closure of Turkish primary schools")]),
    (r"religious education", B,
     "Alternative classes for religious education",
     "Children may be exempted from religious education without authorization or verification of religion.",
     [("Greece", "1", "97", "Children may be exempted from religious education without authorization, verification of religion or any associated sanctions")]),
    # --- HRDs / NGOs ---
    (r"Stop prosecuting|End the intimidation", C,
     "Stop prosecuting and intimidating human rights defenders",
     "The Special Rapporteur reports criminalisation of search-and-rescue work and a hostile environment; Greece states defenders remain fully protected.",
     [("Special Rapporteur on human rights defenders", "2", "26", "criminalization of search and rescue activities at sea under national legislation")]),
    (r"Revisit policies with a view to facilitating the legitimate work|legal framework governing NGOs", B,
     "Facilitate the work of non-profit organisations",
     "Law 5275/2026 limited the registration requirement and removed the review committee, although the Special Rapporteur finds the regime discriminatory.",
     [("Greece", "1", "58", "no registration fee is charged and the three-member committee review has been removed")]),
    # --- defamation ---
    (r"^Decriminalize defamation", B,
     "Decriminalise defamation",
     "Simple defamation (article 362) was repealed in 2024; OSCE-ODIHR asks that remaining criminal defamation and insult provisions be replaced by civil remedies.",
     [("Greece", "1", "71", "Law 5090/2024 repealed Article 362 of the Criminal Code, eliminating the offense of simple defamation"),
      ("OSCE-ODIHR", "3", "12", "criminal provisions for defamation and insult be replaced by proportional civil remedies")]),
    # --- LGBTI ---
    (r"judicial process concerning gender change", D,
     "Replace the judicial gender-change process with an administrative one",
     "The documents contain no information on this ask; JS5 asks that psychiatric evaluation for minors be abolished.", []),
    (r"Protocol 12|Convention for the Protection of Human Rights and Fundamental Freedoms", C,
     "Ratify Protocol 12 to the European Convention",
     "ELEN recommends ratification of Protocol 12; none is reported.",
     [("ELEN", "3", "3", "recommended to ratify Protocol 12 of the European Convention on Human Rights")]),
    # --- women ---
    (r"pay gap|equal pay|gender pay", B,
     "Narrow the gender pay gap",
     "Law 5316/2026 requires pay transparency and sanctions unjustified pay disparities over 5%; the gap stands at 13.4%.",
     [("Greece", "1", "37", "sanctioning enterprises with unjustified pay disparities exceeding 5%, to operationalize pay transparency")]),
    (r"femicide|Council of Europe Convention on Preventing and Combating Violence", B,
     "Implement the Istanbul Convention",
     "Law 5172/2025 transposed EU standards; the GNCHR and CEDAW ask for a legal definition of femicide and a gender-killings observatory.",
     [("Greece", "1", "39", "In its report, the GNCHR stressed that an official definition of femicide and a dedicated observatory on gender-related killings should be established")]),
    (r"national action plan on gender", B,
     "Adopt the national action plan on gender equality",
     "The incoming National Action Plan 2026-2030 is being prepared with civil-society input.",
     [("Greece", "1", "33", "The incoming Plan 2026–2030, currently under preparation with civil society input")]),
    (r"Greek national human rights institution", B,
     "Strengthen the national human rights institution's work on women's rights",
     "The GNCHR completed its first comprehensive Report on the Status of Women in Greece in 2024; CEDAW asks that its resources be increased.",
     [("Greece", "1", "33", "In 2024, the GNCHR completed its first comprehensive Report on the Status of Women in Greece")]),
    # --- poverty / business ---
    (r"national strategy for social integration and poverty", B,
     "Conclude the national strategy on social integration and poverty reduction",
     "JS2 asks that the strategy be fully implemented and funded, which implies it exists.",
     [("JS2", "3", "11", "fully implement and adequately fund the National Strategy for Social Integration and Poverty Reduction")]),
    (r"Develop a national action plan in line with the Guiding Principles", D,
     "National action plan on business and human rights",
     "The documents contain no information on this ask.", []),
    # --- children / migrants ---
    (r"unaccompanied minors", B,
     "Protect unaccompanied minors",
     "Greece launched a National Guardianship System (January 2024, 8,189 children served), a National Emergency Response Mechanism and Safe Areas; 1,465 unaccompanied children were in the system in May 2026.",
     [("Greece", "1", "55", "On 1 January 2024, the National Guardianship System for Unaccompanied Minors was operationally launched")]),
    (r"guardianship", B,
     "Review the guardianship system",
     "The guardianship system was launched in 2024 and Law 5307/2026 transferred the appointment of guardians to the General Secretary.",
     [("Greece", "1", "55", "Law 5307/2026 transferred competence for the appointment of guardians from the Public Prosecutor to the General Secretary")]),
    (r"Mercenar|mercenar", D, "Mercenaries", "The documents contain no information on this ask.", []),
    (r"refugees and migrants in accordance|protection of refugees and migrants|human rights and dignity of refugees", C,
     "Protect refugees and migrants in accordance with international law",
     "The Human Rights Committee remains gravely concerned about pushbacks and Greece suspended asylum registration in 2025.",
     [("Human Rights Committee", "2", "53", "remained gravely concerned about pushbacks")]),
    (r"sanitation within refugee camps|health conditions", D,
     "Sanitation and health in refugee camps",
     "The documents contain no specific information on sanitation measures.", []),
    (r"mental health policies", D,
     "Human-rights-based mental health policies",
     "The documents contain no information on this ask.", []),
    (r"meaningful participation of refugee|participation of refugee", D,
     "Participation of refugee and asylum-seeking women",
     "The documents contain no information on this ask.", []),
    (r"included in the national recovery and resilience", D,
     "Include migrants in the national recovery and resilience plan",
     "The documents contain no information on this ask.", []),
    (r"birth registration", C,
     "Birth registration for children of migrants and Roma",
     "The Committee on the Rights of the Child recommends further facilitation of birth registration; no new measure is reported.",
     [("Committee on the Rights of the Child", "2", "60", "further facilitate access to birth registration procedures and identity documentation, and to correction of birth certificates for Roma children and children of migrant parents, free of charge")]),
    (r"Strengthen the registration system for asylum seekers", C,
     "Strengthen the asylum registration system",
     "Civil society reports the online asylum platform requires detention of up to 25 days and suspended registration in 2025.",
     [("Several submissions", "3", "40", "the new online platform to apply for asylum, introduced in 2022, required a detention period of up to 25 days")]),
    (r"Roma", B,
     "National strategy for Roma social inclusion",
     "The National Strategy and Action Plan for Roma Social Inclusion 2021-2030 is being implemented with a Roma Forum; the Council of Europe Commissioner asks for faster implementation and better monitoring.",
     [("Greece", "1", "23", "The National Strategy and Action Plan for Roma Social Inclusion 2021–2030")]),
    (r"^Revise its national legislation with a view to recognizing the right to conscientious", B,
     "Recognise the right to conscientious objection",
     "Law 5265/2026 reformed the review committee and procedure; alternative service remains longer than military service.",
     [("Greece", "1", "78", "Under Law 5265/2026, applications are reviewed by a committee comprising three university professors, a State Legal Council member and one Armed Forces Officer")]),
    (r"^Establish effective mechanisms to counter pushbacks", C,
     "Establish effective mechanisms to counter pushbacks",
     "Greece denies that pushbacks are compatible with its procedures and points to a three-tier complaints system whose independence the Human Rights Committee questions.",
     [("Greece", "1", "50", "Allegations of pushbacks are not compatible with the well-established standard operating procedures of the Hellenic authorities"),
      ("Human Rights Committee", "2", "53", "affirm the independence and impartiality of the monitoring mechanisms involved in investigating violations of the human rights of migrants and asylumseekers at borders")]),
]

FALLBACK = (
    D, "Miscellaneous",
    "No rule matched and the evidence base contains no specific information on this recommendation.",
    [],
)
