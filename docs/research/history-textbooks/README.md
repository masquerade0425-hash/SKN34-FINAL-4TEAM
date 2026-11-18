# 역사 통사 원문과 한국어 번역 작업

기준일: 2026-11-13. 브랜치: feat/history-templates.

**미국28장·프랑스8장·일본15장 및 부록·중국22장 및 후속자료·이탈리아11장의 지정 범위 번역 초안과 통합본을 저장했다. 영국44장도 역사본문 초안을 모두 저장했으며 한국도63/63장 본문과 서문·서론 통합 초안을 저장했다. 스페인은8장 자작 서술본문·연대표·활동과 추가 개념자료를 저장했으나 권리 보류 항목과 일반 사전어휘 등이 남는다. 국가별 정확한 제외 범위·현대사 공백·권리 조건은 아래와 각 폴더 안내를 따른다. 전문 역사감수·최종 교정·서비스 역사 카드 구현은 미완료다.** 독일은 보류한다. 기존 장르 템플릿·애플리케이션·DB를 수정하지 않았고 커밋·푸시하지 않았다.

## 현재 실제 확보한 자료

### 미국: 28장 한국어 대조 초안 저장 완료

The American Yawp의 현행 웹 교재 28장 모두 직접 HTTP 200으로 확보했다. 공개 홈페이지의 장별 링크를 따라 수집했으며, 각 파일에서 본문 구역과 CC BY-SA 4.0 표시를 확인했다. 첫 장 원주민 기원부터 마지막 장의 2025년 서술까지 포함한다. 최신 웹 판본은 편집될 수 있으므로 이번 로컬 스냅샷과 해시를 기준으로 작업한다.

- 홈페이지: https://www.americanyawp.com/
- 판본 변경 기록: https://www.americanyawp.com/text/updates/
- 공식 이용조건: https://www.americanyawp.com/text/about/
- 라이선스: https://creativecommons.org/licenses/by-sa/4.0/
- 원문 HTML: usa/original-html/ (28개, 총 5,257,863바이트)
- 본문 추출 텍스트: usa/original-text/ (28개, 2,226,508자, 공백 구분 약 334,530단어)
- 위 분량은 각주·참고문헌·목차·그림 설명을 포함한 기계적 집계이며 순수 서술 본문 단어 수와 다르다.
- 원문 URL·파일·SHA-256·HTTP 상태: usa/source-manifest.json
- 추출본 분량·SHA-256·번역 상태: usa/text-manifest.json
- 이용조건 페이지 사본: usa/license-about.html
- 한국어: 미국28장 전체 서술·장 안의 사료 소개문·설명문·참고자료 대조 초안과 장별 통합본을 저장했다. 한 파일 통합본은 usa/american-yawp-28-chapters.ko.draft.md이다. 추천문헌709건·고유주석1,421건의 원어 서지와 한국어 제목·설명을 병기했고, 설명문385회 가운데 CC BY-NC 1회는 별도 파일로 분리했다. 이미지·대체텍스트·그림 속 표 셀·링크된 외부 사료 전문은 제외한다. 최종 문체·용어 통일과 전면 역사감수는 미완료다.
- 파생 세계관: usa/worldbuilding-ko/의 주제별 문서에 후보20개를 저장했다(초기 서론 샘플 별도). 실제 인용과 허구 인물·기관·사건을 구분했으며 서비스 카드·DB에 등록하지 않았다.

원문과 번역/각색의 저자 표시 및 CC BY-SA 4.0 동일조건을 보존한다. 공식 About는 사용·다운로드·배포·수정을 허용한다. 확인한 공식 About와 장별 페이지에서 별도 생성형 AI 이용 금지 조항은 찾지 못했다. 이를 사이트 전체 약관에 대한 법률 검토로 과장하지 않는다. 별도 이미지 파일은 다운로드하지 않았으며, HTML의 이미지 링크가 모든 이미지의 재배포 허락을 뜻하지 않는다. 사진·그림의 재사용은 개별 권리를 확인하기 전까지 제외한다.

