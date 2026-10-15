# Gaps register

FCT-STANDARDS-1, draft review, 2026-10-15. There are 14 tracked gaps. None is resolved by creating this PR. All category records remain on HOLD and have no effective date or approved numerical ICS ceiling.

| ID | Scope | Gap and required action |
| --- | --- | --- |
| G-01 | All categories, derivation | FCT-DERIVATION-1: template occurrence language conflicts with newer manual/export rules. Elon accepted the government-only bounded draft at 12:50. No occurrence or analog ceilings. Category applicability and decision rules still require a later order before activation. |
| G-02 | EU food source currency | Original 2023/915 food values were confirmed in official Swedish and Lithuanian editions. The listed current consolidation is dated 2026-08-19 but was inaccessible. Confirm applicable amendments and English category wording before treating these historical source values as current ceilings. |
| G-03 | EU food category mapping | Resolve species, tissue, whole-fish, intended infant-food use and wet-weight rules. Dried, diluted, processed and composite food provisions require Article 3 review. No invented processing factor or mapping from a generic seafood label is allowed. Bear meat and offal are outside the transcribed game rows. |
| G-04 | Product bans and fluorine indicators | Denmark and Minnesota bans are not numeric zero limits. Denmark's organic-fluorine indicator is not an individual PFAS maximum. Preserve functional-barrier and component exceptions. Confirm current legal editions and exact product definitions; resolve analytical and documentary evidence for intentional use. |
| G-05 | US drinking water | The 2024 final rule is transcribed, including PFBS having no individual MCL. EPA's current page reports 2026 proposals affecting implementation and some PFAS provisions. Reconfirm final legal status, averaging, sampling point and exact system applicability before adoption. No single-sample or bottled-water ceiling is derived. |
| G-06 | EU drinking-water parameters | EU-W-01 and EU-W-02 have empty value and unit fields: primary directive text could not be opened. Confirm Annex I Part B values, Annex III scope, Article 13(7), Article 25 and national implementation. Official summaries and search snippets were not substituted for the primary text. This is not absence of regulation. |
| G-07 | Bottled water | No directly applicable finished bottled-water PFAS numeric maximum was confirmed in the reviewed instruments. `no regulatory limit; no ICS ceiling set` within this bounded review. Verify bottled and natural mineral water provisions separately; tap-water MCLs do not fill the gap. |
| G-08 | California food packaging | CA-01 is empty with TODO because the statutory text was inaccessible. Agency summaries differ in fluorine terminology and threshold boundary wording. Confirm section 109000 directly, including intentional addition, exact unit, inclusive boundary, scope and date. Do not resolve by choosing a summary. |
| G-09 | All categories, retest schedule | The template provides monthly High-Risk and quarterly Moderate-/Lower-Risk candidate schedules. PFAS category risk assignments, baseline design, representative sampling, actual due dates and change-triggered requirements remain unapproved. No category is active without its recorded schedule. |
| G-10 | All categories, laboratory and license conditions | Approve matrix-specific methods, complete target lists, isomer/sum coverage, blank controls, reporting limits, uncertainty decision rules and evidence handling. Approve license terms, appeals, record retention, confidentiality and mark controls. No fees, contract periods or method performance numbers are invented. |
| G-11 | Infant formula, baby foods, dairy/butter, plant foods/beverages, pet food and non-paper packaging | The bounded sources do not establish finished-product numeric PFAS ceilings for these categories. `no regulatory limit; no ICS ceiling set` for the unfilled category/analyte cells in this review. Food ingredient rules, paper indicators, public-water MCLs and human-food limits cannot be extrapolated into these cells. Broader legislation and product definitions still require review. |
| G-12 | Apparel, toothpaste, baby wipes/lotions/sunscreens and consumer-product analytes | No category-specific numeric PFAS ceiling confirmed here. `no regulatory limit; no ICS ceiling set` within reviewed scope. Class bans may apply after exact cosmetic, juvenile-product, medical or other classification. The Minnesota category list is not an exhaustive national or global survey. |
| G-13 | Template verification | Template typecheck passed. Template tests have existing failures and prebuild stops at stale citation context. Browser acceptance is blocked by missing build output. See docs/VALIDATION.md. No template fixes or ceiling edits are authorized. |
| G-14 | Unregulated analytes and aggregate interpretation | PFBS individual MCL is absent from the cited US rule, though PFBS contributes to its mixture index. Other individual PFAS, precursors and class/fluorine measurements must not inherit PFOA, PFOS or four-PFAS ceilings. Where no applicable numeric maximum is identified: `no regulatory limit; no ICS ceiling set`. Unconfirmed laws remain TODO. Define the full category panel and jurisdiction coverage before adoption. |

## Gate answers

Elon answered FCT-DERIVATION-1 and FCT-SOURCE-ACCESS-1 with Option 1 in the bridge at 2026-10-15 12:50 Asia/Nicosia. The bounded government-only draft, historical-edition labels, three empty TODO value rows and unset numerical ICS ceilings are accepted for this draft PR. No operational gate blocks delivery.

Scientific, source-currency, applicability and operational activation gaps remain as recorded above. A later order is required to approve applicability and decision rules or to verify separately deposited current official instruments. The gate answers do not activate a standard or clear any HOLD.

## Category and analyte coverage detail

These are unresolved cells in the reviewed register, not declarations that no law exists anywhere. They share the gap IDs above and do not add new counted gaps.

| Category scope | Analyte or endpoint gap | Disposition |
| --- | --- | --- |
| US regulated drinking-water systems under the cited 2024 rule | PFBS individual MCL | Explicitly absent in the source; its mixture-index role remains. G-05 and G-14. |
| Finished infant formula, baby food, dairy/butter, plant food/beverages and pet food | Individual PFOA, PFOS, PFNA and PFHxS; their sum | No numeric ceiling established for these finished matrices by the reviewed food rows. G-11. |
| Drafted food categories | PFBS, HFPO-DA, PFHxA, PFDA and 6:2 FTOH; precursor and PFCA/PFSA class endpoints | No numeric food ceiling established by this register. These are review targets from the queue, not an approved laboratory panel or a claim of equivalent chemical behavior. G-14. |
| Bottled and natural mineral water | Individual PFAS and aggregate PFAS endpoints | Public-system values do not resolve the bottled-water legal category. G-07. |
| Paper and board packaging | Individual PFAS, migration and organic-fluorine indicator | Ban evidence and bulk organic fluorine cannot be substituted for one another. G-04 and G-08. |
| Consumer products and other packaging | Individual PFAS, class totals and total organic fluorine | Nonnumeric class restrictions can apply despite missing numeric ceilings. G-04, G-11, G-12 and G-14. |

For each genuinely unfilled numeric category/analyte cell within this bounded review: `no regulatory limit; no ICS ceiling set`. For a known instrument whose text or value remains unconfirmed, retain TODO instead.
