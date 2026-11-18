from pathlib import Path
import re,json
p=Path(__file__).resolve().parents[2];o=p/'tmp/frontmatter-index'
rows=[];page=0
for l in (o/'index-bilingual.tsv').read_text('utf-8').splitlines():
 if l.startswith('§'):page=int(l[1:])
 elif '||' in l:
  en,ko=l.split('||');rows.append({'id':len(rows)+1,'printed_page_start':page,'printed_page_end':page+int(en.startswith(('Bologna,','Florence,','Medici, Salvestro','Sardinia island'))),'english':en,'korean':ko})
alpha={'Abati,':'A','Baccio Valori':'B','Cadorna,':'C','Dandolo,':'D','Education directed':'E','Facino Cane':'F','Gaimar,':'G','Hadrian,':'H','Iconoclasts,':'I','James I.':'J','Kingdom of Italy,':'K','Ladislas,':'L','Machiavelli,':'M','Naples—':'N','Octavian,':'O','Padua,':'P','Quadrilateral,':'Q','Radetzki,':'R','San Marino,':'S','Tagliacozzo,':'T','Ugolino':'U','Vachero,':'V','Waldenses,':'W','Zachary,':'Z'}
intro="""# 『History of Italy』 인쇄 색인 영문·한국어 대조 초안

William Hunt, Macmillan, 1883년 제2판. INDEX → 색인.

## 범위와 읽는 방법

토론토본 PDF 277~287, 인쇄 261~271쪽의 색인 전체를 550개 항목으로 옮겼다. 같은 제목에 여러 사람·소주제·참조번호가 딸린 경우 하나의 원문 항목 안에 모두 유지했다. 항목마다 먼저 영문을 두고 다음 줄에 한국어를 붙였다. 원래의 영어 알파벳 순서와 A~W 및 Z의 표제 순서를 따르며, 원저에는 X·Y 표제가 없다.

- 대조용 영문은 원본 이미지에 따라 OCR을 교정한 작업 전사이다. 행말 분철, 공백, 일부 구두점·서체는 읽기 좋게 정리했으므로 원본 조판의 문자 단위 복제본은 아니다. 인물·지명 표기와 실질 내용, 로마숫자, 참조 쪽수는 유지했다.
- 숫자는 원저의 **인쇄 쪽수**이다. 새 통합 번역 파일의 줄번호나 PDF 위치가 아니다. 각 페이지 제목의 토론토·구글 위치는 별도 표기했다. 구글본 색인은 PDF 280~290이며 본문용 오프셋과 다르다.
- `ib.`는 바로 앞 참조의 ‘같은 쪽’을 뜻한다. 번역에도 `같은 쪽(ib.)`으로 남겼다. `See/see` 및 `which see` 참조는 ‘참조’로 유지했다. 숫자를 새로 추정하여 채우지 않았다.
- 페이지를 넘는 Bologna(261~262), Florence(263~264), Medici(266~267), Sardinia(269~270)는 항목이 시작된 쪽 아래에 이어 붙였다. 다음 쪽의 머리 부분은 중복 번역하지 않았다.
- 한국어 인명·지명은 기존 통합본문의 표기를 우선했다. 원저가 영어식·이탈리아식 등 다른 이름을 쓰는 경우 영문을 함께 보아야 한다. 본문 자체의 표기 변이(피우스/비오, 요한/요한네스 등)를 전부 표준화한 것이 아니다.
- 저자의 오류일 가능성이 있는 왕호·관계·참조번호도 몰래 바꾸지 않았다. 예컨대 Theophanô의 Otto III., Sicily의 50, Milan의 Francis,38 등은 원저 표기를 유지하고 `frontmatter-index-qa.ko.md`에서 구별했다. 색인 번호가 실제 해당 내용을 정확히 가리키는지 전 항목을 역검증한 판은 아니다.
- ‘야만’, ‘참주’, ‘타락’, ‘예속’, ‘해방’ 등은 원저의 19세기 서술과 색인 표현이다. 번역자의 현대적 평가나 역사적 사실 검증 결과가 아니다. 전문 역사 감수·독립 문장별 번역 검수·최종 교열은 미완료다.

원문, 기존 장별 번역·QA, 연대표와 통합본문은 변경하지 않았다. 본문은 대략 476~1870년 및 명시적으로 1874년 시점의 말미 평가까지이며 이후 현대사 공백은 그대로다. 지도 도판·지도 위 모든 지명·출판 광고·디지털화 법률 고지는 이 색인에 합치지 않았다. 권리 및 디지털 파일 이용 주의는 README.md를 따른다.
"""
out=[intro];lastpage=0;checks=[]
for r in rows:
 page=r['printed_page_start'];en=r['english'];ko=r['korean']
 if page!=lastpage:
  out.append(f'\n## 인쇄 {page}쪽 / 토론토 PDF {page+16} / 구글 PDF {page+19}\n');lastpage=page
 for start,letter in alpha.items():
  if en.startswith(start):out.append(f'\n### {letter}.\n')
 suffix=f" (다음 인쇄 {r['printed_page_end']}쪽까지 이어짐)" if r['printed_page_end']>page else ''
 out.append(f"\n- **{r['id']:03d}.** {en}{suffix}\n  - {ko}\n")
 knr=ko;allowances=[]
 for enword,koword in [('Quadruple','4국'),('May','5월'),('September','9월'),('Fourth','제4차')]:
  if enword in en:
   assert koword in knr,(enword,en)
   knr=knr.replace(koword,re.sub(r'\d+','',koword));allowances.append({'english':enword,'korean':koword})
 digits=re.findall(r'\d+',en);kd=re.findall(r'\d+',knr)
 romans=re.findall(r'(?<![A-Za-z])[IVXLCDM]+(?![A-Za-z])',en);kr=re.findall(r'(?<![A-Za-z])[IVXLCDM]+(?![A-Za-z])',ko)
 ib=len(re.findall(r'\bib\.',en));kib=ko.count('(ib.)');see=len(re.findall(r'(?<!Holy )\bsee\b',en,re.I));ksee=ko.count('참조')
 checks.append({'id':r['id'],'head':en.split(',')[0],'printed_pages':[page,r['printed_page_end']],'arabic_tokens':digits,'roman_or_initial_tokens':romans,'ib_count':ib,'see_count':see,'lexical_number_renderings':allowances,'arabic_sequence_matches':digits==kd,'roman_sequence_matches':romans==kr,'ib_count_matches':ib==kib,'see_count_matches':see==ksee})
 for flag in ['arabic_sequence_matches','roman_sequence_matches','ib_count_matches','see_count_matches']:assert checks[-1][flag],(flag,r)
(p/'printed-index.en-ko.draft.md').write_text(''.join(out),encoding='utf-8')
(o/'index-records.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
(o/'index-checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'entries':len(rows),'arabic_numeric_tokens':sum(len(c['arabic_tokens']) for c in checks),'roman_or_initial_tokens':sum(len(c['roman_or_initial_tokens']) for c in checks),'ib':sum(c['ib_count'] for c in checks),'see':sum(c['see_count'] for c in checks),'checks_passed':True,'index_bytes':(p/'printed-index.en-ko.draft.md').stat().st_size},ensure_ascii=False))