### 프랑스: 역사적 교재, 현대판과 구별

Charlotte M. Yonge, History of France (History Primers, 1882).
원문209,182바이트와8개장82개번호절의 한국어 대조 초안을 france/에 저장했다. 통합본 france/eight-chapters.ko.draft.md, 세계관 후보4개는 france/worldbuilding-4-candidates.derived-draft.md이다. 역사본문은 고대 개관~1871년까지이며20–21세기가 빠져 있다. 출판사 광고·전자본 이용고지는 원문에 보존하되 번역에서 제외했다. 19세기 민족·문명 위계 관점과 왕조 중심 설명의 한계가 있다. 현행 교과서라고 소개하지 않는다.

## 다른 나라의 현재 상태

- 영국: Charles Oman, A History of England,11판1904,44장, 고대~1902. 공식PG47753 원문1,881,002바이트를 england/oman-1904/에 저장했다. 학교 상급반·대학시험용 교재이지만20세기 대부분·21세기 부재. 인종·문명위계·제국주의 관점을 현대 합의로 취급하지 않는다. 44장 역사본문과 서문2편을 england/oman-1904/england-44-chapters.ko.draft.md(1,986,614바이트)에 무변경 통합했고 창작 후보2개를 별도 저장했다. 산문 대응단위1,735개와 서문6문단을 구분한다. 원목차·지도30건·계보목록9건과 색인1208표제어(계속블록 포함1212대조블록)도 별도 파일로 저장했다. 광고·실제지도영상·전사자/배포 안내의 한국어 전사는 제외한다.
- 일본: David Murray, Japan,3판1896,15장+부록4개. japan/source-en.txt663,800바이트. 주요 역사서술은1889년헌법·1890년의회예고까지.20–21세기 부재. 헌법조문수 등 원문 오류와 구시대 관점을 README에 경고했다. 서문·본문15장·부록4개·원주1~344의 한국어 통합 대조 초안과 세계관2개를 저장했다. 실제 그림 이미지·목차/표제면 별도 번역·Gutenberg 안내 한국어 번역은 제외했고, 전문가 전수 감수와 현대 공백 보완은 미완료다.
- 중국: Demetrius Charles Boulger, China, Hazeltine 보충장 포함본. china/source-en.txt1,154,261바이트,22장+후속2항목,1898년9월까지. 실제전자판 인쇄연도 미확인,1893초판으로 단정하지 않는다. 강한 서구중심·제국주의 시각이 있다. 번호본문22장488문단과 후속2항28문단, 헌사·서문을 포함한 통합 초안1,229,649바이트를 china/china-complete-text.ko.draft.md에 저장했다. 창작 후보2개는 별도다. 표제지·목차·권두 캡션·실제 이미지·PG 안내의 한국어 전사는 제외하며 전문 검수는 미완료다.
- 에스파냐: 교육부 Historia de España(2016), 외국학생의 스페인어 이중언어 교육용 간략교재. spain/ministry-2016-noncommercial-research/에 전체PDF278쪽(학생용175쪽+교사용자료)을 저장했다.8장 자작서술본문32쪽은 한국어 통합초안으로 저장했으며 세계관 후보3개도 작성했다. 비교연표8쪽147행도 번역했으며, 제1~8장 활동의 저자 작성 본문도 번역 초안으로 저장했다. 외부 인용·사진·가사는 제외했다. 교수학습 안내2쪽과 개념203항목 중190개 전문·1개 부분을 추가 저장했고12개 정의 및 표어1개는 보류했다. 개념부록203항목은 장별 정의와 중복됨을 확인해 대응 색인으로 연결했다. 교사용103쪽도 구조·권리를 검토하고8장 저자 안내·답안의 문자 초안을 별도로 저장했다. 외부 기사·헌법 인용·가사·사전형 정의 등의 재인용 답안은 보류해 전체 완역이 아니다. 일반 사전어휘 등의 제외 범위는 README.concepts-progress.ko.md와 README.teacher-progress.ko.md를 따른다. 주요서술본문 종점은2011년이나 개념부록에는2015·2016년 정보도 있다. 위 재사용 가능 범위36개 구성파일은 spain-reusable-text.ko.partial.md(564,985바이트)로 무변경 통합했으며 전체278쪽 완역은 아니다. 최신 통합범위는 README.reusable-text-progress.ko.md를 따른다. CC BY-NC-SA이나 버전은 원문미표기이며 비상업 조건으로 분리한다. Ayén의 별도 공개교재 첫HTML장 주요자작본문과 세계관1개도 spain/ayen-noncommercial-research/에 보존했다.
- 이탈리아: William Hunt, History of Italy, 실제표제1883제2판, 학교용Historical Course제4권. 원문OCR581,291바이트와 기존Google스캔299쪽6,277,770바이트, 같은판본 토론토스캔296쪽14,373,105바이트를 보존했다. 역사본문11장157절과 연대표4쪽91행의 통합 대조초안569,169바이트를 italy/hunt/integrated-11-chapters.ko.collated-draft.md에 저장했다. 기존2~9장 추정63곳을 새 스캔으로 판독해 통합본에만 반영했고 기존 초안·QA는 보존했다. 전문 역사 감수·전문 교열·전 페이지 양스캔 대조는 미완료이며 문자 결손 복구가 원저의 역사 오류 해결을 뜻하지 않는다. 주된 범위는476~1870년과1874년현재 평가로 고대전체·20~21세기는 없다. 원목차·지도목록과 인쇄색인550개 항목의 별도 대조초안도 저장했다. 지도 내부의 모든 지명·범례 및 출판 광고는 미번역이며 창작 후보2개는 별도 파일이다. 원저 공공영역·스캔 제공조건·웹페이지 권리 표기를 구분한다.
- 한국: Homer B.Hulbert, The History of Korea, Seoul1905 원판2권. korea/hulbert-1905/에 총2,010,860바이트,63장 및색인 원문 저장. 고대~1904년말, 영어 역사개설서이며 한국 국정교과서가 아니다. 후대Weems서문·주석판과 구분한다. 선교사·문명관·옛지명·신화 서술의 한계가 있다. 제1권 고대사1~13장317문단의 통합 초안과 별도 서문·서론20문단을 저장했다. 중세사1~13장과 조선사1~9장 초안도 추가해 제1권35장 전체를 서문·서론과 함께1,189,722바이트 통합초안으로 저장했다. 제2권 I·I-A·II–XXVII의28개 장을 모두 추가해 본문63/63장 초안을 저장했다. 전2권63장 및 서문·서론 통합본은 korea/hulbert-1905/korea-63-chapters.ko.draft.md(2,087,690바이트)이며 표제지·목차와 색인3,144논리 항목도 별도 대조 초안으로 저장했다. 미확정 이름은 영문을 보존하며 실제 인용 쪽 전수 검증은 미완료다. 전수 전문 감수는 미완료다. 고대사 통합본은 보존했고 새 제1권 통합본은 korea/hulbert-1905/vol1-35-chapters.ko.draft.md이다.
- 한국 현대 국정교과서 및 우리역사넷 자료의 전문 재사용 허가는 아직 확인되지 않았다. 한국사연대기·오늘의역사 공공데이터 두 항목의 제4유형 권리를 다른 콘텐츠에 확대 적용하지 않는다.

