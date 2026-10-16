// Dependency-free, local Chrome checks. No live website or personal browser profile.
import { spawn } from 'node:child_process';
import { mkdtemp, readFile, writeFile, mkdir, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import assert from 'node:assert/strict';

const here = dirname(fileURLToPath(import.meta.url));
const output = resolve(process.argv[2] || 'dist/evaluations/v0.5/study');
await mkdir(output, { recursive: true });
const profile = await mkdtemp(resolve(tmpdir(), 'cinematic-moss-chrome-'));
const chrome = spawn(process.env.CINEMATIC_CHROME_BINARY || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', [
  '--headless=new', '--remote-debugging-port=0', '--remote-debugging-address=127.0.0.1',
  `--user-data-dir=${profile}`, '--no-first-run', '--no-default-browser-check',
  '--disable-background-networking', '--disable-sync', 'about:blank',
], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
const errors = [], checks = [], samples = [];
let ws, count = 0;
const pending = new Map();
const report = { scope: 'Synthetic local fixture; Chrome viewport/input emulation only', checks, samples, errors };

try {
  let port;
  for (let i = 0; i < 100; i++) {
    try { port = Number((await readFile(resolve(profile, 'DevToolsActivePort'), 'utf8')).split('\n')[0]); break; }
    catch { await sleep(100); }
  }
  assert.ok(port, 'Chrome debugging endpoint starts');
  const targets = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
  ws = new WebSocket(targets.find(t => t.type === 'page').webSocketDebuggerUrl);
  await new Promise((ok, fail) => { ws.onopen = ok; ws.onerror = fail; });
  ws.onmessage = ({ data }) => {
    const message = JSON.parse(data);
    if (message.id) {
      const entry = pending.get(message.id);
      if (!entry) return;
      clearTimeout(entry.timer); pending.delete(message.id);
      message.error ? entry.fail(new Error(JSON.stringify(message.error))) : entry.ok(message.result);
    } else if (message.method === 'Runtime.exceptionThrown') errors.push(message.params.exceptionDetails);
    else if (message.method === 'Log.entryAdded' && message.params.entry.level === 'error') errors.push(message.params.entry);
  };
  const call = (method, params = {}) => new Promise((ok, fail) => {
    const id = ++count;
    const timer = setTimeout(() => { pending.delete(id); fail(new Error(`CDP timeout: ${method}`)); }, 15000);
    pending.set(id, { ok, fail, timer });
    ws.send(JSON.stringify({ id, method, params }));
  });
  const evaluate = async expression => {
    const result = await call('Runtime.evaluate', { expression, returnByValue: true, awaitPromise: true });
    assert.ok(!result.exceptionDetails, JSON.stringify(result.exceptionDetails));
    return result.result.value;
  };
  const note = (name, observation) => checks.push({ name, observation, result: 'pass' });
  const metrics = (width, height, mobile = false) => call('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile });
  const capture = async name => {
    const { data } = await call('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
    await writeFile(resolve(output, `${name}.png`), Buffer.from(data, 'base64'));
  };
  const state = () => evaluate(`(() => {
    const box = s => { const r = document.querySelector(s).getBoundingClientRect(); return {x:r.x,y:r.y,width:r.width,height:r.height}; };
    return { width:innerWidth,height:innerHeight,overflow:document.documentElement.scrollWidth>innerWidth,
      status:document.querySelector('#motion-status').textContent,
      transform:getComputedStyle(document.querySelector('#vessel')).transform,
      animations:document.getAnimations().filter(a=>a.playState==='running').length,
      booking:box('.booking'),illustration:box('#illustration'),vessel:box('#vessel'),replay:box('#replay'),
      heading:document.querySelector('h1').textContent, focused:document.activeElement.id || document.activeElement.className };
  })()`);
  const click = async (selector, touch = false) => {
    const p = await evaluate(`(() => {const e=document.querySelector(${JSON.stringify(selector)});e.scrollIntoView({block:'nearest'});const r=e.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2};})()`);
    await sleep(80);
    if (touch) {
      await call('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x: p.x, y: p.y }] });
      await call('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] });
    } else {
      await call('Input.dispatchMouseEvent', { type: 'mousePressed', ...p, button: 'left', clickCount: 1 });
      await call('Input.dispatchMouseEvent', { type: 'mouseReleased', ...p, button: 'left', clickCount: 1 });
    }
  };
  await call('Page.enable'); await call('Runtime.enable'); await call('Log.enable');
  report.browser = await call('Browser.getVersion');
  report.build = (await readFile(resolve(here, 'study.js'), 'utf8')).length;
  const url = pathToFileURL(resolve(here, 'index.html')).href;
  const navigate = async suffix => {
    await call('Page.navigate', { url: url + (suffix || '') });
    for (let i = 0; i < 100; i++) {
      if (await evaluate("document.readyState==='complete' && !!document.querySelector('#vessel')")) break;
      await sleep(30);
    }
  };

  for (const [width, height] of [[360,640],[390,844],[1280,720],[1440,900]]) {
    await metrics(width, height); await navigate(); await sleep(1300);
    const s = await state(); samples.push({ scenario: `${width}x${height} opening`, ...s });
    assert.equal(s.overflow, false);
    assert.ok(s.booking.y >= 0 && s.booking.y + s.booking.height <= height, 'booking initially reachable');
    await capture(`${width}x${height}-opening`);
    await click('#replay'); await sleep(150);
    const moving = await state(); samples.push({ scenario: `${width}x${height} replay`, ...moving });
    assert.equal(moving.overflow, false);
    // A comparison control is useful only when the corresponding artwork is visible.
    assert.ok(moving.vessel.y >= 0 && moving.vessel.y + moving.vessel.height <= height, 'whole replay vessel visible');
    await capture(`${width}x${height}-moving`);
    await sleep(1100);
    assert.equal((await state()).animations, 0);
    note(`${width}x${height}`, 'No horizontal overflow; initial booking visible; replay artwork visible and movement settles.');
  }
  await metrics(1280,720); await navigate(); await sleep(1300);
  await click('#replay');
  const a = await state(); await sleep(180); const b = await state(); await sleep(1100); const c = await state();
  samples.push({ scenario:'wall-clock motion samples', start:a, during:b, settled:c });
  assert.notEqual(a.transform, b.transform); assert.equal(c.transform, 'none');
  note('Temporal observation', 'Transform changes over wall-clock time, then returns to complete still composition; no loop.');
  for (const [name, time] of [['start',0],['change',350],['settled',1100]]) {
    await click('#replay');
    await evaluate(`document.getAnimations().forEach(a=>{a.pause();a.currentTime=${time}})`);
    await capture(`storyboard-${name}`);
  }
  note('Storyboard frames', 'Deterministically paused/seeked browser captures; separate from wall-clock observation.');
  await click('#settle'); assert.equal((await state()).animations,0);
  await click('#replay'); await metrics(390,844); await sleep(150);
  assert.equal((await state()).animations,0); note('Resize interruption','Resize ends motion in complete still state.');
  await click('#replay'); await evaluate('window.scrollTo(0,document.documentElement.scrollHeight)'); await sleep(150);
  assert.ok(await evaluate('scrollY>0'));
  note('Scrolling during movement','Native scrolling remains available during replay; no locked scroll. Leaving the artwork entirely depends on page height.');

  await call('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
  await navigate(); await sleep(150);
  assert.equal((await state()).animations,0);
  assert.equal(await evaluate("document.querySelector('#replay').disabled"),true);
  await capture('390x844-reduced-motion'); note('Reduced motion','Actual emulated preference yields complete static illustration and disabled replay.');
  await call('Emulation.setEmulatedMedia', { features: [] });
  await metrics(390,844,true); await call('Emulation.setTouchEmulationEnabled',{enabled:true});
  await navigate(); await sleep(1300); await click('#replay',true); await sleep(120);
  assert.ok((await state()).animations>0, 'Touch replay actually starts motion');
  await click('#settle',true);
  assert.equal((await state()).animations,0); note('Touch input emulation','Real dispatched touch events activate replay and still controls.');
  await call('Emulation.setTouchEmulationEnabled',{enabled:false}); await metrics(1280,720);
  await navigate(); await sleep(1300);
  await evaluate("document.querySelector('.skip').focus()");
  const focus = [];
  for (let i=0;i<8;i++) {
    await call('Input.dispatchKeyEvent',{type:'keyDown',key:'Tab',code:'Tab',windowsVirtualKeyCode:9});
    await call('Input.dispatchKeyEvent',{type:'keyUp',key:'Tab',code:'Tab',windowsVirtualKeyCode:9});
    focus.push(await evaluate('document.activeElement.id || document.activeElement.className'));
  }
  report.focusOrder = focus;
  assert.ok(focus.includes('replay') && focus.includes('settle') && focus.includes('booking'), JSON.stringify(focus));
  await evaluate("document.querySelector('#replay').scrollIntoView({block:'nearest'});document.querySelector('#replay').focus({preventScroll:true})");
  await sleep(100);
  await call('Input.dispatchKeyEvent',{type:'keyDown',key:'Enter',code:'Enter',windowsVirtualKeyCode:13,text:'\r',unmodifiedText:'\r'});
  await call('Input.dispatchKeyEvent',{type:'keyUp',key:'Enter',code:'Enter',windowsVirtualKeyCode:13});
  await sleep(50); const keyboardState = await state(); report.keyboardState = keyboardState;
  assert.ok(keyboardState.animations>0, JSON.stringify(keyboardState)); note('Keyboard', { focusOrder:focus, enter:'Replay activates through Enter.' });
  await click('.booking'); await sleep(100);
  assert.equal(await evaluate('location.hash'),'#booking-note');
  note('Booking placeholder','Link leads to explicit unavailability note, without fictional dates or live transaction.');
  const history = await call('Page.getNavigationHistory');
  await call('Page.navigateToHistoryEntry',{entryId:history.entries[history.currentIndex-1].id});
  await sleep(150); assert.equal(await evaluate('location.hash'),'');
  note('History return','Browser history returns from the placeholder anchor to the study without hiding content.');
  report.localNavigation = await evaluate("performance.getEntriesByType('navigation')[0]?.toJSON()");
  report.loadingLimit = 'Local file URL, system fonts, inline SVG; no network/mobile field performance claim.';
  await call('Emulation.setScriptExecutionDisabled',{value:true}); await navigate(); await sleep(100);
  assert.equal((await state()).transform,'none'); await capture('1280x720-no-script');
  await click('.booking'); assert.equal(await evaluate('location.hash'),'#booking-note');
  note('No script','Complete still artwork/text remain available; native booking link is exercised with page scripts disabled.');
  await call('Emulation.setScriptExecutionDisabled',{value:false});
  assert.equal(errors.length,0); note('Console','No captured browser errors or uncaught exceptions.');
} catch (error) {
  report.failure = error.message; report.failureStack = error.stack; process.exitCode = 1;
} finally {
  report.recordedAt = new Date().toISOString();
  await writeFile(resolve(output,'observations.json'),JSON.stringify(report,null,2)+'\n');
  ws?.close(); chrome.kill('SIGTERM'); await sleep(300);
  await rm(profile,{recursive:true,force:true,maxRetries:5,retryDelay:150});
}
console.log(JSON.stringify({ checks:checks.length, failure:report.failure || null, output }));
