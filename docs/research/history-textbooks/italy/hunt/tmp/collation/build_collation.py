from pathlib import Path
import re
P=Path('docs/research/history-textbooks/italy/hunt')
def markers(ch):
 t=(P/f'{ch:02d}-main-prose.ko.draft.md').read_text(encoding='utf-8-sig')
 out=[]
 for m in re.finditer(r'\[문맥상 추정: ',t):
  depth=1; i=m.end()
  while depth:
   if t[i]=='[': depth+=1
   elif t[i]==']': depth-=1
   i+=1
  s=t[m.end():i-1]
  if s!='…':out.append(s)
 return out

def write(ch, rows, extras=''):
 ms=markers(ch)
 assert len(ms)==len(rows),(len(ms),len(rows))
 out=[f'# 제{ch}장 훼손 구절 복구 대조초안\n\n작성일: 2026-11-13. William Hunt, History of Italy, Second Edition, Macmillan, 1883.\n\n## 범위와 근거\n\n기존 본문·QA의 문맥 추정 {len(rows)}곳을 같은 판의 Toronto 스캔 이미지와 대조했다. OCR은 탐색에만 사용하고 아래 인쇄면을 직접 확인했다. 기존 Google 스캔의 손상 위치도 비교했다. 기존 본문·QA·원문은 덮어쓰지 않았다.\n\n- 기존 스캔: `../source-scan.pdf`.\n- 대조 스캔: `../source-toronto-1883-scan.pdf`, SHA-256 `65697AE4B66BBF789C5E78214033868D7864B3EDFCDE2B365C5D1700EB0F3CA1`.\n- PDF 쪽수는 파일 처음부터 1로 센 위치다. 아래 위치에서 기존 PDF는 인쇄 쪽+17, 새 PDF는 인쇄 쪽+16이다.\n- 영문은 인쇄면의 행갈이와 행 끝 하이픈만 연결했다. 서체·따옴표 모양은 일반 텍스트로 정리했다.\n']
 for i,(title,pages,en,ko,note) in enumerate(rows,1):
  old=ms[i-1]; ko=old if ko is None else ko
  pos=lambda delta:'~'.join(str(x+delta) for x in pages)
  out.append(f'## {ch:02d}-{i:02d}. {title}\n\n- 위치: 인쇄{pos(0)} / 기존 PDF{pos(17)} / 새 PDF{pos(16)}.\n- 이전 표시: `[문맥상 추정: {old}]`\n\n확인한 영문:\n\n> {en}\n\n수정 한국어(병합 전 교체 후보):\n\n{ko}\n\n판독 결과: {note}\n\n남은 불확실성: 이 구절의 문자 결손은 해소되었다. 역사적 주장·연대·인물관계의 정확성까지 검증했다는 뜻은 아니다.\n')
 if extras: out.append(extras)
 out.append('## 상태와 적용 한계\n\n이 파일은 손상 복구에 한정한 대조초안이다. 원문과 뜻이 일치하는 기존 번역은 불필요하게 다시 쓰지 않았다. 기존 본문의 추정 표지는 아직 그대로이므로 이 기록을 검토한 뒤 별도 병합해야 한다. 역사 오류가 의심되어도 저자의 문장을 다른 역사 사실로 바꾸지 않았다. 전문가 역사 감수와 한국어 최종 교열은 미완료다. 476년 이전 고대사·1874년 이후 현대사 공백과 파생 세계관의 구분은 유지한다. 앱·DB·학습 코퍼스 통합, 커밋·푸시는 하지 않았다.\n')
 f=P/'collation'/f'{ch:02d}-recovered-passages.ko.draft.md'
 f.write_text('\n'.join(out),encoding='utf-8')
 print(f, f.stat().st_size, 'bytes',len(rows),'entries')
