"""Thailand — implementation assessment of its 3rd-cycle (2021, A/HRC/49/16)
UPR recommendations, graded against the 4th-cycle documentation (session 53):
National Report A/HRC/WG.6/53/THA/1, OHCHR Compilation /2 and Stakeholders'
Summary /3.

    python scripts/run_assess.py thailand

First pass for expert review. Quotes are verbatim from the three documents.
Recommendations are numbered 51.x (supported) and 52.x (noted).
"""

from __future__ import annotations

from recommendations.models import Grade

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

# theme -> (grade, action_summary, rationale, [(org, doc "1"|"2"|"3", para, quote)])
CLUSTERS = {
    "Freedom of opinion and expression & access to information": (
        C, "Protect freedom of expression and peaceful assembly; reform lèse-majesté, sedition, defamation and computer-crime laws",
        "No amendment of sections 112, 116, defamation provisions or the "
        "Computer Crime Act is reported; HRW counts at least 1,997 people "
        "prosecuted since 2014 for expression and assembly, FLD reports "
        "cumulative sentences, and the UN country team reports prosecutions "
        "under the Public Assembly Act. Thailand reports only anti-SLAPP "
        "measures (see separate asks).",
        [
            ("HRW", "3", "34", "at least 1,997 people had been prosecuted in Thailand for exercising their rights to free expression and peaceful assembly"),
            ("FLD", "3", "35", "the issuance of cumulative sentences by the courts had significantly closed civic space"),
            ("United Nations country team", "2", "24", "restrictions on freedom of peaceful assembly, particularly under the Public Assembly Act"),
        ],
    ),
    "Death penalty": (
        C, "Move towards abolition of the death penalty or a formal moratorium",
        "The National Report is silent on the death penalty; courts continue to "
        "impose it, including for drug offences, and the NHRCT asks for a "
        "time-bound abolition plan.",
        [
            ("Committee against Torture", "2", "16", "courts continued to impose the death penalty, including for drug-related and other offences"),
            ("NHRCT", "3", "6", "adopt a time-bound action plan with clear targets and measurable indicators to advance the gradual abolition of the death penalty"),
        ],
    ),
    "Ratification of & accession to international instruments": (
        C, "Ratify outstanding international instruments",
        "Thailand ratified ICPPED (2024) and ILO Conventions 144 and 155, but "
        "no ratification of the instruments in question is reported; ILO "
        "Conventions 87 and 98, OP2-ICCPR, ICRMW, the refugee conventions "
        "and the Rome Statute remain outstanding.",
        [
            ("United Nations country team", "2", "5", "recommended that Thailand ratify the International Convention on the Protection of the Rights of All Migrant Workers and Members of Their Families"),
            ("NHRCT", "3", "4", "no concrete progress had been made toward the ratification of ILO Conventions Nos. 87 and 98"),
        ],
    ),
    "Children: definition": (
        B, "Protect children and promote children's rights",
        "Thailand prohibited corporal and psychological punishment in all "
        "settings (Act No. 25, in force 25 March 2025), raised the age of "
        "criminal responsibility to 12, withdrew its reservation to CRC "
        "article 22 and developed an MOU and SOPs for children below the "
        "age of criminal responsibility.",
        [
            ("Thailand", "1", "53", "which prohibits corporal and psychological punishment of children in all settings, entered into force on 25 March 2025"),
            ("Thailand", "1", "54", "increased the minimum age of criminal responsibility from 10 to 12 years old"),
            ("Thailand", "1", "52", "deposited with the United Nations an instrument of withdrawal of its reservation to Article 22"),
        ],
    ),
    "Equality & non-discrimination": (
        B, "Protect LGBTIQ+ persons and marginalised groups from discrimination",
        "The Marriage Equality Act (in force 23 January 2025), coverage of "
        "gender-affirming hormone therapy under universal coverage (July 2025), "
        "the 5th National Human Rights Plan and dialogues with law enforcement "
        "were adopted; the Anti-Discrimination Bill is still being drafted and "
        "LBTIQ+ persons face discrimination.",
        [
            ("Thailand", "1", "74", "which came into effect on 23 January 2025"),
            ("Thailand", "1", "73", "The Thai Government is drafting the Anti-Discrimination Bill"),
            ("Working Group on discrimination against women and girls", "2", "57", "LBTIQ+ women and girls continued to face discrimination in many areas, including employment, education, housing and healthcare"),
        ],
    ),
    "Right to health": (
        B, "Universal health coverage and equitable access to health services",
        "The universal health coverage scheme was extended to the "
        "'30 Baht Treats Everywhere' model, a health insurance system for "
        "non-Thai persons (HINT) was developed with WHO, and telemedicine and "
        "village health volunteer services were expanded; the UN country team "
        "still asks for equitable access for migrants and stateless persons.",
        [
            ("Thailand", "1", "32", "Health Insurance for Non-Thai People System (HINT)"),
            ("Thailand", "1", "31", "integrated medical innovations to enhance access to health services, including telemedicine, telepharmacy, and digital health data management"),
            ("United Nations country team", "2", "36", "ensure equitable access to affordable, quality healthcare for migrants, displaced persons, stateless persons and persons under screening in the national screening mechanism"),
        ],
    ),
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)": (
        B, "Criminalise torture and enforced disappearance and prevent ill-treatment",
        "The Prevention and Suppression of Torture and Enforced Disappearance "
        "Act entered into force on 26 February 2023 and interpretative "
        "declarations to CAT were withdrawn; the Committee against Torture "
        "notes provisions not yet in full conformity and the NHRCT reports "
        "weak enforcement.",
        [
            ("Thailand", "1", "89", "enacted the Prevention and Suppression of Torture and Enforced Disappearance Act, B.E. 2565 (2022), which entered into force on 26 February 2023"),
            ("Thailand", "1", "88", "withdrew its Interpretative Declarations to the Convention against Torture"),
            ("NHRCT", "3", "2", "persistent challenges in enforcing the 2022 Prevention and Suppression of Torture and Enforced Disappearance Act"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        B, "Strengthen the National Human Rights Commission in line with the Paris Principles",
        "GANHRI restored the NHRCT to A status in March 2022; the Committee "
        "against Torture and JS38 note that the 2017 Organic Act removed "
        "powers and that independence of appointments needs reform.",
        [
            ("Thailand", "1", "24", "restored the accreditation status of the National Human Rights Commission of Thailand (NHRCT) to Category A status"),
            ("Committee against Torture", "2", "12", "the Organic Act of the National Human Rights Commission of Thailand, adopted in 2017, removed the Commission’s power to file lawsuits"),
        ],
    ),
    "Migrants": (
        B, "Protect the rights of migrant workers",
        "Migrant Worker Assistance Centres were expanded from 10 to 30 "
        "provinces, health coverage was extended to undocumented migrant "
        "workers (HINT) and ILO projects on fair recruitment run; the NHRCT "
        "and CERD report gaps in labour and social protection.",
        [
            ("Thailand", "1", "79", "increased the numbers of Migrant Worker Assistance Centres from 10 provinces to 30 provinces nationwide"),
            ("NHRCT", "3", "10", "migrant workers, informal workers and workers in new forms of work such as platform workers remained inadequately protected by labour law"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        B, "Combat trafficking in persons and protect victims",
        "A National Referral Mechanism with a reflection period has operated "
        "since 2022, an Anti-Cyber Scam Centre and the SHIELD database were "
        "created and over 13,500 people were repatriated from scam centres; "
        "CERD and the NHRCT report inconsistent identification and returns "
        "without referral.",
        [
            ("Thailand", "1", "47", "Since 2022, the Thai Government has implemented the National Referral Mechanism (NRM) for the screening, identification, and protection of trafficking victims"),
            ("Thailand", "1", "48", "assisted in repatriating over 13,500 individuals of 47 nationalities rescued from scam centres"),
            ("NHRCT", "3", "9", "persons were returned to their countries of origin without going through the National Referral Mechanism (NRM)"),
        ],
    ),
    "Freedom of association": (
        D, "Revise the draft law on non-profit organisations",
        "The documents contain no information on this ask.", [],
    ),
    "National Human Rights Action Plans (or specific areas) / implementation plans": (
        B, "Develop and implement national plans",
        "The 5th National Human Rights Plan (2023-2027), the UPR National "
        "Action Plan (Cabinet, 20 December 2022) and sectoral plans were "
        "adopted; the UN country team asks for updated, resourced plans.",
        [
            ("Thailand", "1", "9", "Approved by the Cabinet on 20 December 2022"),
            ("Committee against Torture", "2", "14", "welcomed the adoption of the Fifth National Human Rights Plan (2023–2027)"),
        ],
    ),
    "Sexual & gender-based violence": (
        B, "Strengthen the response to sexual and gender-based violence",
        "A Six-Year Action Plan on Rape and Sexual Harassment (2022-2027) and "
        "a National Action Plan on the Elimination of Violence against Women "
        "(2025-2027) were adopted and sexual harassment was criminalised "
        "(30 December 2025); CEDAW notes weak investigation and protection "
        "mechanisms under the Domestic Violence Victim Protection Act.",
        [
            ("Thailand", "1", "58", "Six-Year Action Plan on the Prevention and Resolution of Rape and Sexual Harassment B.E. 2565-2570 (2022–2027) was approved by the Cabinet on 20 December 2022"),
            ("Thailand", "1", "61", "Enactment of specific legislation to address sexual harassment, pursuant to the Act Amending the Criminal Code (No. 30) B.E. 2568 (2025) on 30 December 2025"),
            ("Committee on the Elimination of Discrimination against Women", "2", "45", "the absence of effective investigation, enforcement and survivor protection mechanisms in the Domestic Violence Victim Protection Act B.E. 2550 (2007)"),
        ],
    ),
    "Human rights defenders": (
        B, "Protect human rights defenders and civil society",
        "The Witness Protection Act was amended (November 2022) to cover "
        "whistleblowers, the Criminal Procedure Code was amended on SLAPPs and "
        "the Supreme Court President issued criteria on section 161/1 (2026); "
        "the Committee against Torture reports attacks, including the killing of "
        "Roning Dalah, and continuing SLAPPs.",
        [
            ("Thailand", "1", "90", "extends protection to whistleblowers and informants regarding criminal offences"),
            ("Thailand", "1", "92", "Recommendation of the President of the Supreme Court on the Criteria and Procedures for Case Consideration under Section 161/1 of the Criminal Procedure Code B.E. 2569 (2026)"),
            ("Committee against Torture", "2", "25", "recurring reports of attacks and reprisals against human rights defenders in the country"),
        ],
    ),
    "Constitutional & legislative framework": (
        B, "Review and align legislation with international human rights obligations",
        "Thailand adopted numerous laws in the period (torture, marriage "
        "equality, ethnic groups, sexual harassment, corporal punishment) and "
        "is drafting several others; no repeal of rights-restrictive "
        "legislation is reported.",
        [
            ("Thailand", "1", "23", "Thailand has made significant progress in developing laws and policies that protect and promote human rights"),
        ],
    ),
    "Persons with disabilities: definition, general principles": (
        B, "Protect the rights of persons with disabilities",
        "The 4th Education Plan for Persons with Disabilities 2023-2027 was "
        "adopted and the draft Persons with Disabilities Empowerment Act (No. 3) "
        "is advancing to align the law with the CRPD.",
        [
            ("Thailand", "1", "65", "advancing the draft Persons with Disabilities Empowerment Act (No. 3)"),
            ("Thailand", "1", "39", "4th Education Plan for Persons with Disabilities B.E. 2023-2027"),
        ],
    ),
    "Economic, social & cultural rights - general measures of implementation": (
        B, "Social development and narrowing the digital divide",
        "A National Multidimensional Poverty Index and the 13th National "
        "Economic and Social Development Plan guide targeted social policies; "
        "Thailand has not ratified OP-ICESCR.",
        [
            ("Thailand", "1", "28", "adopted the National Multidimensional Poverty Index (MPI)"),
        ],
    ),
    "Discrimination against women": (
        B, "Advance gender equality and combat discrimination against women",
        "A Gender Equality Promotion Action Plan 2023-2027, a Women's "
        "Development Action Plan, Gender Equality Centres in 76 provinces and "
        "Labour Protection Act amendments (maternity leave raised to 120 days) "
        "were adopted; CEDAW notes a significant gender pay gap and informal "
        "employment gaps.",
        [
            ("Thailand", "1", "61", "Establishment of Gender Equality Centres across all 76 provinces"),
            ("Thailand", "1", "45", "maternity leave up to 120 days per pregnancy (previously was 98 days)"),
            ("Committee on the Elimination of Discrimination against Women", "2", "33", "the significant gender pay gap"),
        ],
    ),
    "Violence against women": (
        B, "Prevent and combat violence against women",
        "A National Action Plan on the Elimination of Violence against Women "
        "(2025-2027) and a Six-Year Action Plan on rape and sexual harassment "
        "were adopted; CEDAW and the Committee against Torture report "
        "underreporting and weak protection.",
        [
            ("Thailand", "1", "58", "Six-Year Action Plan on the Prevention and Resolution of Rape and Sexual Harassment B.E. 2565-2570 (2022–2027) was approved by the Cabinet on 20 December 2022"),
            ("Committee on the Elimination of Discrimination against Women", "2", "45", "the absence of effective investigation, enforcement and survivor protection mechanisms in the Domestic Violence Victim Protection Act B.E. 2550 (2007)"),
        ],
    ),
    "Enforced disappearances": (
        A, "Ratify the Convention for the Protection of All Persons from Enforced Disappearance",
        "Thailand ratified ICPPED on 14 May 2024 (in force 13 June 2024) and "
        "enacted the Prevention and Suppression of Torture and Enforced "
        "Disappearance Act.",
        [
            ("Thailand", "1", "87", "ratified the International Convention for the Protection of All Persons from Enforced Disappearance (ICPPED), which subsequently entered into force for Thailand on 13 June 2024"),
        ],
    ),
    "Business & Human Rights": (
        B, "Implement the business and human rights agenda and mandatory human rights due diligence",
        "The 2nd National Action Plan on Business and Human Rights (2023-2027) "
        "reports 112 of 125 activities implemented and a Promotion of "
        "Responsible Business Conduct Act (mandatory due diligence) is being "
        "drafted; the plan is non-binding.",
        [
            ("Thailand", "1", "107", "112 out of 125 activities under the Action Plan have been implemented, representing 89.60 per cent of the Plan"),
            ("Thailand", "1", "108", "The Thai Government is drafting the Promotion of Responsible Business Conduct Act"),
        ],
    ),
    "Participation of women in political & public life": (
        B, "Increase women's representation in political and public life",
        "A Women's Development Action Plan 2023-2027 includes a pillar on "
        "participation at decision-making level; the Working Group on "
        "discrimination against women notes persisting underrepresentation.",
        [
            ("Thailand", "1", "60", "promotion of women's participation at the decision-making level"),
            ("Working Group on discrimination against women and girls", "2", "49", "women’s political representation remained a challenge"),
        ],
    ),
    "Children: protection against exploitation": (
        B, "Prevent sexual exploitation and child labour",
        "Online child sexual offences were criminalised in 2025 and trafficking "
        "responses expanded; HKC reports that progress has been insufficient "
        "for the scale of online child exploitation.",
        [
            ("HKC", "3", "58", "the delayed criminalization of online offenses until 2025 indicated that insufficient progress had been made against the scale of the problem of child sexual exploitation"),
        ],
    ),
    "Rights related to name, identity & nationality": (
        B, "Nationality and documentation for stateless children and persons",
        "A Cabinet resolution (29 October 2024) shortened approval for "
        "residence and nationality for stateless persons from 270 and 180 days "
        "to 5 days: 121,471 were granted status by July 2026; 108,478 students "
        "without civil registration were enrolled; CERD finds the number of "
        "stateless persons very high.",
        [
            ("Thailand", "1", "85", "121,471 stateless individuals have been granted permanent residency or citizenship under the scheme"),
            ("Thailand", "1", "41", "A total of 108,478 students without civil registration records or Thai nationality have received education"),
            ("Committee on the Elimination of Racial Discrimination", "2", "62", "the number of stateless persons remained very high"),
        ],
    ),
    "Refugees & asylum seekers": (
        C, "Ratify the Refugee Convention and protect refugees and asylum seekers",
        "Thailand created a National Screening Mechanism (2023) and allowed "
        "Myanmar displaced persons in shelters to work (August 2025), but has "
        "no refugee legislation; refugees are treated as irregular migrants "
        "and the Committee against Torture reports mass expulsions.",
        [
            ("Thailand", "1", "81", "put in place the National Screening Mechanism (NSM) since 2023"),
            ("Fortify Rights", "3", "68", "refugees were treated as irregular migrants under the Immigration Act of 1979 and were therefore subject to arrest, detention and deportation"),
        ],
    ),
    "Human rights & climate change": (
        B, "Rights-based climate action and participation",
        "A Department of Climate Change and Environment was created (August "
        "2023) and a Climate Change Act was approved by Cabinet (expected 2027) "
        "and a Clean Air Act advanced; CEDAW notes gaps in women's participation.",
        [
            ("Thailand", "1", "110", "established the Department of Climate Change and Environment on 18 August 2023"),
            ("Thailand", "1", "111", "The draft Act has been approved by the Cabinet and is currently under consideration of the Office of the Council of State"),
        ],
    ),
    "Right to social security": (
        B, "Strengthen social security and protection of vulnerable groups",
        "The Thai social protection system was reinforced through the 13th "
        "Plan's social protection milestone and the Social Security Act; "
        "migrant and informal workers remain insufficiently covered.",
        [
            ("Thailand", "1", "29", "sets Milestone 9: “Thailand has less intergenerational poverty and adequate, appropriate social protection.”"),
            ("JS49", "3", "46", "ensure inclusion of domestic workers, including migrant domestic workers, in the mandatory social security system without delay"),
        ],
    ),
    "Right to education": (
        B, "Basic education for all, including ethnic groups and migrant children",
        "The Zero Dropout initiative identified over 18,000 out-of-school "
        "children, a 2025 announcement admitted students without civil "
        "registration (108,478 enrolled) and 1,604 schools in special areas "
        "were supported.",
        [
            ("Thailand", "1", "36", "more than 18,000 children who were identified as missing from the system in its first year"),
            ("Thailand", "1", "41", "A total of 108,478 students without civil registration records or Thai nationality have received education"),
        ],
    ),
    "National Preventive Mechanism (NPM)": (
        C, "Ratify OP-CAT and establish an independent national preventive mechanism",
        "The NHRCT conducted awareness visits as a prospective NPM but Thailand "
        "has neither acceded to OP-CAT nor established an NPM; the NHRCT "
        "recommends a time-bound roadmap.",
        [
            ("Thailand", "1", "25", "has demonstrated its readiness to serve as the National Preventive Mechanism (NPM) by conducting field visits to raise awareness on recommendations concerning accession to the Optional Protocol"),
            ("NHRCT", "3", "3", "adopt a time-bound roadmap for accession to the OP-CAT"),
        ],
    ),
    "Cooperation & consultation with civil society": (
        C, "Guarantee civil society space",
        "The National Report reports consultations on the UPR but no measure "
        "on civil society space; HRW and FLD report restrictions, SLAPPs and "
        "the absence of a legal framework for defenders.",
        [
            ("FLD", "3", "20", "Thailand lacked any specific laws, effective policies or practices addressing human rights defenders"),
        ],
    ),
    "Members of minorities": (
        B, "Promote and protect ethnic, religious and linguistic minorities",
        "The Protection and Promotion of the Way of Life of Ethnic Groups Act "
        "entered into force on 19 September 2025 and an Action Plan on "
        "Peaceful Coexistence 2023-2027 was adopted; the UN country team "
        "notes the Act does not recognise Indigenous Peoples and FPIC only "
        "partially.",
        [
            ("Thailand", "1", "71", "Protection and Promotion of the Way of Life of Ethnic Groups Act B.E. 2568 (2025) entered into force on 19 September 2025"),
            ("United Nations country team", "2", "55", "did not explicitly recognize Indigenous Peoples and only reflected free, prior and informed consent partially"),
        ],
    ),
    "Conditions of detention": (
        B, "Improve prison conditions and reduce overcrowding",
        "Thailand expanded non-custodial measures and diversion, health "
        "services and vocational training in prisons; the Committee against "
        "Torture reports continuing overcrowding, with 70% of prisoners "
        "held for drug offences.",
        [
            ("Thailand", "1", "100", "systematic expansion of alternatives to imprisonment (non-custodial measures)"),
            ("Committee against Torture", "2", "19", "prisons continued to face high levels of overcrowding, an associated lack of staff and deteriorating conditions of detention"),
        ],
    ),
    "Human rights & poverty": (
        B, "Reduce poverty",
        "Thailand has achieved SDG 1 according to the Sustainable Development "
        "Report 2026 and adopted a National Multidimensional Poverty Index.",
        [
            ("Thailand", "1", "28", "adopted the National Multidimensional Poverty Index (MPI)"),
            ("Thailand", "1", "3", "having achieved SDG 1 (No Poverty) and SDG 4 (Quality Education)"),
        ],
    ),
    "Sexual & reproductive health and rights": (
        B, "Access to sexual and reproductive health services, including for migrant workers",
        "Health insurance was extended to non-Thai persons (HINT), but UNCT "
        "and the Working Group note abortion is not fully decriminalised and "
        "access remains constrained.",
        [
            ("Thailand", "1", "32", "Health Insurance for Non-Thai People System (HINT)"),
            ("United Nations country team", "2", "37", "abortion was not yet fully decriminalized and that access to safe and legal abortion remained severely constrained in practice"),
        ],
    ),
    "Cooperation with human rights mechanisms & requests for technical assistance": (
        A, "Cooperate with the Human Rights Council, special procedures and OHCHR",
        "Thailand sits on the Human Rights Council (2025-2027), welcomed two "
        "special procedure visits and maintains regular engagement with the "
        "OHCHR Regional Office.",
        [
            ("Thailand", "1", "15", "welcomed the official visits of two special procedures mandate holders"),
            ("Thailand", "1", "13", "maintains regular engagement with the Regional Office for South-East Asia of the Office of the United Nations High Commissioner for Human Rights (OHCHR) in Bangkok"),
        ],
    ),
    "Economic, social & cultural rights": (
        B, "Access to social services for women, children and persons with disabilities",
        "Universal coverage, Zero Dropout, subsidies for 503 boarding schools "
        "and disability welfare services were expanded.",
        [
            ("Thailand", "1", "38", "A total of 1,604 schools in special areas received support to improve the effectiveness of education management"),
        ],
    ),
    "Labour rights and right to work": (
        C, "Ratify ILO Conventions 87 and 98 and protect all workers",
        "Thailand ratified ILO Conventions 144 and 155 but no progress was made "
        "on Conventions 87 and 98.",
        [
            ("Thailand", "1", "43", "ratified ILO’s Occupational Safety and Health Convention 1981 (No. 155)"),
            ("NHRCT", "3", "4", "no concrete progress had been made toward the ratification of ILO Conventions Nos. 87 and 98"),
        ],
    ),
    "Cooperation & Follow up with Treaty Bodies": (
        D, "Adopt an open, merit-based process for national candidates to treaty bodies",
        "The documents contain no information on this ask.", [],
    ),
    "Racial discrimination": (
        B, "Eliminate racial discrimination",
        "The Ethnic Groups Act (2025) and an Anti-Discrimination Bill (under "
        "drafting) address discrimination; CERD recommends a stand-alone "
        "anti-discrimination law.",
        [
            ("Thailand", "1", "73", "The Thai Government is drafting the Anti-Discrimination Bill"),
            ("Committee on the Elimination of Racial Discrimination", "2", "10", "adopt a comprehensive, stand-alone anti-discrimination law"),
        ],
    ),
    "Right to development": (
        B, "Human-centred development",
        "The 13th National Economic and Social Development Plan guides "
        "development and SDG progress.",
        [
            ("Thailand", "1", "29", "sets Milestone 9: “Thailand has less intergenerational poverty and adequate, appropriate social protection.”"),
        ],
    ),
    "Good governance & corruption": (
        B, "Public service efficiency and accountability",
        "The Act Prescribing Timeframes for Judicial Proceedings (2022), the "
        "Act on Facilitation of Government Licences (2026) and an amendment "
        "of the Organic Act on Anti-Corruption (2025) were adopted.",
        [
            ("Thailand", "1", "94", "enacted the Act Prescribing Timeframes for Judicial Proceedings, B.E. 2565 (2022)"),
        ],
    ),
    "Access to justice & remedy": (
        C, "Strengthen women's access to justice",
        "The National Report describes general online justice services but "
        "nothing specific for rural, Indigenous or disabled women; CERD notes "
        "access barriers for minorities.",
        [
            ("Committee on the Elimination of Racial Discrimination", "2", "21", "barriers preventing ethnic and ethno-religious groups, Indigenous Peoples, migrants, refugees, asylum-seekers and stateless persons from accessing justice"),
        ],
    ),
    "Right to an adequate standard of living": (
        B, "Raise the standard of living",
        "Poverty and social-protection policies were strengthened (MPI, 13th "
        "Plan).",
        [
            ("Thailand", "1", "28", "adopted the National Multidimensional Poverty Index (MPI)"),
        ],
    ),
    "Persons with disabilities: independence, inclusion": (
        B, "Simplify access to the disability grant",
        "A One Stop Service system with health facilities is being developed for "
        "disability identification cards and welfare benefits.",
        [
            ("Thailand", "1", "67", "the development of a One Stop Service system in collaboration with health facilities to facilitate the issuance of disability identification cards"),
        ],
    ),
    "Cooperation & Follow up with Special Procedures": (
        A, "Endorse requests for visits by special procedures",
        "Thailand hosted visits by the Working Group on discrimination against "
        "women and girls (December 2024) and the Special Rapporteur on health "
        "(February 2025).",
        [
            ("Thailand", "1", "15", "welcomed the official visits of two special procedures mandate holders"),
        ],
    ),
    "National Mechanisms for Reporting & Follow-up (NMRF)": (
        B, "Standing national mechanism for reporting and follow-up",
        "A Committee on Driving Forward Human Rights Work in Thailand, chaired "
        "by a Deputy Prime Minister, serves as the NMIRF and a National "
        "Committee oversees UPR implementation.",
        [
            ("Thailand", "1", "26", "serves as the National Mechanism for Implementation, Reporting and Follow-up (NMIRF)"),
        ],
    ),
    "Data collection & research": (
        A, "Enact the data protection act",
        "The Personal Data Protection Act entered into force on 1 June 2022.",
        [
            ("Thailand", "1", "116", "The Personal Data Protection Act B.E. 2562 (2019) (PDPA) entered into force on 1 June 2022."),
        ],
    ),
    "Support to victims & witnesses": (
        B, "Implement a national referral mechanism for trafficking victims",
        "A National Referral Mechanism has operated since 2022; the NHRCT reports "
        "identification and screening are not applied consistently.",
        [
            ("Thailand", "1", "47", "Since 2022, the Thai Government has implemented the National Referral Mechanism (NRM) for the screening, identification, and protection of trafficking victims"),
            ("NHRCT", "3", "9", "The processes of identification, screening, and protection of victims were not applied consistently."),
        ],
    ),
    "Advancement of women": (
        B, "Women's economic empowerment and representation",
        "A Women's Development Action Plan 2023-2027, an MoU for women-owned SMEs "
        "and presidential-level programmes support economic empowerment.",
        [
            ("Thailand", "1", "60", "promotion of women's participation at the decision-making level"),
        ],
    ),
    "Persons with disabilities: protection and safety in situations of risk": (
        B, "Align legislation with the Convention on the Rights of Persons with Disabilities",
        "A draft Persons with Disabilities Empowerment Act (No. 3) is "
        "advancing to align the law with the CRPD.",
        [
            ("Thailand", "1", "65", "advancing the draft Persons with Disabilities Empowerment Act (No. 3)"),
        ],
    ),
    "Right to peaceful assembly": (
        C, "Review regulations restricting freedom of assembly",
        "No review is reported; the UN country team reports prosecutions under "
        "the Public Assembly Act.",
        [
            ("United Nations country team", "2", "24", "restrictions on freedom of peaceful assembly, particularly under the Public Assembly Act"),
        ],
    ),
}

KEYWORDS = [
    # --- ratification specifics ---
    (r"Enforced Disappearance", A,
     "Ratify the Convention for the Protection of All Persons from Enforced Disappearance",
     "Thailand ratified ICPPED on 14 May 2024 (in force 13 June 2024).",
     [("Thailand", "1", "87", "ratified the International Convention for the Protection of All Persons from Enforced Disappearance (ICPPED), which subsequently entered into force for Thailand on 13 June 2024")]),
    (r"^Consider acceding to the International Convention on the Protection of the Rights of All Migrant Workers", B,
     "Ratify ICRMW and ICPPED",
     "Thailand ratified ICPPED (2024) but not ICRMW.",
     [("Thailand", "1", "87", "ratified the International Convention for the Protection of All Persons from Enforced Disappearance (ICPPED), which subsequently entered into force for Thailand on 13 June 2024"),
      ("United Nations country team", "2", "5", "recommended that Thailand ratify the International Convention on the Protection of the Rights of All Migrant Workers and Members of Their Families")]),
    (r"^Ratify the Convention against Discrimination in Education", C,
     "Ratify the UNESCO Convention against Discrimination in Education",
     "UNESCO continues to recommend ratification; none is reported.",
     [("UNESCO", "2", "8", "recommended that Thailand ratify the Convention against Discrimination in Education")]),
    # --- torture legislation ---
    (r"^(Adopt national legislation criminalizing torture and enforced disappearance|Enact legislation that criminalizes torture|Enact legislation criminalizing torture|Expedite the process of the legislation outlawing torture)", A,
     "Enact legislation criminalising torture and enforced disappearance",
     "The Prevention and Suppression of Torture and Enforced Disappearance Act entered into force on 26 February 2023; the Committee against Torture asks for fuller conformity with the Convention.",
     [("Thailand", "1", "89", "enacted the Prevention and Suppression of Torture and Enforced Disappearance Act, B.E. 2565 (2022), which entered into force on 26 February 2023"),
      ("Committee against Torture", "2", "11", "welcomed the adoption of the Prevention and Suppression of Torture and Enforced Disappearance Act B.E. 2565 (2022)")]),
    (r"^(Align the draft prevention and suppression of torture|Adopt legislation to implement Thailand)", B,
     "Align torture and enforced disappearance legislation with international obligations and prosecute alleged cases",
     "The Prevention and Suppression of Torture and Enforced Disappearance Act entered into force on 26 February 2023; the Committee against Torture asks that the list of torture purposes be illustrative and superior responsibility and amnesty exemptions be clarified, and reports credible investigations are rare.",
     [("Thailand", "1", "89", "enacted the Prevention and Suppression of Torture and Enforced Disappearance Act, B.E. 2565 (2022), which entered into force on 26 February 2023"),
      ("Committee against Torture", "2", "11", "ensuring that the list of purposes for torture contained in the Act was established as illustrative, rather than exhaustive"),
      ("Committee against Torture", "2", "17", "authorities routinely failed to carry out credible investigations except in a few high-profile cases that received media attention")]),
    (r"Optional Protocol to the Convention against Torture", C,
     "Ratify the Optional Protocol to the Convention against Torture",
     "The NHRCT conducted awareness visits as a prospective NPM; Thailand has not acceded and the NHRCT recommends a time-bound roadmap.",
     [("Thailand", "1", "25", "has demonstrated its readiness to serve as the National Preventive Mechanism (NPM) by conducting field visits to raise awareness on recommendations concerning accession to the Optional Protocol"),
      ("NHRCT", "3", "3", "adopt a time-bound roadmap for accession to the OP-CAT")]),
    (r"^Ratify the Optional Protocol to the Convention against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment, and pass legislation", B,
     "Ratify OP-CAT and legislate against torture and enforced disappearance",
     "The Anti-Torture and Enforced Disappearance Act (2023) was enacted; OP-CAT is not ratified.",
     [("Thailand", "1", "89", "enacted the Prevention and Suppression of Torture and Enforced Disappearance Act, B.E. 2565 (2022), which entered into force on 26 February 2023"),
      ("NHRCT", "3", "3", "adopt a time-bound roadmap for accession to the OP-CAT")]),
    (r"^(Advance in the establishment of an independent mechanism|Set up an independent mechanism)", C,
     "Establish an independent mechanism for the prevention and suppression of torture and enforced disappearances",
     "The NHRCT has conducted awareness visits as a prospective national preventive mechanism but no independent mechanism has been established and OP-CAT is not ratified.",
     [("Thailand", "1", "25", "has demonstrated its readiness to serve as the National Preventive Mechanism (NPM) by conducting field visits to raise awareness on recommendations concerning accession to the Optional Protocol"),
      ("NHRCT", "3", "3", "adopt a time-bound roadmap for accession to the OP-CAT")]),
    (r"^Conduct prompt, transparent and impartial investigations into reports of enforced disappearances", C,
     "Investigate enforced disappearances, including the case of Wanchalearm Satsaksit",
     "The Committee against Torture notes an apparent lack of progress in investigating and prosecuting enforced disappearances.",
     [("Committee against Torture", "2", "20", "the apparent lack of progress in investigating and prosecuting enforced disappearances")]),
    # --- NHRI A status ---
    (r"^(Continue measures with the aim of obtaining A-level status|Expedite the process of returning the National Human Rights Commission)", A,
     "Obtain A-level status for the National Human Rights Commission",
     "GANHRI restored the NHRCT to Category A in March 2022.",
     [("Thailand", "1", "24", "restored the accreditation status of the National Human Rights Commission of Thailand (NHRCT) to Category A status")]),
    # --- death penalty ---
    (r"^Conduct awareness-raising campaigns with the aim of educating the public|^Strengthen public awareness campaigns on the death penalty", D,
     "Public awareness campaigns on alternatives to the death penalty",
     "The documents contain no information on this ask.", []),
    # --- LGBTIQ+ and marriage ---
    (r"same-sex marriage|equality in marriage", A,
     "Recognise same-sex marriage",
     "Civil and Commercial Code Amendment Act (No. 24) B.E. 2567 (Marriage Equality Act) came into effect on 23 January 2025.",
     [("Thailand", "1", "74", "which came into effect on 23 January 2025")]),
    (r"^Enact a gender identity, gender expression and sex characteristics act", C,
     "Enact a gender identity, gender expression and sex characteristics act",
     "No such law is reported; RSAT notes critical gaps in legislation protecting LGBTIQ+ individuals and the Anti-Discrimination Bill is only a draft.",
     [("RSAT", "3", "65", "critical gaps in Thai legislation continued to deny LGBTIQ+ individuals the protection")]),
    (r"^Maintain efforts to promote and protect the rights of LGBTIQ\+ people", A,
     "Promote and protect the rights of LGBTIQ+ people",
     "The Marriage Equality Act is in force (January 2025), gender-affirming hormone therapy is covered under universal coverage (July 2025), the 5th National Human Rights Plan targets LGBTIQ+ persons and dialogues are held with law enforcement.",
     [("Thailand", "1", "74", "which came into effect on 23 January 2025"),
      ("Thailand", "1", "77", "has regularly convened dialogues across various provinces nationwide to foster respect for the rights and appropriate treatment of LGBTIQ+ persons among law enforcement officers")]),
    (r"^(Train education personnel, both in public and private institutions|Include the right to non-discrimination of people of diverse sexual orientations)", D,
     "Educate on diversity and non-discrimination of LGBTIQ+ persons",
     "The documents contain no information on this ask; CEDAW's Working Group reports bullying of LBTIQ+ students.",
     []),
    (r"^(Review the law on gender equality|Improve the gender equality law)", C,
     "Review the gender equality law",
     "Only a draft Anti-Discrimination Bill is reported; no amendment of the gender equality law.",
     [("Thailand", "1", "73", "The Thai Government is drafting the Anti-Discrimination Bill")]),
    # --- corporal punishment / marriage ---
    (r"corporal punishment", A,
     "Prohibit corporal punishment of children in all settings",
     "Civil and Commercial Code Amendment Act (No. 25) B.E. 2568 prohibits corporal and psychological punishment in all settings, including homes, schools and childcare (in force 25 March 2025).",
     [("Thailand", "1", "53", "which prohibits corporal and psychological punishment of children in all settings, entered into force on 25 March 2025")]),
    (r"^(Ensure that children cannot be legally married|Continue to address concerns about the prevalence of early and forced child marriage)", A,
     "End legal child marriage",
     "The Marriage Equality Act raised the minimum legal age of marriage to 18 years.",
     [("Thailand", "1", "74", "adjusts the minimum legal age for marriage to 18 years")]),
    (r"^Continue the gradual expansion of the child support grant", D,
     "Expand the child support grant scheme",
     "The documents contain no information on this ask.", []),
    # --- women ---
    (r"^Develop a national plan against sexual and gender-based violence", A,
     "Develop a national plan against sexual and gender-based violence",
     "A National Action Plan on the Elimination of Violence against Women (2025-2027) and a Six-Year Action Plan on Rape and Sexual Harassment (2022-2027) were adopted.",
     [("Thailand", "1", "58", "Six-Year Action Plan on the Prevention and Resolution of Rape and Sexual Harassment B.E. 2565-2570 (2022–2027) was approved by the Cabinet on 20 December 2022"),
      ("Thailand", "1", "61", "Formulation of the Action Plan on Women, Peace and Security")]),
    (r"genital circumcision", D,
     "Abolish female genital circumcision",
     "The documents contain no information on this ask.", []),
    (r"Security council resolution 1325", A,
     "Increase women's representation in public life under Security Council resolution 1325",
     "A National Action Plan on Women, Peace and Security (2025-2027) was formulated.",
     [("Thailand", "1", "61", "Formulation of the Action Plan on Women, Peace and Security")]),
    (r"^Ensure the effective participation of women in the formulation and implementation of policies and action plans on climate change", C,
     "Women's participation in climate change policy",
     "CEDAW notes underrepresentation of women among scientists and policymakers addressing climate change.",
     [("Committee on the Elimination of Discrimination against Women", "2", "42", "the underrepresentation of women among scientists and policymakers supporting the country’s efforts to address climate change")]),
    (r"^Ensure in national legislation the effective participation of civil society, especially women", D,
     "Civil society participation in climate change policy",
     "The documents contain no information on this ask.", []),
    # --- children and strategy ---
    (r"strategy to combat stereotypes against children with disabilities|Adopt a strategy to combat stereotypes", B,
     "Strategy against stereotypes about children with disabilities",
     "The 4th Education Plan for Persons with Disabilities 2023-2027 and a foster-family programme exist; no strategy on stereotypes is reported.",
     [("Thailand", "1", "39", "4th Education Plan for Persons with Disabilities B.E. 2023-2027")]),
    # --- SLAPP ---
    (r"^Enact legal protection against strategic litigation", B,
     "Enact legal protection against SLAPPs",
     "An Anti-SLAPP Bill is being drafted, the Criminal Procedure Code was amended and the Supreme Court President issued criteria on section 161/1 (2026); no standalone law exists.",
     [("Thailand", "1", "91", "The Thai Government is conducting a study on and drafting of the Anti-Strategic Lawsuit Against Public Participation Act"),
      ("Thailand", "1", "92", "Recommendation of the President of the Supreme Court on the Criteria and Procedures for Case Consideration under Section 161/1 of the Criminal Procedure Code B.E. 2569 (2026)")]),
    (r"^Take measures aimed at ensuring increased efficiency and accountability in public service", B,
     "Public service efficiency and accountability",
     "The Act Prescribing Timeframes for Judicial Proceedings (2022) and the Act on Facilitation of Government Licences (2026) were adopted.",
     [("Thailand", "1", "94", "enacted the Act Prescribing Timeframes for Judicial Proceedings, B.E. 2565 (2022)")]),
    (r"^(In order to ensure the protection of human rights defenders, amend sections 326|End arbitrary detentions, arrests and any acts of harassment against political actors)", C,
     "Amend defamation provisions and end arbitrary detention of activists",
     "Criminal defamation provisions (sections 326-333) remain; HRW and FLD report prosecutions and harassment of defenders and political actors.",
     [("HRW", "3", "34", "at least 1,997 people had been prosecuted in Thailand for exercising their rights to free expression and peaceful assembly"),
      ("FLD", "3", "55", "repeal the existing criminal defamation laws under Sections 326-333 of the Criminal Code")]),
    # --- refugees / migrants ---
    (r"^Stop immediately the return of refugees from Myanmar", E,
     "Stop the return of refugees to Myanmar",
     "The Committee against Torture reports a mass expulsion of asylum-seekers from Myanmar on 25 June 2024 and HRW reports the return of 40 Uyghur men in February 2025: practice contrary to the recommendation.",
     [("Committee against Torture", "2", "61", "allegations of the mass expulsion of asylum-seekers from Myanmar on 25 June 2024"),
      ("HRW", "3", "69", "The Government sent 40 Uyghur men to a neighbouring country in February 2025")]),
    (r"^(Implement legal measures to ensure proper protection of refugees|Expand social welfare initiatives to refugees)", B,
     "Protect refugees and asylum seekers and allow them to work",
     "A National Screening Mechanism operates since 2023 and a Cabinet resolution (26 August 2025) lets Myanmar displaced persons in shelters work (6,089 had entered the labour market) and obtain ID cards; there is no refugee law.",
     [("Thailand", "1", "81", "put in place the National Screening Mechanism (NSM) since 2023"),
      ("Thailand", "1", "82", "6,089 MDPs have entered the labour market")]),
    (r"^Consider ratifying the International Convention on the Protection of the Rights of All Migrant Workers", C,
     "Ratify the Migrant Workers Convention",
     "No ratification is reported; the UN country team continues to recommend it.",
     [("United Nations country team", "2", "5", "recommended that Thailand ratify the International Convention on the Protection of the Rights of All Migrant Workers and Members of Their Families")]),
    # --- health ---
    (r"^(Continue its inclusive COVID-19 vaccination policy|Continue to uphold human rights in the design and provision of COVID-19|Uphold the approach of prioritizing the mental health|Guarantee the right to access an adequate standard of health services for all, including sex workers|Provide health-care services to migrants, refugees and asylum seekers in detention centres)", D,
     "COVID-19 response, mental health, sex workers and detained migrants' health",
     "The documents contain no information on this ask; JS50 reports structural limits in mental health services.",
     []),
    (r"^Develop a national plan to guarantee access to comprehensive sexual and reproductive health services", D,
     "National plan for access to sexual and reproductive health services",
     "The documents contain no information on this ask.", []),
    # --- misc ---
    (r"^Adopt an open, merit-based process", D,
     "Open, merit-based selection of treaty body candidates",
     "The documents contain no information on this ask.", []),
    (r"^Ensure the effective implementation of the 20-year National Strategy", D,
     "Implement the 20-year National Strategy",
     "The documents contain no information on this ask.", []),
    (r"^Train public and educational institutions on human rights, with emphasis on the elimination of violence", D,
     "Human rights training for public and educational institutions",
     "The documents contain no information on this ask.", []),
    (r"^Fully implement and consider renewing the 2018", A,
     "Implement and renew the plan for coexistence in a multicultural society",
     "An Action Plan on the Promotion of Peaceful Coexistence in a Multicultural Society 2023-2027 was adopted as national policy.",
     [("Thailand", "1", "72", "Action Plan on the Promotion of Peaceful Coexistence in a Multicultural Society in Thailand B.E. 2566-2570 (2023-2027)")]),
    (r"^Ratify the Optional Protocol to the International Covenant on Economic, Social and Cultural Rights", C,
     "Ratify the Optional Protocol to the ICESCR",
     "UNESCO continues to recommend ratification; none is reported.",
     [("UNESCO", "2", "3", "recommended that Thailand ratify the Optional Protocol to the International Covenant on Economic, Social and Cultural Rights")]),
    (r"^Take action to repeal or amend such legislation", C,
     "Repeal or amend rights-restrictive legislation",
     "No repeal or amendment of the restrictive legislation is reported.",
     [("HRW", "3", "34", "at least 1,997 people had been prosecuted in Thailand for exercising their rights to free expression and peaceful assembly")]),
    (r"^Ratify International Labour Organization core conventions No. 87", C,
     "Ratify ILO Conventions 87 and 98",
     "No progress toward ratification is reported.",
     [("NHRCT", "3", "4", "no concrete progress had been made toward the ratification of ILO Conventions Nos. 87 and 98")]),
    (r"^Strengthen efforts to abolish the continued practice of genital circumcision", D,
     "Abolish female genital circumcision",
     "The documents contain no information on this ask.", []),
    (r"^Ensure Thai women have the right to pass on their citizenship|^Ensure that Thai women have the right to pass on their citizenship", D,
     "Equal right of Thai women to pass nationality to spouses and children",
     "The documents contain no information on this ask.", []),
    (r"^Undertake actions to strengthen women.s access to justice", C,
     "Women's access to justice",
     "The National Report describes general online justice services but nothing specific for rural, Indigenous or disabled women.",
     [("Committee on the Elimination of Racial Discrimination", "2", "21", "barriers preventing ethnic and ethno-religious groups, Indigenous Peoples, migrants, refugees, asylum-seekers and stateless persons from accessing justice")]),
    (r"^Ensure that the protection and promotion of the way of life of ethnic groups act", B,
     "Draft and implement the Ethnic Groups Act in line with international standards",
     "The Act entered into force on 19 September 2025; the UN country team notes it does not recognise Indigenous Peoples and reflects FPIC only partially.",
     [("Thailand", "1", "71", "Protection and Promotion of the Way of Life of Ethnic Groups Act B.E. 2568 (2025) entered into force on 19 September 2025"),
      ("United Nations country team", "2", "55", "did not explicitly recognize Indigenous Peoples and only reflected free, prior and informed consent partially")]),
    (r"^Establish a permanent national mechanism for the reporting", B,
     "Permanent national mechanism for reporting and follow-up",
     "A Committee on Driving Forward Human Rights Work in Thailand serves as the NMIRF.",
     [("Thailand", "1", "26", "serves as the National Mechanism for Implementation, Reporting and Follow-up (NMIRF)")]),
]

FALLBACK = (D, "No information on this ask",
            "The documents contain no information on this ask.", [])
