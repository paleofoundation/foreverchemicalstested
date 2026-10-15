# Validation report

Run date: 2026-10-15. FCT base commit: `f6835a2d20e990298db899a0f1034c9e77f343dc`. Template reference: `236a3b887216208f973dfea43b9c57ae717cee70`.

## FCT content checks

`python3 tools/check-draft.py` checks CSV schema, unique source IDs, official-source host allowlist, numeric versus nonnumeric record roles, explicit TODO values, source units, category references, unset ceiling and approval fields, gap references, scheduled retesting sections, local links and prohibited terminology/dashes. The companion `VALIDATION.json` records the final run.

The package contains 73 source rows: 56 numeric regulatory records, one indicator, 12 product-ban records, one explicit absence of an individual limit and three unconfirmed-value TODO records. There are 33 category standard pages and 14 tracked gaps. No category has an approved ICS ceiling.

Manual source review compared all 50 EU food values across official Swedish and Lithuanian original-edition tables, including all category splits. US values were checked against the final-rule table in mg/l, not converted from a summary in another unit. The Danish indicator retains its own original unit and remains separate from the statutory prohibition. Source review corrected the Danish transition locator to section 25. Unverified values remained empty. These are source-transcription checks, not a current worldwide legal-applicability signoff.

No spreadsheet artifact runtime was available in this environment. The requested plain CSV was authored and round-trip checked with the Python standard library, preserving literal strings, Unicode units and blank fields. No workbook or calculated ceiling was substituted for the CSV.

## Template checks in disposable copies

The template checkout was used only for reading and local archiving. Dependencies installed from the existing local package cache with `npm ci --offline --ignore-scripts --no-audit --no-fund`; no package download was used. Tests and build ran in disposable archive directories. The successful typecheck preceded the build. Tests were rerun in a pristine archive to distinguish existing template failures from generator output.

| Command | Exit | Result |
| --- | --- | --- |
| `npm ci --offline --ignore-scripts --no-audit --no-fund` | 0 | Local cached dependency installation completed. |
| `npm test` | 1 | 209 tests: 201 passed, 8 failed in the pristine template archive. |
| `npm run check` | 0 | TypeScript typecheck passed. |
| `npm run build` | 1 | Prebuild stopped at `citation-context`: stale page context for `briefings/heavy-metals-in-peptides-and-sarms [1]`. Quartz build and postbuild did not run. |
| `npm run check:v3` | 2 | No `public/` output exists because build was blocked. No rendered visual pass claimed. |

The test failures are one module-load failure in `tools/tests/finder-source-values.test.mjs` (`finderLimit` undefined), and seven failed assertions in `tools/tests/occurrence-authority.test.mjs`. The latter cover regulatory/precautionary provenance, occurrence fallback and retired source-type handling. They are existing template failures and were not repaired in this order.

A local Node preload denied external network during these checks. An initial attempt to apply an operating-system sandbox was unavailable; an initial overly strict preload blocked local test-runner IPC. The preload was corrected to permit local sockets before the reported tests. Those setup attempts are not reported as template test failures.

The FCT repository contains a content draft and local validator, not the template application framework. There is no FCT site build to claim. No deploy, merge, domain, application intake, certificate issuance or existing standard modification was performed.
