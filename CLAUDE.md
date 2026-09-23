# voice-box

런주호 콘텐츠 제작 저장소. 여기서 작업하는 모든 Claude 세션이 참고할 것.

## 카드/비주얼 디자인 톤 (2026-09-23 확정)

애플 스타일. 카드뉴스, 썸네일, 배너 등 **비주얼 콘텐츠를 새로 만들거나 고칠 때는 아래 톤을 기본값으로 쓴다.**
사용자가 특정 소재에 한해 다른 스타일을 명시하면 그 지시가 우선한다.

### 색상
| 토큰 | 값 | 용도 |
|---|---|---|
| 배경 | `#000000` | 순정 블랙 |
| 텍스트 | `#F5F5F7` | 기본 텍스트 (애플 시스템 화이트) |
| 보조 텍스트 | `#86868B` | 캡션, 라벨 (애플 시스템 그레이) |
| 포인트 | `#0A84FF` | 유일한 액센트 컬러 (애플 다크모드 시스템 블루). 호버/보조로 `#409CFF` |
| 구분선 | `rgba(245,245,247,.14)` | 헤어라인 |
| 채움 | `rgba(255,255,255,.06)` | 패널/타일 배경 |

포인트 컬러는 하나만 쓴다. 대체 스와치가 필요하면 애플 시스템 컬러 계열(`#5E5CE6` 인디고, `#64D2FF` 틸)로 확장.

### 타이포그래피
시스템 폰트 스택만 쓴다. 커스텀 디스플레이 서체(블랙한산스 등)를 쓰지 않는다 — 위계는 굵기로 표현.

```
--sans: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
--display: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Apple SD Gothic Neo', sans-serif;
```

한글은 `Apple SD Gothic Neo`가 애플이 실제로 쓰는 조합이라 폴백에 반드시 포함한다.

### 레이아웃
- 라운드 코너 필수: 패널/타일 20px, 슬랩/좁은 로우 16px, 필(pill)·버튼·핸들은 999px(캡슐)
- 각진 사각형, 진한 색 블록의 배지, 좌측 컬러바(border-left) 지양 — 색은 면이 아니라 얇은 강조로만
- 넓은 여백, 스펙 숫자는 초대형 볼드 + 작은 라벨(애플 제품 스펙 페이지 참조)
- 액센트 컬러를 배경으로 채운 블록은 텍스트를 화이트(`#FFFFFF`)로 — 블루 위에 검정 텍스트 쓰지 말 것

## cards/

인스타그램 카드 캐러셀 소스.

### 결과물 전달 방식 (2026-09-23 확정 — 이 방식만 쓴다)

사용자는 **카톡으로 받은 링크를 카톡 인앱 브라우저에서 바로 열고, "전체 저장" 한 번 → 공유 시트 "이미지 N개 저장"으로 사진 앱에 한 번에 저장**한다. 트랜스제주 때부터 쓰던 방식.

- **클로드 아티팩트(claude.ai/artifact) 링크로 보내지 않는다.** iframe 안이라 공유 시트(여러 장 저장)가 막힌다.
- **jsdelivr 로 호스팅하지 않는다.** HTML 을 text/plain 으로 내보내 페이지로 안 열린다.
- ZIP, 한 장씩 저장 확인창 방식도 원하지 않는다.
- 호스팅은 Higgsfield `media_upload`(일반 파일) → `https://d2ol7oe51mr4n9.cloudfront.net/user_3EZ4QOXFWGtMb7s78DjLab81Lak/<id>.<ext>` 독립 페이지.
- 카드는 **미리 JPG 로 뽑아 올리고**, 페이지엔 `<img>` 만 싣는다 (길게 눌러 한 장 저장도 되게). 폰에서 html2canvas 로 그리지 않는다.
- 공유는 `navigator.share({ files })` — **파일만** 넘긴다. title·text 를 같이 넘기면 iOS 가 "이미지 N개 저장" 항목을 뺀다.

순서:
1. 카드 내용 수정 → `python3 cards/build_page.py` (standalone.html·export.html 생성)
2. `node cards/render_cards.mjs` → `cards/out/card-XX.png`, 이어서 JPG(q92)로 변환
3. `media_upload` files[] 로 JPG 업로드(PUT) → `media_confirm` → URL 들을 `cards/share_images.json` 에 저장
4. `python3 cards/build_share.py` → `cards/share.html` (약 7KB)
5. `media_upload`(text/html)로 share.html 업로드 → confirm → Higgsfield `sandbox_exec` 로 CloudFront URL 이 text/html·이미지 200 인지 확인 (이 세션 네트워크에선 CloudFront 가 막혀 있음)
6. 카톡(PlayMCP 나에게 보내기)으로 share.html 링크 전송

### 파일

- `cards/build_page.py` — 카드 마크업 원본. `export.html`(아티팩트용, 참고)·`standalone.html`(렌더용 완전한 문서) 생성
- `cards/render_cards.mjs` — standalone.html 을 열어 카드 9장을 1080×1350 PNG 로 저장
- `cards/build_share.py`, `cards/share_images.json`, `cards/share.html` — 카톡 전달용 공유 페이지
- `cards/out/card-XX.jpg` — 업로드한 카드 이미지 (PNG 는 커밋 안 함)
- `cards/caption.md` — 업로드 캡션, 커버 문구 대안, 첫 댓글 (두 빌더가 모두 읽는다)
- `cards/vendor/html2canvas.min.js` — 렌더용(인라인)
- `cards/assets/*.png` — 카드에 들어간 제품 컷
- `cards/project/*` — 예전 캔버스 소스. 더 안 씀.

### 콘텐츠 규칙

- 과장 금지. 확인 안 된 수치는 "미공개"나 "확인 필요"로 둔다.
- 발매 전 프리뷰·루머 기사 수치는 확정처럼 쓰지 않는다. 발매 후엔 실제 판매처 스펙시트나 브랜드 공식 발표를 우선하고, 하나뿐이면 다른 출처와 교차 확인한다.
- 출처를 마지막 장(또는 카드 하단)에 명시한다.
- 장비 소식이라도 마지막은 "부상 없이 꾸준히" 관점으로 닫는다.
