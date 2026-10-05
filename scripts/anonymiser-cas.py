from pathlib import Path
import io
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parent.parent
SURNAME = ''.join(map(chr, [65, 77, 82, 65, 78, 73]))
CHANGED = []
TEXT_EXTENSIONS = {'.md', '.html', '.json', '.js', '.mjs', '.css', '.txt', '.xml', '.yml', '.yaml', '.csv', '.py', '.ps1'}

def anonymise(text):
    text = re.sub(r'nadia\.' + SURNAME + r'@example\.invalid', 'nadia@example.invalid', text, flags=re.I)
    text = re.sub(r'"nom"\s*:\s*"' + SURNAME + '"', '"civilite": "Madame"', text, flags=re.I)
    text = re.sub(r'Nom\s*:\s*' + SURNAME + r'\.\s*Prénom\s*:\s*Nadia\.', 'Appellation : Madame Nadia.', text, flags=re.I)
    text = re.sub(r'(?:Madame\s+)?Nadia\s+' + SURNAME, 'Madame Nadia', text, flags=re.I)
    return re.sub(SURNAME, 'Madame Nadia', text, flags=re.I)

def transform(data, name):
    suffix = Path(name).suffix.lower()
    if suffix in {'.zip', '.docx'}:
        result = io.BytesIO()
        changed = False
        with zipfile.ZipFile(io.BytesIO(data)) as source, zipfile.ZipFile(result, 'w') as target:
            target.comment = anonymise(source.comment.decode('utf8', errors='replace')).encode('utf8')
            for info in source.infolist():
                original = source.read(info)
                replacement = transform(original, info.filename)
                new_name = anonymise(info.filename)
                changed |= replacement != original or new_name != info.filename
                info.filename = new_name
                info.comment = anonymise(info.comment.decode('utf8', errors='replace')).encode('utf8')
                target.writestr(info, replacement)
        return result.getvalue() if changed else data
    if suffix in TEXT_EXTENSIONS:
        try:
            original = data.decode('utf8')
        except UnicodeDecodeError:
            return data
        return anonymise(original).encode('utf8')
    return data

for folder in ['documents', 'docs', 'mon-dossier-challenge-100j', 'mini-site-seance-04', 'sources-fournies', 'travail-personnel']:
    for file in (ROOT / folder).rglob('*'):
        if not file.is_file() or 'node_modules' in file.parts or 'dist' in file.parts:
            continue
        original = file.read_bytes()
        replacement = transform(original, file.name)
        if replacement != original:
            file.write_bytes(replacement)
            CHANGED.append(str(file.relative_to(ROOT)))
for file in ROOT.glob('*.md'):
    original = file.read_bytes()
    replacement = transform(original, file.name)
    if replacement != original:
        file.write_bytes(replacement)
        CHANGED.append(file.name)
print(json.dumps({'fichiers_modifies': len(CHANGED), 'fichiers': CHANGED}, ensure_ascii=True))
