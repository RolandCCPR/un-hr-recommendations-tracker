"""Denmark — implementation assessment of its 3rd-cycle (2021, A/HRC/48/10)
UPR recommendations, graded against the 4th-cycle documentation (session 52):
National report A/HRC/WG.6/52/DNK/1, OHCHR Compilation /2, Stakeholders'
Summary /3.

    python -m countries.denmark.assess

First pass for expert review. Quotes are verbatim from the three documents.
"""

from __future__ import annotations

from recommendations.models import Grade
from scripts.assess import run

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

# theme -> (grade, action_summary, rationale, [(org, doc "1"|"2"|"3", para, quote)])
CLUSTERS = {
    "Equality & non-discrimination": (
        B, "Anti-discrimination framework; national action plan against racism",
        "Denmark has a broad anti-discrimination legal framework and in February "
        "2025 adopted a National Action Plan against Racism with 36 initiatives, "
        "alongside successive action plans against antisemitism; CERD and "
        "stakeholders nonetheless report persistent gaps - no legislative "
        "prohibition of racial or ethnic profiling, weak hate-crime data, and a "
        "2025 plan criticised for limited scope and for lacking a definition of "
        "racism.",
        [
            ("Denmark", "1", "112", "In February 2025, the Danish Government presented a national action plan against racism with 36 initiatives and the ambition to fight racism in a variety of areas in society"),
            ("Joint submission 1; Joint submission 2", "3", "21", "welcomed the adoption of a national action plan against racism in February 2025. However, they were concerned that the plan had limitations in scope and lacked a clear definition of racism"),
            ("Committee on the Elimination of Racial Discrimination", "2", "9", "expressed concern about the lack of a clear prohibition of racial profiling and of operational guidelines to combat racial profiling"),
        ],
    ),
    "Ratification of & accession to international instruments": (
        B, "Ratify outstanding international instruments",
        "Denmark ratified the International Convention for the Protection of All "
        "Persons from Enforced Disappearance (January 2022) and ILO Convention "
        "No. 190 (2024), but has not acceded to the Optional Protocol to the "
        "ICESCR, has expressly decided not to sign the ICRMW, and has not "
        "ratified the Treaty on the Prohibition of Nuclear Weapons.",
        [
            ("Committee against Torture", "2", "2", "welcomed the ratification by Denmark of the International Convention for the Protection of All Persons from Enforced Disappearance in 2022"),
            ("Denmark", "1", "6", "Denmark ratified the International Convention for the Protection of All Persons from Enforced Disappearance (ICPPED) on 13 January 2022 ... Denmark has decided not to sign ICRMW"),
            ("UNESCO", "2", "2", "noted that Denmark was not a party to the Optional Protocol to the International Covenant on Economic, Social and Cultural Rights"),
        ],
    ),
    "Reservations": (
        C, "Withdraw or review reservations and declarations",
        "No withdrawal of reservations is reported; Denmark has not accepted the "
        "individual complaints procedure under the Enforced Disappearance "
        "Convention and remains outside the Optional Protocol to the ICESCR.",
        [
            ("Denmark", "1", "6", "The Government of Denmark has not accepted the individual right of appeal to the Committee under the [Enforced Disappearance] convention"),
            ("Denmark", "1", "7", "Denmark has acceded to the Optional Protocols establishing access to the individual complaints procedures ... with the exception of ICESCR"),
        ],
    ),
    "Labour rights and right to work": (
        B, "Equal pay, ILO standards and labour-market inclusion",
        "Denmark ratified ILO Convention No. 190 on violence and harassment at "
        "work (2024), is implementing the EU Pay Transparency Directive and "
        "adopted a 2025-2028 disability employment action plan; a 12.3 per cent "
        "gender pay gap persists and the employment rate of persons with "
        "disabilities remains lower than others.",
        [
            ("Denmark", "1", "8", "In 2024, Denmark ratified ILO convention number 190 concerning the elimination of violence and harassment in the world of work"),
            ("Institute for Protection of Women's Rights", "3", "47", "the average Danish woman earned 12.3 percent less than the average Danish man in 2023, linked to occupational and hierarchical segregation"),
            ("Committee on the Rights of Persons with Disabilities", "2", "32", "the employment rate of persons with disabilities was lower than that of others and recommended that Denmark adopt a long-term employment strategy"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        B, "Combat trafficking in persons",
        "Denmark adopted a National Action Plan to Combat Trafficking in Human "
        "Beings 2022-2025 (with a 2026-2029 plan in preparation) and established "
        "a Special Crime Unit; CAT, CEDAW and the DIHR report a persistently low "
        "number of investigations and convictions, a limited recovery and "
        "reflection period, and no independent national rapporteur.",
        [
            ("Committee against Torture", "2", "30", "welcomed the adoption by Denmark of a National Action Plan to Combat Trafficking in Human Beings 2022-2025. However, it was concerned about the low number of investigations and convictions for trafficking in human beings and the limited recovery and reflection period for victims"),
            ("Denmark", "1", "73", "A new action plan against human trafficking for the period of 2026-2029 is under preparation"),
            ("Danish Institute for Human Rights", "3", "8", "a low number of convictions for trafficking of human beings, while the number of persons exposed to trafficking had increased ... establish a permanent, independent National Rapporteur"),
        ],
    ),
    "National Human Rights Action Plans (or specific areas) / implementation plans": (
        B, "Adopt and implement national action plans",
        "Denmark works through numerous multi-year action plans (against racism "
        "2025, antisemitism 2022 and 2025, intimate-partner violence 2023-2026, "
        "trafficking, LGBT+, disability 2025-2028); the DIHR and civil society "
        "note several lack measurable goals and indicators and that the "
        "intimate-partner-violence plan expires in 2026 without a successor.",
        [
            ("Danish Institute for Human Rights", "3", "2", "a national action plan against racism was published in February 2025 and recommended that Denmark expand the action plan with specific, measurable goals and indicators"),
            ("Danish Institute for Human Rights", "3", "9", "the national action plan against intimate partner violence and homicide would expire in 2026 ... recommended that Denmark adopt a renewed national action plan to combat violence against women"),
        ],
    ),
    "Right to health": (
        B, "Access to health care; psychiatric coercion; Greenland",
        "All residents have free access to public healthcare and Denmark adopted "
        "a 10-year psychiatry plan (2025) targeting a 30 per cent cut in "
        "coercive measures by 2030; CRPD and JS2 report coercion in psychiatric "
        "care remains high with the enabling legal changes not due before 2027, "
        "and CEDAW/DIHR flag unaddressed health gaps in Greenland (abortion "
        "rate, sexually transmitted infections, suicide).",
        [
            ("Denmark", "1", "87", "The most recent comprehensive political agreement from May 2025 ... contribute to the new and ambitious goal to reduce coercive measures by 30% by 2030"),
            ("Joint submission 2", "3", "27", "coercive measures continued to be excessively used in psychiatric institutions and that the 10-year plan adopted in 2025 ... lacked a necessary preventive approach"),
            ("Committee on the Elimination of Discrimination against Women", "2", "57", "the high prevalence of suicide and suicide attempts in Greenland and recommended that Denmark collect comprehensive data on the causes and address them"),
        ],
    ),
    "Sexual & gender-based violence": (
        B, "Prevent and address sexual and gender-based violence",
        "Denmark adopted a consent-based rape law (2020), a National Action Plan "
        "on Intimate Partner Violence and Killings 2023-2026, psychological-"
        "violence provisions, a victims' hotline and new shelters (including for "
        "men, 2024); CEDAW, CAT and JS2 report rising gender-based violence, few "
        "rape convictions, and the Istanbul Convention still not applied to "
        "Greenland and the Faroe Islands.",
        [
            ("Committee against Torture", "2", "35", "welcomed the adoption of the National Action Plan to Combat Intimate Partner Violence and Intimate Partner Killings 2023-2026"),
            ("Committee on the Elimination of Discrimination against Women", "2", "36", "it noted with concern the rise in gender-based violence against women, high incidences of sexual violence against women with disabilities and the reported high prevalence of sexual harassment in the workplace and the education system"),
            ("Joint submission 2", "3", "46", "a small proportion of reported cases of rape resulting in convictions, and a high number of suspected femicides in the first half of 2025"),
        ],
    ),
    "Violence against women": (
        B, "Prevent and address violence against women",
        "Denmark maintains national action plans against intimate-partner "
        "violence since 2002 (current plan 2023-2026), a consent-based rape law "
        "(2020), crisis shelters and a victims' hotline; stakeholders report "
        "rising femicide, gaps in restraining-order use, and that the current "
        "plan expires in 2026 without a successor.",
        [
            ("Denmark", "1", "49", "Since 2002, national action plans to combat intimate partner violence and intimate partner killings have been in place. The current National Action Plan (2023-2026)"),
            ("Maat Foundation for Peace, Development and Human Rights", "3", "44", "47.5 percent of women had experienced physical or sexual violence or threats thereof, and referred to an increase in femicides"),
            ("Danish Institute for Human Rights", "3", "9", "recommended that Denmark adopt a renewed national action plan to combat violence against women and introduce a dedicated offence code for intimate partner homicide"),
        ],
    ),
    "Refugees & asylum seekers": (
        E, "Fair asylum procedures; end externalisation",
        "Denmark has enacted legislation enabling the externalisation of its "
        "asylum policy and the processing of asylum claims in a third country, "
        "contrary to recommendations for fair and accessible asylum; CAT, UNHCR "
        "and the DIHR call for this to be revisited, and CAT also criticises "
        "reliance on diplomatic assurances and prison-like conditions in the "
        "Ellebaek return centre.",
        [
            ("Committee against Torture", "2", "47", "concerned about legislation enabling the externalization of the asylum policy of Denmark, and about plans to process asylum claims in a third country. The Committee recommended that Denmark revisit legislation and plans for such externalization"),
            ("Danish Institute for Human Rights", "3", "11", "legislation allowing the transfer of asylum seekers to a third country, to have their asylum case processed, lacked important legal safeguards"),
            ("Council of Europe (CPT); Joint submission 2", "3", "53", "the conditions at the Ellebaek return centre were prison-like"),
        ],
    ),
    "Migrants": (
        B, "Limit immigration detention; family reunification",
        "The Human Rights Committee asked Denmark to amend the Aliens Act to "
        "limit immigration detention and reduce restrictions on family "
        "reunification for persons under temporary protection; the National "
        "Report describes detention as a last resort and states minors are 'as "
        "a general rule' not detained, but CAT remains concerned the option to "
        "detain children remains in law and that the 'tolerated stay' regime "
        "bars work.",
        [
            ("Human Rights Committee", "2", "48", "asked Denmark to indicate the steps taken to amend the Aliens Act, with a view to limiting the detention of migrants and asylum-seekers to the shortest possible period"),
            ("Denmark", "1", "63", "detention according to the Danish Aliens Act only takes place as a last resort ... as a general rule, Denmark does not detain minors"),
            ("Committee against Torture", "2", "51", "while noting information provided by Denmark that children would not be detained for the purpose of return, the Committee remained concerned that such an option continued to exist in law"),
        ],
    ),
    "Constitutional & legislative framework": (
        C, "Legislative reforms (torture offence, defamation, expression)",
        "Torture is still not a distinct criminal offence in Danish, Greenlandic "
        "or Faroese law; defamation remains criminalised; and a 2023 provision "
        "criminalising 'improper treatment of objects with significant religious "
        "significance' has drawn Human Rights Committee and civil-society "
        "concern over vagueness and chilling effects on expression.",
        [
            ("Committee against Torture", "2", "12", "torture was not criminalized as a distinct offence in the Danish Penal Code, the Military Criminal Code or the Greenlandic or Faroese criminal law"),
            ("Human Rights Committee", "2", "24", "the amendment to section 110 (e) of the Penal Code, which criminalized the 'improper treatment of objects with significant religious significance' ... concerns about the vagueness of the terms and potential chilling effects on legitimate expression"),
            ("UNESCO", "2", "23", "defamation was a criminal offence under Danish law and recommended that Denmark decriminalize defamation"),
        ],
    ),
    "Business & Human Rights": (
        B, "Business and human rights, including mandatory due diligence",
        "Denmark actively supported the EU Corporate Sustainability Due Diligence "
        "Directive introducing mandatory human-rights and environmental due "
        "diligence and maintains an OECD National Contact Point; JS2 seeks "
        "stronger arms-export controls and post-employment rules, and Denmark's "
        "approach to the 'Omnibus' simplification has drawn concern about "
        "weakening the directive.",
        [
            ("Denmark", "1", "118", "Denmark has actively supported the introduction of mandatory human rights and environmental due diligence at the EU level through the adoption of the Corporate Sustainability Due Diligence Directive (CSDDD)"),
            ("Joint submission 2", "3", "28", "adopt a case-by-case assessment of arm export licenses and prohibit exports if there was an overriding risk that this would contribute to breach of international humanitarian law"),
        ],
    ),
    "Children: definition": (
        B, "Child protection; violence against children",
        "The Danish Child's Act entered into force on 1 January 2024 "
        "incorporating CRC obligations, and psychological violence against "
        "children has been criminalised; CAT and JS2 remain concerned about "
        "children in social care placed in closed facilities and the very low "
        "number of psychological-violence cases reaching the courts.",
        [
            ("Denmark", "1", "96", "The Danish Child's Act entered into force on January 1st 2024. The law ensures that the obligations of Denmark in relation to the UN Convention on the Rights of the Child ... are respected"),
            ("Joint submission 2", "3", "48", "a significant number of children in Denmark continued to be subjected to corporal and psychological violence ... only very few cases of psychological violence were brought to the judicial system"),
        ],
    ),
    "Human rights & counter-terrorism": (
        D, "Counter-terrorism measures and safeguards",
        "The National Report notes only that combating terrorism is a 'highly "
        "important priority' with initiatives since 2015; the 4th-cycle "
        "documentation contains no specific information on measures responsive "
        "to these recommendations or on Danish counter-terrorism safeguards.",
        [
            ("Denmark", "1", "77", "Substantial counter-terrorism initiatives have been launched since the 2015 terror attacks in Copenhagen"),
        ],
    ),
    "Right to education": (
        C, "Inclusive and non-discriminatory education",
        "The Committee on the Rights of Persons with Disabilities reports that "
        "segregated schooling has increased and barriers to inclusive education "
        "persist; an expert group reported recommendations in June 2025 but no "
        "legislative change is reported, and stakeholders describe persistent "
        "discrimination against ethnic-minority students.",
        [
            ("Committee on the Rights of Persons with Disabilities", "2", "33", "segregated schooling had increased and that barriers to inclusive education had resulted in school refusal and the involuntary absence of children with disabilities"),
            ("Denmark", "1", "94", "In May 2024 the Danish Government established an expert group to prepare specific recommendations for adjustments to the legislative framework for inclusion ... The expert group published its recommendations in June 2025"),
        ],
    ),
    "Conditions of detention": (
        B, "Improve detention conditions; reduce pre-trial detention",
        "A new disciplinary system (September 2023) reduced long-term solitary "
        "confinement over 14 days and prison capacity is being expanded, but "
        "CAT, the CPT and the DIHR report continuing overcrowding, extensive and "
        "lengthening pre-trial detention, and remand prisoners in de facto "
        "isolation up to 23 hours a day.",
        [
            ("Denmark", "1", "80", "A new disciplinary penalty system entered into force in September 2023, which has led to ... a substantial decrease in long-term solitary confinement exceeding 14 days"),
            ("Danish Institute for Human Rights", "3", "3", "some detainees stayed in their cells close to 23 hours a day, often without access to meaningful activities and with restrictions on contact with the outside world"),
            ("Committee against Torture", "2", "14", "a high proportion of remand detention and an increase in the duration of pretrial detention, with low usage of alternatives to detention"),
        ],
    ),
    "Administration of justice & fair trial": (
        C, "Access to justice; police complaints; safeguards",
        "CRPD reports persistent barriers to access to justice for persons with "
        "disabilities, and the DIHR calls for the Independent Police Complaints "
        "Authority's mandate to be expanded to assess human-rights violations; "
        "no responsive legislative change is reported.",
        [
            ("Committee on the Rights of Persons with Disabilities", "2", "21", "barriers to access to justice for persons with disabilities, across Denmark, the Faroe Islands and Greenland, including the insufficient provision of procedural accommodation"),
            ("Danish Institute for Human Rights", "3", "4", "expand the mandate of the Independent Police Complaints Authority to include assessing and deciding on whether individuals who file complaints against the police had been subjected to human rights violations"),
        ],
    ),
    "Right to adequate housing": (
        B, "Right to housing; homelessness",
        "'Housing First' has guided Danish homelessness policy since 2009 and key "
        "elements were placed in legislation in October 2023; but CERD and civil "
        "society find the 'Parallel Society'/'Ghetto' laws drive housing "
        "insecurity and demolition of social housing for residents of "
        "'non-Western' background.",
        [
            ("Denmark", "1", "106", "Since October 2023, key elements of Housing First have been part of national Danish legislation. The main goals are significantly decreasing the number of persons in homelessness and ending long-term homelessness"),
            ("Maat Foundation for Peace, Development and Human Rights", "3", "25", "the Parallel Society Act ... was leading to the reduction or demolition of social housing and the termination of rental contracts, resulting in housing insecurity"),
        ],
    ),
    "Freedom of thought, conscience & religion": (
        C, "Freedom of religion or belief",
        "The 2023 provision on 'improper treatment of objects with significant "
        "religious significance' has raised expression concerns, and the "
        "European Association of Jehovah's Witnesses reports unaddressed hate "
        "incidents; the National Report describes a 2025 revision of the Act on "
        "Religious Communities but no measure directly responsive to these "
        "recommendations.",
        [
            ("European Association of Jehovah's Witnesses", "3", "35", "reports of hate incidents and acts of violence affecting Jehovah witnesses in Denmark, including in the context of the peaceful public manifestation of their beliefs"),
            ("Denmark", "1", "84", "The [Act on Religious Communities] was revised in 2025 ... The revision, which entered into force on January 1st, 2026, includes additional codification of existing practices"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        B, "Strengthen the national human rights institution",
        "The Danish Institute for Human Rights retains A-status accreditation; "
        "the Human Rights Committee has asked Denmark to amend the DIHR Act to "
        "secure an independent board-removal procedure, liability protection and "
        "adequate funding, and no NHRI has yet been established in the Faroe "
        "Islands.",
        [
            ("Human Rights Committee", "2", "4", "amending the Act on the Danish Institute for Human Rights to establish an independent procedure for removal of board members ... guaranteeing adequate funding to fulfil its mandate"),
            ("Denmark", "1", "150", "The Government has explored different options for establishing a national human rights institution [in the Faroe Islands], adapted to the small Faroese society, and will continue to do so"),
        ],
    ),
    "Human rights & the environment": (
        B, "Climate change and environment",
        "Denmark's Climate Act sets a 70 per cent emissions-reduction target for "
        "2030 and net-negative 110 per cent by 2050, and Greenland joined the "
        "Paris Agreement in 2024; the Human Rights Committee still seeks "
        "information on climate impacts on the right to life in Greenland and "
        "the Faroe Islands.",
        [
            ("Denmark", "1", "193", "The Danish Climate Act sets a target of reducing Denmark's GHG emissions with 70% in 2030 compared to 1990 and Denmark aims to achieve net-negative by 110% by 2050"),
            ("Denmark", "1", "143", "Greenland withdrew its territorial reservation and joined the Paris Agreement in 2024"),
        ],
    ),
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)": (
        C, "Criminalise torture; safeguards against ill-treatment",
        "Torture is still not a stand-alone offence in Danish, Greenlandic or "
        "Faroese criminal law despite repeated CAT recommendations; safeguards "
        "from the outset of detention and limits on strip-searching are also "
        "found wanting.",
        [
            ("Committee against Torture", "2", "12", "torture was not criminalized as a distinct offence in the Danish Penal Code, the Military Criminal Code or the Greenlandic or Faroese criminal law"),
            ("Committee against Torture", "2", "16", "sufficient legal safeguards, including timely access to legal representation and adequate interpretation and translation, were not always guaranteed from the outset of detention"),
        ],
    ),
    "Human rights & poverty": (
        C, "Combat poverty, including child poverty",
        "Denmark maintains an extensive social-protection system but has no "
        "official poverty definition and does not intend to adopt one; JS2 "
        "reports roughly 49,500 people in poverty and a benefit reform reducing "
        "income for an estimated 11,000 children, and calls for a national "
        "child-poverty action plan.",
        [
            ("Denmark", "1", "101", "There is no official poverty definition in Denmark. The Government does not intend to introduce an official definition of poverty"),
            ("Joint submission 2", "3", "38", "49,500 persons lived in poverty and the social benefit reform would reduce income for an estimated 11,000 children ... initiate a national action plan to combat child poverty"),
        ],
    ),
    "Persons with disabilities: independence, inclusion": (
        C, "De-institutionalisation; legal capacity; accommodation",
        "The Committee on the Rights of Persons with Disabilities finds no "
        "comprehensive de-institutionalisation strategy, continued forced "
        "treatment and guardianship-based restrictions on legal capacity, and "
        "that the disability-discrimination Act still imposes no general duty of "
        "reasonable accommodation; a 2025-2028 action plan on education and "
        "employment is noted.",
        [
            ("Committee on the Rights of Persons with Disabilities", "2", "43", "amend the Guardianship Act to guarantee full legal capacity and replace substituted decision-making systems with supported decision-making systems"),
            ("Committee on the Rights of Persons with Disabilities", "2", "44", "the Act on Prohibition of Discrimination on Grounds of Disability did not impose an obligation to provide reasonable accommodation or to ensure accessibility"),
            ("Denmark", "1", "35", "The Danish Government has allocated 25.7 million DKK from 2025-2028 for an action plan for better inclusion for people with disabilities in education and in the labour market"),
        ],
    ),
    "Persons with disabilities: definition, general principles": (
        C, "Rights of persons with disabilities",
        "CRPD finds continued forced treatment, guardianship-based restrictions "
        "on legal capacity and no general duty of reasonable accommodation in "
        "the disability-discrimination Act; Denmark points to a 2025-2028 "
        "inclusion action plan and a 2025 awareness campaign.",
        [
            ("Committee on the Rights of Persons with Disabilities", "2", "38", "repeal all laws and abolish all practices that allowed for the deprivation of liberty on the basis of impairment and forced treatment"),
            ("Denmark", "1", "36", "In 2025, a national disability week and an information campaign ... was initiated"),
        ],
    ),
    "Children: family environment & alternative care": (
        B, "Quality and stability of alternative care",
        "Since 2021 Denmark has issued initiatives to improve foster-care quality "
        "and stability, with implementation funding from 2025, and the 2024 "
        "Child's Act tightened safeguards on non-consensual placement; CAT "
        "remains concerned about children placed in closed facilities alongside "
        "sentenced children.",
        [
            ("Denmark", "1", "99", "Since 2021, new initiatives have been issued to improve the quality of foster care and to ensure stability and continuity in the upbringing of children living in foster homes"),
            ("Committee against Torture", "2", "37", "children in social care were placed in secure residential facilities along with children serving custodial sentences"),
        ],
    ),
    "Children: juvenile justice": (
        C, "Juvenile justice safeguards",
        "The National Report notes that minors may be placed in a penalty cell "
        "for up to 7 days as a disciplinary sanction (longer if violent against "
        "staff); CAT continues to recommend ending solitary confinement of "
        "children.",
        [
            ("Denmark", "1", "81", "Minors can be imposed penalty cell as a disciplinary sanction for no more than 7 days, unless the minor has been violent against staff in the institution"),
            ("Committee against Torture", "2", "18", "solitary confinement could last up to four weeks and was still allowed for juveniles"),
        ],
    ),
    "Rights related to name, identity & nationality": (
        B, "Legal gender recognition; nationality of stateless children",
        "Denmark allows administrative legal gender change from age 18 and since "
        "2023 a procedure for minors to obtain an identification number "
        "reflecting their gender identity; legal gender recognition regardless "
        "of age was rejected by Parliament in January 2025, and children born "
        "stateless still do not acquire nationality automatically at birth.",
        [
            ("Joint submission 2", "3", "50", "legal gender recognition regardless of age had not been adopted, following the rejection of a parliamentary proposal in January 2025"),
            ("Committee on the Elimination of Discrimination against Women; UNHCR", "2", "53", "children born stateless in Denmark did not automatically acquire nationality at birth ... ensure, by law, that children born in the country were automatically granted Danish citizenship if they would otherwise be stateless"),
        ],
    ),
    "Rights related to marriage & family": (
        C, "Family reunification",
        "The Human Rights Committee and UNHCR call for amendment of the Aliens "
        "Act to reduce restrictions on family reunification for persons under "
        "temporary protection and to remove mandatory waiting periods; no such "
        "amendment is reported, though 2025 changes protect accompanying family "
        "members subjected to domestic violence.",
        [
            ("Human Rights Committee", "2", "29", "asked Denmark to indicate the steps taken to amend the Aliens Act with a view to reducing restrictions on family reunification for persons under temporary protection status"),
            ("Office of the United Nations High Commissioner for Refugees", "2", "28", "remove mandatory waiting periods for family reunification for all beneficiaries of international protection"),
        ],
    ),
    "Members of minorities": (
        C, "Rights of ethnic and religious minorities",
        "CERD and stakeholders find the 'non-Western'/'Parallel Society' "
        "framework in law and policy stigmatising and discriminatory toward "
        "ethnic minorities, and Denmark has renamed rather than repealed it.",
        [
            ("Committee on the Elimination of Racial Discrimination", "2", "7", "the laws previously known as the 'Ghetto Package' had a discriminatory impact on ethnic minorities ... (b) repeal discriminatory provisions"),
            ("Denmark", "1", "105", "A political agreement has been reached to change the term 'ghetto' ... to 'parallel societies' and 'areas of transformation'"),
        ],
    ),
    "Liberty & security of the person": (
        C, "Detention safeguards; deprivation of liberty on grounds of disability",
        "CRPD calls on Denmark to repeal laws allowing detention and compulsory "
        "treatment based on impairment; no such repeal is reported.",
        [
            ("Committee on the Rights of Persons with Disabilities", "2", "38", "repeal all laws and abolish all practices that allowed for the deprivation of liberty on the basis of impairment and forced treatment, including mental health laws and institutionalization policies"),
        ],
    ),
    "Right to development": (
        B, "Development cooperation and ODA",
        "Denmark has met the UN 0.7 per cent of GNI target for official "
        "development assistance for over 45 years and applies a human-rights-"
        "based approach to development cooperation.",
        [
            ("Denmark", "1", "115", "For more than 45 years, Denmark has committed at least 0.7 pct. of Gross National Income (GNI) in Official Development Assistance (ODA) in line with the UN target"),
            ("Maat Foundation for Peace, Development and Human Rights", "3", "42", "Denmark was among the countries that had achieved the United Nations target on official development assistance"),
        ],
    ),
    "Cooperation & Follow up with Treaty Bodies": (
        A, "Cooperate with treaty bodies and special procedures",
        "Denmark maintains a standing invitation to special procedures, reports "
        "regularly to the treaty bodies and submitted its first report under the "
        "Enforced Disappearance Convention in May 2025.",
        [
            ("Denmark", "1", "1", "special procedures of the Human Rights Council have a standing invitation"),
            ("Denmark", "1", "82", "The first report of the Danish Government regarding measures taken by Denmark to give effect to its obligations under the [Enforced Disappearance] convention was submitted to the Committee on Enforced Disappearances (CED) on 3 May 2025"),
        ],
    ),
    "Racial discrimination": (
        B, "Combat racial discrimination",
        "CERD finds persistent gaps: no legislative prohibition of racial "
        "profiling, weak hate-crime data, and the discriminatory 'non-Western'/"
        "'Parallel Society' framework retained under renamed terminology.",
        [
            ("Committee on the Elimination of Racial Discrimination", "2", "8", "the underreporting of racist hate crimes and hate speech, the lack of comprehensive data collection in that regard and gaps between the number of hate crimes registered by police, the number of prosecutions and the number of convictions"),
        ],
    ),
    "Human rights & climate change": (
        B, "Climate change mitigation and adaptation",
        "Denmark's Climate Act targets a 70 per cent emissions cut by 2030 and "
        "net-negative 110 per cent by 2050; the Human Rights Committee still "
        "seeks information on climate impacts on the right to life in Greenland "
        "and the Faroe Islands.",
        [
            ("Denmark", "1", "193", "The Danish Climate Act sets a target of reducing Denmark's GHG emissions with 70% in 2030 compared to 1990 and Denmark aims to achieve net-negative by 110% by 2050"),
        ],
    ),
    "Discrimination against women": (
        B, "Combat discrimination against women",
        "Denmark reformed parental leave for equal rights (2022), introduced a "
        "40/60 board gender-balance target for large listed companies (2024) and "
        "full gender equality in military conscription (2025); persistent "
        "occupational segregation and a gender pay gap remain.",
        [
            ("Denmark", "1", "19", "In December 2024, further rules were introduced that require the largest listed companies to reach a set target figure of a 40/60 gender representation on their board of Directors"),
            ("Institute for Protection of Women's Rights", "3", "47", "persistent gender pay gaps remained, as the average Danish woman earned 12.3 percent less than the average Danish man in 2023"),
        ],
    ),
    "Advancement of women": (
        B, "Advance women's participation and equality",
        "Denmark reformed parental leave (2022), set a 40/60 board gender-balance "
        "target for large listed companies (2024) and introduced equal military "
        "conscription (2025); women remain under-represented in leadership and "
        "high-paying occupations.",
        [
            ("Denmark", "1", "20", "Full equality between men and women in relation to military conscription was introduced in 2025"),
        ],
    ),
    "Sexual & reproductive health and rights": (
        B, "Sexual and reproductive health and rights",
        "Denmark raised the abortion time-limit to 18 weeks (adopted 24 April "
        "2025) and mandates sexuality education through upper-secondary "
        "education; CEDAW notes unaddressed sexual and reproductive health gaps "
        "for women and girls in Greenland.",
        [
            ("European Centre for Law and Justice", "3", "40", "the adoption, on 24 April 2025, of a proposal relating to abortion raising the limit for abortion to 18 weeks of pregnancy"),
            ("Committee on the Elimination of Discrimination against Women", "2", "58", "the high abortion rate and the high prevalence of sexually transmitted infections among women and girls in Greenland"),
        ],
    ),
    "Access to justice & remedy": (
        C, "Access to justice and effective remedies",
        "CRPD reports persistent barriers to access to justice for persons with "
        "disabilities and the DIHR seeks an expanded police-complaints mandate; "
        "no responsive change is reported.",
        [
            ("Committee on the Rights of Persons with Disabilities", "2", "21", "barriers to access to justice for persons with disabilities ... insufficient provision of procedural accommodation in judicial and administrative proceedings"),
        ],
    ),
    "Legal & institutional reform": (
        C, "Legal and institutional reform",
        "Key reforms sought - a stand-alone torture offence, decriminalisation "
        "of defamation, a duty of reasonable accommodation - are not reported as "
        "carried out.",
        [
            ("Committee against Torture", "2", "12", "torture was not criminalized as a distinct offence in the Danish Penal Code, the Military Criminal Code or the Greenlandic or Faroese criminal law"),
        ],
    ),
    "Research & other measures of implementation": (
        C, "Data collection and disaggregated statistics",
        "CERD and the DIHR report that Denmark still does not collect adequate "
        "data on ethnicity or disaggregated data on hate crimes and on Greenland.",
        [
            ("Committee on the Elimination of Racial Discrimination", "2", "10", "the lack of data on the ethnicity of persons residing in Denmark ... revise its data-collection processes to ensure that it collected data on ethnicity"),
        ],
    ),
    "Unilateral coercive measures": (
        D, "Unilateral coercive measures",
        "The 4th-cycle documentation contains no information relevant to this "
        "recommendation.",
        [],
    ),
}

# (regex on rec text, grade, action_summary, rationale, [quotes]); last match wins
KEYWORDS = [
    (r"Enforced Disappearance|Protection of All Persons from Enforced", A,
     "Ratify the Convention against Enforced Disappearance",
     "Denmark ratified the International Convention for the Protection of All "
     "Persons from Enforced Disappearance on 13 January 2022 and submitted its "
     "first report to the Committee in May 2025; it has not accepted the "
     "individual complaints procedure.",
     [("Denmark", "1", "6", "Denmark ratified the International Convention for the Protection of All Persons from Enforced Disappearance (ICPPED) on 13 January 2022"),
      ("Committee against Torture", "2", "2", "welcomed the ratification by Denmark of the International Convention for the Protection of All Persons from Enforced Disappearance in 2022")]),
    (r"Migrant Workers|ICRMW|Rights of All Migrant Workers", E,
     "Ratify the Migrant Workers Convention (ICRMW)",
     "Denmark has expressly decided not to sign the International Convention on "
     "the Protection of the Rights of All Migrant Workers, contrary to the "
     "recommendation.",
     [("Denmark", "1", "6", "As explained in more detail in the Annex, Denmark has decided not to sign ICRMW"),
      ("Committee on the Elimination of Discrimination against Women; Committee on the Elimination of Racial Discrimination", "2", "2", "encouraged Denmark to ratify the International Convention on the Protection of the Rights of All Migrant Workers and Members of Their Families")]),
    (r"Optional Protocol to the International Covenant on Economic|OP-ICESCR|OP-CESCR", C,
     "Accede to the Optional Protocol to the ICESCR",
     "Denmark remains outside the Optional Protocol to the ICESCR, having "
     "acceded to the individual-complaints protocols for the other treaties it "
     "is party to.",
     [("UNESCO", "2", "2", "noted that Denmark was not a party to the Optional Protocol to the International Covenant on Economic, Social and Cultural Rights"),
      ("Denmark", "1", "7", "Denmark has acceded to the Optional Protocols establishing access to the individual complaints procedures ... with the exception of ICESCR")]),
    (r"Prohibition of Nuclear Weapons|nuclear-weapon|nuclear weapon", C,
     "Ratify the Treaty on the Prohibition of Nuclear Weapons",
     "Denmark has not ratified the Treaty on the Prohibition of Nuclear "
     "Weapons.",
     [("International Campaign to Abolish Nuclear Weapons", "3", "19", "recommended that Denmark ratify the Treaty on the Prohibition of Nuclear Weapons")]),
    (r"externaliz|third country|offshore|process(ing)? .*asylum .*(abroad|third)", E,
     "End externalisation of asylum and offshore detention",
     "Denmark has legislated to enable transfer of asylum-seekers to a third "
     "country for processing and plans a prison abroad for foreign nationals, "
     "contrary to recommendations; CAT, UNHCR, the DIHR and civil society call "
     "for these to be reversed.",
     [("Committee against Torture", "2", "47", "concerned about legislation enabling the externalization of the asylum policy of Denmark, and about plans to process asylum claims in a third country"),
      ("Joint submission 2", "3", "32", "the plan by Denmark to establish a prison in a third country for foreigners convicted by Danish courts would outsource responsibility for the proper treatment of detainees ... reverse its decision")]),
    (r"Istanbul Convention", B,
     "Apply the Istanbul Convention, including to Greenland and the Faroe Islands",
     "Denmark ratified the Istanbul Convention in 2014 and Greenland ratified "
     "it in 2022, but it is still not applied to Greenland or the Faroe "
     "Islands; work to extend it is under way.",
     [("Denmark", "1", "48", "In 2014, Denmark ratified the Istanbul Convention on preventing and combating violence against women and domestic violence"),
      ("Committee on the Elimination of Discrimination against Women", "2", "59", "the non-application of the ... Istanbul Convention to Greenland and the Faroe Islands ... extend the application of the Istanbul Convention to Greenland and the Faroe Islands")]),
    (r"consent-based rape|lack of consent|definition of rape|rape.{0,15}consent", A,
     "Define rape on the basis of lack of consent",
     "Denmark adopted a consent-based rape provision in 2020, under which sex "
     "without consent is rape.",
     [("Denmark", "1", "56", "The Danish Parliament adopted in 2020 a consent-based rape provision according to which sex without consent is considered rape"),
      ("Joint submission 2", "3", "46", "welcomed that Denmark's rape provision had been amended to be based on lack of consent")]),
    (r"racial profiling|ethnic profiling", C,
     "Prohibit racial and ethnic profiling",
     "There is still no legislative prohibition of racial or ethnic profiling "
     "and no operational guidelines, per CERD.",
     [("Committee on the Elimination of Racial Discrimination", "2", "9", "the lack of a clear prohibition of racial profiling and of operational guidelines to combat racial profiling ... define and prohibit racial profiling in legislation")]),
    (r"parallel societ|ghetto|non-Western|Ghetto Package", C,
     "Repeal the 'Parallel Society' / 'Ghetto' laws",
     "CERD and civil society call for repeal of the discriminatory "
     "'non-Western'/'Parallel Society' provisions; Denmark has renamed the "
     "terminology but retained the framework.",
     [("Committee on the Elimination of Racial Discrimination", "2", "7", "the laws previously known as the 'Ghetto Package' had a discriminatory impact on ethnic minorities ... (b) repeal discriminatory provisions"),
      ("Denmark", "1", "105", "A political agreement has been reached to change the term 'ghetto' ... to 'parallel societies' and 'areas of transformation'")]),
    (r"intersex", C,
     "End non-consensual surgery on intersex children",
     "CAT and JS2 report continuing non-consensual, irreversible surgery on "
     "intersex children and no impartial investigation; Denmark cites an "
     "existing prohibition of cosmetic operations but reports no new measure.",
     [("Committee against Torture", "2", "45", "reports of non-consensual, irreversible surgeries performed on intersex children ... enforce its prohibition of irreversible surgical operations on intersex children for cosmetic reasons"),
      ("Joint submission 2", "3", "51", "allegedly unnecessary and irreversible medical treatment and surgery were performed on intersex children and that no impartial investigation had been conducted")]),
    (r"reasonable accommodation", C,
     "Introduce a general duty of reasonable accommodation",
     "The Act on Prohibition of Discrimination on Grounds of Disability still "
     "imposes no general obligation to provide reasonable accommodation, per "
     "CRPD.",
     [("Committee on the Rights of Persons with Disabilities", "2", "44", "the Act on Prohibition of Discrimination on Grounds of Disability did not impose an obligation to provide reasonable accommodation or to ensure accessibility")]),
    (r"solitary confinement|de facto isolation", B,
     "Restrict solitary confinement",
     "A new disciplinary system (September 2023) substantially reduced "
     "long-term solitary confinement exceeding 14 days, but the law still "
     "allows up to 4 weeks in exceptional cases and up to 7 days for juveniles, "
     "and remand prisoners face de facto isolation.",
     [("Denmark", "1", "80", "A new disciplinary penalty system entered into force in September 2023, which has led to ... a substantial decrease in long-term solitary confinement exceeding 14 days"),
      ("Committee against Torture", "2", "18", "solitary confinement could last up to four weeks and was still allowed for juveniles")]),
    (r"sexual orientation|gender identity|\bLGBT|lesbian, gay|transgender|homosexual|same-sex", B,
     "Protect LGBTI persons from discrimination",
     "Denmark strengthened protection of LGBT+ people in December 2021 by "
     "adding gender identity, gender expression and sex characteristics to the "
     "hate-crime, hate-speech and discrimination laws, funds LGBT+ action plans "
     "and introduced 'co-fatherhood' in 2025; legal gender recognition for "
     "minors regardless of age was rejected by Parliament in January 2025.",
     [("Denmark", "1", "29", "In December 2021, Denmark strengthened the protection of LGBT+ people by explicitly referring to gender identity, gender expression and sex characteristics as grounds of protection in the Danish laws covering hate crimes, hate speech and discrimination"),
      ("Joint submission 2", "3", "50", "legal gender recognition regardless of age had not been adopted, following the rejection of a parliamentary proposal in January 2025")]),
    (r"torture .*(offence|crime|criminaliz)|criminaliz.*torture|specific offence of torture", C,
     "Criminalise torture as a distinct offence",
     "Torture is still not a stand-alone offence in Danish, Greenlandic or "
     "Faroese criminal law, despite repeated CAT recommendations.",
     [("Committee against Torture", "2", "12", "torture was not criminalized as a distinct offence in the Danish Penal Code, the Military Criminal Code or the Greenlandic or Faroese criminal law"),
      ("Danish Institute for Human Rights", "3", "12", "torture was not explicitly defined as a punishable act in Greenland's Penal Code and recommended that Greenland incorporate torture as a specific crime")]),
]


if __name__ == "__main__":
    run("denmark", clusters=CLUSTERS, keywords=KEYWORDS)
