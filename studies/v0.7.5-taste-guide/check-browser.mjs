// Dependency-free, local Chrome checks. No live website or personal browser profile.
import { spawn } from 'node:child_process';
import { mkdtemp, readFile, writeFile, mkdir, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import assert from 'node:assert/strict';

const here = dirname(fileURLToPath(import.meta.url));
const output = resolve(process.argv[2] || 'dist/evaluations/v0.7.5/taste-guide/browser');
await mkdir(output, { recursive: true });
const profile = await mkdtemp(resolve(tmpdir(), 'cinematic-taste-chrome-'));
const chrome = spawn(process.env.CINEMATIC_CHROME_BINARY || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', [
  '--headless=new', '--remote-debugging-port=0', '--remote-debugging-address=127.0.0.1',
  `--user-data-dir=${profile}`, '--no-first-run', '--no-default-browser-check',
  '--disable-background-networking', '--disable-sync', 'about:blank',
], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
const errors = [], checks = [], samples = [], requests = [];
let ws, count = 0, loadCount = 0, navigationCount = 0;
const pending = new Map();
const report = { scope: 'Synthetic local fixture; Chrome viewport/input emulation only', checks, samples, errors, requests };

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
    } else if (message.method === 'Page.loadEventFired') loadCount++;
    else if (message.method === 'Runtime.exceptionThrown') errors.push(message.params.exceptionDetails);
    else if (message.method === 'Log.entryAdded' && ['error','warning'].includes(message.params.entry.level)) errors.push(message.params.entry);
    else if (message.method === 'Network.requestWillBeSent') requests.push(message.params.request.url);
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
  const key = async (key, code, number) => {
    const native = process.platform==='darwin' ? {nativeVirtualKeyCode:({Home:115,ArrowDown:125,Enter:36,Tab:48})[key]} : {};
    await call('Input.dispatchKeyEvent', { type:'rawKeyDown', key, code, windowsVirtualKeyCode:number, ...native });
    await call('Input.dispatchKeyEvent', { type:'keyUp', key, code, windowsVirtualKeyCode:number, ...native });
  };
  const node = async selector => {
    const {root} = await call('DOM.getDocument');
    const {nodeId} = await call('DOM.querySelector', {nodeId:root.nodeId, selector});
    assert.ok(nodeId, `Element exists: ${selector}`); return nodeId;
  };
  const click = async (selector, touch = false) => {
    const nodeId = await node(selector);
    await call('DOM.scrollIntoViewIfNeeded', {nodeId});
    const {model} = await call('DOM.getBoxModel', {nodeId});
    const q = model.border;
    const point = {x:(q[0]+q[2]+q[4]+q[6])/4, y:(q[1]+q[3]+q[5]+q[7])/4};
    if (touch) {
      await call('Input.dispatchTouchEvent', {type:'touchStart',touchPoints:[point]});
      await call('Input.dispatchTouchEvent', {type:'touchEnd',touchPoints:[]});
    } else {
      await call('Input.dispatchMouseEvent', {type:'mouseMoved',...point});
      await call('Input.dispatchMouseEvent', {type:'mousePressed',...point,button:'left',clickCount:1});
      await call('Input.dispatchMouseEvent', {type:'mouseReleased',...point,button:'left',clickCount:1});
    }
  };
  const choose = async (selector, index) => {
    await call('DOM.focus',{nodeId:await node(selector)});
    const letter=['n','c','a','m'][index];
    await call('Input.dispatchKeyEvent',{type:'char',text:letter,unmodifiedText:letter});
    await key('Tab','Tab',9);
    samples.push({select:selector,phase:'committed',value:await evaluate(`document.querySelector(${JSON.stringify(selector)}).value`)});
  };
  const type = async (selector, text) => {
    await call('DOM.focus', {nodeId:await node(selector)});
    await call('Input.insertText', {text});
  };
  const capture = async (name, waitForFrame = true) => {
    if (waitForFrame) await evaluate('new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))');
    const {data} = await call('Page.captureScreenshot', {format:'png',captureBeyondViewport:false});
    await writeFile(resolve(output,`${name}.png`), Buffer.from(data,'base64'));
  };
  const state = () => evaluate(`({
    overflow:document.documentElement.scrollWidth>innerWidth,
    studies:document.querySelectorAll('.study').length,
    running:document.getAnimations().length,
    summary:document.querySelector('#summary').value,
    horizontalClips:[...document.querySelectorAll('.sample-title')].filter(e=>e.scrollWidth>e.clientWidth+1).length,
    toolsHidden:document.querySelector('#summary-tools').hidden
  })`);
  const url = pathToFileURL(resolve(here,'../../assets/taste-guide.html')).href;
  const navigate = async () => {
    const before=loadCount;
    await call('Page.navigate',{url:url+'?check='+(++navigationCount)});
    for (let i=0;i<100;i++) {
      if (loadCount>before && await evaluate("document.readyState==='complete' && !!document.querySelector('#experimental')")) return;
      await sleep(30);
    }
    throw new Error('Guide did not finish loading');
  };
  await call('Page.enable'); await call('Runtime.enable'); await call('Log.enable');
  await call('DOM.enable'); await call('CSS.enable'); await call('Network.enable');
  report.browser = await call('Browser.getVersion');
  for (const [width,height] of [[320,640],[360,640],[390,844],[1024,600],[1440,900]]) {
    await call('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:false});
    await navigate(); const observed=await state(); samples.push({width,height,...observed});
    assert.equal(observed.overflow,false); assert.equal(observed.horizontalClips,0);
    assert.equal(observed.studies,8); assert.equal(observed.running,0);
    assert.ok(observed.summary.includes('No examples chosen yet'));
    assert.ok(observed.summary.includes('motion: Uncertain'));
    await capture(`${width}x${height}-opening`);
    if (width===1440) {
      for (const id of ['editorial','brutalist','gallery','typographic','playful','tactile','technical','experimental']) {
        await call('DOM.scrollIntoViewIfNeeded',{nodeId:await node(`#${id} .preview`)});
        await capture(`study-${id}`);
      }
    }
    await click('a[href="#your-notes"]');
    assert.ok((await evaluate('location.hash')).includes('your-notes'));
    assert.equal((await state()).overflow,false);
    note(`${width}x${height} layout`, 'Eight rendered still studies; native notes link; no horizontal overflow or clipped title text. Desktop Chrome viewport emulation.');
  }
  await navigate();
  await key('Tab','Tab',9);
  assert.equal(await evaluate('document.activeElement.className'),'skip');
  await key('Enter','Enter',13);
  assert.equal(await evaluate('location.hash'),'#studies');
  note('Keyboard entry','Native Tab/Enter reaches and activates the skip link.');
  await choose('#reaction-editorial',1);
  assert.equal(await evaluate("document.querySelector('#reaction-editorial').value"),'Curious');
  await type('#note-editorial','Clarity yes; palette no. <img src=x onerror=alert(1)>');
  await choose('#reaction-typographic',3);
  await type('#note-typographic','The scale, with another palette.');
  await click('input[name="eccentricity"][value^="Maximum"]');
  await click('input[name="artistry"][value^="Maximum"]');
  await type('#other-notes','Borrow qualities, keep my story. Phone access matters.');
  const summary=(await state()).summary;
  assert.ok(summary.includes('01 Editorial / architectural practice: Curious'));
  assert.ok(summary.includes('04 Typographic / type exhibition: Mixed'));
  assert.ok(summary.includes('eccentricity: Maximum'));
  assert.ok(summary.includes('artistry: Maximum'));
  assert.ok(summary.includes('motion: Uncertain'),'Visual appetite does not select motion');
  assert.ok(summary.includes('No concept, motion treatment or production approval.'));
  assert.equal(await evaluate("document.querySelectorAll('img').length"),0,'Notes remain text');
  assert.ok(summary.includes('<img src=x onerror=alert(1)>'));
  await click('#select-notes');
  assert.ok(await evaluate("document.activeElement.id==='summary' && document.activeElement.selectionStart===0 && document.activeElement.selectionEnd===document.activeElement.value.length"));
  await capture('preferences-and-notes');
  note('Mixed preferences and copy','Native select type-ahead, text/radio/copy input preserves reasons and separates maximum ambition from unknown motion. Literal notes and selection work without clipboard access.');
  await call('Emulation.setEmulatedMedia',{media:'print'});
  assert.ok(await evaluate("getComputedStyle(document.querySelector('#print-notes')).display==='block' && document.querySelector('#print-notes').textContent===document.querySelector('#summary').value"));
  await call('Emulation.setEmulatedMedia',{media:''});
  note('Print notes','A wrapping text block includes the full summary rather than a clipped textarea. No OS print-dialog test.');
  await navigate();
  for (const id of ['editorial','brutalist','gallery','typographic','playful','tactile','technical','experimental']) {
    await choose(`#reaction-${id}`,2);
  }
  await type('#other-notes','None of these fits. I want another reference.');
  const outside=(await state()).summary;
  assert.equal(outside.split('\n').filter(line=>line.includes(': Avoid')).length,8);
  assert.ok(outside.includes('None of these fits'));
  assert.ok(outside.includes('motion: Uncertain'));
  await click('#select-notes'); await capture('outside-the-examples');
  note('Reject all / other taste','All eight can be rejected; outside preferences remain verbatim and do not select a style or infer motion.');
  await call('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await call('Emulation.setTouchEmulationEnabled',{enabled:true}); await navigate();
  await click('input[name="motion"][value="Expressive"]',true);
  assert.ok((await state()).summary.includes('motion: Expressive'));
  note('Touch input','Chrome touch emulation can choose motion appetite; not an Android/iPhone hardware test.');
  await call('Emulation.setTouchEmulationEnabled',{enabled:false});
  await call('Emulation.setDeviceMetricsOverride',{width:360,height:640,deviceScaleFactor:1,mobile:false});
  await navigate();
  await call('CSS.setEffectivePropertyValueForNode',{nodeId:await node('html'),propertyName:'font-size',value:'200%'});
  assert.equal((await state()).overflow,false);
  await capture('360x640-enlarged-text');
  note('Enlarged text','200% root text size reflows without page-level horizontal overflow. Not assistive-technology testing.');
  await navigate();
  await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});
  assert.equal((await state()).running,0); note('Reduced motion','The guide has no running animations with or without the preference.');
  const tree=await call('Accessibility.getFullAXTree');
  const names=tree.nodes.filter(n=>!n.ignored).map(n=>n.name?.value).filter(Boolean);
  assert.ok(names.includes('Select notes to copy'));
  assert.ok(names.some(n=>n.includes('Eccentricity / willingness to surprise')));
  note('Accessibility structure','Browser accessibility tree exposes the notes action and grouped preference legend; no screen-reader audit claimed.');
  await call('Emulation.setScriptExecutionDisabled',{value:true}); await navigate();
  const noScript=await state(); assert.equal(noScript.studies,8); assert.equal(noScript.toolsHidden,true);
  assert.ok(await evaluate("document.body.innerText.includes('Automatic notes are unavailable')"));
  await capture('360x640-no-script',false);
  note('No JavaScript','All eight studies and prompts remain in the readable document; automatic notes are hidden with a visible explanation.');
  await call('Emulation.setScriptExecutionDisabled',{value:false});
  assert.equal(requests.some(url=>/^https?:/.test(url)),false,JSON.stringify(requests));
  assert.equal(errors.length,0,JSON.stringify(errors));
  note('Local-only delivery','No page HTTP(S) requests, console warnings/errors or uncaught exceptions were captured.');
} catch (error) {
  report.failure=error.message; report.failureStack=error.stack; process.exitCode=1;
} finally {
  report.recordedAt=new Date().toISOString();
  await writeFile(resolve(output,'observations.json'),JSON.stringify(report,null,2)+'\n');
  ws?.close(); chrome.kill('SIGTERM'); await sleep(300);
  await rm(profile,{recursive:true,force:true,maxRetries:5,retryDelay:150});
}
console.log(JSON.stringify({checks:checks.length,failure:report.failure || null,output}));
