#!/usr/bin/env python3
"""cards/export.html 를 만든다. 카드 8장 마크업 + 이미지 data URI + 캡션을 한 파일로 묶는다."""
import json, pathlib

ROOT = pathlib.Path(__file__).parent
IMG = json.load(open('/tmp/claude-0/imgs.json'))
CAPTION = (ROOT / 'caption.md').read_text()


def section(md, head):
    """caption.md 에서 한 섹션 본문만 떼어낸다."""
    body = md.split('## ' + head, 1)[1]
    return body.split('\n## ', 1)[0].strip()


CAP_MAIN = section(CAPTION, '업로드 캡션')
CAP_HOOKS = section(CAPTION, '커버 문구 대안 (후킹)')
CAP_REPLY = section(CAPTION, '첫 댓글용')


TOTAL = 9


def head(n):
    return (f'<div class="c-head"><span class="c-mark"></span>'
            f'<span class="c-brand">RUNJUHO</span><span class="c-sp"></span>'
            f'<span class="c-num">0{n} / 0{TOTAL}</span></div>')


def foot(note):
    return (f'<div class="c-foot"><span class="c-handle">@runjuho</span>'
            f'<span class="c-sp"></span><span class="c-note">{note}</span></div>')


def row(label, value, sub=None, cls='row'):
    s = f'<div class="{cls}"><span class="lbl">{label}</span><span class="val">{value}'
    if sub:
        s += f'<br><span class="sub">{sub}</span>'
    return s + '</span></div>'


