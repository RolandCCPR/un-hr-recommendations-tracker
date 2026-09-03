"""Paraguay — implementation assessment of its 3rd-cycle (2021, A/HRC/48/9) UPR
recommendations, graded against the 4th-cycle documentation (session 52):
National report A/HRC/WG.6/52/PRY/1, OHCHR Compilation /2, Stakeholders' /3.

    python -m countries.paraguay.assess
"""

from __future__ import annotations

from recommendations.models import Grade
from scripts.assess import run

A, B, C, D, E = Grade.A, Grade.B, Grade.C, Grade.D, Grade.E

CLUSTERS = {
    "Equality & non-discrimination": (
        C, "Adopt a comprehensive anti-discrimination law",
        "Paraguay still has not adopted a comprehensive law against all forms of "
        "discrimination despite recommendations across successive cycles; the "
        "Special Rapporteur on minority issues, three treaty bodies and the UN "
        "country team all call for it, and the Constitution's equality clause is "
        "not backed by implementing legislation.",
        [
            ("Special Rapporteur on minority issues; Committee on Migrant Workers", "2", "12", "Paraguay still had not adopted a law against all forms of discrimination, despite the numerous international recommendations"),
            ("Special Rapporteur on minority issues; treaty bodies; United Nations country team", "2", "13", "recommended that Paraguay promptly adopt a law against all forms of discrimination"),
            ("Paraguay", "1", "100", "the absence of a regulatory law cannot be invoked to restrict rights or guarantees"),
        ],
    ),
    "Violence against women": (
        B, "Prevent and address violence against women and femicide",
        "Paraguay implements Act No. 5777/2016 on comprehensive protection of "
        "women, declared a social emergency on violence against women and "
        "children (Act No. 7239/2024), operates the SOS Mujer hotline, shelters, "
        "femicide protocols and electronic monitoring, and made training "
        "mandatory for civil servants; Amnesty International and the country team "
        "report femicide and very high prevalence persist, Act 5777 budgets "
        "remain inadequate, and bills to abolish the Ministry for Women and ban "
        "gender mainstreaming pose a risk of regression.",
        [
            ("Paraguay", "1", "113", "The State has stepped up its efforts to prevent and combat violence against women and girls by taking measures under Act No. 5777/2016 ... supplemented by Act No. 7239/2024, declaring a social emergency in respect of violence against women, children and adolescents"),
            ("Amnesty International", "3", "45", "78.5% of women experienced gender-based violence ... legislative initiatives such as a bill to ban gender mainstreaming and another to eliminate the Ministry for Women involved a serious risk of regression"),
            ("United Nations country team", "2", "50", "cases of femicide had been observed in Paraguay in previous years and, according to a national survey, the level of violence against women was very high"),
        ],
    ),
    "National Human Rights Institution (NHRI)": (
        B, "Strengthen the Ombudsman (national human rights institution)",
        "Paraguay's Ombudsman's Office regained GANHRI category A status in 2025 "
        "and its budget was increased; the UN country team notes it still has "
        "one of the lowest budgets of any agency, and civil society reports the "
        "selection process is not regulated, merit-based or transparent, leaving "
        "the Office vulnerable to political capture.",
        [
            ("Paraguay", "1", "17", "The Office of the Ombudsman was re-accredited with category A status ... officially granted in 2025 and certifies that the Office is in full compliance with the Paris Principles"),
            ("United Nations country team", "2", "7", "The budget allocated to the institution had been increased, but it continued to have one of the lowest budgets of any agency"),
            ("Joint Submission 3", "3", "19", "the lack of political independence of the Ombudsman's Office, which resulted from the lack of a regulated, merit-based selection process"),
        ],
    ),
    "Freedom of association": (
        E, "Repeal the NGO oversight law (Act No. 7363/2024)",
        "Act No. 7363/2024 (the 'Garrote' Act on oversight and transparency of "
        "non-profit organisations), adopted in 2024, imposes vague and "
        "disproportionate requirements and penalties that restrict freedom of "
        "association; the Ombudsman's Office and multiple stakeholders call for "
        "its repeal - a regression against recommendations to protect civic "
        "space.",
        [
            ("Ombudsman's Office of Paraguay", "3", "5", "Act No. 7363/64 on the Oversight, Transparency and Accountability of Non-profit Organizations ... imposed requirements and procedures that restricted the exercise of the right of association"),
            ("Several stakeholders (OHCHR summary)", "3", "27", "Act No. 7363 (the Garrote Act), adopted in 2024, abusively restricted freedom of association with vague provisions and unclear penalties ... A number of communications recommended repealing Act No. 7363"),
            ("Paraguay", "1", "93", "Act No. 7363/2024, establishing the oversight and transparency of non-profit organizations, was enacted and is regulated by Decree 4806/2025"),
        ],
    ),
    "Administration of justice & fair trial": (
        B, "Judicial independence; access to justice; impunity",
        "Paraguay has digitalised case files and strengthened judicial-ethics "
        "training, but the Special Rapporteur on hazardous wastes describes the "
        "judicial system as slow and inefficient with most human-rights "
        "complaints uninvestigated, and civil society reports no measures to "
        "guarantee judicial independence and systematic impunity for "
        "dictatorship-era crimes against humanity.",
        [
            ("Special Rapporteur on hazardous substances and wastes", "2", "20", "the country's judicial system was slow and inefficient, with most reports of human rights violations not being investigated"),
            ("Joint Submission 3", "3", "24", "Paraguay had not taken measures to guarantee the independence and impartiality of the judiciary"),
            ("Paraguay", "1", "62", "Progress has been made in modernizing the judicial system by digitalizing case files, electronically allocating cases and publishing decisions and statistics"),
        ],
    ),
    "Right to education": (
        B, "Quality, inclusive and non-discriminatory education",
        "Paraguay expanded the 'Zero Hunger in Schools' meals programme to full "
        "national coverage and runs inclusion support centres, but the Committee "
        "on the Rights of Persons with Disabilities reports under-investment in "
        "inclusive education and persistent segregated special education, and "
        "dropout rates remain high among rural, low-income and Indigenous "
        "students.",
        [
            ("Committee on the Rights of Persons with Disabilities", "2", "43", "concern at the lack of investment in the right to education of persons with disabilities ... redouble its efforts to end segregated special education"),
            ("Joint Submission 2", "3", "42", "dropout rates remained high among rural and low-income students as a result of poverty, the lack of infrastructure, poor quality education"),
            ("Paraguay", "1", "22", "the 'Zero Hunger in Schools' programme ... achieving 100% coverage nationwide and feeding more than 1,050,000 children and adolescents every day"),
        ],
    ),
    "Ratification of & accession to international instruments": (
        B, "Ratify outstanding international instruments",
        "Paraguay ratified the Convention against Discrimination in Education "
        "(2025) and approved accession to the Inter-American Convention on Older "
        "Persons (December 2025), but has not ratified the Optional Protocol to "
        "the ICESCR (still under 'internal analysis'), the Escazu Agreement, the "
        "Ljubljana-The Hague Convention or the Inter-American Conventions against "
        "racism and discrimination.",
        [
            ("Paraguay", "1", "6", "Paraguay ratified the Convention against Discrimination in Education in 2025. In December 2025, it approved accession to the Inter-American Convention on Protecting the Human Rights of Older Persons"),
            ("Special Rapporteur on minority issues; United Nations country team; UNESCO", "2", "2", "recommended that Paraguay ratify the Optional Protocol to the International Covenant on Economic, Social and Cultural Rights"),
            ("Amnesty International; Joint Submission 3", "3", "13", "the failure to ratify the Regional Agreement on Access to Information, Public Participation and Justice in Environmental Matters in Latin America and the Caribbean (Escazu Agreement)"),
        ],
    ),
    "Right to health": (
        B, "Access to health care; mental health; maternal mortality",
        "Paraguay is decentralising services through family and community health "
        "teams, doubled public-hospital mammography machines, enacted a "
        "mental-health Act (No. 7018/2022) with a 2024-2030 plan, and adopted a "
        "Plan to Reduce Maternal, Fetal and Neonatal Mortality 2023-2030; the UN "
        "country team and CRPD report continuing quality gaps in rural and "
        "Indigenous areas, prolonged institutionalisation without consent, and "
        "that Act 7018/2022 keeps a medical model of disability.",
        [
            ("Paraguay", "1", "41", "The enactment of Act No. 7018/2022 initiated the process of reforming mental healthcare"),
            ("United Nations country team", "2", "64", "the enactment of the Mental Health Act and its National Plan 2024-2030. However, it added that serious shortcomings persisted, including the use of prolonged institutionalization without consent"),
            ("United Nations country team", "2", "36", "challenges continued to surround the quality of healthcare, especially in rural areas and Indigenous communities"),
        ],
    ),
    "Conditions of detention": (
        B, "Prison overcrowding; pre-trial detention; torture prevention",
        "Paraguay closed the Casa del Buen Pastor prison, opened a 1,200-place "
        "women's prison in Emboscada and approved a 2024 protocol on "
        "alternatives to pre-trial detention, but the UN country team and the "
        "National Mechanism for the Prevention of Torture report a structural "
        "crisis: 70 per cent of prisoners in pre-trial detention, 435 per cent "
        "overcrowding nationwide (over 1,100 per cent in some units), and "
        "maximum-security regimes amounting to torture.",
        [
            ("United Nations country team", "2", "17", "A total of 70% of the prison population was in pretrial detention, and overcrowding had reached 435% nationwide, with some facilities operating at more than 1,100% of their capacity"),
            ("Paraguay", "1", "64", "A historic milestone was achieved with the definitive closure of the Casa del Buen Pastor Prison and the opening of a women's prison complex in Emboscada with capacity for more than 1,200 women"),
            ("National Mechanism for the Prevention of Torture of Paraguay", "3", "25", "the persistent abuse of pretrial detention; overcrowding; maximum security regimes that constitute torture; corruption and control of prisons by criminal groups"),
        ],
    ),
    "Human trafficking & contemporary forms of slavery": (
        B, "Combat trafficking in persons",
        "Paraguay implemented a National Plan to Prevent and Combat Trafficking "
        "2020-2024 (extended to 2025-2026), designated the Ministry of the "
        "Interior as lead agency with a dedicated fund (2025), opened the "
        "Nasaindy Protection Centre and maintains a specialised prosecution "
        "unit; the Committee on Migrant Workers finds standards still "
        "unsatisfactory, the ECLJ reports declining case numbers since 2019, and "
        "CRC calls for a national anti-trafficking strategy and elimination of "
        "criadazgo.",
        [
            ("Paraguay", "1", "78", "The implementation of the National Plan to Prevent and Combat Trafficking in Persons 2020-2024 consolidated the State's response ... It was therefore decided to extend the implementation of the Plan for the period 2025-2026"),
            ("Committee on Migrant Workers", "2", "26", "Paraguay had not yet achieved satisfactory standards in its fight against trafficking in persons and that children, especially those living on the street in the tri-border area, continued to be subjected to exploitation"),
            ("European Centre for Law and Justice", "3", "34", "the number of human trafficking cases that opened every year had decreased since 2019 due to corruption, impunity, lack of resources and inadequate victim support"),
        ],
    ),
    "Sexual & reproductive health and rights": (
        C, "Sexual and reproductive health; decriminalise abortion",
        "Paraguay adopted a National Sexual and Reproductive Health Plan "
        "2024-2030 and a Plan to Reduce Maternal Mortality, but abortion remains "
        "criminalised except where life or health is at risk with no clear "
        "protocol (4,691 registered abortions in 2024; 19 maternal deaths by "
        "June 2025), the Ministry of Education restricts age-appropriate "
        "sexuality education (Resolution 933/2023), and CRC recommends "
        "decriminalisation and mandatory comprehensive sexuality education.",
        [
            ("Committee on the Rights of the Child", "2", "40", "repealing resolution No. 933/2023 of the Ministry of Education and Sciences ... decriminalizing abortion in all circumstances and ensuring access to safe, timely and quality abortion and post-abortion care services"),
            ("Joint Submission 13", "3", "39", "In 2024, the Ministry of Health registered 4,691 abortions and, as of June 2025, 19 women had died. Under current legislation, women were forced to seek clandestine abortions"),
            ("Paraguay", "1", "44", "The National Sexual and Reproductive Health Plan 2024-2030 promotes equitable and inclusive policies to improve access to, and the quality of, care"),
        ],
    ),
    "Participation of women in political & public life": (
        C, "Women's political participation; parity law",
        "Paraguay runs training academies and an Observatory for Women's "
        "Political Participation, but women held only about 23 per cent of "
        "Congress in 2023, the 'democratic parity' bill has not been adopted, "
        "and the country team notes women's representation in governance remains "
        "limited.",
        [
            ("Joint Submission 12", "3", "31", "women accounted for only 23.2% of members of Congress and recommended the adoption of the bill on democratic parity, in accordance with the Constitution"),
            ("Paraguay", "1", "102", "women accounting for an average of 22.6% of the legislature in 2023 ... the State recognizes that challenges remain"),
        ],
    ),
    "Indigenous peoples": (
        B, "Indigenous land rights, consultation and services",
        "Paraguay has a National Plan for Indigenous Peoples 2020-2030, carried "
        "out 637 consultation processes (2022-2025), acquired 3,115 ha for "
        "communities and complied with three Inter-American Court "
        "land-restitution judgments; the Special Rapporteur, the country team "
        "and stakeholders report 66 per cent of Indigenous people in poverty, "
        "stalled land regularisation, rising forced evictions, an under-funded "
        "plan and a non-binding free, prior and informed consent protocol.",
        [
            ("Paraguay", "1", "146", "The National Plan for Indigenous Peoples 2020-2030 is in force ... Between 2022 and 2025, 637 consultation processes were carried out"),
            ("United Nations country team", "2", "66", "66.2% of members of Indigenous Peoples lived in poverty while 34.4% lived in extreme poverty, these figures being three times the national average"),
            ("Special Rapporteur on minority issues", "2", "68", "Indigenous Peoples' lands were not adequately protected, and noted an increase in forced evictions affecting Indigenous Peoples"),
        ],
    ),
    "Human rights defenders": (
        C, "Protect human rights defenders and journalists",
        "A bill to protect journalists and human rights defenders - required by "
        "an Inter-American Court ruling - has been pending in Congress since "
        "2021 with no progress; the country team and civil society report "
        "continuing attacks, reprisals and criminalisation of defenders and "
        "impunity for most murders of journalists.",
        [
            ("United Nations country team", "2", "23", "the bill presented for this purpose had not made any progress through the parliament since 2021 ... the majority of murders of journalists remained unpunished"),
            ("Paraguay", "1", "89", "a bill on the protection of journalists and human rights defenders, which, after being studied in committees, was referred back to the Senate for detailed analysis"),
        ],
    ),
    "Human rights & poverty": (
        B, "Reduce poverty and inequality",
        "Monetary poverty fell from about 26 per cent to 20 per cent between "
        "2021 and 2024 and Paraguay implements the Naime Poraveta Poverty "
        "Reduction Plan 2023-2030, the Tekopora cash-transfer programme and a "
        "universal old-age pension (Act No. 7322/2024, 340,203 beneficiaries); "
        "CRC and stakeholders report large numbers of children in poverty, "
        "sharp rural-urban and Indigenous disparities and high land "
        "concentration.",
        [
            ("Paraguay", "1", "18", "Between 2021 and 2024, the monetary poverty rate in Paraguay fell from approximately 26% to 20% of the population, reaching one of the lowest levels ever recorded"),
            ("Paraguay", "1", "26", "Act No. 7322/2024, which establishes the universal pension for older adults ... currently benefits 340,203 people"),
            ("Committee on the Rights of the Child", "2", "33", "the large number of children living in poverty and the regional disparities in access to rights"),
        ],
    ),
    "Right to an adequate standard of living": (
        B, "Adequate standard of living; land; housing",
        "Paraguay runs the Tekoha land-legalisation and Che Roga Pora housing "
        "programmes and reduced multidimensional poverty, but the Committee on "
        "the Rights of the Child records many children without adequate housing, "
        "water and sanitation, and civil society reports high land concentration "
        "and criminalisation of campesino activism.",
        [
            ("Committee on the Rights of the Child", "2", "33", "strengthen measures to end child poverty and ensure the right of all children to an adequate standard of living, including their access to adequate housing, water and sanitation"),
            ("Joint Submission 3", "3", "37", "Paraguay was marked by a high concentration of land ownership, low levels of public investment in the rural sector and the increasing criminalization of campesino activism"),
        ],
    ),
    "Right to social security": (
        A, "Extend social protection coverage",
        "Paraguay enacted a universal old-age pension (Act No. 7322/2024) "
        "reaching 340,203 people and runs the Tekopora conditional cash-transfer "
        "programme for 573,478 people; CRC still recommends expanding child-grant "
        "coverage and improving inter-agency coordination.",
        [
            ("Paraguay", "1", "26", "Act No. 7322/2024, which establishes the universal pension for older adults, provides for the granting of a monthly pension of no less than 25% of the current legal minimum wage ... It currently benefits 340,203 people"),
            ("Committee on the Rights of the Child", "2", "32", "increase budget allocations for social protection programmes affecting children ... expanding coverage of the child grant programme"),
        ],
    ),
    "Persons with disabilities: independence, inclusion": (
        B, "Align disability law and policy with the CRPD",
        "Paraguay implements the National Action Plan for the Rights of Persons "
        "with Disabilities 2015-2030, modernised disability certification and "
        "strengthened the National Commission; CRPD reports limited "
        "implementation of accessibility Act No. 4934/13, involuntary "
        "psychiatric treatment, a persisting medical model in Act No. 7018/2022 "
        "and under-resourced institutions.",
        [
            ("Paraguay", "1", "161", "The National Action Plan for the Rights of Persons with Disabilities 2015-2030 is currently being implemented. Furthermore, the National Commission on the Rights of Persons with Disabilities was strengthened"),
            ("Committee on the Rights of Persons with Disabilities", "2", "62", "little progress made in implementing Act No. 4934/13 on accessibility"),
            ("Committee on the Rights of Persons with Disabilities", "2", "19", "the involuntary treatment to which persons with disabilities were subjected at the psychiatric hospital"),
        ],
    ),
    "Persons with disabilities: definition, general principles": (
        B, "Rights of persons with disabilities",
        "The National Action Plan 2015-2030 is being implemented and disability "
        "certification digitalised, but CRPD reports the accessibility law is "
        "barely implemented, involuntary treatment continues and Act 7018/2022 "
        "keeps a medical model of disability.",
        [
            ("Committee on the Rights of Persons with Disabilities", "2", "41", "the persistence of the medical model of disability in Act No. 7018/2022"),
            ("Paraguay", "1", "166", "The disability certification process has been modernized, migrating to a digital system"),
        ],
    ),
    "Children: definition": (
        B, "Child protection; violence against children; criadazgo",
        "Paraguay runs the 'Seeds of the Future' early-childhood programme, the "
        "Abrazo child-labour programme, a National Registry of Sex Offenders and "
        "a Guardian Families alternative-care policy, but CRC reports high rates "
        "of missing children and child sexual abuse, and Congress rejected a "
        "2024 bill to criminalise criadazgo (unpaid domestic child servitude).",
        [
            ("Paraguay", "1", "142", "Although the bill presented in 2024 [to eradicate criadazgo] was not passed, the National Commission for the Eradication of Child Labour ... plans to resume the legislative process"),
            ("Committee on the Rights of the Child", "2", "57", "high rate of child sexual abuse, in particular of girls and Indigenous children, both online and in the context of tourism"),
        ],
    ),
    "Children: juvenile justice": (
        C, "Juvenile justice; restorative measures",
        "Paraguay operates a restorative educational-support model and "
        "non-custodial protocols in juvenile centres, but the National "
        "Mechanism for the Prevention of Torture and JS11 report harsher "
        "penalties in the juvenile system and pending bills to lower the age of "
        "criminal responsibility.",
        [
            ("Joint Submission 11", "3", "26", "penalties were becoming harsher in the juvenile justice system and recommended vetoing bills that would lower the age of criminal responsibility and/or increase penalties for adolescents"),
            ("Paraguay", "1", "73", "The Adolescent Offenders Welfare Service has an educational support model, based on a restorative and interdisciplinary approach"),
        ],
    ),
    "Prohibition of torture & ill-treatment (including cruel, inhuman or degrading treatment)": (
        B, "Prevent torture; investigate ill-treatment",
        "Paraguay approved 2023-2024 protocols for monitoring prisons and "
        "recording torture allegations, but the National Mechanism for the "
        "Prevention of Torture reports maximum-security regimes that constitute "
        "torture, prolonged detention in inhumane conditions and torture cases "
        "with no charges brought, and CRC records torture and ill-treatment of "
        "children in police stations.",
        [
            ("National Mechanism for the Prevention of Torture of Paraguay", "3", "25", "prolonged periods of detention in inhumane conditions and cases of torture for which no charges were brought"),
            ("Committee on the Rights of the Child", "2", "16", "cases of torture or ill-treatment of children in police stations and centres of deprivation of liberty"),
        ],
    ),
    "Right to life": (
        C, "Regulate use of force; accountability for killings",
        "The Committee on the Rights of the Child found Paraguay accountable for "
        "grave violations over the killing of two 11-year-old girls in a 2020 "
        "Joint Task Force operation and called for the truth to be established "
        "and the law-enforcement framework strengthened; no responsive legal "
        "reform is reported.",
        [
            ("Committee on the Rights of the Child", "2", "15", "Paraguay was accountable for grave human rights violations concerning the killings of two 11-year-old girls during an operation conducted by the Joint Task Force of Paraguay ... take further steps to establish the truth"),
        ],
    ),
    "Migrants": (
        C, "Adopt and implement a rights-compliant migration law",
        "A migration bill has been pending for more than five years; the "
        "Committee on Migrant Workers urges its adoption in line with the "
        "ICRMW, regular regularisation mechanisms, alternatives to "
        "administrative detention, and repeal of Emergency Act No. 6524/2020 "
        "excluding migrants and refugees from informal-sector aid.",
        [
            ("Committee on Migrant Workers", "2", "6", "it was concerned that the [migration] bill was still pending more than five years after it had been introduced ... urged Paraguay to adopt and publish the migration law"),
            ("Committee on Migrant Workers", "2", "75", "Emergency Act No. 6524/2020, which made migrants and refugees ineligible for the aid offered to workers in the informal sector"),
        ],
    ),
    "Cultural rights": (
        B, "Protect Indigenous languages and bilingualism",
        "Paraguay adopted Act No. 7008/22 creating a Commission for Indigenous "
        "Languages, but the Special Rapporteur on minority issues reports six of "
        "the 19 Indigenous languages are endangered and calls for legislation "
        "ensuring effective Spanish-Guarani bilingualism in State institutions "
        "and official documents.",
        [
            ("Special Rapporteur on minority issues", "2", "47", "among the 19 Indigenous languages spoken in Paraguay, six of those languages were in danger of extinction ... enacting new legislation to ensure equal and effective bilingualism"),
            ("Paraguay", "1", "147", "Act No. 7008/22 was adopted, establishing the National Commission for the Strengthening, Promotion and Appreciation of Indigenous Languages in Paraguay"),
        ],
    ),
    "Racial discrimination": (
        B, "Combat discrimination against people of African descent",
        "Paraguay enacted Act No. 6940 (2022) establishing mechanisms to prevent "
        "and punish racism against people of African descent and created a "
        "National Council, but the country team says implementation is still "
        "pending and the Special Rapporteur reports the Afro-descendant minority "
        "remains largely invisible in official data.",
        [
            ("Paraguay", "1", "159", "In 2022, Act No. 6940 was enacted, establishing mechanisms and procedures to prevent and punish acts of racism and discrimination against people of African descent"),
            ("United Nations country team", "2", "71", "the adoption of Act No. 6940 ... constituted partial progress and that its implementation was still pending"),
        ],
    ),
    "Human rights & the environment": (
        C, "Protect against toxics; environmental justice",
        "Paraguay reports steps in hazardous-waste management and a 2022 Climate "
        "Change Adaptation Plan, but the Special Rapporteur on hazardous "
        "substances reports rural communities and Indigenous Peoples face an "
        "alarming level of exposure to hazardous pesticides, most environmental "
        "laws are not observed, and Paraguay has not complied with Human Rights "
        "Committee Views in the Campo Agua'e and Colonia Yeruti cases.",
        [
            ("Special Rapporteur on hazardous substances and wastes", "2", "49", "Rural communities and Indigenous Peoples faced an alarming level of exposure to toxic substances, particularly hazardous pesticides and most of the country's environmental laws were not observed"),
            ("Special Rapporteur on hazardous substances and wastes; United Nations country team", "2", "3", "recommended that Paraguay fully comply with the Views of the Human Rights Committee in the cases relating to Campo Agua' and Colonia Yeruti"),
        ],
    ),
    "Human rights & climate change": (
        B, "Climate change adaptation",
        "Paraguay operates a National Commission on Climate Change and is "
        "implementing its 2022 National Climate Change Adaptation Plan and "
        "updating its nationally determined contribution; civil society reports "
        "insufficient action on deforestation from agricultural expansion.",
        [
            ("Paraguay", "1", "95", "the National Climate Change Adaptation Plan, approved in 2022, is being implemented ... incorporates climate adaptation measures into national and local planning instruments"),
            ("Joint Submission 3", "3", "44", "Paraguay had taken insufficient action to tackle the challenges of climate change, particularly with regard to halting deforestation caused by the expansion of monoculture farming"),
        ],
    ),
    "National Human Rights Action Plans (or specific areas) / implementation plans": (
        B, "Implement the National Human Rights Plan",
        "Paraguay approved the fourth Action Plan of the Human Rights Network "
        "(2024-2028) and coordinates implementation through the Ministry of "
        "Justice and the SIMORE Plus system; civil society reports the action "
        "plans were prepared without broad participation and there is no "
        "comprehensive new national plan.",
        [
            ("Paraguay", "1", "9", "the fourth Action Plan of the Human Rights Network (2024-2028) was approved in 2024 with the strategic aim of promoting inter-agency and intersectoral coordination to implement the National Human Rights Plan"),
            ("Joint Submission 5", "3", "17", "authorities had prepared the III Action Plan 2021-2023 without broad citizen participation and so far, there was no evidence of a comprehensive new national plan"),
        ],
    ),
    "Cooperation & Follow up with Special Procedures": (
        B, "Cooperate with UN and inter-American mechanisms",
        "Paraguay maintains an open and standing invitation to special "
        "procedures, hosted two Special Rapporteur visits in 2022, is up to date "
        "with treaty-body reporting, served on the Human Rights Council "
        "(2022-2024) and runs the SIMORE Plus follow-up system; civil society "
        "notes reparations ordered by the Human Rights Committee in several "
        "cases remain unpaid.",
        [
            ("Paraguay", "1", "10", "official visits were received in 2022 from the Special Rapporteur on ... hazardous substances and wastes and the Special Rapporteur on minority issues"),
            ("Joint Submission 3", "3", "16", "the failure to provide the reparations ordered by the Human Rights Committee in a number of cases"),
        ],
    ),
    "Cooperation with human rights mechanisms & requests for technical assistance": (
        B, "Cooperate with human rights mechanisms",
        "Paraguay is up to date with treaty-body reporting, submitted its UPR "
        "mid-term report and runs the SIMORE Plus implementation and follow-up "
        "system developed with OHCHR; several Human Rights Committee reparation "
        "orders remain unimplemented.",
        [
            ("Paraguay", "1", "11", "Paraguay is up to date with its reporting obligations to the treaty bodies"),
            ("Committee on Migrant Workers; Committee on the Rights of Persons with Disabilities", "2", "4", "acknowledged the SIMORE recommendations monitoring mechanism, as an outcome of a cooperation project between Paraguay and OHCHR"),
        ],
    ),
    "Labour rights and right to work": (
        B, "Decent work; formalisation; forced labour",
        "Paraguay adopted a National Employment Plan 2022-2026 and an Integrated "
        "Strategy for Employment Formalisation 2025-2028 and is developing "
        "National Strategies on Forced Labour and Child Labour 2026-2030; the "
        "country team recommends ratifying ILO Convention No. 190, and "
        "Indigenous domestic workers report abuse and exploitation.",
        [
            ("Paraguay", "1", "28", "The Integrated Strategy for Employment Formalization 2025-2028 was approved to address the significant challenges posed by informal employment"),
            ("United Nations country team", "2", "31", "recommended ratifying the Violence and Harassment Convention, 2019 (No. 190) ... of the International Labour Organization"),
        ],
    ),
    "Freedom of opinion and expression & access to information": (
        C, "Protect freedom of expression and journalists",
        "A bill to protect journalists has been pending since 2021; JS3 recorded "
        "122 attacks on journalists and two killings since the previous review "
        "(21 killed 1991-2025), and UNESCO recommends decriminalising "
        "defamation, which remains a criminal offence.",
        [
            ("Joint Submission 3", "3", "28", "recorded 122 cases of violence directed at journalists by the authorities and criminal organizations and two journalists killed since the previous universal periodic review"),
            ("UNESCO", "2", "25", "recommended decriminalizing defamation and placing it within civil defamation legislation that was in accordance with international standards"),
        ],
    ),
    "Right to peaceful assembly": (
        C, "Guarantee the right to peaceful assembly",
        "JS5 reports Paraguay supported but did not implement a recommendation "
        "on peaceful assembly, that the 1997 'Marchodromo' Law grants "
        "authorities excessive discretion to restrict demonstrations, and that "
        "September 2025 protests were monitored without judicial authorisation "
        "and violently suppressed.",
        [
            ("Joint Submission 5", "3", "30", "Law No. 1.066/1997 (Marchodromo Law) proscribed time and place restrictions on demonstrations and the obligation to notify the police, granting authorities excessive discretion to restrict them"),
            ("Joint Submission 1", "3", "30", "during peaceful 'Gen Z' demonstrations in September 2025 authorities used open-source intelligence systems and cyber-patrol tools to monitor participants without judicial authorisation, and demonstrations were violently suppressed"),
        ],
    ),
    "Right to privacy": (
        C, "Regulate surveillance and data protection",
        "TEDIC and JS1 report Paraguay acquired surveillance tools without an "
        "adequate legal framework or independent oversight, and drone "
        "regulation is fragmented; no responsive framework has been adopted.",
        [
            ("TEDIC", "3", "32", "the lack of transparency of surveillance policies and practices, and that Paraguay had obtained tools to conduct surveillance without an appropriate legal framework"),
            ("Joint Submission 1", "3", "32", "the lack of independent oversight mechanisms in the acquisition and use of mass surveillance technologies, raising serious privacy-related concerns"),
        ],
    ),
    "Children: protection against exploitation, violence and abuse": (
        C, "Protect children from exploitation, violence and abuse",
        "Paraguay runs the Abrazo child-labour programme and a Comprehensive "
        "Care Programme for child victims, but CRC reports high rates of child "
        "sexual abuse and missing children and Congress rejected a 2024 bill to "
        "criminalise criadazgo.",
        [
            ("Committee on the Rights of the Child", "2", "57", "high rate of child sexual abuse, in particular of girls and Indigenous children, both online and in the context of tourism"),
            ("Committee on the Rights of the Child", "2", "28", "eliminate the practice of criadazgo (forced child servitude) and provide full protection to children who were victims"),
        ],
    ),
    "Right to participate in public affairs & right to vote": (
        C, "Political participation of women and Indigenous Peoples",
        "Women held only about 23 per cent of Congress in 2023 and the "
        "'democratic parity' bill is not adopted; the Human Rights Committee and "
        "country team also note very low Indigenous participation in political "
        "life and public administration.",
        [
            ("Joint Submission 12", "3", "31", "women accounted for only 23.2% of members of Congress and recommended the adoption of the bill on democratic parity"),
            ("Paraguay", "1", "148", "an inter-agency cooperation agreement between the High Court of Electoral Justice and the National Institute of Indigenous Affairs ... to guarantee the effective exercise of the civil and political rights of Indigenous communities"),
        ],
    ),
    "Discrimination against women": (
        B, "Combat discrimination against women",
        "Paraguay strengthened the Ministry for Women's budget, adopted the "
        "first Action Plan on Care 2025-2030, introduced gender-budgeting "
        "guidance and increased women's access to land titling and rural "
        "housing; the country team reports persistent gender norms restricting "
        "women's participation and only 13.4 per cent of titled land plots held "
        "by women.",
        [
            ("Paraguay", "1", "107", "a preferential interest rate of financing of 0% for women and 4% for men for the purchase of plots of land ... an increase in women's participation: from 35% to 46% in respect of land allocation"),
            ("United Nations country team", "2", "54", "the persistence of gender norms restricted their full participation in the labour market and society ... women owned only 13.4% of plots of land with firm titles"),
        ],
    ),
    "Advancement of women": (
        B, "Advance women's rights and empowerment",
        "Paraguay adopted the first Action Plan on Care 2025-2030, revived the "
        "Tripartite Commission on Equal Opportunities and expanded women's "
        "access to finance, land and training; women's representation in "
        "governance remains limited.",
        [
            ("Paraguay", "1", "106", "The approval of the first Action Plan on Care for 2025-2030 marked a fundamental milestone in the implementation of the National Care Policy"),
            ("United Nations country team", "2", "55", "women's representation in governance spaces remained limited"),
        ],
    ),
    "Sexual & gender-based violence": (
        B, "Prevent and address sexual and gender-based violence",
        "Paraguay declared a social emergency on violence against women and "
        "children (Act No. 7239/2024), runs the SOS Mujer hotline, shelters and "
        "femicide protocols, and made civil-servant training mandatory; "
        "prevalence and femicide remain very high.",
        [
            ("Paraguay", "1", "113", "supplemented by Act No. 7239/2024, declaring a social emergency in respect of violence against women, children and adolescents"),
            ("Amnesty International", "3", "45", "78.5% of women experienced gender-based violence and, in 2024, an average of 103 people per day submitted reports of domestic violence"),
        ],
    ),
    "Rights related to name, identity & nationality": (
        B, "Universal birth registration",
        "Paraguay's Civil Registry runs a single online birth-registration "
        "system with hospital offices in 21 locations, but CRPD reports a 30 per "
        "cent under-registration rate for births and CRC calls for free "
        "immediate registration for all children regardless of parents' "
        "immigration status.",
        [
            ("Committee on the Rights of Persons with Disabilities", "2", "79", "the 30 per cent underregistration rate for births ... step up the activities of the 'Right to an Identity' programme"),
            ("Paraguay", "1", "144", "the Directorate General of the Civil Registry implements a single register of persons that allows for the online registration of births and facilitates registration through offices established within hospitals"),
        ],
    ),
    "Rights related to marriage & family": (
        C, "End child and adolescent marriage",
        "The law still allows marriage from age 16 with court authorisation; CRC "
        "and UNESCO call for a minimum age of 18 without exception, and reform "
        "is only under consideration.",
        [
            ("Committee on the Rights of the Child; UNESCO", "2", "53", "amend the legislation to ensure that the minimum age of marriage was 18 years, without exception"),
            ("Paraguay", "1", "143", "A proposal for regulatory reform to eliminate exceptions to the minimum age for marriage ... is currently under consideration"),
        ],
    ),
    "Land & property rights": (
        B, "Indigenous and campesino land rights",
        "Paraguay acquired 3,115 ha for Indigenous communities (2020-2025) and "
        "settled three communities under Inter-American Court judgments, but the "
        "Special Rapporteur and civil society report inadequate protection of "
        "Indigenous lands, stalled restitution and rising forced evictions, and "
        "high concentration of agricultural land ownership.",
        [
            ("Special Rapporteur on minority issues", "2", "68", "Indigenous Peoples' lands were not adequately protected, and noted an increase in forced evictions affecting Indigenous Peoples"),
            ("Paraguay", "1", "149", "Between 2020 and 2025, the State acquired 3,115 ha for Indigenous communities"),
        ],
    ),
    "Good governance & corruption": (
        B, "Strengthen transparency and anti-corruption",
        "Paraguay approved a National Anti-Corruption Strategy (2023) and enacted "
        "Act No. 7389/2024 establishing a National System for Integrity, "
        "Transparency and the Prevention of Corruption with annual measurable "
        "agency goals; civil society reports the Anti-Corruption Commission "
        "remains under-resourced.",
        [
            ("Paraguay", "1", "58", "In 2023, the National Anti-Corruption Strategy was approved to strengthen transparency and integrity in the civil service"),
            ("Paraguay", "1", "59", "In 2024, Act No. 7389/2024 was enacted, establishing the National System for Integrity, Transparency and the Prevention of Corruption"),
        ],
    ),
    "Human rights education, trainings & awareness raising": (
        B, "Implement the National Plan for Human Rights Education",
        "The Ombudsman's Office and JS2 report the National Plan for Human "
        "Rights Education has been only partially and unevenly implemented, with "
        "gaps in budget, infrastructure and teacher training.",
        [
            ("Ombudsman's Office of Paraguay", "3", "10", "effectively implementing the National Plan for Human Rights Education, ensuring that it was allocated the necessary budget"),
            ("Joint Submission 2", "3", "43", "the implementation of the National Plan for Human Rights Education had been partial and uneven"),
        ],
    ),
    "Legal & institutional reform": (
        C, "Legal and institutional reform",
        "Key reforms sought - a comprehensive anti-discrimination law, a "
        "rights-compliant migration law, an 18-year minimum marriage age, "
        "criminalisation of criadazgo - remain unadopted.",
        [
            ("Special Rapporteur on minority issues; Committee on Migrant Workers", "2", "12", "Paraguay still had not adopted a law against all forms of discrimination, despite the numerous international recommendations"),
        ],
    ),
    "Access to justice & remedy": (
        C, "Access to justice and reparations",
        "The judicial system is described as slow and inefficient with most "
        "human-rights complaints uninvestigated, and civil society reports "
        "reparations ordered by the Human Rights Committee and the "
        "Inter-American Court in several cases remain unpaid.",
        [
            ("Special Rapporteur on hazardous substances and wastes", "2", "20", "the country's judicial system was slow and inefficient, with most reports of human rights violations not being investigated"),
            ("Joint Submission 3", "3", "16", "the failure to provide the reparations ordered by the Human Rights Committee in a number of cases"),
        ],
    ),
    "Safe drinking water & sanitation": (
        C, "Access to safe water and sanitation",
        "The Ombudsman's Office and country team report persistent violations of "
        "Indigenous Peoples' rights to drinking water and sanitation and gaps in "
        "rural areas; some progress is noted in the Inter-American Court "
        "communities.",
        [
            ("Ombudsman's Office of Paraguay", "3", "12", "the persistent violations of Indigenous Peoples' rights to land, drinking water and sanitation"),
        ],
    ),
    "National Preventive Mechanism (NPM)": (
        C, "Strengthen the National Preventive Mechanism against torture",
        "The National Mechanism for the Prevention of Torture reports that its "
        "budget has not been changed and that it lacks the resources to fulfil "
        "its mandate across the prison system.",
        [
            ("National Mechanism for the Prevention of Torture of Paraguay", "3", "25", "the failure to change the budget assigned to the National Mechanism for the Prevention of Torture; and the failure to professionalize prison staff"),
        ],
    ),
    "Right to development": (
        B, "National development planning",
        "Paraguay's National Development Plan 2050 and the Naime Poraveta "
        "Poverty Reduction Plan 2023-2030 guide long-term, people-centred "
        "planning with inter-agency monitoring.",
        [
            ("Paraguay", "1", "20", "The National Development Plan 2050 is the State's guiding instrument for long-term planning ... align public policies, investment and State actions with a vision of sustainable, inclusive and people-centred development"),
        ],
    ),
    "Persons with disabilities: protection against exploitation, violence and abuse": (
        C, "Protect persons with disabilities from violence and coercion",
        "CRPD is concerned about involuntary treatment, isolation and mechanical "
        "restraints against persons with disabilities in the psychiatric "
        "hospital and about insufficient measures against violence towards women "
        "with disabilities.",
        [
            ("Committee on the Rights of Persons with Disabilities", "2", "19", "explicitly prohibiting by law the use of isolation, mechanical restraints, forced medication, electroconvulsive therapy, confinement in individual cells and isolation rooms, and forced treatment in crisis situations"),
        ],
    ),
    "Enforced disappearances": (
        C, "Search for the disappeared; reparations for dictatorship crimes",
        "The Ombudsman's Office and JS3 report systematic impunity for crimes "
        "against humanity during the 1954-1989 dictatorship, defunding of the "
        "programme to search for disappeared persons, and delays and statute-of-"
        "limitations obstacles to civil reparation.",
        [
            ("Joint Submission 3", "3", "23", "the defunding of, and lack of government support for, the programme to search for and identify disappeared persons, the delays and red tape surrounding reparation measures and the statute of limitations applicable to civil compensation proceedings"),
            ("Ombudsman's Office of Paraguay", "3", "4", "strengthening the mechanism for compensating victims of human rights violations during the dictatorship"),
        ],
    ),
}

