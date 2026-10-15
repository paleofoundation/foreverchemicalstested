# Official-source review

Reviewed 2026-10-15. This is a bounded source register, not a global regulatory survey. All numerical cells are transcription strings. No conversion, inferred chemical identifier, intake-to-product calculation or certification ceiling is added.

## Source roles and access

| Rows | Official source and exact review scope | Disposition |
| --- | --- | --- |
| US-01 to US-07 | [EPA final rule, 89 FR 32532](https://www.federalregister.gov/documents/2024/04/26/2024-07773/pfas-national-primary-drinking-water-regulation), 40 CFR 141.61(c) Table 4, printed pages 32745 to 32746; 141.903 and 141.905 | Confirmed original 2024 text. Five concentration MCLs, one dimensionless index and one explicit absence of an individual MCL. No MCLG or index denominator is relabelled an MCL. |
| US current-status context | [EPA PFAS drinking-water rule page](https://www.epa.gov/sdwa/and-polyfluoroalkyl-substances-pfas), updated 2026-05-18 | Reports proposed implementation and rescission actions. Used to flag currency review only. No proposed value replaces a final-rule transcription. |
| EU-W-01 and EU-W-02 | [Directive (EU) 2020/2184](https://eur-lex.europa.eu/eli/dir/2020/2184/oj/eng), Annex I Part B and Annex III Part B | Primary text inaccessible. No value or unit populated. Official explanatory material and indexed snippets are discovery leads only. |
| EU-F rows | [Regulation (EU) 2023/915, original Swedish edition](https://eur-lex.europa.eu/eli/reg/2023/915/oj/swe), Annex I 4.2; cross-checked against the [official Lithuanian edition](https://eur-lex.europa.eu/eli/reg/2023/915/oj/lit) | All ten category rows and five analyte columns read directly. The original source uses decimal commas and μg/kg. The current consolidation link is [2026-08-19](https://eur-lex.europa.eu/eli/reg/2023/915/2026-08-19/eng); its body was inaccessible, so currency remains a gap. |
| DK-01 | [Danish Order 681](https://www.retsinformation.dk/eli/lta/2020/681/pdf), section 8 on PDF page 2; section 25 on pages 4 to 5 | Confirmed original Danish law. Marketing prohibition, functional-barrier exception and transition retained. No numerical concentration is stated in section 8. |
| DK-02 | [Danish regulator's June 2020 fact sheet](https://en.foedevarestyrelsen.dk/Media/638210239823191854/Faktaark%20FCM%20%28english%29.pdf), Indicator value, pages 1 to 2 | Primary regulator statement introducing its own indicator. This row is explicitly an indicator, not a statutory maximum or a borrowed secondary summary. |
| MN-01 to MN-11 | [Minnesota Statutes 116.943](https://www.revisor.mn.gov/statutes/cite/116.943), 2025 edition, subdivisions 1, 5 and 8 | Confirmed eleven category prohibitions and exceptions. The page flags a 2026 amendment to subdivision 2. No reporting deadline is represented by these rows. |
| CA-01 | [California Health and Safety Code 109000](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=109000.) | Access failure. Value and unit empty; exact scope and threshold are TODO. No agency summary is used as the statutory value. |

## EU food scope detail

The aggregate label in the CSV, `Summan av PFOS, PFOA, PFNA och PFHxS`, is the published Swedish column label. Its English working translation is the sum of PFOS, PFOA, PFNA and PFHxS. All individual columns and that sum include linear and branched stereoisomers. Maximum levels apply to wet weight. The sum uses the source's lower-bound convention. This does not make the individual measurements below quantification measured zeros.

Fish group 4.2.2.1.2 is restricted to the listed species and excludes intended production of infant and young-child foods. The published scientific-name list is: Clupea harengus membras; Sarda spp. and Orcynopsis spp.; Lota lota; Sprattus sprattus; Platichthys flesus and Glyptocephalus cynoglossus; Mugil cephalus; Trachurus trachurus; Esox spp.; Pleuronectes spp. and Lepidopsetta spp.; Sardina spp.; Dicentrarchus spp.; Silurus spp. and Pangasius spp.; Petromyzon marinus; Tinca tinca; Coregonus albula and Coregonus vandesius; Phosichthys argenteus; wild species of Salmo and Oncorhynchus; Anarhichas spp. No retail species mapping has been inferred.

Fish group 4.2.2.1.3 has the same intended-use exclusion and lists: Engraulis spp.; Barbus barbus; Abramis spp.; Salvelinus spp.; Anguilla spp.; Sander spp.; Perca fluviatilis; Rutilus rutilus; Osmerus spp.; Coregonus species other than those in 4.2.2.1.2. Group 4.2.2.1.1 also covers the listed fish when intended for infant and young-child food production. A generic freshwater/marine classification is insufficient to select a row.

When fish are intended to be consumed whole, the whole-fish basis applies. The crustacean and bivalve row retains tissue restrictions, the Pecten maximus provision and the canned-crustacean rule in the CSV notes. Article 3 governs treatment of dried, diluted, processed and composite foods. The draft calculates no factors.

## Reading the CSV

`value_exactly_as_published` and `unit_as_published` remain text. Empty fields are deliberate. `product_ban` has no numeric concentration; `no_individual_limit` records explicit absence in a specified instrument; `unconfirmed_limit` carries TODO; `indicator` is not a statutory ceiling. All values require their notes and exact category scope. The `date` field identifies the source's published edition date, not a claimed effective or review date. `reviewed_on` records this run.

The three TODO value rows are EU-W-01, EU-W-02 and CA-01. Other records confirmed in an older edition can still have a current-status TODO in notes. Those are counted separately from empty unconfirmed-value rows.

The table has no CAS or DOI field. Chemical identifiers were not needed for this bounded draft and none was invented. No occurrence research or commercial summary supplied a limit.