CARDS = [
    ('커버', f'''{head(1)}
<div class="panel grow">
  <img class="fill" src="{IMG['front']}" alt="아디다스 아디제로 아디오스 프로 5 솔라 터보 앞쪽 사선 컷">
</div>
<div class="stack-20">
  <div class="eyebrow-row"><span class="pill">오피셜</span><span class="eyebrow">아디다스 아디제로</span></div>
  <h1 class="c-title big">아디오스 프로 5</h1>
  <div class="kicker">디자인 · 스펙 · 가격 · 출시일</div>
  <p class="lede">새로 나온 것만 빠르게 정리했습니다.<br>살지 말지는 마지막 장에서.</p>
</div>
{foot('저장해두고 발매일에 다시 보기')}'''),

    ('3줄 요약', f'''{head(2)}
<h2 class="c-title">먼저 3줄 요약</h2>
<div class="grow stack-28 spread">
  <div class="row num-row"><span class="num">01</span><span class="col"><span class="lbl">모델</span><span class="big-val">아디제로 아디오스 프로 5<br>‘솔라 터보’</span></span></div>
  <div class="row num-row"><span class="num">02</span><span class="col"><span class="lbl">출시일</span><span class="big-val">2026년 9월 22일</span></span></div>
  <div class="row num-row"><span class="num">03</span><span class="col"><span class="lbl">가격</span><span class="big-val">339,000원<span class="sub-inline"> · 현재 품절</span></span></span></div>
</div>
<div class="quote"><p>한 줄로 줄이면, 프로4의 상징이던 카본 구조 자체를 갈아치운 5세대입니다.</p></div>
{foot('디테일은 다음 장부터')}'''),

    ('디자인', f'''{head(3)}
<h2 class="c-title">디자인</h2>
<div class="panel grow pair">
  <div class="pair-l"><img src="{IMG['side']}" alt="아디오스 프로 5 측면 컷"></div>
  <div class="pair-r"><img src="{IMG['top']}" alt="아디오스 프로 5 어퍼 상단 컷"></div>
</div>
<div class="stack-22">
  {row('컬러', '솔라 터보 / 코어 블랙 / 루시드 레드')}
  {row('어퍼', '아디제로 라이트락 2.0', '형광 핑크 바탕에 도트 패턴 3스트라이프')}
  {row('품번', 'KI8294')}
</div>
{foot('첫 컬러웨이 기준 · 추가 컬러는 순차 공개')}'''),

    ('스펙', f'''{head(4)}
<div class="stack-12">
  <span class="over">adidas 공식 발표 기준</span>
  <h2 class="c-title">스펙</h2>
</div>
<div class="tiles">
  <div class="tile"><span class="lbl">힐 스택</span><span class="stat">39<span class="unit"> mm</span></span></div>
  <div class="tile"><span class="lbl">포어풋 스택</span><span class="stat">35<span class="unit"> mm</span></span></div>
  <div class="tile"><span class="lbl">드롭</span><span class="stat">4<span class="unit"> mm</span></span></div>
  <div class="tile"><span class="lbl">무게(남성)</span><span class="stat">177<span class="unit"> g</span></span><span class="tile-sub">270mm 기준 · 여성 150g(240mm)</span></div>
</div>
<div class="grow stack-20">
  {row('미드솔', '라이트스트라이크 프로 2중 레이어')}
  {row('구조', '카본 에너지림 (신규)', '막대형 에너지로드를 대체 · 발밑 폼 부피를 늘리면서 강성은 유지')}
  {row('아웃솔', '라이트트랙션 · 컨티넨탈 고무')}
</div>
{foot('adidas 공식 보도자료(국내 배포) 기준')}'''),

    ('달라진 점', f'''{head(5)}
<div class="stack-12">
  <span class="over">프로4 &nbsp;→&nbsp; 프로5</span>
  <h2 class="c-title">뭐가 달라졌나</h2>
</div>
<div class="grow stack-26">
  <div class="row bullet"><span class="dot"></span><span class="col"><span class="head-s">카본 구조가 로드에서 림으로 바뀌었습니다</span><span class="body-s">발가락뼈 모양 막대(에너지로드) 대신, 발 둘레를 도는 테두리형 카본(에너지림)으로 전면 교체됐습니다. 부분 변경이 아니라 시스템 자체가 바뀐 겁니다.</span></span></div>
  <div class="row bullet"><span class="dot"></span><span class="col"><span class="head-s">드롭이 낮아졌습니다</span><span class="body-s">드롭 6mm → 4mm, 포어풋 스택 33mm → 35mm. 힐과 포어풋 차이가 줄어 더 평평하게 지면을 딛는 구조입니다.</span></span></div>
  <div class="row bullet"><span class="dot"></span><span class="col"><span class="head-s">무게는 오히려 가벼워졌습니다</span><span class="body-s">남성 177g(270mm 기준)으로 전작 대비 20g 이상, 약 12% 가벼워졌습니다. 에너지 리턴은 9% 향상됐다고 합니다.</span></span></div>
  <div class="row bullet"><span class="dot"></span><span class="col"><span class="head-s">어퍼·아웃솔도 새 버전입니다</span><span class="body-s">라이트락 2.0 어퍼, 라이트트랙션 아웃솔(컨티넨탈 고무)로 각각 업데이트됐습니다.</span></span></div>
</div>
<div class="quote"><p>막대에서 테두리로 카본 구조 자체를 바꾸고, 20g 넘게 뺐습니다. 스펙만 보면 꽤 큰 변화입니다.</p></div>
{foot('adidas 공식 발표 기준 · 착용기는 확보되는 대로 올리겠습니다')}'''),

    ('가격·출시일', f'''{head(6)}
<h2 class="c-title">가격과 출시일</h2>
<div class="tiles two">
  <div class="tile hero"><span class="lbl on">출시일</span><span class="stat">9.22</span><span class="tile-sub on">2026년 · 화요일</span></div>
  <div class="tile"><span class="lbl">국내 정가</span><span class="stat" style="font-size: 58px;">339,000<span class="unit">원</span></span><span class="tile-sub">해외는 $275 · 프로4는 $250</span></div>
</div>
<div class="grow stack-22">
  {row('재고', '공식 스토어 현재 품절', '아디다스는 재입고가 비교적 빠른 편입니다', cls='row wide')}
  {row('대회 착용', '세계육상연맹 공인 리스트 등재 완료', '모델 코드 ONN61 / K10940', cls='row wide')}
  {row('실전 데뷔', '9월 27일 베를린 마라톤', '엘리트 선수 발에서 먼저 확인될 가능성이 큽니다', cls='row wide')}
</div>
{foot('adidas 공식 보도자료 · 국내 정가·재고 기준 (2026.9.23)')}'''),

    ('살까 말까', f'''{head(7)}
<div class="stack-12">
  <span class="over">제 생각은 이렇습니다</span>
  <h2 class="c-title">그래서 지금 사야 하나</h2>
</div>
<div class="grow stack-24">
  <div class="row num-row"><span class="num sm">01</span><span class="col"><span class="head-s">레이스가 3주 안쪽이라면</span><span class="body-s">새 카본화를 바로 실전에 넣지 마세요. 최소 두세 번은 신고 달려봐야 합니다.</span></span></div>
  <div class="row num-row"><span class="num sm">02</span><span class="col"><span class="head-s">프로4를 잘 신고 있다면</span><span class="body-s">지금 갈아탈 이유는 아직 약합니다. 쓰던 신발 수명부터 다 쓰세요.</span></span></div>
  <div class="row num-row"><span class="num sm">03</span><span class="col"><span class="head-s">첫 카본화를 고민 중이라면</span><span class="body-s">저는 잠시 미루라고 말합니다. 종아리와 발목이 먼저 버텨줘야 합니다.</span></span></div>
  <div class="row num-row"><span class="num sm">04</span><span class="col"><span class="head-s">그래도 살 거라면</span><span class="body-s">발매 당일 사이즈부터 빠집니다. 내 사이즈를 미리 정해두세요.</span></span></div>
</div>
<div class="quote"><p class="lg">카본화가 기록을 만들어주지는 않습니다.<br>부상 없이 꾸준히 달리는 게 먼저입니다.</p></div>
{foot('궁금한 건 댓글로')}'''),

    ('바이어 가이드', f'''{head(8)}
<div class="stack-12">
  <span class="over">제 개인 코멘트입니다</span>
  <h2 class="c-title" style="font-size: 76px;">바이어 가이드</h2>
</div>
<div class="quote" style="background: var(--ember); color: #FFFFFF;">
  <span style="display: block; font-size: 22px; font-weight: 900; letter-spacing: .04em; margin-bottom: 8px;">결론부터</span>
  <p style="color: #FFFFFF; font-size: 34px; font-weight: 900;">프로4가 아직 현역이고 마일리지 괜찮으면, 지금은 구매 비추천입니다.</p>
</div>
<div class="grow stack-22">
  <div class="row num-row"><span class="num sm">01</span><span class="col"><span class="head-s" style="font-size: 29px;">업그레이드가 아니라 새 신발입니다</span><span class="body-s" style="font-size: 23px;">드롭도, 미드솔도, 카본 구조도 다 바뀌었습니다. 해외 착용 리뷰들도 프로4 연장선이 아니라 별개 모델처럼 다룹니다. 적응 기간이 필요하다는 뜻입니다.</span></span></div>
  <div class="row num-row"><span class="num sm">02</span><span class="col"><span class="head-s" style="font-size: 29px;">안감이 미끄럽다는 초기 지적이 있습니다</span><span class="body-s" style="font-size: 23px;">해외 초기 착용 리뷰 여러 곳에서 삭 라이너가 미끄러워 장거리에서 마찰이 생겼다는 언급이 나왔습니다. 치명적 하자는 아니지만 신경 쓰이는 부분입니다.</span></span></div>
  <div class="row num-row"><span class="num sm">03</span><span class="col"><span class="head-s" style="font-size: 29px;">짧은 레이스엔 스냅감이 덜합니다</span><span class="body-s" style="font-size: 23px;">미드풋 강성재가 빠지면서 10km 이하 스피드 구간의 반응성이 떨어진다는 평이 있습니다. 마라톤 쪽으로 더 치우친 셋업입니다.</span></span></div>
  <div class="row num-row"><span class="num sm">04</span><span class="col"><span class="head-s" style="font-size: 29px;">사고 싶어도 지금은 품절입니다</span><span class="body-s" style="font-size: 23px;">국내 정가 339,000원인데 현재 품절 상태입니다. 아디다스는 재입고가 비교적 빠른 편이니 급할 필요는 없습니다.</span></span></div>
</div>
<div class="quote"><p>반대로 프로4의 좁은 힐, 물렁한 내구성이 불만이셨다면 프로5가 답일 수 있습니다. 그게 아니라 잘 신고 계신 거면, 지금 급하게 갈아탈 이유는 없습니다.</p></div>
{foot('해외 착용 리뷰 매체 종합 · 커뮤니티 후기는 아직 초기 단계')}'''),

    ('정리·CTA', f'''{head(9)}
<h2 class="c-title">한 장으로 정리</h2>
<div class="stack-18">
  <div class="slab"><span class="lbl">모델</span><span class="slab-v">아디오스 프로 5 ‘솔라 터보’</span></div>
  <div class="slab"><span class="lbl">출시</span><span class="slab-v">2026년 9월 22일</span></div>
  <div class="slab"><span class="lbl">가격</span><span class="slab-v">339,000원 · 현재 품절(재입고 예정)</span></div>
</div>
<div class="grow center stack-22">
  <p class="cta">국내 정가 339,000원, 지금은 품절입니다.<br>아디다스는 재입고가 빠른 편이니 조금만 기다려보세요.</p>
  <div class="handle-row"><span class="handle-pill">@runjuho</span><span class="eyebrow">러닝 장비 소식은 여기서</span></div>
</div>
<div class="src"><p>출처 · adidas 공식 보도자료(국내 배포), 세계육상연맹(World Athletics) 공인 리스트.<br>원화 정가는 매장·시점마다 다를 수 있어 공식 스토어 표기를 우선합니다.</p></div>'''),
]

