from pathlib import Path
import hashlib, json, re, unicodedata
from pypdf import PdfReader

root = Path('Giữa Kỳ/22-24')
out = Path('tmp/study_audit/exam-mlq')
out.mkdir(parents=True, exist_ok=True)
manifest = []
def norm(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn').replace('đ', 'd')
terms = re.compile(r'\bmlfq\b|\bmlq\b|multilevel|multi.level|da muc|da cap|hang doi.{0,30}phan hoi|feedback|cap uu tien|nhieu muc|nhieu cap', re.I)
stop = re.compile(r'^\s*(?:đáp\s*án|hướng\s*dẫn\s*giải|lời\s*giải|answer\s*key)\s*[:\-]?\s*$', re.I)
for f in sorted(root.glob('*.pdf')):
    doc = PdfReader(f)
    blocks, hits, ended = [], [], False
    lens = []
    for i, p in enumerate(doc.pages):
        if ended: break
        t = p.extract_text()
        lines = t.splitlines()
        for j, line in enumerate(lines):
            if stop.match(line):
                lines = lines[:j]
                ended = True
                break
        t = '\n'.join(lines)
        lens.append(len(t))
        blocks.append(f'\n--- PDF PAGE {i+1} ---\n{t}\n')
        for j, line in enumerate(lines):
            if terms.search(norm(line)):
                hits.append({'page':i+1, 'context':'\n'.join(lines[max(0,j-3):min(len(lines),j+4)])})
    cache = out / (hashlib.sha256(str(f).encode()).hexdigest()[:12] + '.txt')
    cache.write_text(''.join(blocks), encoding='utf-8')
    manifest.append({'file':str(f), 'sha256':hashlib.sha256(f.read_bytes()).hexdigest(), 'pages':len(doc.pages), 'pages_checked':len(lens), 'char_counts':lens, 'answer_section_stopped':ended, 'cache':str(cache), 'hits':hits})
(out/'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(manifest, ensure_ascii=False, indent=2))
