// Dependency-free, local Chrome checks. No live website or personal browser profile.
import { spawn } from 'node:child_process';
import { mkdtemp, readFile, writeFile, mkdir, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import assert from 'node:assert/strict';

const here = dirname(fileURLToPath(import.meta.url));
const output = resolve(process.argv[2] || 'dist/evaluations/v0.6/poster-wall/browser');
await mkdir(output, { recursive: true });
const profile = await mkdtemp(resolve(tmpdir(), 'cinematic-poster-chrome-'));
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
  const click = async (selector, touch = false) => {
    await evaluate(`document.querySelector(${JSON.stringify(selector)}).scrollIntoView({block:'nearest'})`);
    await sleep(40);
    const point = await evaluate(`(() => {const r=document.querySelector(${JSON.stringify(selector)}).getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2}})()`);
    if (touch) {
      await call('Input.dispatchTouchEvent', {type:'touchStart',touchPoints:[point]});
      await call('Input.dispatchTouchEvent', {type:'touchEnd',touchPoints:[]});
    } else {
      await call('Input.dispatchMouseEvent', {type:'mousePressed',...point,button:'left',clickCount:1});
      await call('Input.dispatchMouseEvent', {type:'mouseReleased',...point,button:'left',clickCount:1});
    }
  };
  const key = async (key, code, number, text) => {
    await call('Input.dispatchKeyEvent', {type:'keyDown',key,code,windowsVirtualKeyCode:number,...(text ? {text,unmodifiedText:text} : {})});
    await call('Input.dispatchKeyEvent', {type:'keyUp',key,code,windowsVirtualKeyCode:number});
  };
  const state = () => evaluate(`(() => {
    const image = document.querySelector('.detail:not([hidden]) .artwork');
    const r = image?.getBoundingClientRect();
    const title = document.querySelector('.detail:not([hidden]) h2')?.getBoundingClientRect();
    return {view:document.body.dataset.view,hash:location.hash,scrollY,
      width:innerWidth,height:innerHeight,overflow:document.documentElement.scrollWidth>innerWidth,
      running:document.getAnimations().filter(a=>a.playState==='running').length,
      transform:image ? getComputedStyle(image).transform : null,
      image:r ? {x:r.x,y:r.y,width:r.width,height:r.height} : null,
      title:title ? {y:title.y,height:title.height} : null,
      status:document.querySelector('#motion-status').textContent,
      replayDisabled:document.querySelector('#replay').disabled,
      focus:document.activeElement.id || document.activeElement.tagName};
  })()`);
  await call('Page.enable'); await call('Runtime.enable'); await call('Log.enable');
  report.browser = await call('Browser.getVersion');
  const url = pathToFileURL(resolve(here,'index.html')).href;
  const navigate = async (hash = '') => {
    await call('Page.navigate', {url:url+hash});
    for (let i=0;i<100;i++) {
      if (await evaluate("document.readyState==='complete' && !!document.querySelector('#choose-sideways')")) break;
      await sleep(30);
    }
    await sleep(100);
  };
  if (process.argv.includes('--static')) {
    for (const [w,h] of [[360,640],[390,844],[1024,600],[1440,900]]) {
      await metrics(w,h); await navigate(); await capture(`${w}x${h}-collection`);
      assert.equal((await state()).overflow,false);
      await navigate('#sideways'); await capture(`${w}x${h}-detail`);
      assert.equal((await state()).overflow,false);
      note(`${w}x${h} resting composition`, 'Actual static browser capture; no motion quality claim.');
    }
  } else {
    for (const [w,h] of [[360,640],[390,844],[1024,600],[1440,900]]) {
      await metrics(w,h); await navigate(); await capture(`${w}x${h}-collection`);
      assert.equal((await state()).overflow,false);
      await click('#choose-sideways'); await sleep(90);
      const start = await state(); samples.push({scenario:`${w}x${h} A moving`,...start});
      assert.equal(start.view,'detail','Selection opens a usable detail state');
      assert.ok(start.running>0,'A actually moves after selection');
      assert.equal(start.overflow,false);
      assert.ok(start.image.y>=0 && start.image.y+start.image.height<=h+2,'The full moving poster is visible on initial selection');
      assert.ok(start.title.y>=0,'The project title is not clipped above the viewport');
      await capture(`${w}x${h}-A-moving`);
      await sleep(650); const settled=await state();
      assert.equal(settled.running,0); assert.equal(settled.transform,'none');
      await capture(`${w}x${h}-detail`);
      await click('input[value="b"]'); await click('#replay'); await sleep(180);
      const b=await state(); samples.push({scenario:`${w}x${h} B moving`,...b});
      assert.ok(b.running>0); assert.ok(b.image.y<h && b.image.y+b.image.height>0,'Replay artwork is visible');
      await capture(`${w}x${h}-B-moving`);
      await sleep(900); assert.equal((await state()).running,0);
      await click('input[value="still"]'); assert.equal((await state()).running,0);
      assert.equal((await state()).replayDisabled,true);
      await capture(`${w}x${h}-still`);
      note(`${w}x${h} comparison`,'A/B move and settle; still stays static; no horizontal overflow.');
    }
    await metrics(1024,600); await navigate('#sideways');
    assert.equal((await state()).running,0); note('Direct entry','Settled detail without an invented arrival.');
    for (const variant of ['a','b']) {
      await click(`input[value="${variant}"]`); await click('#replay');
      const start=await state(); await sleep(140); const during=await state();
      await sleep(1000); const end=await state();
      assert.notEqual(start.transform,during.transform); assert.equal(end.running,0);
      samples.push({scenario:`${variant} wall-clock`,start,during,end});
      for (const [frame,time] of [['start',0],['change',variant==='a'?180:550],['settled',1000]]) {
        await click('#replay');
        await evaluate(`document.getAnimations().forEach(a=>{a.pause();a.currentTime=${time}})`);
        await capture(`${variant}-storyboard-${frame}`);
      }
    }
    note('Temporal samples','Transforms change with wall-clock time and stop. Separate storyboard frames are paused/seeked.');
    await click('input[value="a"]'); await click('#replay'); await metrics(390,844); await sleep(100);
    assert.equal((await state()).running,0); note('Resize interruption','Motion stops in the readable destination.');
    await click('#replay');
    await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});
    await sleep(100); assert.equal((await state()).running,0); assert.equal((await state()).replayDisabled,true);
    await navigate('#after-hours'); assert.equal((await state()).running,0);
    await capture('390x844-reduced'); note('Reduced motion','Entry and a live preference change settle; replay disabled.');
    await call('Emulation.setEmulatedMedia',{features:[]});
    await metrics(390,844,true); await call('Emulation.setTouchEmulationEnabled',{enabled:true});
    await navigate(); await click('#choose-sideways',true); await sleep(80);
    assert.equal((await state()).hash,'#sideways'); assert.ok((await state()).running>0);
    await click('.detail:not([hidden]) .context a',true); await sleep(80);
    assert.equal((await state()).hash,'#after-hours');
    await sleep(750); assert.equal((await state()).running,0);
    note('Touch / rapid second selection','Dispatched touch opens work; a new selection replaces the prior handoff.');
    await call('Emulation.setTouchEmulationEnabled',{enabled:false}); await metrics(1024,600);
    await navigate();
    await evaluate("document.querySelector('.skip').focus()");
    const focus=[];
    for (let i=0;i<14;i++) { await key('Tab','Tab',9); focus.push(await evaluate('document.activeElement.id || document.activeElement.tagName')); }
    report.focusOrder=focus; assert.ok(focus.includes('choose-sideways'));
    await evaluate("document.querySelector('#choose-sideways').focus()");
    await key('Enter','Enter',13,'\r'); await sleep(70);
    assert.equal((await state()).hash,'#sideways'); assert.equal((await state()).focus,'title-sideways');
    await evaluate("document.querySelector('#replay').focus()");
    await key(' ','Space',32,' '); await sleep(50); assert.ok((await state()).running>0);
    note('Keyboard','Tab reaches study links; Enter navigates and focuses title; Space activates replay.');
    await click('nav a[href="#work"]'); await sleep(100);
    assert.equal((await state()).view,'collection'); assert.equal((await state()).focus,'choose-sideways');
    const history=await call('Page.getNavigationHistory');
    await call('Page.navigateToHistoryEntry',{entryId:history.entries[history.currentIndex-1].id});
    await sleep(200); assert.equal((await state()).hash,'#sideways'); assert.equal((await state()).running,0);
    note('Return / history','Collection restores selected focus; browser Back opens settled detail.');
    await click('#replay'); await click('nav a[href="#contact-note"]'); await sleep(100);
    assert.equal((await state()).running,0); assert.equal((await state()).hash,'#contact-note');
    assert.ok(await evaluate("document.querySelector('#contact-note').getBoundingClientRect().top<innerHeight"));
    note('Contact during motion','Local placeholder remains reachable and the handoff is cancelled.');
    for (const [w,h] of [[360,640],[1024,600]]) {
      await metrics(w,h); await navigate('#sideways'); await evaluate("document.documentElement.style.fontSize='200%'");
      assert.equal((await state()).overflow,false); await capture(`${w}x${h}-enlarged-text`);
      assert.ok(await evaluate("document.querySelector('.detail:not([hidden]) .context').scrollHeight>0"));
    }
    note('Enlarged text','200% root text size reflows at narrow/short widths without horizontal overflow. Not assistive-technology testing.');
    await call('Emulation.setScriptExecutionDisabled',{value:true}); await navigate();
    assert.ok(await evaluate("[...document.querySelectorAll('.detail')].every(e=>e.getBoundingClientRect().height>0)"));
    await click('#choose-sideways'); assert.equal((await state()).hash,'#sideways');
    await capture('1024x600-no-script');
    await click('nav a[href="#contact-note"]'); assert.equal((await state()).hash,'#contact-note');
    note('No script','Both full details and native work/contact links remain usable.');
    await call('Emulation.setScriptExecutionDisabled',{value:false});
    assert.equal(errors.length,0,JSON.stringify(errors)); note('Console','No captured errors or uncaught exceptions.');
  }
} catch (error) {
  report.failure=error.message; report.failureStack=error.stack; process.exitCode=1;
} finally {
  report.recordedAt=new Date().toISOString();
  await writeFile(resolve(output,'observations.json'),JSON.stringify(report,null,2)+'\n');
  ws?.close(); chrome.kill('SIGTERM'); await sleep(300);
  await rm(profile,{recursive:true,force:true,maxRetries:5,retryDelay:150});
}
console.log(JSON.stringify({checks:checks.length,failure:report.failure || null,output}));
