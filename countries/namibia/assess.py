"""Namibia — implementation assessment of its 3rd-cycle (2021, A/HRC/48/4) UPR
recommendations, graded against the 4th-cycle documentation (session 52):
National report A/HRC/WG.6/52/NAM/1, OHCHR Compilation /2, Stakeholders' /3.

    python -m countries.namibia.assess
"""

from __future__ import annotations

from recommendations.models import Grade
from scripts.assess import run

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

CLUSTERS = {
    "Ratification of & accession to international instruments": (
        B, "Ratify outstanding international instruments",
        "Namibia ratified ILO Conventions No. 190 and No. 156 in August 2025, but "
        "has not ratified OP-CAT (with a national preventive mechanism), the "
        "Enforced Disappearance Convention, the 1954 and 1961 Statelessness "
        "Conventions or ILO Convention No. 129; consultations on the Statelessness "
        "Convention are reported.",
        [
            ("Namibia", "1", "16", "Namibia became a state party to the International Labour Organisation (ILO) Convention 190 on sexual harassment and ILO Convention 156 on workers with families and responsibilities ratified on the 14 August 2025"),
            ("Committee against Torture; Human Rights Committee", "2", "2", "Namibia should consider ratifying the Optional Protocol to the Convention against Torture ... with the aim of establishing a national preventive mechanism"),
            ("Committee on the Rights of the Child; Committee on the Elimination of Discrimination against Women", "2", "3", "recommended that Namibia ratify the Convention relating to the Status of Stateless Persons of 1954 and the Convention on the Reduction of Statelessness of 1961"),
        ],
    ),
    "Equality & non-discrimination": (
        C, "Comprehensive anti-discrimination legislation",
        "Namibia enforces the Racial Discrimination Prohibition Act (1991) and has "
        "closed most of its gender gap, but has no comprehensive anti-"
        "discrimination law - a 2021 Ombudsman bill on discrimination, "
        "discriminatory harassment and hate speech is unenacted, the Constitution "
        "does not protect against discrimination on grounds of sexual orientation "
        "or gender identity, and vast racial economic inequalities persist.",
        [
            ("Human Rights Committee", "2", "16", "the prevalence of discrimination and stated that Namibia should ... take measures to eliminate all forms of discrimination"),
            ("Joint submission 2", "3", "8", "in 2021, the Office of the Ombudsman submitted a bill on combating discrimination, discriminatory harassment and hate speech to the government which had yet to be enacted"),
            ("Special procedure mandate holders", "2", "15", "There were currently vast inequalities between white and black Namibians, with white Namibians still controlling a large share of the economy"),
        ],
    ),
    "Sexual & gender-based violence": (
        B, "Prevent and address sexual and gender-based violence",
        "Namibia amended the Combating of Rape Act and Combating of Domestic "
        "Violence Act (2022), operates 17 Gender-Based Violence Protection Units "
        "and implemented a National Plan of Action on GBV 2019-2023; CEDAW, CAT "
        "and the Human Rights Committee report high prevalence, low prosecution "
        "and conviction rates, few shelters, and that the GBV plan expired in "
        "2023 without a successor.",
        [
            ("Namibia", "1", "109", "The Combating of Domestic Violence Act, 2003 and the Combating of Rape Act, 2000 were amended ... to strengthen and provide clarity to the provisions of the amended Acts"),
            ("Human Rights Committee", "2", "61", "the low number of prosecutions and convictions handed down to perpetrators of gender-based violence"),
            ("Joint submission 2", "3", "50", "With the expiration of the aforementioned [GBV] Plan in 2023, no replacement plan had been put in place, which diminished the ability of the government to address gender-based violence"),
        ],
    ),
    "Violence against women": (
        B, "Prevent and address violence against women",
        "Namibia amended the Combating of Rape and Combating of Domestic Violence "
        "Acts (2022) and ran a National Plan of Action on GBV 2019-2023 and an "
        "#EndGBV campaign; prevalence remains high, prosecutions and convictions "
        "low, shelters and protection orders limited, and the GBV plan lapsed in "
        "2023 without a replacement.",
        [
            ("Namibia", "1", "116", "Namibia has amended and promulgated legislation to address Gender Based Violence and Violence against Children. These include the Combating of Rape Amendment Act 2022, Combating of Domestic Violence Amendment Act 2022"),
            ("Committee on the Elimination of Discrimination against Women", "2", "60", "the high prevalence of intimate partner violence and other forms of gender-based violence against women, and the limited access for women to protection orders, reparations, shelters and psychological treatment"),
        ],
    ),
    "Constitutional & legislative framework": (
        B, "Legislative reforms (torture bill, marriage/family laws, data protection)",
        "Namibia passed the Marriage Act and Dissolution of Marriages Act (2024) "
        "and amended the High Court and Magistrates' Courts Acts, but the revised "
        "Torture Bill has been pending since 2019, the Ombudsman Bill (2024) was "
        "withdrawn, and the Data Protection and Cybercrime Bills remain in draft.",
        [
            ("Committee against Torture", "2", "7", "the revised bill on preventing and combating torture had been awaiting parliamentary approval since 2019, and urged Namibia to adopt the bill as soon as possible and to ensure that its provisions defined torture as a specific offence"),
            ("Namibia", "1", "51", "The process to enact the Torture Bill is ongoing. The Torture Bill was withdrawn from the National Assembly to finalize outstanding issues relating to penalties for offences"),
            ("Namibia", "1", "56", "Namibia is yet to enact laws on Data Protection and or Cyber Crime. The Data Protection Bill and Cybercrime Bill are still at drafting and consultations ... stage"),
        ],
    ),
    "Right to health": (
        B, "Access to health care; maternal mortality; SRHR",
        "Namibia approved a Universal Health Coverage policy (2024), reduced "
        "maternal mortality from an estimated 219 (2020) to 139 (2025) and is near "
        "the 95-95-95 HIV targets; CEDAW still calls for decriminalisation of "
        "abortion and better sexual and reproductive health access, mental-health "
        "law reform is outstanding, and the HIV response is threatened by "
        "foreign-aid withdrawal.",
        [
            ("Namibia", "1", "86", "A major milestone was the 2024 approval of a Universal Health Coverage policy, designed to guarantee equitable healthcare access for all citizens without financial burden"),
            ("Committee on the Elimination of Discrimination against Women", "2", "44", "amend section 3 (1) of the Abortion and Sterilization Act (Act No. 2 of 1975) to decriminalize abortion in all cases"),
            ("Joint submission 2", "3", "46", "the HIV/AIDS response, which had previously achieved significant success, was now at risk due to the withdrawal of foreign aid"),
        ],
    ),
    "Legal & institutional reform": (
        B, "Institutional reform (Ombudsman, anti-corruption, oversight)",
        "The Ombudsman retains A-status but the Ombudsman Bill (2024) to secure "
        "its independence and funding was withdrawn following parliamentary "
        "objections, and stakeholders report the Anti-Corruption Commission "
        "remains under-resourced and Ombudsman recommendations are frequently "
        "ignored.",
        [
            ("Namibia", "1", "31", "the Ombudsman Bill 2024 was drafted and tabled during 2025. However, it was withdrawn for further consultations"),
            ("Joint submission 7", "3", "11", "the effectiveness of the Office of the Ombudsman had remained constrained due to persistent financial and staffing shortages"),
        ],
    ),
    "Conditions of detention": (
        C, "Improve detention conditions; reduce pre-trial detention",
        "Namibia rolled out Community Service Orders to reduce overcrowding and "
        "reports overall capacity exceeds the prisoner population, but CAT reports "
        "most pre-trial detainees held in poor, dilapidated and severely "
        "overcrowded police cells, pre-trial detention routinely exceeding legal "
        "limits, and inadequate separation of convicted and remand prisoners.",
        [
            ("Committee against Torture", "2", "20", "most pretrial detainees were held in police detention facilities in poor, dilapidated and severely overcrowded holding cells"),
            ("Committee against Torture", "2", "24", "reports of prolonged pretrial detention, which routinely exceeded legal limits"),
            ("Namibia", "1", "71", "The Namibian Correctional Service (NCS) ... introduced Community Service Orders (CSO) program in 2010 as a measure to reduce overcrowding in the correctional facilities"),
        ],
    ),
    "Human rights & poverty": (
        B, "Address poverty and inequality",
        "Namibia launched a Social Protection Policy 2021-2030 and its 6th "
        "National Development Plan (2025) with poverty eradication as a cross-"
        "cutting issue, but stakeholders report it remains the second most "
        "unequal country in the world (Gini 59.1, 2022), the Basic Income Grant "
        "pilot was never scaled, and multidimensional poverty persists.",
        [
            ("Namibia", "1", "68", "Namibia launched the Social Protection Policy 2021 - 2030 which aims to address risks and vulnerabilities faced by all Namibians to reduce poverty and inequalities"),
            ("Joint submission 7", "3", "40", "With a Gini coefficient of 59.1 (as of 2022), Namibia had remained the second most unequal country in the world in terms of income distribution"),
            ("Joint submission 7", "3", "38", "the demonstrated success of the Basic Income Grant pilot project in Otjivero-Omitara (2008), this project had not been expanded nationally"),
        ],
    ),
    "Safe drinking water & sanitation": (
        B, "Access to safe water and sanitation",
        "Namibia adopted a National Sanitation and Hygiene Strategy 2022-2027 and "
        "completed the Neckertal dam (2019), but per the 2023 census only 36.2 "
        "per cent of rural households have toilet facilities and 22.6 per cent of "
        "urban households lack clean drinking water; access is described as still "
        "limited.",
        [
            ("Namibia", "1", "84", "According to the 2023 Namibia Population and Housing Census, 60% of households in Namibia have access to toilet facilities, while only 36.2% of households in rural areas have access to such facilities"),
            ("Namibia", "1", "126", "Access to water and sanitation is still limited"),
        ],
    ),
    "Right to education": (
        B, "Access to and quality of education",
        "Namibia codified universal primary and secondary education (Basic "
        "Education Act 2020), reports a 95 per cent enrolment rate and will "
        "provide free tertiary education from 2026; UNESCO, the Committee on the "
        "Rights of the Child and stakeholders report persistent classroom "
        "shortages, poor education quality and limited inclusive education for "
        "learners with disabilities.",
        [
            ("UNESCO; United Nations country team", "2", "48", "the announcement by the President of Namibia that the Government would fully subsidize tuition and registration fees at all State-run universities and vocational training centres from 2026"),
            ("UNESCO", "2", "49", "there remained a persistent shortage of classrooms and basic facilities that hindered access to quality education, especially in rural areas ... limited access to inclusive education for learners with disabilities"),
        ],
    ),
    "Human rights education, trainings & awareness raising": (
        C, "Human rights training for officials",
        "The Namibian Police conducts ongoing human-rights and torture-prevention "
        "training and the Ombudsman developed a torture-prevention training "
        "manual; JS2 reports there is still no consistent, comprehensive "
        "human-rights curriculum for all public officials.",
        [
            ("Namibia", "1", "50", "The Namibian Police Force has ongoing workshops to train police officers on human rights in accordance with the Namibian Police Human Rights Training Manual"),
            ("Joint submission 2", "3", "14", "there was a lack of a consistent and comprehensive curriculum to ensure that all public officials, particularly those in law enforcement, received adequate human rights training"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        B, "Strengthen the Ombudsman (national human rights institution)",
        "The Office of the Ombudsman is accredited A-status and has been "
        "decentralised to six regional offices with a rising budget, but the "
        "Ombudsman Bill (2024) to fully align it with the Paris Principles and "
        "secure its independence was withdrawn after parliamentary objections.",
        [
            ("Namibia", "1", "31", "The Ombudsman was accredited as an A status institution in 2019 ... the Ombudsman Bill 2024 was drafted and tabled during 2025. However, it was withdrawn for further consultations"),
            ("Joint submission 7", "3", "7", "The Ombudsman Bill (2024) ... had been withdrawn for further consultations following parliamentary objections"),
        ],
    ),
    "National Human Rights Action Plans (or specific areas) / implementation plans": (
        C, "Adopt a National Human Rights Action Plan",
        "The National Human Rights Action Plan 2015-2019 lapsed; Cabinet issued a "
        "directive in 2024 to review it and develop a successor, which is not yet "
        "adopted.",
        [
            ("Namibia", "1", "9", "In 2024 Cabinet issued a directive that the Government should conduct a review of the National Human Rights Action Plan (NHRAP) 2015-2019 and develop a successor plan"),
        ],
    ),
    "Administration of justice & fair trial": (
        B, "Access to justice; bail; legal aid",
        "Namibia raised the legal-aid qualifying threshold, expanded magistrates' "
        "courts and established victim-friendly courts; CAT and the Human Rights "
        "Committee call for criminal-justice reform, an affordable bail system, "
        "and fundamental safeguards guaranteed from the outset of detention.",
        [
            ("Namibia", "1", "28", "The qualifying amount for legal aid was increased from N$ 3500.00 to N$7000.00"),
            ("Committee against Torture", "2", "23", "Namibia should intensify efforts to reform the criminal justice system ... ensuring a more accessible and affordable bail system"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        B, "Combat trafficking in persons",
        "Namibia implements the Combating of Trafficking in Persons Act, launched "
        "a National Plan of Action on Trafficking 2023-2027 and a National "
        "Referral Mechanism, provides victim services and increased "
        "investigations and prosecutions; the UN country team says the Act needs "
        "amendment to strengthen victim protection and CRC notes rising child "
        "trafficking.",
        [
            ("Namibia", "1", "59", "There is a National Action Plan on Trafficking in Persons for the period 2023-2027 which was officially launched on 28 July 2023"),
            ("European Centre for Law and Justice", "3", "34", "those measures had led to an increase in the number of cases that had been investigated and prosecuted"),
            ("United Nations country team", "2", "33", "the Combating of Trafficking in Persons Act (Act No. 1 of 2018) required amendments to strengthen the protection of victims"),
        ],
    ),
    "Prohibition of all forms of slavery, including trafficking in persons": (
        B, "Combat trafficking in persons",
        "Namibia implements the Combating of Trafficking in Persons Act, a "
        "National Plan of Action 2023-2027 and a National Referral Mechanism and "
        "has increased prosecutions; CRC and the UN country team note gaps in "
        "victim protection and rising child trafficking.",
        [
            ("Namibia", "1", "59", "There is a National Action Plan on Trafficking in Persons for the period 2023-2027 which was officially launched on 28 July 2023"),
            ("Committee on the Rights of the Child", "2", "35", "the increase in the number of children who were trafficked into Namibia and subsequently placed in domestic or hazardous work, or subjected to commercial sexual exploitation"),
        ],
    ),
    "Right to life": (
        C, "Regulate police use of force; investigate excessive force",
        "The Human Rights Committee reports prevalent excessive use of force by "
        "the Namibian Police, including violations of the right to life, and that "
        "provisions authorising potentially lethal force are inconsistent with "
        "international standards; Namibia points to police human-rights training "
        "but reports no legislative change.",
        [
            ("Human Rights Committee", "2", "18", "the reported prevalence of excessive use of force by the Namibian Police Force, including violations of the right to life, and the authorization of the use of potentially lethal force under the Criminal Procedure Act ... which was inconsistent with international human rights standards"),
        ],
    ),
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)": (
        B, "Criminalise torture; investigate ill-treatment",
        "Namibia criminalises torture only indirectly through general provisions "
        "and the stand-alone Torture Bill has been stalled since 2019; CAT and "
        "the Human Rights Committee call for an independent body to investigate "
        "all torture and ill-treatment complaints.",
        [
            ("Committee against Torture", "2", "7", "the revised bill on preventing and combating torture had been awaiting parliamentary approval since 2019 ... ensure that its provisions defined torture as a specific offence"),
            ("Namibia", "1", "49", "Namibia criminalizes acts of torture through its Criminal Procedure Act (sections 40, 42 and 49 schedule 1), Common Law and other Statutes"),
        ],
    ),
    "Freedom of opinion and expression & access to information": (
        B, "Freedom of expression and access to information",
        "Namibia enacted the Access to Information Act (2022) but it is not yet "
        "operational, and the Whistleblower Protection Act (2017) remains "
        "non-operational; stakeholders report media pluralism constrained by "
        "reliance on state advertising and self-censorship on governance and "
        "corruption.",
        [
            ("Joint submission 7", "3", "24", "the delay in bring[ing] this [Access to Information] Act into force had undermined the work of journalists, civil society organizations, and oversight bodies ... the Whistleblower Protection Act (2017), had remained non-operational"),
            ("NMT Media Foundation", "3", "22", "instances where media outlets had self-censored coverage on governance and corruption due to reliance on government advertising"),
        ],
    ),
    "Freedom of peaceful assembly": (
        C, "Guarantee the right to peaceful assembly",
        "The Human Rights Committee calls for amendment of legislation and "
        "practice so that individuals fully enjoy the right of peaceful assembly "
        "and lethal force is used only as a last resort; no responsive change is "
        "reported.",
        [
            ("Human Rights Committee", "2", "27", "Namibia should consider amending its legislation and practices to ensure that individuals fully enjoyed their right of peaceful assembly and ensure that its legislation allowed the use of potentially lethal force by law enforcement officers only as a last resort"),
        ],
    ),
    "Right to privacy": (
        C, "Data protection and privacy legislation",
        "Namibia has no data-protection or cybercrime law; the Data Protection "
        "Bill is ready for tabling and the Cybercrime Bill is still in drafting, "
        "and stakeholders find the draft bill's Data Protection Authority "
        "insufficiently independent.",
        [
            ("Namibia", "1", "56", "The Data Protection Bill and Cybercrime Bill are still at drafting and consultations of stakeholders' stage"),
            ("NMT Media Foundation", "3", "31", "the draft bill ... was found to have had insufficient guarantees of independence for the proposed Data Protection Authority and excessive ministerial discretion in granting exemptions"),
        ],
    ),
    "Rights related to marriage & family": (
        B, "Reform discriminatory marriage and family laws",
        "Namibia passed the Marriage Act and Dissolution of Marriages Act (2024), "
        "abolishing common-law divorce grounds, but the Human Rights Committee "
        "criticises continuing delay in bills to remove gender-discriminatory "
        "aspects of customary marriage, polygamy and matrimonial property law.",
        [
            ("Human Rights Committee", "2", "8", "the delay in adopting bills that sought to address discriminatory aspects of the legislative framework with regard to gender, including the marriage bill, the bill on the recognition of customary marriages, the divorce bill and the uniform matrimonial property bill"),
            ("Namibia", "1", "62", "Namibia passed the Marriage Act during 2024"),
        ],
    ),
    "Participation of women in political & public life": (
        A, "Women's participation in political and public life",
        "After the 2024-2025 elections Namibia has a female President, Vice-"
        "President and Speaker and a 57 per cent female Cabinet and has ratified "
        "the SADC Protocol on Gender and Development; CEDAW still recommends "
        "accelerating parity in the judiciary and public service, and the 50/50 "
        "target is not legislated.",
        [
            ("Namibia", "1", "37", "Since 21 March 2025, Namibia has a female President, Vice President, Speaker of the National Assembly and the majority of Cabinet Ministers in Namibia are female. Currently, Namibia's Cabinet is composed of a majority of women (57%)"),
            ("Committee on the Elimination of Discrimination against Women", "2", "28", "take measures to accelerate gender parity at the national and local levels of government, in particular in decision-making positions in the Cabinet, the judiciary, the public service"),
        ],
    ),
    "Advancement of women": (
        B, "Advance women's equality and empowerment",
        "Namibia implements the Third National Gender Equality and Equity Policy "
        "2025-2035, reports closing 81 per cent of its gender gap and a "
        "majority-female Cabinet; CEDAW seeks stronger action on labour-market "
        "segregation, equal pay and rural women's access to land and finance.",
        [
            ("Namibia", "1", "35", "Namibia is implementing the Third NGEEP 2025-2035 ... aligned to the provisions of various regional and global commitments on gender equality"),
            ("Committee on the Elimination of Discrimination against Women", "2", "64", "ensure women's equal access to bank loans, mortgages and other forms of financial credit ... increase women's access to land"),
        ],
    ),
    "Discrimination against women": (
        B, "Combat discrimination against women",
        "Namibia implements the Third NGEEP 2025-2035 and reports strong gender-"
        "parity outcomes in politics, education and health; CEDAW seeks action on "
        "harmful practices, labour-market segregation and rural women's rights.",
        [
            ("Namibia", "1", "36", "Namibia has closed its gender gap by at least 81.1%. The Country is number 8 globally while in Sub-Saharan Africa, it is number 1"),
            ("Committee on the Elimination of Discrimination against Women", "2", "59", "initiate in-depth participatory research on the communities and contexts in which harmful practices, including polygamy, violent sexual initiation, grooming and cleansing, persisted"),
        ],
    ),
    "Children: definition": (
        B, "Child protection; child marriage; alternative care",
        "Namibia implements the Child Care and Protection Act (2015), the "
        "Marriage Act (2024) sets the marriage age at 18, and a National Plan of "
        "Action on Violence against Children 2021-2025 and an Ending Child "
        "Marriage Strategy are under way; CAT, CEDAW and the Human Rights "
        "Committee report child marriage persists under customary law and "
        "children are held in pre-trial detention with adults.",
        [
            ("Namibia", "1", "120", "Namibia enacted the Child Care and Protection Act 2015 and the Marriage Act 2024 which prohibits practices of marrying of children ... Development of Ending Child Marriage strategy is underway"),
            ("Committee against Torture", "2", "66", "the harmful traditional practice of child marriage under customary law persisted in some communities, despite its prohibition in section 226 of the Child Care and Protection Act"),
            ("Committee on the Rights of the Child", "2", "22", "reports of children held in pretrial detention together with adults"),
        ],
    ),
    "Children: juvenile justice": (
        B, "Juvenile justice; separation from adults",
        "Namibia reports juveniles are kept separate from adult inmates under the "
        "Correctional Services Act; CRC nonetheless reports children held in "
        "pre-trial detention with adults and urges detention as a measure of "
        "last resort.",
        [
            ("Namibia", "1", "75", "Juveniles are kept separate from Adult inmates in accordance with section 64 of the Namibian Correctional Services Act, 2012"),
            ("Committee on the Rights of the Child", "2", "22", "ensure that detention was used as a last resort and for the shortest appropriate period of time, and that ... children were not held together with adults"),
        ],
    ),
    "Labour rights and right to work": (
        B, "Labour rights, minimum wage and equal pay",
        "Namibia ratified ILO Conventions No. 190 and No. 156 (August 2025) and "
        "set a national minimum wage for domestic, agricultural and security "
        "workers (2024-2027); ILO reports continuing challenges implementing "
        "occupational safety and health, and CEDAW recommends equal pay for work "
        "of equal value and action on labour-market segregation.",
        [
            ("Namibia", "1", "103", "Government enacted a Wage Order Setting the National Minimum Wage for certain employees (domestic, agricultural and security), for the years 2024, 2025, 2026 and 2027"),
            ("International Labour Organization", "2", "36", "Namibia continued to face challenges in effectively implementing policies on occupational safety and health"),
        ],
    ),
    "Right to an adequate standard of living": (
        B, "Adequate standard of living; informal settlements",
        "Namibia's Cabinet approved a revised National Housing Policy (2023) and "
        "supports the Shack Dwellers Federation, but stakeholders report more "
        "than 40 per cent of the population (about 80 per cent of the urban "
        "population) live in informal settlements without secure tenure or basic "
        "services.",
        [
            ("Joint submission 7", "3", "41", "more 40 percent of the total population and approximately 80 percent of the urban population lived in informal settlements, often without access to basic services or secure land tenure"),
            ("Namibia", "1", "81", "In 2023, the Cabinet approved the revised National Housing Policy and Implementation Action Plan, which provides for the accelerated interventions ... to scale up the upgrading of informal settlements countrywide"),
        ],
    ),
    "Right to adequate housing": (
        B, "Right to adequate housing; informal settlements",
        "A revised National Housing Policy (2023) and support for the Shack "
        "Dwellers Federation are reported, but a large majority of the urban "
        "population lives in informal settlements without secure tenure, and "
        "evictions of informal occupants continue.",
        [
            ("Joint submission 7", "3", "41", "more 40 percent of the total population and approximately 80 percent of the urban population lived in informal settlements, often without access to basic services or secure land tenure"),
            ("Namibia", "1", "82", "local authority councils have evicted illegal occupants of land in their jurisdictions in accordance with their respective by-laws"),
        ],
    ),
    "Cooperation with human rights mechanisms & requests for technical assistance": (
        C, "Standing invitation to special procedures",
        "Namibia reports full cooperation with treaty bodies (no overdue reports) "
        "and accepted a Special Rapporteur visit request in 2024, but has not "
        "issued a standing invitation to special procedures and requests for "
        "visits by mandate holders are pending.",
        [
            ("United Nations country team", "2", "6", "Namibia had not issued a standing invitation to the special procedures of the Human Rights Council and that requests for visits by mandate holders were pending"),
            ("Namibia", "1", "17", "In 2024, Namibia accepted a request from special rapporteur on freedom of expression and the Government is currently liaising with the special rapporteur for scheduled visit"),
        ],
    ),
    "Cooperation & Follow up with Treaty Bodies": (
        A, "Cooperate with treaty bodies",
        "Namibia has no overdue reports and has submitted all reports to the UN "
        "treaty bodies; in 2024 it was reviewed by the Committee against Torture "
        "and the Human Rights Committee.",
        [
            ("Namibia", "1", "17", "Namibia has no overdue reports and has submitted all the reports to all UN treaty bodies. During 2024, Namibia was reviewed by the Committee against Torture and the Human Rights Committee"),
        ],
    ),
    "Business & Human Rights": (
        C, "Business and human rights",
        "The Ombudsman began a national dialogue on business and human rights in "
        "2025 with a view to a component in the successor National Human Rights "
        "Action Plan; special procedures raise serious concern about the Tsumeb "
        "smelter's environmental harm and a 'grandfather clause' shielding "
        "smelter owners from liability.",
        [
            ("Namibia", "1", "124", "The Ombudsman has started a National dialogue on Business and Human Rights in 2025 and has proposed to incorporate a component on business and Human Rights in the successor plan"),
            ("Special procedure mandate holders", "2", "57", "the 'grandfather clause', a legal provision that shielded smelter owners from liability for the environmental and human rights harm that they had caused ... was not in alignment with international standards"),
        ],
    ),
    "Human rights & the environment": (
        B, "Climate change and environment",
        "Namibia has a National Policy on Climate Change (2011) and a Disaster "
        "Risk Management Act (2012) and integrated gender-responsive climate "
        "strategies into its NGEEP 2025-2035; the UN country team notes the "
        "human-rights-based approach to climate change is still limited, and "
        "CEDAW seeks human-rights impact assessments and community consent for "
        "oil and gas exploration in Kavango.",
        [
            ("United Nations country team", "2", "55", "although Namibia had demonstrated its commitment to climate action through various initiatives, the application of a human right-based approach in addressing climate change was still limited"),
            ("Committee on the Elimination of Discrimination against Women", "2", "56", "ensure that any decisions on oil and gas exploitation in the Kavango region were subject to the full, prior and informed consent of local communities"),
        ],
    ),
    "Refugees & asylum seekers": (
        C, "Refugee rights; non-refoulement; freedom of movement",
        "Namibia enacted a Regularisation of Status Act and a Civil Registration "
        "and Identification Act (2024) advancing the right to identity, but CAT "
        "calls for repeal of a Refugees Act provision inconsistent with "
        "non-refoulement, and Namibia maintains its reservation to article 26 of "
        "the Refugee Convention limiting refugees' freedom of movement and "
        "livelihoods.",
        [
            ("Committee against Torture", "2", "79", "Namibia should repeal section 24 (1) of the Namibia Refugees (Recognition and Control) Act (Act No. 2 of 1999) with a view to guaranteeing the absolute principle of non-refoulement"),
            ("UNHCR; United Nations country team", "2", "80", "Namibia maintained its reservation to article 26 of the Convention relating to the Status of Refugees of 1951, thus limiting the freedom of movement of refugees and preventing their participation in meaningful livelihood opportunities"),
        ],
    ),
    "Rights related to name, identity & nationality": (
        B, "Reduce statelessness; universal birth registration",
        "Namibia enacted the Civil Registration and Identification Act and the "
        "Regularisation of Status Act (2024) - described by UNHCR as a "
        "significant step forward on statelessness - and is rolling out mass "
        "civil registration; the Statelessness Conventions are not ratified "
        "(consultations ongoing) and universal birth registration is not yet "
        "achieved.",
        [
            ("UNHCR", "2", "83", "the Civil Registration and Identification Act (Act No. 13 of 2024) and the Regularization of Status of Certain Residents of Namibia ... represented a significant step forward in ensuring the fundamental right to identity and addressing long-standing issues of statelessness"),
            ("Committee on the Rights of the Child", "2", "84", "strengthen its efforts to achieve universal birth registration and ensure that all children had access to birth registration and identity documents"),
        ],
    ),
    "Persons with disabilities: definition, general principles": (
        B, "Align disability law and policy with the CRPD",
        "Namibia amended the National Disability Council Act and adopted a "
        "revised National Disability Policy (2025), but CRC and the UN country "
        "team report disability law is not yet aligned with the CRPD and access "
        "to services and buildings for persons with disabilities remains "
        "limited.",
        [
            ("Namibia", "1", "118", "during 2025 Namibia amended the National Disability Council Act 2004, which contains the amended National Policy of Disability"),
            ("United Nations country team", "2", "70", "access for persons with disabilities to services remained limited, with many buildings, transport systems and essential facilities lacking ramps, tactile signage or auditory cues"),
        ],
    ),
    "Members of minorities": (
        C, "Recognise and protect Indigenous Peoples and minorities",
        "Namibia reserves higher-education and public-service quotas for "
        "marginalized communities and finalised the Ombudsman's White Paper on "
        "Indigenous Peoples' Rights, but the Human Rights Committee and "
        "stakeholders report Namibia still does not recognise the San, Himba and "
        "others as Indigenous Peoples, the White Paper is unadopted, and "
        "ancestral-land restitution has stalled.",
        [
            ("Human Rights Committee", "2", "71", "Namibia did not recognize certain communities as Indigenous Peoples, instead referring to them as marginalized communities ... consider recognizing communities such as the San, Himba, Ovatue, Ovatjimba and Ovazemba as Indigenous Peoples"),
            ("Joint submission 6", "3", "55", "the White Paper had not been adopted nor implemented by Namibia and consequently considered the recommendations to have not been implemented"),
        ],
    ),
    "Indigenous peoples": (
        C, "Recognise and protect Indigenous Peoples",
        "Namibia finalised the Ombudsman's White Paper on Indigenous Peoples' "
        "Rights and reserves university and public-service quotas for the San, "
        "Ovatue and Ovatjimba, but does not recognise them as Indigenous Peoples "
        "and the White Paper is unadopted; ancestral-land restitution has "
        "stalled.",
        [
            ("Namibia", "1", "122", "The White Paper on indigenous peoples' rights in Namibia has been finalized with input from stakeholders, under the leadership of the Ombudsman ... submitted to the Parliamentary Standing Committee"),
            ("Human Rights Committee", "2", "72", "take appropriate measures with a view to promoting the restitution of ancestral lands to affected communities, including Indigenous Peoples"),
        ],
    ),
    "Right to social security": (
        B, "Extend social protection coverage",
        "Namibia increased the universal old-age pension and launched a Social "
        "Protection Policy 2021-2030, but stakeholders report the policy is weak "
        "in scope and excludes many, and the National Pension Fund and National "
        "Medical Benefit Fund have faced nearly three decades of implementation "
        "delay.",
        [
            ("Joint submission 7", "3", "37", "steps had been taken to strengthen social protection, including a substantial increase in the universal old-age pension and the launch of the Social Protection Policy (2021-2030), but ... that Policy remained weak in scope and excluded many citizens"),
            ("Joint submission 7", "3", "39", "The National Pension Fund and the National Medical Benefit Fund ... had faced delays of nearly three decades in implementation"),
        ],
    ),
    "Human rights & climate change": (
        B, "Climate change and human rights",
        "Namibia has a National Policy on Climate Change (2011) and a Disaster "
        "Risk Management Act (2012) and built gender-responsive climate "
        "strategies into its NGEEP 2025-2035 and participated in the ICJ "
        "advisory proceedings on climate obligations; the UN country team says "
        "a human-rights-based approach to climate change is still limited.",
        [
            ("Namibia", "1", "44", "Namibia has a National Policy on Climate Change (2011). The third NGEEP 2025-2035 makes provision for the implementation of strategies to address the impact of climate change"),
            ("United Nations country team", "2", "55", "the application of a human right-based approach in addressing climate change was still limited"),
        ],
    ),
    "Right to development": (
        B, "National development planning",
        "Namibia launched its 6th National Development Plan (2025) with a costed "
        "implementation, monitoring and evaluation plan and poverty eradication "
        "as a cross-cutting issue; high unemployment and inequality remain the "
        "central challenges.",
        [
            ("Namibia", "1", "42", "In 2025, Namibia launched its National Development Plan Six (NDP 6) which focuses on four (4) pillars ... NDP 6 also has an Implementation, Monitoring and Evaluation Plan (IMEP)"),
            ("Namibia", "1", "125", "Namibia is experiencing a high unemployment rate and requires assistance from the international community"),
        ],
    ),
    "Good governance & corruption": (
        C, "Strengthen anti-corruption capacity",
        "The Anti-Corruption Commission's budget rose modestly for 2025/2026, but "
        "stakeholders report it remains under-resourced - unable to establish an "
        "anti-money-laundering unit needed to exit the FATF grey list - and that "
        "most citizens believe corruption has worsened.",
        [
            ("Namibia", "1", "54", "For the 2025/2026 financial year, the Anti-Corruption Commission is allocated N$116,549,000 ... an increase of 9.96% compared to the 2024/2025 budgetary allocation"),
            ("Joint submission 7", "3", "12", "The current level of funding did not allow for the establishment of specialized units, particularly an anti-money laundering unit ... The persistent under-resourcing of the Commission had hampered its ability to address increasingly sophisticated corruption schemes"),
        ],
    ),
    "Right to food": (
        B, "Right to food and nutrition security",
        "Namibia revised its National Food and Nutrition Security Policy (2021) "
        "and runs food-bank and school-feeding programmes and drought relief, "
        "but the UN country team and CRC record continuing child malnutrition "
        "and stunting and high food insecurity.",
        [
            ("Namibia", "1", "100", "Namibia has a National Food and Nutrition Security policy which was revised during 2021, its implementation plan and, Food and Nutrition Security Coordination structures"),
            ("Committee on the Rights of the Child", "2", "45", "strengthen efforts to reduce infant mortality rates and to eliminate malnutrition, stunting and micronutrient deficiency among children"),
        ],
    ),
    "Economic, social & cultural rights - general measures of implementation": (
        C, "Give effect to economic, social and cultural rights",
        "JS7 reports that most economic, social and cultural rights are not "
        "guaranteed as enforceable rights in the Constitution and are treated as "
        "aspirational policy goals; Namibia has not acceded to the Optional "
        "Protocol to the ICESCR.",
        [
            ("Joint submission 7", "3", "4", "the enforceability of most of the internationally recognised economic, social and cultural rights had not been guaranteed in the Constitution. As a result, those rights had been treated as aspirational policy goals"),
        ],
    ),
    "Access to justice & remedy": (
        B, "Access to justice and effective remedies",
        "Namibia raised the legal-aid threshold and expanded courts, but CEDAW "
        "recommends increased legal-aid funding and effective access to justice "
        "for women throughout the country, and stakeholders report impunity for "
        "bias-motivated violence.",
        [
            ("Committee on the Elimination of Discrimination against Women", "2", "26", "increase funding for legal aid and ensure that women had effective access to justice throughout the country"),
            ("Namibia", "1", "28", "The qualifying amount for legal aid was increased from N$ 3500.00 to N$7000.00"),
        ],
    ),
    "Sexual & reproductive health and rights": (
        C, "Sexual and reproductive health and rights",
        "Namibia prioritises SRHR in national policy and integrated sexuality "
        "education into school programmes, but the restrictive Abortion and "
        "Sterilization Act (1975) is unchanged, comprehensive sexuality "
        "education is under-funded and teachers under-trained, and CEDAW seeks "
        "decriminalisation of abortion and better contraceptive access.",
        [
            ("Committee on the Elimination of Discrimination against Women", "2", "44", "amend section 3 (1) of the Abortion and Sterilization Act (Act No. 2 of 1975) to decriminalize abortion in all cases ... improve women's access to safe abortion and post-abortion services"),
            ("Joint submission 2", "3", "49", "there had been a lack of funding for the full implementation of these [comprehensive sexuality education] programmes and teachers had not been properly trained to teach the curriculum"),
        ],
    ),
}

KEYWORDS = [
    (r"same-sex marriage|recognition of.{0,40}marriage|marriages concluded (abroad|outside)|foreign marriage", E,
     "Recognise same-sex marriages",
     "The consolidated Marriage Act (2024) defines marriage in strictly "
     "heterosexual terms and bars recognition of foreign same-sex marriages, "
     "expressly reversing the Namibian Supreme Court's 2023 judgment - a "
     "regression.",
     [("Christian Council International", "3", "62", "In October 2024, the President of Namibia had assented to a consolidated Marriage Act (2024), which similarly defined marriage in strictly heterosexual terms ... thus directly aiming to reverse the findings of the Supreme Court's 2023 judgment"),
      ("Joint submission 4", "3", "62", "the Act's heteronormative framing was inconsistent with Articles 10 and 14 of the Constitution, which guaranteed equality before the law and protected family life")]),
    (r"decriminaliz.{0,40}same-sex|consensual same-sex|sodomy|same-sex sexual", C,
     "Decriminalise consensual same-sex relations",
     "Consensual same-sex relations remain criminalised under Roman-Dutch "
     "common law; the High Court struck down the sodomy offences in 2024 but "
     "the Government has appealed to the Supreme Court.",
     [("Committee against Torture", "2", "78", "the criminalization of consensual sexual relations between persons of the same sex, and recommended that Namibia decriminalize consensual same-sex relations"),
      ("Joint submission 2", "3", "61", "In 2024, the High Court had struck down the common law offences of sodomy and unnatural offences, and the government has since filed an appeal against this decision to the Supreme Court")]),
    (r"sexual orientation|gender identity|\bLGBT|transgender|gender diverse", C,
     "Protect LGBTI persons from discrimination and violence",
     "The Constitution and key statutes still do not protect against "
     "discrimination on grounds of sexual orientation or gender identity, "
     "stakeholders report escalating hate crimes and violence against LGBTQI+ "
     "people, and the draft Hate Speech Bill omits these grounds.",
     [("Human Rights Committee", "2", "77", "Namibia should amend the Labour Act, the Combating of Domestic Violence Act and the Combating of Rape Act (Act No. 8 of 2000) to extend the protection provided under those Acts to lesbian, gay, bisexual and transgender persons"),
      ("Joint submission 3", "3", "19", "the period under review had witnessed a concerning escalation in violence directed at LGBTQI+ individuals, with reports indicating a substantial increase in hate crimes and homicides")]),
    (r"Optional Protocol to the Convention against Torture|OP-CAT|national preventive mechanism", C,
     "Ratify OP-CAT and establish a national preventive mechanism",
     "Namibia has not ratified OP-CAT and has not established a national "
     "preventive mechanism.",
     [("Committee against Torture; Human Rights Committee", "2", "2", "Namibia should consider ratifying the Optional Protocol to the Convention against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment with the aim of establishing a national preventive mechanism")]),
    (r"Enforced Disappearance", C,
     "Ratify the Convention against Enforced Disappearance",
     "Namibia has not ratified the Enforced Disappearance Convention; CAT "
     "encourages ratification, and stakeholders link the unresolved fate of "
     "persons who disappeared in SWAPO exile camps to non-compliance with "
     "ICPPED, CAT and the ICCPR.",
     [("Committee against Torture", "2", "4", "encouraged Namibia to consider ratifying the International Convention for the Protection of All Persons from Enforced Disappearance"),
      ("Breaking the Wall of Silence", "3", "18", "an estimated 2000 persons had been listed as disappeared ... Namibia had not complied with ICPPED, CAT, and ICCPR")]),
    (r"Statelessness|stateless|Reduction of Statelessness", C,
     "Ratify the Statelessness Conventions",
     "Namibia has not ratified the 1954 and 1961 Statelessness Conventions; "
     "consultations on the Reduction of Statelessness Convention are reported, "
     "and the 2024 Civil Registration and Regularisation Acts are a step "
     "forward.",
     [("Committee on the Rights of the Child; Committee on the Elimination of Discrimination against Women", "2", "3", "recommended that Namibia ratify the Convention relating to the Status of Stateless Persons of 1954 and the Convention on the Reduction of Statelessness of 1961"),
      ("Namibia", "1", "70", "The Ministry of Home Affairs, Immigration, Safety and Security conducted consultations regarding the convention on the Reduction of Statelessness")]),
    (r"abortion", C,
     "Reform the restrictive abortion law",
     "The Abortion and Sterilization Act 1975 still restricts abortion; CEDAW "
     "recommends decriminalisation, a 2020 parliamentary process produced no "
     "reform, and civil society reports persistent unsafe abortions.",
     [("Committee on the Elimination of Discrimination against Women", "2", "44", "amend section 3 (1) of the Abortion and Sterilization Act (Act No. 2 of 1975) to decriminalize abortion in all cases"),
      ("Christian Council International", "3", "44", "the persistence of illegal abortions had demonstrated the existence of gaps in practical support for women, especially those facing poverty or social exclusion")]),
    (r"free (and compulsory )?(primary |secondary |tertiary |basic )?education|tuition|university fees", A,
     "Provide free education",
     "Namibia provides free primary and secondary education and will provide "
     "free tertiary education in phases from 2026.",
     [("Namibia", "1", "79", "free primary and secondary education; free tertiary education will be provided in phases from the year 2026"),
      ("Global Engagement Research Group", "3", "47", "considered a relevant supported recommendation from the previous review to ensure free and compulsory education for all children to have been implemented")]),
    (r"ILO Convention (No\. )?190|violence and harassment (in the world of work|at work)|Convention 190", A,
     "Ratify ILO Convention No. 190",
     "Namibia ratified ILO Convention No. 190 on violence and harassment in "
     "the world of work (and No. 156) on 14 August 2025.",
     [("Namibia", "1", "16", "Namibia became a state party to the International Labour Organisation (ILO) Convention 190 on sexual harassment and ILO Convention 156 on workers with families and responsibilities ratified on the 14 August 2025")]),
    (r"corporal punishment", B,
     "Prohibit corporal punishment in all settings",
     "Corporal punishment is prohibited in schools and institutional settings "
     "and past whipping and caning provisions were struck down by the Supreme "
     "Court; it is not yet explicitly outlawed in the home, addressed for now "
     "through a positive-parenting manual.",
     [("Namibia", "1", "19", "The Child Care and Protection Act of 2015 ... prohibits corporal punishment in settings such as schools, foster care, shelters, prisons, and police cells ... However, it does not explicitly outlaw corporal punishment in the home")]),
    (r"child marriage|early marriage|marriage of (minors|children)|marrying of children", B,
     "End child marriage",
     "The Marriage Act (2024) and Child Care and Protection Act set the "
     "minimum marriage age at 18 and an Ending Child Marriage Strategy is being "
     "developed, but CAT and others report child marriage persists under "
     "customary law.",
     [("Namibia", "1", "120", "the Marriage Act 2024 which prohibits practices of marrying of children ... Development of Ending Child Marriage strategy is underway"),
      ("Committee against Torture", "2", "66", "the harmful traditional practice of child marriage under customary law persisted in some communities")]),
    (r"standing invitation", C,
     "Extend a standing invitation to special procedures",
     "Namibia has still not issued a standing invitation to the special "
     "procedures, a recommendation it supported at the previous review; "
     "requests for visits by mandate holders are pending.",
     [("United Nations country team", "2", "6", "Namibia had not issued a standing invitation to the special procedures of the Human Rights Council and that requests for visits by mandate holders were pending"),
      ("Joint submission 2", "3", "3", "at the previous review, Namibia had supported a recommendation to extend a standing invitation to the special procedures of the Human Rights Council, which had not been implemented")]),
]


if __name__ == "__main__":
    run("namibia", clusters=CLUSTERS, keywords=KEYWORDS)
