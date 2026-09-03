"""Human Rights Committee follow-up gradings for the four assessed countries.

These are the Committee's *own* A-E gradings of the priority ("follow-up")
paragraphs of each country's Concluding Observations, taken verbatim in substance
from the Special Rapporteur's evaluation documents:

  * United States  CCPR/C/USA/CO/4 (110th session, 2014) -> CCPR/C/114/2, first
                   follow-up round, adopted July 2015
  * Denmark        CCPR/C/DNK/CO/6 (117th session, 2016) -> CCPR/C/125/2/Add.4,
                   adopted 125th session, March 2019
  * Namibia        CCPR/C/NAM/CO/2 (116th session, 2016) -> CCPR/C/126/2/Add.4,
                   adopted 126th session, July 2019
  * Paraguay       CCPR/C/PRY/CO/4 (126th session, 2019) -> CCPR/C/140/2/Add.2,
                   adopted 140th session, March 2024

Each limb carries the Committee's grade and a short verbatim excerpt from its
evaluation. Grade meanings: A largely satisfactory; B partially satisfactory,
more needed; C not satisfactory / does not implement; D no cooperation /
no information; E contrary to, or rejection of, the recommendation.
"""

HRC = {
    "USA": {
        "co_symbol": "CCPR/C/USA/CO/4",
        "session": "110th session (March 2014)",
        "assessment_symbol": "CCPR/C/114/2",
        "assessment_date": "adopted July 2015",
        "round": "First follow-up round. The Committee assessed the United States "
                 "across further rounds (114th, 116th, 120th sessions); the grades "
                 "below are the first-round evaluation.",
        "paragraphs": [
            {
                "para": "5",
                "title": "Accountability for unlawful killing, torture and "
                         "enforced disappearance",
                "recommendation": "Ensure that all cases of unlawful killing, "
                    "torture or other ill-treatment, unlawful detention or "
                    "enforced disappearance are effectively, independently and "
                    "impartially investigated, perpetrators (including persons in "
                    "positions of command) prosecuted and sanctioned, and victims "
                    "provided with effective remedies; establish the "
                    "responsibility of those who provided legal pretexts for "
                    "manifestly illegal behaviour; incorporate the doctrine of "
                    "“command responsibility”; and declassify and "
                    "publish the Senate Select Committee on Intelligence report "
                    "on the CIA secret detention programme.",
                "limbs": [
                    {"limb": "(a) investigations, prosecutions and remedies",
                     "grade": "B",
                     "eval": "While noting, with appreciation, the recent "
                             "prosecutions of law-enforcement officials and the "
                             "conviction of four Blackwater USA contractors, the "
                             "Committee requires information on investigations, "
                             "prosecutions or convictions of Government personnel "
                             "in positions of command."},
                    {"limb": "(b) responsibility for legal pretexts",
                     "grade": "C",
                     "eval": "The Committee requires information on measures "
                             "taken to establish the responsibility of those who "
                             "provided legal pretexts for manifestly illegal "
                             "behaviour. It reiterates its recommendations."},
                    {"limb": "(c) doctrine of command responsibility",
                     "grade": "C",
                     "eval": "The Committee regrets that no action has been "
                             "taken to incorporate into its criminal law the "
                             "doctrine of command responsibility for crimes "
                             "under international law."},
                    {"limb": "(d) declassify the SSCI CIA report",
                     "grade": "B",
                     "eval": "The Committee welcomes the declassification and "
                             "release of over 500 pages of the report but is "
                             "concerned that over 6,000 pages remain classified "
                             "and that the Department of Justice does not plan to "
                             "reopen investigations."},
                ],
            },
            {
                "para": "10",
                "title": "Right to life — gun violence and “Stand Your "
                         "Ground” laws",
                "recommendation": "Effectively curb gun violence, including "
                    "legislation requiring background checks for all private "
                    "firearm transfers and strict enforcement of the Lautenberg "
                    "Amendment; and review the Stand Your Ground laws to remove "
                    "far-reaching immunity and ensure necessity and "
                    "proportionality in the use of deadly force.",
                "limbs": [
                    {"limb": "(a) curb gun violence; background checks",
                     "grade": "C",
                     "eval": "While welcoming the Supreme Court decision "
                             "upholding the federal domestic-violence firearms "
                             "ban, the Committee requests information on new "
                             "measures taken since the review and repeats its "
                             "recommendations."},
                    {"limb": "(b) review Stand Your Ground laws",
                     "grade": "C",
                     "eval": "The Committee requests information on measures "
                             "taken to implement the recommendation and is "
                             "concerned that the immunity provided by "
                             "stand-your-ground laws has, in some areas, "
                             "expanded."},
                ],
            },
            {
                "para": "21",
                "title": "Guantánamo Bay — transfer, trial or release, "
                         "and closure",
                "recommendation": "Expedite the transfer of detainees designated "
                    "for transfer and the periodic-review process; ensure trial "
                    "or immediate release and closure of the Guantánamo Bay "
                    "facility; end administrative detention without charge or "
                    "trial; and deal with criminal cases through the ordinary "
                    "criminal justice system rather than military commissions.",
                "limbs": [
                    {"limb": "(a) expedite transfers and review",
                     "grade": "B",
                     "eval": "The Committee welcomes steps taken to expedite the "
                             "review and transfer of detainees but is concerned "
                             "that, at the current rate, review hearings would "
                             "not be completed for all detainees until 2020. "
                             "Updated statistical data is required."},
                    {"limb": "(b) end administrative detention; no military "
                             "commissions",
                     "grade": "C",
                     "eval": "The Committee regrets that persons continue to be "
                             "held without charge or trial, in many cases for "
                             "over a decade, and regrets the plans to continue "
                             "prosecution by military commission, which is "
                             "contrary to its recommendations."},
                ],
            },
            {
                "para": "22",
                "title": "Surveillance and the right to privacy (article 17)",
                "recommendation": "Bring surveillance activities within and "
                    "outside the United States into conformity with article 17 "
                    "(legality, proportionality, necessity, regardless of "
                    "nationality or location); ensure interference is authorised "
                    "by publicly accessible, precise law with effective "
                    "safeguards; reform oversight to include judicial "
                    "involvement; refrain from mandatory third-party data "
                    "retention; and ensure effective remedies for abuse.",
                "limbs": [
                    {"limb": "(a)–(b) conformity with article 17; law-based "
                             "safeguards",
                     "grade": "B",
                     "eval": "While the Committee welcomes the administrative "
                             "measures taken, it requires information on "
                             "legislative measures to ensure the safeguards are "
                             "provided for by law, and is concerned the "
                             "administrative measures do not adequately protect "
                             "article 17 rights."},
                    {"limb": "(c) reform oversight; judicial involvement",
                     "grade": "C",
                     "eval": "No measures appear to have been taken since March "
                             "2014 to provide for judicial involvement in the "
                             "authorization and monitoring of surveillance or to "
                             "establish strong and independent oversight."},
                    {"limb": "(d) no mandatory third-party data retention",
                     "grade": "C",
                     "eval": "The Committee requires information on measures "
                             "taken to stop the practice of mandatory retention "
                             "of data by third parties."},
                    {"limb": "(e) effective remedies for abuse",
                     "grade": "D",
                     "eval": "No information was provided by the State party on "
                             "access to remedies for persons affected in cases "
                             "of abuse."},
                    {"limb": "extraterritorial surveillance",
                     "grade": "C",
                     "eval": "The Committee notes that the State party has not "
                             "responded with regard to surveillance acts outside "
                             "the United States and asks for more information."},
                ],
            },
        ],
    },
    "DNK": {
        "co_symbol": "CCPR/C/DNK/CO/6",
        "session": "117th session (2016)",
        "assessment_symbol": "CCPR/C/125/2/Add.4",
        "assessment_date": "adopted 125th session, March 2019",
        "round": "Single follow-up round; procedure discontinued with outstanding "
                 "points folded into the list of issues for the seventh report.",
        "paragraphs": [
            {
                "para": "20",
                "title": "Domestic violence",
                "recommendation": "Continue efforts to combat domestic violence "
                    "effectively — effective reporting, investigations, "
                    "prosecutions and sanctions; uniform enforcement of "
                    "guidelines across all police districts; continued training "
                    "of all professionals involved.",
                "limbs": [
                    {"limb": "whole paragraph", "grade": "A",
                     "eval": "The Committee welcomes the legislative and policy "
                             "measures taken in Denmark, Greenland and the Faroe "
                             "Islands — including the national unit to "
                             "combat violence in family and intimate relations "
                             "(operational 1 October 2017), the extension of the "
                             "restraining-order Act to Greenland, and the Faroese "
                             "Criminal Code amendments — and requires "
                             "further information on their practical impact."},
                ],
            },
            {
                "para": "24",
                "title": "Solitary confinement",
                "recommendation": "Bring law and practice on solitary confinement "
                    "into line with the Nelson Mandela Rules by abolishing "
                    "solitary confinement of minors and reducing the total "
                    "permissible length for remand detainees; regularly evaluate "
                    "its effects and develop alternatives.",
                "limbs": [
                    {"limb": "whole paragraph", "grade": "C",
                     "eval": "While taking note of the extensive information and "
                             "monitoring efforts, the Committee regrets that the "
                             "State party neither abolished solitary confinement "
                             "for minors nor reduced the total permissible "
                             "length for remand detainees. It reiterates its "
                             "recommendations."},
                ],
            },
            {
                "para": "32",
                "title": "Rights of migrants, refugees and asylum seekers",
                "recommendation": "Ensure returns and expulsions afford "
                    "guarantees of non-refoulement; ensure detention is "
                    "reasonable, necessary and proportionate with alternatives "
                    "used in practice; consider reducing the length of detention "
                    "and improve conditions at Vridsløselille; repeal the "
                    "November 2015 Aliens Act amendment on judicial review; and "
                    "repeal the amendment on confiscation of asylum seekers' "
                    "assets.",
                "limbs": [
                    {"limb": "(a) non-refoulement guarantees", "grade": "B",
                     "eval": "The Committee takes note of the information on the "
                             "asylum procedure and respect for non-refoulement "
                             "and requires additional information, including on "
                             "identification of torture victims among asylum "
                             "seekers."},
                    {"limb": "(b) detention necessary and proportionate; "
                             "alternatives", "grade": "B",
                     "eval": "The Committee welcomes that detention is always to "
                             "be necessary and proportionate following an "
                             "individual examination, but notes the limited "
                             "information on alternatives to detention in "
                             "practice."},
                    {"limb": "(c) reduce length; Vridsløselille conditions",
                     "grade": "B",
                     "eval": "The maximum period of detention remains unchanged "
                             "and the Committee requires information on "
                             "consideration given to reducing it; it appreciates "
                             "that conditions at Vridsløselille have "
                             "improved since autumn 2016."},
                    {"limb": "(d) repeal the November 2015 judicial-review "
                             "amendment (§37k)", "grade": "C",
                     "eval": "The Committee regrets that paragraph 37 (k) of the "
                             "Aliens Act has not been repealed and reiterates "
                             "its recommendation."},
                    {"limb": "(e) repeal the asset-confiscation amendment",
                     "grade": "E",
                     "eval": "The Committee regrets that the State party did not "
                             "implement the recommendation to repeal the "
                             "amendment relating to the confiscation of asylum "
                             "seekers' assets."},
                ],
            },
        ],
    },
    "NAM": {
        "co_symbol": "CCPR/C/NAM/CO/2",
        "session": "116th session (March 2016)",
        "assessment_symbol": "CCPR/C/126/2/Add.4",
        "assessment_date": "adopted 126th session, July 2019",
        "round": "Single follow-up round; no civil-society submission was "
                 "received. Procedure discontinued.",
        "paragraphs": [
            {
                "para": "10",
                "title": "Non-discrimination",
                "recommendation": "Repeal race-discriminatory laws and adopt "
                    "intestate-succession legislation; adopt legislation "
                    "prohibiting discrimination based on sexual orientation "
                    "(including in the Labour Act) and hate-crime legislation; "
                    "abolish the common-law crime of sodomy and include same-sex "
                    "relationships in the Combating of Domestic Violence Act; and "
                    "combat discrimination against persons with disabilities and "
                    "persons who are HIV-positive.",
                "limbs": [
                    {"limb": "(a) repeal race-discriminatory laws; intestate "
                             "succession", "grade": "C",
                     "eval": "The Committee regrets that the State party denies "
                             "the existence of discriminatory laws and requires "
                             "the names and current status of the intestate "
                             "succession bills submitted to the Minister of "
                             "Justice."},
                    {"limb": "(b) prohibit discrimination based on sexual "
                             "orientation; hate-crime law", "grade": "C",
                     "eval": "The Committee regrets the denial of discrimination "
                             "against LGBT persons and that no specific "
                             "legislation or hate-crime law was adopted; the two "
                             "Acts cited pre-date the concluding observations."},
                    {"limb": "(c) abolish the sodomy offence; same-sex partners "
                             "in the DV Act", "grade": "C",
                     "eval": "The Committee regrets that no information was "
                             "provided on abolishing the crime of sodomy or "
                             "including same-sex relationships in the Combating "
                             "of Domestic Violence Act."},
                    {"limb": "(d) discrimination against persons with "
                             "disabilities and HIV-positive persons",
                     "grade": "C",
                     "eval": "The Committee appreciates the National Human "
                             "Rights Action Plan goal but requires detail on "
                             "specific measures, including on HIV-positive "
                             "persons."},
                ],
            },
            {
                "para": "22",
                "title": "Prohibition of torture and ill-treatment",
                "recommendation": "Adopt legislation on the prevention and "
                    "combating of torture and provide training; ensure "
                    "perpetrators are prosecuted before ordinary courts and "
                    "victims compensated; ensure an independent investigation "
                    "mechanism; and ensure sex workers can report crimes without "
                    "risk of prosecution for their occupation.",
                "limbs": [
                    {"limb": "(a) prosecute before ordinary courts; compensate "
                             "victims", "grade": "B",
                     "eval": "The Committee welcomes that a bill criminalizing "
                             "torture will be brought before parliament and "
                             "requires its name, content, conformity with the "
                             "Covenant and a timeline, plus information on "
                             "specific prosecutions and compensation."},
                    {"limb": "(b) independent investigation mechanism",
                     "grade": "B",
                     "eval": "The Committee appreciates the information on the "
                             "police Internal Investigation Directorate and the "
                             "Ombudsman but requires clarification on whether "
                             "these bodies operate independently."},
                    {"limb": "(c) sex workers can report crimes without "
                             "prosecution", "grade": "C",
                     "eval": "The Committee regrets that no information was "
                             "provided on measures to ensure that sex workers "
                             "can report crimes without risking prosecution."},
                ],
            },
            {
                "para": "24",
                "title": "Violence, including sexual violence, against women",
                "recommendation": "Awareness and public-education programmes "
                    "involving traditional leaders; prompt, impartial "
                    "investigation of “passion killings”; dismantle "
                    "barriers to prosecuting domestic violence and increase "
                    "24-hour availability of protection orders; operationalise "
                    "and expand shelters; protect victims from stigmatisation "
                    "and reprisals and adopt witness-protection legislation; and "
                    "train police, prosecutors and judges and adopt pending "
                    "legislation allowing sexual-violence prosecutions to "
                    "continue where a complaint is withdrawn.",
                "limbs": [
                    {"limb": "(a) awareness and education with traditional "
                             "leaders", "grade": "C",
                     "eval": "The campaigns mentioned were conducted before the "
                             "adoption of the concluding observations; the "
                             "Committee reiterates its recommendations and "
                             "requests updated information."},
                    {"limb": "(b) investigate “passion killings”",
                     "grade": "C",
                     "eval": "The Committee regrets the lack of information on "
                             "any investigations to identify, prosecute and "
                             "punish perpetrators of “passion killings”."},
                    {"limb": "(c) dismantle barriers; 24-hour protection orders",
                     "grade": "C",
                     "eval": "The number of magistrates cited and the training "
                             "provided refer to the period prior to the "
                             "concluding observations; the Committee reiterates "
                             "its recommendations."},
                    {"limb": "(d) operationalise and expand shelters",
                     "grade": "C",
                     "eval": "The Committee regrets the lack of information on "
                             "measures to operationalise and expand shelter "
                             "facilities and ensure effective recourse to "
                             "shelter."},
                    {"limb": "(e) protect from stigmatisation/reprisals; "
                             "witness-protection law", "grade": "B",
                     "eval": "The Committee welcomes the legislative measures "
                             "enacted to protect witnesses (Witness Protection "
                             "Act No. 11 of 2017) and seeks clarification on how "
                             "they operate in practice."},
                    {"limb": "(f) train officials; adopt pending "
                             "sexual-violence legislation", "grade": "C",
                     "eval": "The Committee notes training for police but "
                             "regrets the absence of similar training for "
                             "prosecutors and of information on the pending "
                             "legislation on withdrawn complaints."},
                ],
            },
        ],
    },
    "PRY": {
        "co_symbol": "CCPR/C/PRY/CO/4",
        "session": "126th session (2019)",
        "assessment_symbol": "CCPR/C/140/2/Add.2",
        "assessment_date": "adopted 140th session, March 2024",
        "round": "Single follow-up round; procedure discontinued with outstanding "
                 "points folded into the next periodic report.",
        "paragraphs": [
            {
                "para": "13",
                "title": "Human rights violations during the dictatorship "
                         "(1954–1989) and the transition",
                "recommendation": "Duly investigate all cases of serious "
                    "violations during the dictatorship and the transition "
                    "period and bring those responsible to justice; ensure "
                    "prompt, fair and full reparation for all victims and "
                    "families irrespective of when the claim was filed; and "
                    "accelerate the search for missing persons and identification "
                    "of remains, with the necessary resources.",
                "limbs": [
                    {"limb": "whole paragraph", "grade": "B",
                     "eval": "While welcoming the information on cases No. "
                             "3154/89 and No. 53/2017 and the search and "
                             "compensation efforts, the Committee regrets that "
                             "many requests for compensation have been refused "
                             "and requests updated figures and information on "
                             "the pending compensation bill."},
                ],
            },
            {
                "para": "29",
                "title": "Pretrial detention and fundamental safeguards",
                "recommendation": "Continue reforms to significantly reduce the "
                    "use of pretrial detention and ensure non-custodial "
                    "alternatives (bail, electronic monitoring), with pretrial "
                    "detention exceptional, reasonable and as short as possible, "
                    "including for adolescents; and ensure all detainees are "
                    "informed of the reasons and their rights, have access to a "
                    "lawyer and can contact family from the very outset of "
                    "detention.",
                "limbs": [
                    {"limb": "(a) reduce pretrial detention; non-custodial "
                             "alternatives", "grade": "B",
                     "eval": "The Committee welcomes the enactment of Act No. "
                             "6350/19 and Supreme Court Resolution No. 1511, the "
                             "committee on alternative measures and the juvenile "
                             "restorative-justice work, but regrets the lack of "
                             "data on impact and on the use of alternatives."},
                    {"limb": "(b) safeguards from the outset of detention",
                     "grade": "B",
                     "eval": "While noting the free legal aid provided "
                             "nationwide and the ongoing training of public "
                             "defenders and police, the Committee regrets the "
                             "lack of information on specific steps taken during "
                             "the reporting period."},
                ],
            },
            {
                "para": "35",
                "title": "Independence of the judiciary",
                "recommendation": "Strengthen efforts to combat corruption "
                    "within the judiciary, including awareness-raising among "
                    "judges, prosecutors and police; eradicate all forms of "
                    "interference in the judiciary by other branches and "
                    "investigate, prosecute and punish interference and "
                    "corruption; and review the laws and operations of the "
                    "institutions responsible for administering justice and "
                    "appointing judges and prosecutors to guarantee "
                    "independence, impartiality, autonomy and transparency.",
                "limbs": [
                    {"limb": "whole paragraph", "grade": "B",
                     "eval": "While welcoming the measures to fight corruption "
                             "and promote transparency in the judiciary, the "
                             "Committee requests information on their impact and "
                             "regrets the lack of specific information on "
                             "measures to eradicate interference by other "
                             "branches of government."},
                ],
            },
        ],
    },
}
