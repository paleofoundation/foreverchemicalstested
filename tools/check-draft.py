"""Validate the bounded draft without network access or regulatory calculations."""
from pathlib import Path
from urllib.parse import urlparse, unquote
from collections import Counter
import csv
import json
import re

root = Path(__file__).resolve().parents[1]
errors = []
def check(condition, message):
    if not condition:
        errors.append(message)

with (root / 'LIMITS-SOURCES.csv').open(newline='', encoding='utf-8') as handle:
    reader = csv.DictReader(handle)
    fields = reader.fieldnames
    rows = list(reader)
required = {'source_id', 'agency', 'document', 'date', 'section', 'URL',
            'analyte_scope_as_published', 'value_exactly_as_published',
            'unit_as_published', 'product_category', 'notes', 'record_type',
            'verification_status', 'source_language', 'reviewed_on'}
check(set(fields) == required, 'CSV schema mismatch')
check(all(None not in row for row in rows), 'Malformed CSV row')
ids = [row['source_id'] for row in rows]
check(len(ids) == len(set(ids)), 'Duplicate source IDs')
hosts = {'www.federalregister.gov', 'eur-lex.europa.eu', 'www.retsinformation.dk',
         'en.foedevarestyrelsen.dk', 'www.revisor.mn.gov', 'leginfo.legislature.ca.gov'}
for row in rows:
    id = row['source_id']
    for field in required - {'value_exactly_as_published', 'unit_as_published'}:
        check(bool(row[field].strip()), f'{id}: missing {field}')
    check(urlparse(row['URL']).scheme == 'https', f'{id}: non-HTTPS source')
    check(urlparse(row['URL']).hostname in hosts, f'{id}: unapproved source host')
    value, unit = row['value_exactly_as_published'], row['unit_as_published']
    if row['record_type'] in {'numeric_limit', 'indicator'}:
        check(bool(re.fullmatch(r'[0-9]+(?:[.,][0-9]+)?', value)), f'{id}: invalid literal value')
        check(bool(unit), f'{id}: missing source unit')
        check(row['verification_status'] == 'confirmed_in_cited_edition', f'{id}: unverified numeric value')
    else:
        check(value == '' and unit == '', f'{id}: nonnumeric role acquired value/unit')
    if row['record_type'] == 'unconfirmed_limit':
        check('TODO' in row['notes'], f'{id}: missing TODO explanation')
    if id.startswith('EU-F-'):
        check(unit == 'μg/kg' and row['source_language'] == 'sv', f'{id}: source basis changed')
        check('Wet weight' in row['notes'] and 'lower-bound' in row['notes'], f'{id}: lost sum/basis caveat')

catalog = json.loads((root / 'data/standards/categories.json').read_text())
check(catalog['approved'] is False, 'Catalog unexpectedly approved')
cats = catalog['categories']
check(len({c['slug'] for c in cats}) == len(cats), 'Duplicate category slugs')
gaps = (root / 'GAPS.md').read_text()
gap_ids = set(re.findall(r'^\| (G-\d+) \|', gaps, re.M))
used = set()
for cat in cats:
    slug = cat['slug']
    check(cat['ics_ceiling'] is None and cat['status'] == 'draft_on_hold', f'{slug}: unintended ceiling/status')
    page = root / 'content/standards' / f'{slug}.md'
    check(page.exists(), f'{slug}: missing standard')
    text = page.read_text()
    check('effective_date: null' in text and 'approved: false' in text, f'{slug}: activation marker')
    check('## Scheduled retesting' in text and '../program/retesting.md' in text, f'{slug}: missing schedule')
    check('no regulatory limit; no ICS ceiling set' in text, f'{slug}: missing absence disposition')
    for id in cat['source_ids']:
        check(id in ids and f'[{id}](' in text, f'{slug}: invalid source mapping {id}')
        used.add(id)
    check(set(cat['gap_ids']).issubset(gap_ids), f'{slug}: invalid gap mapping')
check(used == set(ids), 'Source rows missing category mapping')

files = [p for p in root.rglob('*') if p.is_file() and '.git' not in p.parts]
for path in files:
    if path.suffix not in {'.md', '.json', '.csv', '.py'}:
        continue
    content = path.read_text()
    check(chr(0x2014) not in content and ('&m' + 'dash;') not in content, f'{path.relative_to(root)}: prohibited dash')
    check(('part' + 'ner') not in content.lower(), f'{path.relative_to(root)}: prohibited terminology')
    if path.suffix == '.md':
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if target.startswith(('https://', 'http://', '#')):
                continue
            resolved = (path.parent / unquote(target.split('#')[0])).resolve()
            check(resolved.is_relative_to(root) and resolved.exists(), f'{path.relative_to(root)}: broken local link {target}')

result = {
    'status': 'PASS' if not errors else 'FAIL',
    'source_rows': len(rows),
    'record_types': dict(Counter(r['record_type'] for r in rows)),
    'numeric_value_rows': sum(bool(r['value_exactly_as_published']) for r in rows),
    'empty_TODO_value_rows': sum(r['record_type'] == 'unconfirmed_limit' for r in rows),
    'category_pages': len(cats), 'tracked_gaps': len(gap_ids),
    'approved_ics_ceilings': sum(c['ics_ceiling'] is not None for c in cats),
    'errors': errors,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
