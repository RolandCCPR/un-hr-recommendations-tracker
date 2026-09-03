# How the Human Rights Committee grades follow-up — evidence from the full corpus

*Analysis of every "Follow-up Report of the Special Rapporteur on follow-up on Concluding
Observations" for the ICCPR (OHCHR Treaty Body Database, TreatyID=8, DocTypeID=117,
DocTypeCategoryID=3). Based only on the follow-up reports themselves — no State or NGO
submissions were consulted. Compiled 3 September 2026.*

---

## 1. The corpus — how many there are

**143 documents** are returned by that search. They are not 143 separate gradings; they
break down as:

| Kind | Count (approx.) | What it is |
|---|---|---|
| Sessional base reports `CCPR/C/<session>/2` (or `/3`) | ~28 | "Report on follow-up to the concluding observations". Up to session **123** each one contains the full grade tables for **all** States reviewed that session. From session **124–125** onward the base report is just a cover note. |
| Per-country evaluation addenda `…/2/Add.N` | ~95 | "Evaluation of the information on follow-up to the concluding observations: COUNTRY" — one reviewed State each. Practice began at session 125 (2019). |
| Recurring "ANNEX – Status of follow-up…" tables | ~20 | Cumulative running status list since the 105th session. No letter grades — just "dialogue ongoing / completed". |

Sessions covered run from the **98th (2010)** to the **145th (May 2026)** — about **45
sessional reports**, with a few gaps (111, 142, 143). I downloaded and text-mined **120**
of the 143 (every substantive grading document; `CCPR/C/111/2` would not retrieve).

Within the letter-grade era there are **~152 country-review evaluations**, ~70 States with
a dedicated per-country document, and **~800 individually graded recommendation
sub-limbs**. Before ~2013 the Committee used a narrative scale
("reply generally / largely satisfactory", "not satisfactory", "incomplete") which later
mapped onto A/B and C.

---

## 2. The scale (verbatim, unchanged since c. 2013)

> **A – Reply/action largely satisfactory:** the State party has provided evidence of
> significant action taken towards the implementation of the recommendation.
> **B – Reply/action partially satisfactory:** the State party has taken steps towards
> implementation, but additional information or action remains necessary.
> **C – Reply/action not satisfactory:** a response has been received, but the action
> taken or information provided is not relevant or does not implement the recommendation.
> **D – No cooperation with the Committee:** no follow-up report has been received after
> the reminder(s).
> **E – Information or measures taken are contrary to, or reflect rejection of, the
> recommendation.**

---

## 3. Distribution of ~800 graded sub-limbs

Two independent extraction methods (the header summary line of each review; and every
in-text evaluation block) converge:

| Grade | Share | Plain reading |
|---|---|---|
| **A** | **4–6 %** | rare — roughly 1 in 20 |
| **B** | **43–45 %** | the workhorse |
| **C** | **~43 %** | equally common; overtook B around 2018 |
| **D** | **4–5 %** | almost all pre-2016 |
| **E** | **~3 %** | very rare — roughly 1 in 30 |

**B and C together are ~86 % of every grade ever given.** The entire system essentially
turns on one boundary: *did the State take a real step on the specific ask (B) or not (C)?*

### Trend — the Committee has hardened

| Era | A | B | C | D | E |
|---|---|---|---|---|---|
| 2013–2016 (s109–118) | 6 % | **45 %** | 39 % | 9 % | 1 % |
| 2016–2018 (s119–124) | 4 % | 44 % | 46 % | 2 % | 4 % |
| 2018–2021 (s125–133) | 8 % | 39 % | **51 %** | 0 % | 2 % |
| 2022–2026 (s134–145) | 8 % | 38 % | 42 % | 2 % | **9 %** |

- **B is falling, C is rising** — a State reply that would have drawn B a decade ago now
  frequently draws C.
- **D has collapsed** — near-universal engagement with the procedure means non-response is
  no longer the story.
- **E has tripled-plus** in the last four years — the Committee now openly grades
  rejection and regression where it used to stay at C.

### Sub-limb granularity

The Committee splits **~64 %** of follow-up paragraphs into lettered sub-limbs and grades
each one. **36 %** of paragraphs end up with **mixed** sub-limb grades (e.g. B for (a),
C for (b)). Commonest patterns: uniform B, uniform C, then `BC` / `CB`. Splitting a
paragraph is normal; the Committee only writes one grade for the whole paragraph when the
sub-limbs genuinely point the same way.

---

## 4. The linguistic fingerprint of each grade

From ~1,780 evaluation passages. These are the phrases that actually travel with each
grade — useful as a decision rule.

### A — "welcomes … has [done X]"
- 41 % contain **"welcomes"**; ~5 % "appreciates"; then a request for confirmation detail
  "in its next periodic report".
- **Almost never** co-occurs with "regrets" (7 %) or "no action / lack of information" (~1 %).
- A is given for **one discrete completed act**, even with implementation still unproven:
  *"the Committee notes that the State party has implemented a new Civil Code regulating
  the legal capacity of persons with disabilities"*; *"welcomes the protocol signed in
  August 2012 … to provide low-cost housing to victims of domestic violence"*.
