from pathlib import Path
import io
import json
import zipfile

ROOT = Path(__file__).resolve().parent.parent
BOM = b'\xef\xbb\xbf'
changes = []
repairs = {
    'Ex?cution': 'Exécution', 'ex?cution': 'exécution', 'Ex?cut?': 'Exécuté', 'ex?cut?': 'exécuté',
    'r?dactionnelle': 'rédactionnelle', ' ? la demande': ' à la demande',
    's?par?': 'séparé', 'attest?e': 'attestée', 'p?dagogique ?': 'pédagogique —',
    'p?dagogique': 'pédagogique', ' ? effectuer': ' à effectuer', 'pr?pare': 'prépare',
    'adapt?': 'adapté', 'd?marrage': 'démarrage', 'ind?pendante': 'indépendante',
    'priorit?s': 'priorités', 'r?sultats': 'résultats', 'pr?cise': 'précise',
    'premi?re': 'première', '?ch?ance': 'échéance',
    'para?t': 'paraît', 'r?duis': 'réduis', 'p?rim?tre': 'périmètre',
    'r?server': 'réserver', 'cr?neaux': 'créneaux', 'cr?neau': 'créneau',
    'apr?s': 'après', 'Apr?s': 'Après', 'd?j?': 'déjà', 'pr?vois': 'prévois',
    'dur?e': 'durée', 'n?cessaire': 'nécessaire', 'd?passent': 'dépassent',
    't?che': 'tâche', 'plut?t': 'plutôt', 'impr?vus': 'imprévus', 'impr?vu': 'imprévu',
    'Lorsqu?une': 'Lorsqu’une', 'difficult?': 'difficulté', 'appara?t': 'apparaît',
    'r?organise': 'réorganise', 'pr?parer': 'préparer', 'limit?e': 'limitée',
    '?tait': 'était', 'pr?vu': 'prévu', 'a ?t? r?alis?': 'a été réalisé',
    'pr?vu ? ce': 'prévu à ce', 'prévu ? ce': 'prévu à ce',
    'r?serve': 'réserve', ' ? poser': ' à poser', 'd?place': 'déplace',
    'l?action': 'l’action', 'concern?e': 'concernée', 'j?inscris': 'j’inscris',
    'corrig?e': 'corrigée', 'propos?e': 'proposée', 'r?organisation': 'réorganisation',
    'g?n?rale': 'générale', 'pr?ciser': 'préciser', 'r?serv?': 'réservé',
    'd?crit': 'décrit', 'r?ponse ? une': 'réponse à une',
    'd?placer': 'déplacer', 'd?clar?e': 'déclarée', 'accept?e': 'acceptée',
    'conserv?es': 'conservées', 'Contr?le': 'Contrôle', 'contr?le': 'contrôle',
    'r?ellement': 'réellement', '?crits': 'écrits', 'Non attribu?e': 'Non attribuée',
    '? organiser': 'À organiser', '? effectuer': 'À effectuer',
    ' ? compl?ter': ' à compléter', ': ? compl?ter': ': à compléter',
    'Responsabilit?': 'Responsabilité', '?ch?ance : ? choisir': 'Échéance : à choisir',
    'échéance : ? choisir': 'Échéance : à choisir',
    ': ? choisir': ': à choisir', 'mod?le': 'modèle', 'Non effectu?s': 'Non effectués',
    'connect?': 'connecté', 'restent ? v?rifier': 'restent à vérifier',
    'Non modifi?s': 'Non modifiés', 'd?p?t': 'dépôt', 'pr?sent': 'présent',
    'Non effectu?e': 'Non effectuée', 'pr?t ? examiner': 'prêt à examiner',
    'bin?me': 'binôme', 'appliqu?': 'appliqué',
    'r?f?rences': 'références', 'pr?serv?es': 'préservées',
    'r?ponse': 'réponse',
    'attribu?': 'attribué', 'ou ? Nadia': 'ou à Nadia', 'activit?': 'activité',
    ' ? terminer': ' à terminer', 'r?aliste': 'réaliste', 'r?sultat': 'résultat',
    'fix?s': 'fixés', 'disponibilit?s': 'disponibilités', 'r?pond': 'répond',
    'cadrage ? ': 'cadrage « ', 'imprévu ?.': 'imprévu ».', 'm?thode': 'méthode',
    '?crans': 'écrans',
}

def fix_generated(text):
    for before, after in repairs.items():
        text = text.replace(before, after)
    return text

def transform(data, name):
    suffix = Path(name).suffix.lower()
    if suffix in {'.zip', '.docx'}:
        output = io.BytesIO()
        changed = False
        with zipfile.ZipFile(io.BytesIO(data)) as source, zipfile.ZipFile(output, 'w') as target:
            target.comment = source.comment
            for info in source.infolist():
                original = source.read(info)
                corrected = transform(original, info.filename)
                changed |= corrected != original
                target.writestr(info, corrected)
        return output.getvalue() if changed else data
    if suffix in {'.md', '.txt', '.csv'}:
        text = data.decode('utf-8-sig')
        return BOM + text.encode('utf8')
    return data

# Restaurer uniquement les fichiers de l'essai généré dont les accents avaient été perdus.
for folder in (ROOT / 'travail-personnel').glob('essai-nadia-*'):
    for file in folder.iterdir():
        if file.is_file() and file.suffix in {'.md', '.json'}:
            original = file.read_bytes()
            corrected = fix_generated(original.decode('utf-8-sig')).encode('utf8')
            if corrected != original:
                file.write_bytes(corrected)
                changes.append(str(file.relative_to(ROOT)))

for file in ROOT.rglob('*'):
    if not file.is_file() or any(part in {'node_modules', '.git', 'dist'} for part in file.parts):
        continue
    original = file.read_bytes()
    corrected = transform(original, file.name)
    if corrected != original:
        file.write_bytes(corrected)
        changes.append(str(file.relative_to(ROOT)))
print(json.dumps({'fichiers_corriges_ou_utf8_explicite': len(set(changes))}, ensure_ascii=True))