KEYWORDS = [
    (r"Act No\.? ?7363|Garrote|non-?profit organi[sz]ation|freedom of association|civic space", E,
     "Repeal the NGO oversight law (Act No. 7363/2024)",
     "Act No. 7363/2024 (the 'Garrote' Act), adopted in 2024, imposes vague and "
     "disproportionate requirements and penalties on non-profit organisations "
     "that restrict freedom of association; the Ombudsman's Office and multiple "
     "stakeholders call for its repeal - a regression.",
     [("Several stakeholders (OHCHR summary)", "3", "27", "Act No. 7363 (the Garrote Act), adopted in 2024, abusively restricted freedom of association with vague provisions and unclear penalties ... A number of communications recommended repealing Act No. 7363"),
      ("Ombudsman's Office of Paraguay", "3", "5", "Act No. 7363/64 on the Oversight, Transparency and Accountability of Non-profit Organizations ... imposed requirements and procedures that restricted the exercise of the right of association")]),
    (r"gender (theory|ideology|mainstreaming|perspective)|comprehensive sexuality education|Resolution (No\. )?933|decision No\. 29", E,
     "Repeal restrictions on gender and sexuality education",
     "The Ministry of Education adopted Resolution No. 933/2023 and decision "
     "No. 29.664 restricting the teaching of gender and age-appropriate sexual "
     "and reproductive health information in schools, and bills to ban gender "
     "mainstreaming and abolish the Ministry for Women are pending - regressive "
     "against recommendations to guarantee comprehensive sexuality education.",
     [("Committee on the Rights of the Child", "2", "40", "the prohibition by the Ministry of Education and Science on disseminating age-appropriate information on sexual and reproductive health in educational institutions"),
      ("United Nations country team", "2", "73", "repealing decision No. 29.664 of the Ministry of Education and Science, which prohibited the teaching of topics related to gender theory in schools")]),
    (r"abortion|termination of pregnancy|voluntary interruption", C,
     "Decriminalise abortion and ensure access to safe abortion",
     "Abortion remains criminalised except where life or health is at risk, "
     "with no clear protocol; CRC recommends decriminalisation in all "
     "circumstances, and stakeholders report 19 maternal deaths by June 2025 "
     "and women forced into clandestine abortions.",
     [("Committee on the Rights of the Child", "2", "40", "decriminalizing abortion in all circumstances and ensuring access to safe, timely and quality abortion and post-abortion care services"),
      ("Joint Submission 13", "3", "39", "as of June 2025, 19 women had died. Under current legislation, women were forced to seek clandestine abortions")]),
    (r"criadazgo|domestic (child )?servitude|unpaid domestic (work|labour)", C,
     "Prohibit and eradicate criadazgo (child servitude)",
     "Criadazgo (unpaid domestic child servitude) persists; a 2024 bill to "
     "criminalise it was rejected by the National Congress, though the "
     "Government plans to resume the legislative process.",
     [("Committee on the Rights of the Child", "2", "28", "eliminate the practice of criadazgo (forced child servitude) and provide full protection to children who were victims"),
      ("Joint Submission 6", "3", "51", "the National Congress had rejected a bill aimed at protecting children against criadazgo on the grounds that it was part of Paraguayan culture")]),
    (r"minimum age (of|for) marriage|child marriage|early marriage|marriage of (adolescents|children)|child union", C,
     "Set the minimum age of marriage at 18 without exception",
     "The law still allows marriage from age 16 with court authorisation; CRC "
     "and UNESCO call for a minimum age of 18 without exception, and a "
     "regulatory reform is only 'under consideration'.",
     [("Committee on the Rights of the Child; UNESCO", "2", "53", "amend the legislation to ensure that the minimum age of marriage was 18 years, without exception"),
      ("Paraguay", "1", "143", "A proposal for regulatory reform to eliminate exceptions to the minimum age for marriage and impose a total ban on marriage between adolescents is currently under consideration")]),
    (r"Optional Protocol to the International Covenant on Economic|OP-ICESCR|OP-CESCR", C,
     "Ratify the Optional Protocol to the ICESCR",
     "Paraguay has not ratified OP-ICESCR; the National Report says it remains "
     "under 'internal analysis'.",
     [("Special Rapporteur on minority issues; United Nations country team; UNESCO", "2", "2", "recommended that Paraguay ratify the Optional Protocol to the International Covenant on Economic, Social and Cultural Rights"),
      ("Paraguay", "1", "8", "the possible ratification of the Optional Protocol to the International Covenant on Economic, Social and Cultural Rights continues to be the subject of internal analysis")]),
    (r"Escaz|Regional Agreement on Access to Information.{0,60}Environmental", C,
     "Ratify the Escazu Agreement",
     "Paraguay has not ratified the Escazu Agreement; the Government says it "
     "will 'move forward with a process of analysis and dialogue'.",
     [("Amnesty International; Joint Submission 3", "3", "13", "the failure to ratify the Regional Agreement on Access to Information, Public Participation and Justice in Environmental Matters in Latin America and the Caribbean (Escazu Agreement)")]),
    (r"comprehensive.{0,25}(law|legislation).{0,25}discriminat|law against (all forms of )?discriminat|anti-?discrimination (law|legislation)", C,
     "Adopt a comprehensive anti-discrimination law",
     "Paraguay still has not adopted a comprehensive law against all forms of "
     "discrimination despite recommendations across cycles.",
     [("Special Rapporteur on minority issues; Committee on Migrant Workers", "2", "12", "Paraguay still had not adopted a law against all forms of discrimination, despite the numerous international recommendations"),
      ("Joint Submission 12", "3", "20", "adopting legislation prohibiting all forms of discrimination, including on the grounds of gender, sexual orientation, gender identity and expression, race, ethnicity, disability and age")]),
    (r"sexual orientation|gender identity|\bLGBT|lesbian, gay|transgender|same-sex|self-perceived gender", C,
     "Protect LGBTIQ+ persons from discrimination",
     "There is no anti-discrimination legislation protecting LGBTIQ+ people, no "
     "legal recognition of same-sex civil unions or of self-perceived gender "
     "identity, and stakeholders and Amnesty International report rising hate "
     "speech and violence with impunity.",
     [("Amnesty International", "2", "21", "impunity for hate speech and the promotion of discrimination against lesbian, gay, bisexual, transgender and intersex persons"),
      ("REPAR+", "3", "61", "the situation of the LGBTQ+ population in Paraguay remained marked by the absence of legislation, by institutional and social discrimination, and the rise of hate speech")]),
    (r"journalist|human rights defender|protection mechanism for", C,
     "Adopt a protection mechanism for journalists and human rights defenders",
     "A bill to protect journalists and human rights defenders, required by an "
     "Inter-American Court ruling, has been pending in Congress since 2021; "
     "attacks and criminalisation of defenders continue and most murders of "
     "journalists remain unpunished.",
     [("United Nations country team", "2", "23", "although the Inter-American Court of Human Rights had issued a ruling ordering the establishment of a mechanism for protecting journalists and defenders, the bill presented for this purpose had not made any progress through the parliament since 2021"),
      ("Amnesty International", "3", "29", "regretted the lack of progress made towards adopting the bill to protect journalists and human rights defenders")]),
    (r"Ombudsman|national human rights institution|Paris Principles|Defensor", B,
     "Strengthen the Ombudsman (national human rights institution)",
     "The Ombudsman's Office regained GANHRI category A status in 2025 and its "
     "budget rose, but it remains among the lowest-funded agencies and its "
     "selection process is not regulated or merit-based.",
     [("Paraguay", "1", "17", "The Office of the Ombudsman was re-accredited with category A status ... officially granted in 2025 and certifies that the Office is in full compliance with the Paris Principles"),
      ("United Nations country team", "2", "7", "The budget allocated to the institution had been increased, but it continued to have one of the lowest budgets of any agency")]),
    (r"Inter-American Court|Yakye Axa|Sawhoyamaxa|Xakmok|X.kmok|land restitution|ancestral (land|territ)|restitution of (indigenous )?(land|territ)", B,
     "Comply with Inter-American Court land-restitution judgments",
     "Paraguay has restored land and provided services to the Yakye Axa, "
     "Sawhoyamaxa and Xakmok Kasek communities in compliance with "
     "Inter-American Court judgments, but broader Indigenous land "
     "regularisation and restitution remain stalled, with rising forced "
     "evictions.",
     [("Paraguay", "1", "156", "The Yakye Axa community has been definitively settled on the 11,312 ha restored to it ... the Inter-American Court of Human Rights deemed the work to be finished in 2025"),
      ("Joint Submission 3", "3", "57", "little progress had been made towards the restitution of Indigenous territories")]),
]


if __name__ == "__main__":
    run("paraguay", clusters=CLUSTERS, keywords=KEYWORDS)