각 고전의 공식Gutenberg/공개도서관 판권·저자·바이트·해시는 국가별 README와 manifest에 기록했다. 미국 퍼블릭도메인 표기를 전 세계의 법률 보증으로 확대하지 않는다. 원문 확보와 번역 완료, 원문 역사범위와 현대통사 완결성은 각각 구분한다. 현대 후보 비교는 MODERN-CANDIDATES.partial-ko.md를 참조한다.
OpenStax U.S. History의 현행 페이지는 CC BY-NC-SA 표시 외 생성형 AI 이용 제한 문구가 있어 이번 전문 AI 번역 원문으로 채택하지 않았다. 공개 열람 가능 여부와 전문 재사용 권리는 구분했다. 접근 통제 우회는 하지 않았다.

## 완료와 남은 일

- 원문 확보: 미국28개웹장, 프랑스1책, 영국Oman1책, 일본1책, 중국보충장포함1책, 스페인교육부PDF학생용+교사용, 한국Hulbert2권, 이탈리아Hunt전체OCR. 이탈리아OCR과 대조용스캔은 확보했으나 전면대조 미완료, 모든 시대·현대까지를 갖춘8개국 교과서 묶음이라는 뜻은 아니다.
- 번역 초안: 미국28장(기존 제외범위 유지), 프랑스8장 역사본문, 스페인8장 자작서술본문32쪽과Ayén첫HTML장의 주요자작본문. 일본 서문·15장·부록4개·원주1~344도 통합 초안 저장. 이탈리아11장의 지정 훼손63곳을 복구한 통합본과 연대표도 저장했으나 전면 교열·일부 부속자료는 미완료. 중국 번호본문22장·후속2항·헌사·서문도 통합 초안이 있으며 이미지·목차 등 제외 범위는 국가별 안내에 명시했다. 영국44장·서문 통합본과 원목차·색인 부속 초안도 저장했다. 광고·실제 지도영상 등 제외 범위는 국가별 안내를 따른다. 한국의 나머지 장과 스페인의 권리 보류 자료 등은 미완료.
- 창작 후보: 총38개. 미국20개, 프랑스4개, 스페인교육부3개 및Ayén1개, 일본2개, 이탈리아2개, 중국2개, 영국2개, 한국2개이다. 역사 근거·원문 저자 주장·허구를 구별했으며 앱·DB에 등록하지 않았다.
- 남음: 추가 전문번역, 구시대자료의 현대 공백과 편향 보완 여부 결정, 저자별 권리 유지, 전면 역사감수·최종교정, 세계관의 서비스규격 검토와 구현.
- VALIDATION-REPORT.json 및 FACT-CHECK.partial-ko.md는 미국 작업의 검증 범위와 표본·특정주장 검증 기록이다. 새 국가 전체의 사실 검증 완료를 뜻하지 않는다.
## 통합 초안 파일

