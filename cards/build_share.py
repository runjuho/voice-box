#!/usr/bin/env python3
"""카톡으로 보낼 가벼운 공유 페이지(cards/share.html)를 만든다.

카드 이미지는 미리 JPG 로 뽑아 CloudFront 에 올려두고(share_images.json),
페이지는 <img> 만 싣는다. '전체 저장'은 그 이미지들을 받아 navigator.share({files})
로 넘기고, iOS 공유 시트의 '이미지 N개 저장'이 사진 앱에 한 번에 넣는다.
클로드 아티팩트(iframe) 안에서는 공유가 막히므로 이 파일은 독립 페이지로 호스팅한다.
"""
import html, json, pathlib

ROOT = pathlib.Path(__file__).parent
IMAGES = json.load(open(ROOT / 'share_images.json'))
CAPTION = (ROOT / 'caption.md').read_text()


def section(md, head):
    body = md.split('## ' + head, 1)[1]
    return body.split('\n## ', 1)[0].strip()


caps = [('업로드 캡션', section(CAPTION, '업로드 캡션')),
        ('커버 문구 대안', section(CAPTION, '커버 문구 대안 (후킹)')),
        ('첫 댓글', section(CAPTION, '첫 댓글용'))]

imgs = '\n'.join(
    f"<img data-set='0' src='{u}' alt='카드 {i + 1:02d}' loading='eager'>"
    for i, u in enumerate(IMAGES))

cap_html = '\n'.join(
    f"""<div class="cap"><div class="cap-h"><span>{t}</span><button data-cap="c{i}">복사</button></div>
<pre id="c{i}">{html.escape(body)}</pre></div>""" for i, (t, body) in enumerate(caps))

page = f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>아디오스 프로 5 카드뉴스</title>
<style>
:root {{ --bg:#000; --text:#F5F5F7; --muted:#86868B; --accent:#0A84FF; --fill:rgba(255,255,255,.06);
  --sans:-apple-system,BlinkMacSystemFont,'SF Pro Text','Apple SD Gothic Neo','Malgun Gothic',sans-serif; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--text); font-family:var(--sans); -webkit-font-smoothing:antialiased; }}
.wrap {{ max-width:720px; margin:0 auto; padding:16px 16px 48px; }}
.tip {{ background:var(--fill); border-radius:16px; padding:14px 16px; font-size:15px; line-height:1.55; }}
.tip small {{ display:block; color:var(--muted); font-size:14px; margin-top:4px; }}
.brand {{ margin:28px 0 6px; color:var(--accent); font-size:14px; font-weight:700; letter-spacing:.04em; }}
.head {{ display:flex; align-items:center; gap:12px; margin-bottom:16px; }}
.head h1 {{ flex:1; margin:0; font-size:22px; font-weight:800; line-height:1.3; }}
.saveall {{ border:0; border-radius:999px; background:var(--accent); color:#fff; font:700 15px var(--sans);
  padding:12px 20px; min-height:44px; white-space:nowrap; }}
.saveall:disabled {{ opacity:.55; }}
.hide {{ display:none; }}
.set {{ display:flex; flex-direction:column; gap:12px; }}
.set img {{ width:100%; height:auto; display:block; border-radius:16px; -webkit-touch-callout:default; }}
.cap {{ margin-top:16px; background:var(--fill); border-radius:16px; padding:14px 16px; }}
.cap-h {{ display:flex; align-items:center; justify-content:space-between; font-weight:700; margin-bottom:8px; }}
.cap-h button {{ border:0; border-radius:999px; background:rgba(255,255,255,.12); color:var(--text); font:600 14px var(--sans); padding:8px 14px; }}
pre {{ margin:0; white-space:pre-wrap; word-break:keep-all; font:15px/1.6 var(--sans); }}
</style></head>
<body><div class="wrap">
<div class="tip">📱 <b>전체 저장</b>을 누르고 공유 시트에서 '이미지 저장'을 고르면 {len(IMAGES)}장이 통째로 사진 앱에 들어갑니다
<small>한 장만 받으실 땐 그 카드를 길게 누르세요</small></div>
<div class="brand">런주호</div>
<div class="head"><h1>아디오스 프로 5 오피셜 · {len(IMAGES)}장</h1>
<button class="saveall hide" data-set="0" data-prefix="adios-pro-5">전체 저장</button></div>
<div class="set">
{imgs}
</div>
{cap_html}
</div>
<script>
// 공유 시트로 넘기면 '이미지 저장'이 한 세트를 통째로 사진 앱에 넣는다.
// 저장 위치는 웹이 못 정하므로 이게 사진 앱으로 가는 유일한 길이다.
try {{ const t = new File([new Uint8Array([0])], 'a.jpg', {{type:'image/jpeg'}});
  if (navigator.canShare && navigator.canShare({{files:[t]}}))
    document.querySelectorAll('.saveall').forEach(b => b.classList.remove('hide')); }} catch (e) {{}}

document.querySelectorAll('.saveall').forEach(b => b.addEventListener('click', async () => {{
  const imgs = [...document.querySelectorAll("img[data-set='" + b.dataset.set + "']")];
  const label = b.textContent; b.disabled = true; b.textContent = '준비 중';
  try {{
    const files = await Promise.all(imgs.map(async (im, i) => {{
      const bl = await (await fetch(im.src)).blob();
      return new File([bl], b.dataset.prefix + '-' + String(i + 1).padStart(2, '0') + '.jpg', {{type:'image/jpeg'}});
    }}));
    if (navigator.canShare && navigator.canShare({{files}})) await navigator.share({{files}});
    else b.textContent = '이 브라우저는 안 됨';
  }} catch (e) {{ if (e && e.name !== 'AbortError') b.textContent = '실패 · ' + e.name; }}
  finally {{ setTimeout(() => {{ b.disabled = false; b.textContent = label; }}, 1200); }}
}}));

document.querySelectorAll('button[data-cap]').forEach(b => b.addEventListener('click', async () => {{
  const el = document.getElementById(b.dataset.cap);
  try {{ await navigator.clipboard.writeText(el.textContent); b.textContent = '복사됨'; }}
  catch (e) {{ const r = document.createRange(); r.selectNodeContents(el);
    const s = getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = '선택됨'; }}
  setTimeout(() => b.textContent = '복사', 1600);
}}));
</script>
</body></html>
"""
(ROOT / 'share.html').write_text(page)
print('share.html', len(page), 'bytes')
