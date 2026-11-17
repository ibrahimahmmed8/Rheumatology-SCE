import fitz,re,json,collections
from pathlib import Path
src=Path('/mnt/data/Rheumatology_SCE_Question_Bank_Corrected (1).pdf')
dst=Path(__file__).parent
pdf=fitz.open(src)
raw='\n'.join(page.get_text(sort=True) for page in pdf)
markers=list(re.finditer(r'(?m)^Question\s+(\d+)\s*$',raw))
questions=[]; problems=[]
for i,m in enumerate(markers):
    body=raw[m.end():markers[i+1].start() if i+1<len(markers) else len(raw)]
    lines=[s.strip() for s in body.splitlines() if s.strip()]
    option_indices=[j for j,s in enumerate(lines) if re.match(r'^[A-E]\.\s+',s)]
    answer_indices=[j for j,s in enumerate(lines) if s.startswith('Answer:')]
    if len(option_indices)!=5 or len(answer_indices)!=1:
        problems.append((int(m.group(1)),len(option_indices),len(answer_indices)));continue
    ai=answer_indices[0]
    if option_indices != sorted(option_indices) or option_indices[-1]>=ai:
        problems.append((int(m.group(1)),'order'));continue
    stem=' '.join(lines[:option_indices[0]])
    options={}
    for idx,j in enumerate(option_indices):
        end=option_indices[idx+1] if idx<4 else ai
        piece=' '.join(lines[j:end]); letter=piece[0];options[letter]=piece[3:].strip()
    ans=' '.join(lines[ai:])
    match=re.match(r'^Answer:\s*([A-E])\.\s*',ans)
    if not match:
        problems.append((int(m.group(1)),'answer format'));continue
    correct=match.group(1)
    rem=ans[match.end():].strip()
    # Remove the repeated answer label, including if it wrapped to more than one line.
    correct_text=options[correct]
    clean=lambda x:re.sub(r'\s+',' ',x).strip()
    normal=lambda s:re.sub(r'\s*-\s*','-',re.sub(r'\s+',' ',s)).strip()
    rem_normal=normal(rem); option_normal=normal(correct_text)
    if rem_normal.startswith(option_normal):
        explanation=rem_normal[len(option_normal):].strip()
    else:
        # Extract text remaining after the answer option by word-level matching.
        words=correct_text.split(); remwords=rem.split(); k=0
        while k<min(len(words),len(remwords)) and words[k].strip()==remwords[k].strip():k+=1
        if k>=max(1,len(words)-2):explanation=' '.join(remwords[k:])
        else:
            problems.append((int(m.group(1)),'answer text mismatch',correct_text[:80],rem[:80])); explanation=rem
    explanation=re.sub(r'\s*Questions\s+\d+\s*[-–]\s*\d+\s*$','',explanation).strip()
    questions.append({'id':int(m.group(1)),'stem':stem,'options':options,'answer':correct,'explanation':explanation})
(dst/'questions.json').write_text(json.dumps(questions,ensure_ascii=False,separators=(',',':')),encoding='utf8')
print('extracted',len(questions),'issues',len(problems),problems[:30]);print('nonempty',sum(bool(q['explanation']) for q in questions));print('answer distribution',collections.Counter(q['answer'] for q in questions));print('file bytes',(dst/'questions.json').stat().st_size)