- A does **not** require outcome statistics or full implementation.

### B — "welcomes / notes the steps … **but requires additional information**"
- 25 % "welcomes", **18 % "requires additional information"**, 9 % "requests updated
  information", only 5 % "regrets".
- Signature = **credit for a real step + an open information request**.
- Reliably B: a **draft bill submitted**, a law **adopted but not yet in force**, an
  institution **created but not yet shown to work**, measures taken **without impact
  data**. *"the Committee appreciates the draft law … is being revised … requires
  additional information"*; *"notes the amendments proposed … by the working group …
  further information is required on whether the Ministry has submitted a bill"*.

### C — "**regrets** that … **The Committee reiterates its recommendation.**"
- **28 % "regrets"**, **18 % "reiterates its recommendation"**, 11 % "no concrete
  action/measure/progress", 9 % "lack of specific information", 4 % "has not been
  adopted/enacted/repealed/established".
- C often still opens with "while noting…" or even "welcomes…" — **partial credit does
  not lift it off C** if the core ask is untouched.
- **Tell:** C "**reiterates its recommendation**"; B "reiterates its **request** [for
  information]". If the Committee re-issues the *recommendation*, it's C.
- Reliably C: "no information was provided on [sub-limb]"; measures that pre-date the
  concluding observations; a bill "still pending" with nothing new; a reform that
  "does not implement" the specific point.

### D — "the State party has not provided … information"
- 27 % "no action", 19 % "no information provided", 24 % "reiterates its recommendation".
- Purely about **non-response**, never about the merits. Effectively obsolete in current
  practice.

### E — "regrets … **repeated information** / **does not intend to** / **contrary to**"
- **Highest "regrets" rate of any grade (42 %)** + 22 % "reiterates its recommendation".
- Distinctive markers absent from C: *"the State party **repeated** information provided
  in its periodic report"*, *"**does not intend to** [repeal / amend]"*, *"the reported
  **amendment of legislation in 2022** resulting in the extended application of capital
  punishment"*, definition/measure *"is fully compliant … no amendments are necessary"*,
  *"does not intend to repeal the Amnesty Act"*.
- **E = active rejection or regression, never mere inaction.**

### C vs E — the boundary
| | C | E |
|---|---|---|
| State's stance | silent / vague / "working on it" | "we will not" / "current law is fine" / defends the impugned measure |
| Movement | none | **backwards** (new contrary law, new amnesty, tightened restriction) |
| Typical verb | "regrets that no concrete action…" | "regrets that the State party **does not intend to**…" / "**repeated** its earlier position" |

---

## 5. How this squares with the blind-test result

The blind test scored **18/24**, and **all six misses were one grade too strict** — five
were C-where-the-Committee-said-B, one was B-where-it-said-A.

The corpus explains why:

1. **The whole system lives on the B/C line** (86 % of grades). An error rate concentrated
   there is an error rate on the only distinction that matters — and mine was
   systematically on the strict side of it.

2. **My working C threshold was the Committee's *does not implement* wording taken at face
   value. The Committee's actual C threshold is narrower:** "regrets / no concrete action
   / not relevant / **reiterates the recommendation**". If the State did something real and
   on point — passed a law (even not in force), built a body, tabled a bill — and the
   Committee's natural sentence is "welcomes … but requires further information", that is
   **B**. "Framework restated + bill pending + no outcome data" lands on **B** far more
   often than I assumed, and *more so still* when no NGO submission contradicts the State
   (cf. Namibia ¶22 — "a bill will soon be brought before parliament" → B).

3. **A is more reachable than I treated it.** It is routinely given for a single completed
   act with implementation questions still open. Denmark ¶20 (a whole package of
   legislative + policy + training measures across three jurisdictions) → A is squarely in
   character; my "no outcome statistics → B" was mis-calibrated for a "continue efforts"
   recommendation.

4. **E was calibrated correctly.** My one E (Denmark ¶32(e), State "has no plans to
   repeal") matches the Committee verbatim-style; and pulling back to C on ¶32(d)
   ("access retained on request / never activated") was right. Keep E for explicit refusal
   ("does not intend to") or a new contrary measure — but note the base rate has risen to
   ~9 % in 2022–2026, so it is no longer almost-never.

### Corrected decision rule (for the UPR assessments in this project)

- **Did the State respond at all on this sub-limb?** No → **D**.
- **Is the response a refusal, a defence of the impugned measure, or a step backwards
  (new contrary law)?** Yes → **E**.
- **Did the State take a concrete, on-point step** — enacted or drafted legislation, a new
  institution/mechanism, a policy with something to show, credible action on the specific
  ask? 
  - No — only generic assurances, restated pre-existing framework, "under study", nothing
    new since the COs → **C**.
  - Yes, but incomplete — not in force, no impact data, partial, one of several sub-asks
    → **B**.
  - Yes, and the core ask is essentially met (even if refinements remain) → **A**.
- When sub-limbs of one paragraph diverge, **grade them separately** — the Committee does
  this 64 % of the time.
- Split a compound recommendation ("investigate *and* compensate *and* set up a
  mechanism") into its parts before grading.
