# 스페인 교재 한국어 문자 통합: 최신 추가 안내

## 이번 추가 통합 안내

[spain-reusable-text.ko.partial.md](spain-reusable-text.ko.partial.md)는 기존 비상업 연구용 한국어 초안 36개를 각 1회, 전체 파일의 원래 바이트 그대로 모은 **부분 통합본**이다. 전체 278쪽 완역이나 상용 재사용 가능 판정이 아니다.

원전은 스페인 교육·문화·체육부, *Historia de España. Manual para estudiantes de español de las Secciones Bilingües*, 2016-11-28, NIPO 030-16-656-0이다. [원본 PDF](source-es.pdf)는 278쪽·14,018,454바이트이며 SHA-256은 52f69a10d2ad5c679b922a39b185065438b1211554abef0fa3c134010ab251ab이다. [기존 확보 기록](source-manifest.json)의 미러·공식 목록을 유지했다.

CC BY-NC-SA 이름은 표시되어 있으나 버전은 미명시다. 임의로 3.0·4.0을 지정하지 않는다. 출처표시·비상업·동일조건 연구 한정이며 권리 소유·전체 재배포·상업 이용을 보장하지 않는다. 상용 앱·DB·템플릿에 통합하지 않았다. 원저자 승인·공식 한국어판도 아니다.

기존 [README.partial-ko.md](README.partial-ko.md), [개념 진행표](README.concepts-progress.ko.md), [교사용 진행표](README.teacher-progress.ko.md)를 수정하지 않고 이 추가 안내를 새로 두었다. 앞선 기록의 ‘개념·교사용 미번역’은 당시 단계의 설명이다. 아래 추가 완료 범위를 반영해 읽되, 기존의 외부 자료·권리 보류까지 해제된 것으로 해석하지 않는다.

## 정확한 구성 선택

| 구성 | 선택한 기존 파일 | 범위와 상태 |
| --- | --- | --- |
| 교수학습 안내 | 00-didactic-guide.ko.draft.md | PDF 5–6쪽 문자 초안. 아이콘 그림 제외 |
| 주요 서술 본문 | eight-chapters-main-prose.ko.draft.md 1개 | 8장·32쪽. 개별 본문 8개를 다시 붙이지 않음 |
| 비교연표 | chronology-01~08.ko.draft.md 8개 | 별도 합본 없음. 총 147행·지역 빈칸 222개·연도 빈칸 1개 |
| 학생 활동 | 01~08-activities-author-prose.ko.draft.md 8개 | 저자 지시·질문 등. 원문 범위 67쪽의 완역이 아님 |
| 역사 개념 | 01~08-concepts-attributed.ko.draft.md 8개 | 표제어 203개: 정의 전문 초안 190, 부분 1, 정의 전체 보류 12 |
| 개념 부록 대응 | concepts-appendix-index.ko.md 1개 | 203개 정의는 장별과 동일. 정의 재수록 없이 대응 색인만 포함, 신규 고유 정의 0 |
| 교사용 앞부분 | teacher-00-frontmatter.ko.draft.md 1개 | 표지·저자·목차 문자 및 빈 쪽·뒤표지 경계 기록 |
| 교사용 안내·답안 | teacher-01~08-guidance-answers.ko.draft.md 8개 | 새 저자 문자 1차 처리, 학생용 중복은 기존 정확한 파일·절 링크 유지 |

‘정의 전문 초안 190개’는 정의 범위의 번역 상태이며 전문 교열·독창성·권리 확인 완료 수가 아니다. 부록 203개를 새 번역 203개로 더하지 않는다.

교사용 176–278쪽의 **103쪽 구조·권리 경계 검토**, **85쪽 개별 렌더 대조**, **8장 새 저자 문자·중복 연결·보류 표시 1차 처리**는 서로 다른 상태다. 이 세 수치를 교사용 103쪽 완역·최종 감수 완료로 합치지 않는다. 이번 통합은 기존 QA 기록을 승계하고 파일 무결성을 새로 검사했으며, PDF 전쪽 렌더 감수를 다시 수행하지 않았다.

## 함께 보관할 부속 기록

- [통합 QA](spain-reusable-text.qa.partial.json): 원바이트 구간·전체 문자열 1회·원문 파일별 보존·선택 및 중복 배제·상대 링크 검사.
- [통합 manifest](spain-reusable-text.manifest.partial.json): 36개 구성 순서·범위·SHA-256·바이트 구간과 산출물 해시.
- [학생용 manifest](translation-manifest.partial.json), [개념 manifest](concepts-translation-manifest.partial.json), [교사용 manifest](teacher-translation-manifest.partial.json): 각 이전 단계의 상세 범위·검증.
- [학생용 권리목록](rights-inventory.student.partial-ko.md), [교사용 권리목록](teacher-rights-inventory.ko.md), [개념 QA](concepts-qa.partial.json), [교사용 QA](teacher-qa.partial.json), [교사용 쪽별 기록](teacher-page-coverage.partial.json).

통합본은 현재 564,985바이트, 구성 파일 원바이트 합계는 539,798바이트다. 차이는 새 머리말·목차·구분 표시에 해당한다. 구성 파일은 같은 폴더에서 계속 보관한다. 상대 링크를 바꾸지 않았으므로 통합본 하나만 다른 폴더로 옮기면 부속 기록·장별 참조 링크를 사용할 수 없다.

기존 최상위 60개 파일과 검수용 tmp 하위 137개 파일, 합계 197개의 SHA-256·크기를 통합 전후 비교했다. 원본·번역·QA·manifest와 이전 README를 모두 보존한다. 소스·부속 기록은 수록 내용이 아니라 링크로 연결하며, 개별 본문 8개는 선택한 합본 내부에 각각 이미 1회 포함되어 있다.

## 계속 남아 있는 범위

외부 기사·각색문·헌법 직접 인용·의회 연설·가사·표어·사전 정의·지도·사진·이미지 내부 문자·음원·영상과 기존 제외를 그대로 유지했다. 보류 개념 12개와 부분 보류 표어, 교사용 로마시설 정의 10개, 제7장 영화/TV 소개 3건도 그대로다. 교사용 답안에서 같은 자료를 우회 번역하지 않았다. 일반 언어 어휘와 학생용 앞뒤 구성의 전체 한국어판도 완성되지 않았다.

주요 서술 본문의 사건 종점은 2011년이지만 개념·교사용에는 2015·2016년 정보도 있다. 당시 법·정치·권리 설명은 현행 정보가 아니다. 현대사를 포함한 역사·법률·번역 전문 감수는 미완료다.

Francisco Ayén의 별도 교재와 세계관 창작 후보는 이 번역 통합본의 수록 대상이 아니다. 소유권이나 상용 이용 가능성을 새로 판정하지 않았다. 커밋·푸시·앱·DB 변경 없음. 외부 링크 접속·현재 유효성 검사는 이번 작업에서 하지 않았다.
