---
title: "Drinking water from regulated supplies: draft standard"
type: standard-in-development
status: draft_on_hold
standard_version: draft-2026-10-15
effective_date: null
approved: false
---

# Drinking water from regulated supplies

This is a draft category standard. It awards no certification or mark.

## Scope

Community and non-transient non-community systems for US source rows. EU water parameters remain unconfirmed from the primary directive. No transfer to bottled water.

## Regulatory source register

Values below are source transcriptions, not approved ICS ceilings. Source dates, legal roles, matrix restrictions and unresolved current-status checks are in [LIMITS-SOURCES.csv](../../LIMITS-SOURCES.csv). The original legal instrument governs its own scope.

| Source row | Published analyte scope | Published value | Published unit | Legal role |
| --- | --- | --- | --- | --- |
| [US-01](https://www.federalregister.gov/documents/2024/04/26/2024-07773/pfas-national-primary-drinking-water-regulation) | PFOA | 0.0000040 | mg/l | numeric_limit |
| [US-02](https://www.federalregister.gov/documents/2024/04/26/2024-07773/pfas-national-primary-drinking-water-regulation) | PFOS | 0.0000040 | mg/l | numeric_limit |
| [US-03](https://www.federalregister.gov/documents/2024/04/26/2024-07773/pfas-national-primary-drinking-water-regulation) | PFHxS | 0.00001 | mg/l | numeric_limit |
| [US-04](https://www.federalregister.gov/documents/2024/04/26/2024-07773/pfas-national-primary-drinking-water-regulation) | PFNA | 0.00001 | mg/l | numeric_limit |
| [US-05](https://www.federalregister.gov/documents/2024/04/26/2024-07773/pfas-national-primary-drinking-water-regulation) | HFPO-DA | 0.00001 | mg/l | numeric_limit |
| [US-06](https://www.federalregister.gov/documents/2024/04/26/2024-07773/pfas-national-primary-drinking-water-regulation) | Hazard Index PFAS (HFPO-DA, PFBS, PFHxS, and PFNA) | 1 | unitless | numeric_limit |
| [US-07](https://www.federalregister.gov/documents/2024/04/26/2024-07773/pfas-national-primary-drinking-water-regulation) | PFBS | No numeric value | Not populated | no_individual_limit |
| [EU-W-01](https://eur-lex.europa.eu/eli/dir/2020/2184/oj/eng) | PFAS Total | TODO | Not populated | unconfirmed_limit |
| [EU-W-02](https://eur-lex.europa.eu/eli/dir/2020/2184/oj/eng) | Sum of PFAS | TODO | Not populated | unconfirmed_limit |

Where no applicable numeric limit is identified in the bounded category review: `no regulatory limit; no ICS ceiling set`. Inaccessible or unconfirmed limits remain TODO instead of being labelled absent. Class-based prohibitions still apply.

## Proposed conformance requirements

The licensee must identify the exact product form, intended use, tissue or material, intended market, applicable legal category and relevant analyte scope. The operator must approve those mappings before applying a numerical result. Requirements from different matrices or aggregation definitions are not interchangeable. A product prohibition cannot be satisfied merely by reporting an analytical non-detect.

The laboratory report must identify the sampling unit, sample basis, method version, target analytes and isomer coverage, quantification and detection limits, blanks, recovery, uncertainty and any statutory summation convention. A report missing a required target or capable reporting limit is incomplete. A non-detect is not a measured zero or evidence of absence of all PFAS.

For a confirmed, applicable numeric maximum, the draft derivation is direct adoption on the same basis after current legal text and the decision rule are approved. No scaling, analog read-across or occurrence calculation is proposed. Until that review is complete, the ICS ceiling remains unset and this category stays on HOLD.

## Scheduled retesting

This category requires scheduled retesting under the [retesting policy](../program/retesting.md). Before activation the operator must approve its risk tier, laboratory capability, named sampling unit, calendar interval and next due date. The template's monthly High-Risk and quarterly Moderate-/Lower-Risk schedules are candidate intervals, not assigned PFAS category frequencies. Missing assignment prevents activation. Material, formulation, supplier, water source or process changes trigger additional review and documented testing when needed.

## Licensee obligations and holds

The [licensee terms](../program/licensee-terms.md) apply to this category. Open gaps: G-01, G-05, G-06, G-09, G-10, G-14; see [GAPS.md](../../GAPS.md). No certificate may describe a broader analyte panel, matrix, product set or period than the approved evidence supports.
