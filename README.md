# Forever Chemicals Tested

FCT-STANDARDS-1 is a draft PFAS certification program and category standards package for review. No standard is effective and no numerical ICS ceiling is approved.

- [Program structure](content/program/structure.md), [method](content/program/method.md), [scheduled retesting](content/program/retesting.md), and [licensee terms](content/program/licensee-terms.md).
- [Category standards](content/standards/index.md).
- [LIMITS-SOURCES.csv](LIMITS-SOURCES.csv): official-source transcriptions, legal roles, edition limits and blank TODO values.
- [Template map](docs/TEMPLATE-MAP.md) and [source review](docs/SOURCE-REVIEW.md).
- [Gaps and approval questions](GAPS.md).
- [Validation report](docs/VALIDATION.md).

This is a content draft in the template's program/standards layout. It does not copy the template's metal datasets or implement a site framework, application or deployment. The source register preserves published values and units. Category records keep `ics_ceiling: null` until source currency, applicability, derivation, analytical decision rules and retest assignments are approved.

Run the local content integrity check with `python3 tools/check-draft.py`. Template tests and build were run in a disposable local archive; their results are reported separately from FCT validation.