- usa/01-american-origins.ko.draft.md
- usa/02-making-an-atlantic-world.ko.draft.md
- usa/03-colliding-cultures.ko.draft.md
- usa/04-british-north-america.ko.draft.md
- usa/05-colonial-society.ko.draft.md
- usa/06-the-american-revolution.ko.draft.md
- usa/07-a-new-nation.ko.draft.md
- usa/08-the-early-republic.ko.draft.md
- usa/09-getting-forward.ko.draft.md
- usa/10-american-democracy.ko.draft.md
- usa/11-growth-and-conflict.ko.draft.md
- usa/12-the-national-crisis.ko.draft.md
- usa/13-the-civil-war.ko.draft.md
- usa/14-reconstruction.ko.draft.md
- usa/15-capital-and-labor.ko.draft.md
- usa/16-geographies-of-empire.ko.draft.md
- usa/17-new-lives.ko.draft.md
- usa/18-the-progressive-era.ko.draft.md
- usa/19-world-war-i.ko.draft.md
- usa/20-the-new-era.ko.draft.md
- usa/21-the-great-depression.ko.draft.md
- usa/22-world-war-ii.ko.draft.md
- usa/23-the-cold-war.ko.draft.md
- usa/24-the-affluent-society.ko.draft.md
- usa/25-the-sixties.ko.draft.md
- usa/26-the-unraveling.ko.draft.md
- usa/27-the-triumph-of-the-right.ko.draft.md
- usa/28-american-carnage.ko.draft.md


