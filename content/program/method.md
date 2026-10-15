---
title: PFAS standards method draft
type: program
status: draft_on_hold
approved: false
---

# Method

The draft uses a government-limit lookup for an exact category and analyte scope. [LIMITS-SOURCES.csv](../../LIMITS-SOURCES.csv) is the transcription register. It preserves the official source's value string and unit, rather than silently converting values to a common display unit.

## Derivation sequence

1. Identify the final government instrument, edition, jurisdiction, effective date and legal role. Confirm current amendments. A proposal, screening indicator, monitoring trigger or intake guidance value is not a product maximum.
2. Match the product category, tissue or material, analyte definition, isomer coverage, reporting basis, intended use and compliance statistic. Retain any formulation split, exception and transition rule.
3. Where multiple directly applicable finalized limits can be compared on exactly the same scope and basis, the template's strictest-government-maximum rule is the candidate rule. Record every comparison and controlling source before approval. This draft does not claim a worldwide survey or a global strictest value.
4. Preserve the regulatory value directly. Any required conversion, composite-food factor, mixture calculation, analog mapping or change from annual-average compliance to an individual sample decision requires a documented method and GATE. No such calculation is made here.
5. Where the bounded review identifies no applicable numeric limit: `no regulatory limit; no ICS ceiling set`. Where a source is inaccessible or its value unconfirmed: leave value and unit empty with TODO. These are different evidence states.
6. Obtain the category applicability, analytical decision-rule and schedule approval before a standard can take effect. Until then all numerical ICS ceiling fields remain null.

## Separate kinds of evidence

US drinking-water individual MCLs, the dimensionless mixture Hazard Index, EU food individual maxima and the lower-bound sum are different criteria. Total organic fluorine is not interchangeable with a targeted PFAS sum. An intentional-use prohibition is not a zero-concentration limit, and a non-detect does not establish compliance with an intentional-use ban.

Preserve laboratory non-detect notation, detection and quantification limits, uncertainty and method scope. Where a legal instrument prescribes a lower-bound sum, record that calculation separately from measured concentrations. Do not replace underlying censored observations with measured zeros. Do not apply a sum convention to another regulatory aggregate.

The PFAS measurement-uncertainty decision rule, retest sampling design and complete matrix-specific panel require approval. The template's metal uncertainty factors, species-parent relationships, baseline counts and alert thresholds are not PFAS rules.

## Derivation gate

FCT-DERIVATION-1 records conflicts between the template method JSON and newer manual/export provisions. Elon accepted direct government-source transcription with unresolved applicability held in the 2026-10-15 12:50 gate answer. Numerical ICS ceilings remain unset until a later order approves applicability and decision rules. No occurrence percentile, cross-product read-across, index concentration distribution, or unverified chemical identifier supplies a missing ceiling. See [TEMPLATE-MAP.md](../../docs/TEMPLATE-MAP.md), [SOURCE-REVIEW.md](../../docs/SOURCE-REVIEW.md) and [GAPS.md](../../GAPS.md).