CARD_NAMES = [f'{i + 1:02d}-{name}' for i, (name, _html) in enumerate(CARDS)]

slots = '\n'.join(
    f'''<figure class="slot-wrap">
  <div class="slot" id="slot{i+1}"><div class="stage"><div class="card" id="card{i+1}">{html}</div></div></div>
  <figcaption class="cap"><span class="cap-n">0{i+1}</span><span class="cap-t">{name}</span>
    <button type="button" class="btn ghost js-one" data-card="card{i+1}" data-name="{i+1:02d}-{name}">PNG 저장</button>
  </figcaption>
</figure>''' for i, (name, html) in enumerate(CARDS))

page = f'''<title>아디오스 프로 5 카드뉴스</title>
<style>
:root {{
  --ink: #000000; --paper: #F5F5F7; --muted: #86868B; --ember: #0A84FF; --ember-hi: #409CFF;
  --line: rgba(245,245,247,.14); --fill: rgba(255,255,255,.06);
  --shell: #000000; --shell-2: #1C1C1E; --shell-line: rgba(245,245,247,.14);
  --sans: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
  --display: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Apple SD Gothic Neo', sans-serif;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--shell); color: var(--paper); font-family: var(--sans); }}
.wrap {{ max-width: 1180px; margin: 0 auto; padding-block: 28px 64px; padding-left: 20px; padding-right: 20px; }}
.tip {{ background: var(--fill); border-radius: 16px; padding: 16px 18px; margin-bottom: 20px; font-size: 14px; line-height: 1.6; color: var(--muted); }}
.tip b {{ color: var(--paper); }}

/* ---- toolbar ---- */
.bar {{ display: flex; flex-wrap: wrap; align-items: flex-end; gap: 16px 20px; padding-bottom: 20px; border-bottom: 1px solid var(--shell-line); }}
.bar h1 {{ margin: 0; font-family: var(--display); font-size: 34px; line-height: 1.1; letter-spacing: -.01em; }}
.bar .meta {{ margin: 6px 0 0; font-size: 14px; font-weight: 500; color: var(--muted); }}
.bar .acts {{ margin-left: auto; display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }}
.btn {{ font-family: var(--sans); font-size: 15px; font-weight: 700; padding: 12px 20px; min-height: 44px;
  border: 1px solid var(--ember); border-radius: 12px; background: var(--ember); color: #FFFFFF; cursor: pointer; }}
.btn:hover {{ background: var(--ember-hi); border-color: var(--ember-hi); }}
.btn.ghost {{ background: transparent; color: var(--paper); border-color: var(--shell-line); }}
.btn.ghost:hover {{ border-color: var(--ember); color: var(--ember); background: transparent; }}
.btn:disabled {{ opacity: .5; cursor: progress; }}
.btn:focus-visible, textarea:focus-visible {{ outline: 2px solid var(--ember); outline-offset: 2px; }}
.status {{ font-size: 14px; font-weight: 700; color: var(--muted); min-height: 20px; }}
.status.warn {{ color: #FF9F0A; }}

/* ---- previews ---- */
.grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 26px 20px; margin-top: 30px; }}
.slot-wrap {{ margin: 0; }}
.slot {{ position: relative; width: 100%; aspect-ratio: 1080 / 1350; overflow: hidden; background: var(--ink); border: 1px solid var(--shell-line); border-radius: 20px; }}
.stage {{ position: absolute; top: 0; left: 0; transform-origin: top left; }}
.cap {{ display: flex; align-items: center; gap: 10px; padding-top: 10px; }}
.cap-n {{ font-family: var(--display); font-size: 15px; color: var(--ember); }}
.cap-t {{ font-size: 14px; font-weight: 700; color: var(--muted); flex-grow: 1; }}
.cap .btn {{ font-size: 13px; padding: 8px 12px; min-height: 36px; }}

/* ---- caption panel ---- */
.copy {{ margin-top: 48px; display: grid; grid-template-columns: 1.5fr 1fr; gap: 20px; align-items: start; }}
.box {{ background: var(--shell-2); border: 1px solid var(--shell-line); border-radius: 20px; padding: 22px; display: flex; flex-direction: column; gap: 14px; }}
.box h2 {{ margin: 0; font-size: 17px; font-weight: 900; letter-spacing: .02em; }}
.box .hint {{ margin: 0; font-size: 13px; font-weight: 500; color: var(--muted); }}
textarea {{ width: 100%; background: #000000; color: var(--paper); border: 1px solid var(--shell-line);
  border-radius: 12px; font-family: var(--sans); font-size: 14px; line-height: 1.65; padding: 14px; resize: vertical; }}
textarea.main {{ min-height: 340px; }}
textarea.side {{ min-height: 150px; }}

@media (max-width: 1000px) {{ .grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }} .copy {{ grid-template-columns: 1fr; }} }}
@media (max-width: 560px) {{ .grid {{ grid-template-columns: 1fr; }} .bar .acts {{ margin-left: 0; width: 100%; }} }}
@media (prefers-reduced-motion: reduce) {{ * {{ transition: none !important; }} }}

/* ================= CARD ================= */
.card {{ width: 1080px; height: 1350px; padding: 72px; background: var(--ink); color: var(--paper);
  display: flex; flex-direction: column; gap: 36px; font-family: var(--sans); }}
.card .grow {{ flex-grow: 1; }}
.card .c-sp {{ flex-grow: 1; }}
.c-head {{ display: flex; align-items: center; gap: 14px; }}
.c-mark {{ width: 14px; height: 14px; border-radius: 50%; background: var(--ember); }}
.c-brand {{ font-size: 20px; font-weight: 700; letter-spacing: .18em; }}
.c-num {{ font-size: 20px; font-weight: 700; letter-spacing: .14em; color: var(--muted); }}
.c-title {{ margin: 0; font-family: var(--display); font-size: 82px; line-height: 1.02; letter-spacing: -.02em; }}
.c-title.big {{ font-size: 116px; line-height: .98; }}
.c-foot {{ display: flex; align-items: center; border-top: 1px solid var(--line); padding-top: 24px; }}
.c-handle {{ font-size: 21px; font-weight: 700; color: var(--muted); }}
.c-note {{ font-size: 21px; font-weight: 500; color: var(--muted); margin-left: auto; }}

.panel {{ background: var(--paper); border-radius: 20px; overflow: hidden; display: flex; align-items: center; justify-content: center; }}
.panel img.fill {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 45%; }}
.panel.pair {{ gap: 0; }}
.pair-l, .pair-r {{ height: 100%; display: flex; align-items: center; justify-content: center; padding: 18px; }}
.pair-l {{ flex-grow: 1.55; }}
.pair-r {{ flex-grow: 1; }}
.panel.pair img {{ max-width: 100%; max-height: 100%; object-fit: contain; }}

.stack-12, .stack-18, .stack-20, .stack-22, .stack-24, .stack-26, .stack-28 {{ display: flex; flex-direction: column; }}
.stack-12 {{ gap: 12px; }} .stack-18 {{ gap: 18px; }} .stack-20 {{ gap: 20px; }} .stack-22 {{ gap: 22px; }}
.stack-24 {{ gap: 24px; }} .stack-26 {{ gap: 26px; }} .stack-28 {{ gap: 28px; }}
.center {{ justify-content: center; }}
.spread {{ justify-content: space-between; }}

.eyebrow-row {{ display: flex; align-items: center; gap: 14px; }}
.pill {{ background: var(--ember); color: #FFFFFF; border-radius: 999px; font-size: 24px; font-weight: 900; padding: 8px 18px; }}
.eyebrow {{ font-size: 24px; font-weight: 700; color: var(--muted); }}
.kicker {{ font-size: 38px; font-weight: 900; color: var(--ember); }}
.lede {{ margin: 0; font-size: 27px; font-weight: 500; line-height: 1.5; color: var(--muted); }}
.over {{ font-size: 26px; font-weight: 700; letter-spacing: .1em; color: var(--ember); }}

.row {{ display: flex; gap: 24px; align-items: baseline; border-top: 1px solid var(--line); padding-top: 22px; }}
.row.num-row, .row.bullet {{ align-items: flex-start; gap: 26px; padding-top: 26px; }}
.row .col {{ display: flex; flex-direction: column; gap: 8px; }}
.num {{ font-family: var(--display); font-size: 40px; color: var(--ember); min-width: 62px; flex-shrink: 0; }}
.num.sm {{ font-size: 32px; min-width: 52px; }}
.dot {{ width: 12px; height: 12px; border-radius: 50%; background: var(--ember); margin-top: 16px; flex-shrink: 0; }}
.lbl {{ font-size: 22px; font-weight: 700; letter-spacing: .08em; color: var(--muted); min-width: 132px; flex-shrink: 0; }}
.row.wide .lbl {{ min-width: 150px; }}
.tile .lbl, .row.num-row .lbl, .slab .lbl {{ min-width: 0; }}
.slab .lbl {{ min-width: 118px; }}
.val {{ font-size: 32px; font-weight: 900; line-height: 1.35; }}
.row.wide .val {{ font-size: 29px; line-height: 1.4; }}
.sub {{ font-size: 25px; font-weight: 500; color: var(--muted); }}
.sub-inline {{ font-size: 30px; font-weight: 700; color: var(--muted); }}
.big-val {{ font-size: 42px; font-weight: 900; line-height: 1.25; }}
.head-s {{ font-size: 36px; font-weight: 900; line-height: 1.3; }}
.row.num-row .head-s {{ font-size: 32px; }}
.body-s {{ font-size: 26px; font-weight: 500; line-height: 1.5; color: var(--muted); }}
.row.num-row .body-s {{ font-size: 25px; }}

.tiles {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px; }}
.tile {{ background: var(--fill); border-radius: 20px; padding: 30px 32px; display: flex; flex-direction: column; gap: 10px; }}
.tiles.two .tile {{ padding: 34px 32px; }}
.tile.hero {{ background: var(--ember); color: #FFFFFF; }}
.tile .lbl.on {{ color: #FFFFFF; font-weight: 900; }}
.stat {{ font-family: var(--display); font-size: 66px; line-height: 1; }}
.tiles.two .stat {{ font-size: 72px; }}
.unit {{ font-family: var(--sans); font-size: 30px; font-weight: 700; color: var(--muted); }}
.tile-sub {{ font-size: 25px; font-weight: 700; color: var(--muted); }}
.tile-sub.on {{ color: #FFFFFF; }}

.quote {{ background: var(--fill); border-radius: 20px; padding: 28px 32px; }}
.quote p {{ margin: 0; font-size: 28px; font-weight: 700; line-height: 1.5; }}
.quote p.lg {{ font-size: 30px; font-weight: 900; line-height: 1.45; }}
.slab {{ display: flex; gap: 22px; align-items: baseline; background: var(--fill); border-radius: 16px; padding: 26px 30px; }}
.slab-v {{ font-size: 32px; font-weight: 900; }}
.cta {{ margin: 0; font-size: 36px; font-weight: 900; line-height: 1.45; }}
.handle-row {{ display: flex; align-items: center; gap: 18px; }}
.handle-pill {{ background: var(--ember); color: #FFFFFF; border-radius: 999px; font-family: var(--display); font-size: 44px; padding: 14px 28px; }}
.src {{ border-top: 1px solid var(--line); padding-top: 24px; }}
.src p {{ margin: 0; font-size: 20px; font-weight: 500; line-height: 1.6; color: var(--muted); }}
</style>

<div class="wrap">
  <div class="tip">📱 <b>전체 저장</b>을 누르고 공유 시트에서 '이미지 저장'을 고르면 9장이 통째로 사진 앱에 들어갑니다.<br>한 장만 받으실 땐 그 카드의 'PNG 저장'을 누르거나 카드를 길게 누르세요. 꼭 <b>사파리(카톡 인앱 브라우저 아님)</b>에서 열어주세요.</div>
  <header class="bar">
    <div>
      <h1>아디오스 프로 5 오피셜</h1>
      <p class="meta">1080 × 1350 · 9장 · 런주호 카드 캐러셀</p>
    </div>
    <div class="acts">
      <span class="status" id="status" role="status"></span>
      <button type="button" class="btn" id="saveAll">전체 저장</button>
    </div>
  </header>

  <div class="grid">
{slots}
  </div>

  <section class="copy">
    <div class="box">
      <h2>업로드 캡션</h2>
      <textarea class="main" id="cap-main" readonly aria-label="업로드 캡션">{CAP_MAIN}</textarea>
      <button type="button" class="btn js-copy" data-target="cap-main">캡션 복사</button>
    </div>
    <div class="box">
      <h2>커버 문구 대안</h2>
      <textarea class="side" id="cap-hooks" readonly aria-label="커버 문구 대안">{CAP_HOOKS}</textarea>
      <button type="button" class="btn ghost js-copy" data-target="cap-hooks">문구 복사</button>
      <h2>첫 댓글</h2>
      <textarea class="side" id="cap-reply" readonly aria-label="첫 댓글">{CAP_REPLY}</textarea>
      <button type="button" class="btn ghost js-copy" data-target="cap-reply">댓글 복사</button>
      <p class="hint">복사가 막히면 칸을 눌러 전체 선택 후 직접 복사하세요.</p>
    </div>
  </section>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script>
(function () {{
  var statusEl = document.getElementById('status');
  function say(msg, warn) {{
    statusEl.textContent = msg || '';
    statusEl.classList.toggle('warn', !!warn);
  }}

  /* 미리보기: 카드는 실제 1080px 로 두고 감싼 stage 만 축소한다. */
  function fit() {{
    document.querySelectorAll('.slot').forEach(function (slot) {{
      var s = slot.clientWidth / 1080;
      slot.querySelector('.stage').style.transform = 'scale(' + s + ')';
    }});
  }}
  fit();
  window.addEventListener('resize', fit);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);

  var downloads = null, dlReady = (function () {{
    try {{
      return Promise.resolve(window.claude && window.claude.use ? window.claude.use('downloads') : null)
        .then(function (d) {{ downloads = d; return d; }})
        .catch(function () {{ return null; }});
    }} catch (e) {{ return Promise.resolve(null); }}
  }})();

  /* 캡처할 때는 복제본에서 축소를 풀고 카드만 원점에 둔다. */
  function shoot(id) {{
    var card = document.getElementById(id);
    return html2canvas(card, {{
      backgroundColor: '#000000', scale: 1, logging: false, imageTimeout: 0,
      width: 1080, height: 1350, windowWidth: 1080, windowHeight: 1350, scrollX: 0, scrollY: 0,
      onclone: function (doc) {{
        var clone = doc.getElementById(id);
        doc.body.style.margin = '0';
        Array.prototype.forEach.call(doc.body.children, function (ch) {{ ch.style.display = 'none'; }});
        var holder = doc.createElement('div');
        holder.style.cssText = 'position:absolute;left:0;top:0;margin:0;padding:0;';
        holder.appendChild(clone);
        doc.body.appendChild(holder);
      }}
    }});
  }}

  function toBlob(canvas) {{
    return new Promise(function (res) {{ canvas.toBlob(res, 'image/png'); }});
  }}

  function save(filename, data) {{
    return dlReady.then(function () {{
      if (!downloads) throw new Error('no-downloads');
      return downloads.save({{ filename: filename, data: data }});
    }});
  }}

  function fail(err) {{
    var code = err && (err.code || err.message);
    if (code === 'declined') return say('저장을 취소했습니다.');
    if (code === 'no-downloads' || code === 'unavailable' || code === 'not_granted') {{
      return say('이 화면에서는 저장이 막혀 있습니다. 아티팩트를 새 창으로 열고 다시 눌러보세요.', true);
    }}
    say('저장하지 못했습니다: ' + (code || '알 수 없는 오류'), true);
  }}

  document.querySelectorAll('.js-one').forEach(function (btn) {{
    btn.addEventListener('click', function () {{
      btn.disabled = true;
      say('카드를 굽는 중…');
      shoot(btn.dataset.card).then(toBlob).then(function (blob) {{
        return save('adios-pro-5-' + btn.dataset.name + '.png', blob);
      }}).then(function () {{ say('저장했습니다.'); }})
        .catch(fail)
        .then(function () {{ btn.disabled = false; }});
    }});
  }});

  var NAMES = {json.dumps(CARD_NAMES, ensure_ascii=False)};

  /* 카드 9장을 전부 캡처해 File[] 로 모은다. */
  function shootAllFiles() {{
    var files = [];
    return NAMES.reduce(function (chain, name, idx) {{
      return chain.then(function () {{
        var n = idx + 1;
        say('카드 ' + n + '/' + NAMES.length + ' 준비 중…');
        return shoot('card' + n).then(toBlob).then(function (blob) {{
          files.push(new File([blob], 'adios-pro-5-' + name + '.png', {{ type: 'image/png' }}));
        }});
      }});
    }}, Promise.resolve()).then(function () {{ return files; }});
  }}

  /* 1) 먼저 네이티브 공유 시트로 9장을 한번에 넘겨본다 — 지원되면
     카톡/사파리가 "이미지 9개 저장" 같은 일괄 저장 옵션을 보여준다.
     iframe 권한 정책이 막으면 조용히 false 를 반환하고 2)로 넘어간다. */
  function tryShareAll() {{
    if (!(navigator.share && navigator.canShare)) return Promise.resolve(false);
    return shootAllFiles().then(function (files) {{
      if (!files.length || !navigator.canShare({{ files: files }})) return false;
      say('공유 시트에서 "이미지 ' + files.length + '개 저장"을 선택하세요.');
      return navigator.share({{ files: files, title: '아디오스 프로 5 카드뉴스' }})
        .then(function () {{ say('공유를 완료했습니다.'); return true; }})
        .catch(function (e) {{
          if (e && e.name === 'AbortError') {{ say('공유를 취소했습니다.'); return true; }}
          return false; /* 권한 거부·미지원: 2)로 폴백 */
        }});
    }}).catch(function () {{ return false; }});
  }}

  /* 2) 폴백 — 한 장씩 저장 확인을 순서대로 띄운다 (ZIP 없이 개별 저장). */
  function sequentialSaveAll() {{
    var total = NAMES.length, stopped = false;
    return NAMES.reduce(function (chain, name, idx) {{
      return chain.then(function () {{
        if (stopped) return;
        var n = idx + 1;
        say('카드 ' + n + '/' + total + ' 저장 창을 여는 중…');
        return shoot('card' + n).then(toBlob).then(function (blob) {{
          return save('adios-pro-5-' + name + '.png', blob);
        }}).catch(function (err) {{
          var code = err && (err.code || err.message);
          if (code === 'declined') {{ stopped = true; say(n + '번째에서 저장을 취소했습니다. (' + (n - 1) + '/' + total + '장 저장됨)'); return; }}
          throw err;
        }});
      }});
    }}, Promise.resolve()).then(function () {{ if (!stopped) say(total + '장 모두 저장했습니다.'); }});
  }}

  document.getElementById('saveAll').addEventListener('click', function () {{
    var btn = this;
    btn.disabled = true;
    tryShareAll()
      .then(function (shared) {{ return shared ? null : sequentialSaveAll(); }})
      .catch(fail)
      .then(function () {{ btn.disabled = false; }});
  }});

  document.querySelectorAll('.js-copy').forEach(function (btn) {{
    btn.addEventListener('click', function () {{
      var el = document.getElementById(btn.dataset.target);
      var done = function () {{ say('복사했습니다.'); }};
      var manual = function () {{
        el.focus(); el.select();
        say('복사가 막혀 있습니다. 선택된 텍스트를 직접 복사하세요.', true);
      }};
      try {{
        if (navigator.clipboard && navigator.clipboard.writeText) {{
          navigator.clipboard.writeText(el.value).then(done).catch(function () {{
            el.focus(); el.select();
            try {{ document.execCommand('copy') ? done() : manual(); }} catch (e) {{ manual(); }}
          }});
          return;
        }}
        el.focus(); el.select();
        document.execCommand('copy') ? done() : manual();
      }} catch (e) {{ manual(); }}
    }});
  }});
}})();
</script>
'''

(ROOT / 'export.html').write_text(page)
print('export.html', len(page), 'bytes')
