// 카드 9장을 1080x1350 PNG 로 뽑는다: python3 build_page.py 후 node render_cards.mjs
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
await p.goto(new URL('./standalone.html', import.meta.url).href);
await p.waitForFunction(() => document.querySelectorAll('.shot').length === 9, null, { timeout: 90000 });
const data = await p.evaluate(async () => Promise.all([...document.querySelectorAll('.shot')].map(async img => {
  const bl = await (await fetch(img.src)).blob();
  return await new Promise(r => { const fr = new FileReader(); fr.onload = () => r(fr.result.split(',')[1]); fr.readAsDataURL(bl); });
})));
data.forEach((d, i) => fs.writeFileSync(new URL(`./out/card-${String(i+1).padStart(2,'0')}.png`, import.meta.url), Buffer.from(d, 'base64')));
console.log('dumped', data.length);
await b.close();
