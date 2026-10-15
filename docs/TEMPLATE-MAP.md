# Template map

Order: FCT-STANDARDS-1. Draft review only, 2026-10-15.

Read-only source: `paleofoundation/heavymetalcertified`, commit `236a3b887216208f973dfea43b9c57ae717cee70`. FCT starts from its own `origin/main`. No template content, thresholds, assets, identifiers, application form, or deployment configuration is imported wholesale.

| Surface | Template location and role | FCT draft location and disposition |
| --- | --- | --- |
| Program | `content/program/structure.md`, `method.md`, `two-pathways.md`, `readiness.md`, `remediation.md`, `corrective-action.md` | `content/program/structure.md`, `method.md`, `retesting.md`, `licensee-terms.md`; category conformance, evidence review and corrective action |
| Category standards | `content/standards/`, including separate infant formula powder and ready-to-feed pages | `content/standards/`; distinct product matrices and legal subcategories, source-linked limits or explicit unresolved cells |
| Data and limits | `data/standards/hmtc_standards_catalog.json`, category `*-pages.json`, category `*-compiled/*.json`; `content/static/data/standards.csv` and `.json` | Root `LIMITS-SOURCES.csv` preserves source strings; `data/standards/categories.json` maps draft category scope to source rows; neither is an approved ceiling catalog |
| Generation | `tools/build-standards-pages.mjs`, `render-all-standard-pages.mjs`, `build-standards-export.mjs`, `lib/standard-export-cell.mjs` | No metal-specific generators copied. FCT content is a reviewable Markdown draft, with a local integrity check |
| Method | `data/method/method-v2.json`; `content/program/method.md`; category manual Parts 1, 2 and 5 | Government lookup retained, ambiguity logged in GATE FCT-DERIVATION-1; occurrence and analog ceilings excluded by the order |
| Retest schedule | `data/manuals/cat1-manual/part4-lot-testing.md`, sections 4.2, 4.4 and 4.9 | `content/program/retesting.md`; template Certified schedule is monthly for High-Risk and quarterly for Moderate-/Lower-Risk, assigned after laboratory review. Proposed use in FCT requires PFAS category risk assignment; no automatic metal risk-tier transfer |
| License conditions | `data/manuals/cat1-manual/part2-program.md`, sections 2.4 to 2.7; `content/program/corrective-action.md`; `content/apply.md`, `content/portal.md`, `content/verify.md` | `content/program/licensee-terms.md` covers scope, records, mark removal and corrective action. No standalone executed license agreement was identified in these surfaces; commercial terms remain unresolved |
| Application | `content/apply.md` combines application, pricing, term options and contact workflow | No separate FCT intake or fee schedule. Future application belongs at the central ICS hub; Q11 is not implemented |
| Evidence firewall | Template README and `tools/firewall-cert-lint.mjs` describe outbound index citations | FCT may cite Forever Chemicals Index as contextual evidence. The index does not promote certification and does not supply regulatory ceilings |
| Verification | `package.json`: test, check, check:v3, build with extensive prebuild/postbuild hooks | Run template checks in a disposable local archive only. The template checkout stays untouched. Network-dependent package/browser retrieval is outside this order; blocked checks are reported literally |

## Documented derivation and conflicts

`content/standards/infant-formula-powder.md` describes selection of the strictest applicable government maximum, preservation of formulation splits, native-basis handling and disclosed read-across where exact product regulation is absent. `tools/lib/standard-export-cell.mjs` preserves source unit and basis, separates pending/control/numeric records, rejects occurrence-derived read-across, and labels government cells as the strictest applicable finalized maximum.

The template is internally inconsistent. `data/method/method-v2.json` still describes selective occurrence percentiles and occurrence values for unregulated cells. `content/program/structure.md` and `two-pathways.md` retain related language. In contrast, `data/manuals/cat1-manual/part2-program.md` section 2.1 and Part 5 reject distribution-derived limits, while the export code rejects occurrence-derived read-across. The catalog also retains legacy occurrence language. There is no justified PFAS-specific percentile rule in these files.

FCT-DERIVATION-1 was filed and answered by Elon at 12:50 Asia/Nicosia on 2026-10-15: preserve directly cited government values in their own matrix, scope, units and legal role; do not infer a universal FCT number from unlike standards. No occurrence calculation, matrix conversion, analogous-product read-across, or cross-analyte substitution is applied in this draft. Elon accepted this bounded government-only approach and left numerical ICS ceilings unset pending later applicability and decision-rule approval. The template remains unchanged.

Where no applicable numeric limit is identified in the bounded source review, use `no regulatory limit; no ICS ceiling set`. The phrase describes the reviewed category/analyte scope, not proof that no jurisdiction anywhere regulates it. An inaccessible or unconfirmed source is separately marked TODO, not classified as absence of law.

## Retesting and terms boundary

The template also contains production-lot testing and remediation requirements that conflict with this order. They are not ported. FCT describes a standard per product category with scheduled retesting and documented change-triggered review. Numeric surveillance intervals above are identified template provisions, not invented PFAS findings. Before operation, the operator must approve the PFAS category assignment and dated schedule. No mark can be awarded by this draft.

Template baseline counts, metal panels, measurement-uncertainty factors, fees, commercial terms and identifiers are not silently applied to PFAS. Proposed FCT laboratory decision rules and license conditions remain expressly draft and must resolve the gaps before activation.