각 장 파일은 해당 장에 한정된다. 전체28장 통합본도 함께 저장했으며 전문 감수는 미완료다. 각 절의 범위·출처·검수 메모도 보존했다. 제3장 그림3.4 설명은 CC BY-NC 4.0이므로 일반 본문과 권리를 구분하여 별도 파일에 보관했다.

## 별도 사실검증

FACT-CHECK.partial-ko.md에 공식 출처로 확인한 오류와 확인 대기 항목을 구분했다. 제2장의 세라1789년 샌디에이고 선교소 설립 주장은 미국 의회 공식 자료의1769년 설립·1784년 사망과 충돌한다. 원문과 충실 번역을 보존하면서 정정 근거를 별도로 제시했다. 공개 라이선스는 정확성 보증이 아니며 이 번역을 검증 완료된 역사 정답 데이터로 취급하면 안 된다.

문서·자료만 추가했으므로 저장소 지침에 따라 애플리케이션 테스트·빌드는 실행하지 않았다. 기존 장르·앱·DB는 변경하지 않았고 커밋·푸시하지 않았다. ‘전문 확보’는 원문 직접 수집 완료이며 번역 완료나 역사적 정확성 보증이 아니다.


## 전체 통합본과 검증 기록

- usa/american-yawp-28-chapters.ko.draft.md: 28장 한 파일 통합본(전문 감수 미완료).
- usa/translation-files-manifest.json: 번역 파일·통합본의 크기와 SHA-256 목록.
- SOURCE-QUALITY-REVIEW.partial-ko.md: 확인된 오류와 추가 검증 대상 구분.
- FACT-CHECK.partial-ko.md: 공식·학술 출처로 대조한7개 특정 주장. 나머지 원문 전체 검증을 뜻하지 않는다.

## 별도 현대 유럽 참고 원문

PCC Christopher Brooks, Western Civilization:A Concise History 제3권 V3.0(2024)의 공식 공개 원문TXT697,934바이트·DOCX13,199,356바이트를 europe-modern-reference-noncommercial/에 분리보관했다. 국가별 통사를 대체하는 자료가 아니며 전체번역은 시작하지 않았다. CC BY-NC-SA4.0 본문과 Fair Use 등 개별이미지권리를 구별해야 하고, 확인된 사실오류가 있어 무교정 정답자료로 채택하지 않는다. 판본·실제시대범위·표본대조와 출처는 그 폴더 README.ko.md와 VERIFICATION.partial-ko.md를 따른다. 기존8개국 번역과 독일보류상태는 변경하지 않는다.

## 통합 파일 찾아보기

[국가별 통합 초안 빠른 안내](READING-INDEX.ko.md)와 [현재 크기·해시 목록](CURRENT-COLLECTION.manifest.json)을 추가했다. 이 목록은 실제 파일 위치와 지정 범위를 정리한 것이며 현대사 공백·권리 보류·전문 감수 미완료를 해소한 것은 아니다.


## PG 전사판 표제와 미완료 범위

한국 제2권의 I-A는 원서 인쇄 표제가 아니라, XI로 오인쇄된 두 번째 장을 구분하기 위해 PG 전사자가 붙인 식별자다. 전사자주17882–17884행이 근거이며 X가 XX로 인쇄된 오류도 함께 적혀 있다. 내용 단위35+28=63이라는 집계는 유지하되 이 표기를 원서의 정확한 인쇄 표제라고 부르지 않는다.

[현대 통사·세계관 검수·서비스 적용의 남은 범위](REMAINING-SCOPE.ko.md)를 별도 정리했다. 저작권·품질 불명 자료를 추가 채택하거나 현대사 공백을 임의로 메우지 않았다. 서비스 구현·DB 등록·최종 고증 완료로 표시하지 않는다.
