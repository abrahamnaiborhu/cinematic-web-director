// Dependency-free, local Chrome checks. No live website or personal browser profile.
import { spawn } from 'node:child_process';
import { mkdtemp, readFile, writeFile, mkdir, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import assert from 'node:assert/strict';

const here = dirname(fileURLToPath(import.meta.url));
const output = resolve(process.argv[2] || 'dist/evaluations/v0.8/motion-companion/browser');
await mkdir(output, { recursive: true });
const profile = await mkdtemp(resolve(tmpdir(), 'cinematic-motion-chrome-'));
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
  const tab=targets.find(t => t.type === 'page');
  ws = new WebSocket(tab.webSocketDebuggerUrl);
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
    // Buttons activate on Enter's character event, so Enter must carry text like a real keyboard.
    const text = key==='Enter' ? {text:'\r'} : {};
    await call('Input.dispatchKeyEvent', { type:text.text ? 'keyDown' : 'rawKeyDown', key, code, windowsVirtualKeyCode:number, ...native, ...text });
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
  const capture = async (name,script=true) => {
    if(script) await evaluate('new Promise(resolve=>requestAnimationFrame(()=>requestAnimationFrame(resolve)))');
    const {data}=await call('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});
    await writeFile(resolve(output,name+'.png'),Buffer.from(data,'base64'));
  };
  const state=()=>evaluate(`({
    phase:document.querySelector('#scene').dataset.phase,
    treatment:document.querySelector('#scene').dataset.treatment,
    view:document.querySelector('#scene').dataset.view,
    running:document.getAnimations().filter(a=>a.playState==='running').length,
    animations:document.getAnimations().length,
    clones:document.querySelector('#overlay').children.length,
    title:document.querySelector('#detail-title').textContent,
    overflow:document.documentElement.scrollWidth>innerWidth,
    motion:document.querySelector('#motion').checked,
    status:document.querySelector('#status').textContent,
    focus:document.activeElement.id || document.activeElement.dataset.work,
    hash:location.hash,
    href:location.href,visibility:document.visibilityState,
    frame:document.querySelector('.viewer').getBoundingClientRect().toJSON(),
    flight:document.querySelector('.flight')?.getBoundingClientRect().toJSON()
  })`);
  const waitFor=async (predicate,message)=>{
    for(let i=0;i<160;i++){const s=await state();if(predicate(s))return s;await sleep(20);}
    throw new Error(message+': '+JSON.stringify(await state()));
  };
  const url=pathToFileURL(resolve(here,'../../assets/motion-companion.html')).href;
  const navigate=async (hash='',enhanced=true)=>{
    const before=loadCount;
    const target=url+'?check='+(++navigationCount)+hash;
    await call('Page.navigate',{url:target});
    for(let i=0;i<100;i++){
      if(loadCount>before && await evaluate(`location.href===${JSON.stringify(target)} && document.readyState==='complete' && ${enhanced ? "document.documentElement.classList.contains('enhanced')" : 'true'}`))return;
      await sleep(30);
    }
    throw new Error('Companion did not load');
  };
  const metrics=(width,height,mobile=false)=>call('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile});
  await call('Page.enable');await call('Runtime.enable');await call('Log.enable');
  await call('DOM.enable');await call('CSS.enable');await call('Network.enable');
  report.browser=await call('Browser.getVersion');
  for(const [w,h] of [[320,640],[360,640],[390,844],[1024,600],[1440,900]]){
    await metrics(w,h);await navigate();
    assert.equal((await state()).phase,'collection');assert.equal((await state()).animations,0);
    assert.equal((await state()).overflow,false);await capture(`${w}x${h}-collection`);
    for(const treatment of ['hold','context','cut']){
      await click(`input[value="${treatment}"]`);assert.equal((await state()).animations,0,'Radio change does not autoplay');
      await click('#play');
      const start=await state();samples.push({scenario:`${w}x${h}-${treatment}-start`,...start});
      assert.equal(start.view,'detail');assert.equal(start.overflow,false);
      if(start.frame.height<=h-16){assert.ok(start.frame.top>=0 && start.frame.bottom<=h+1,'Explicit playback frames the usable viewer');}
      if(treatment==='cut'){assert.equal(start.animations,0);assert.equal(start.phase,'settled');}
      else{assert.ok(start.running>0,'Authored treatment actually moves');}
      if(treatment==='context'){await sleep(180);await capture(`${w}x${h}-context-moving`);}
      const settled=await waitFor(s=>s.phase==='settled','Opening settles');
      assert.equal(settled.animations,0);assert.equal(settled.clones,0);assert.equal(settled.overflow,false);
      assert.ok(await evaluate("[...document.querySelector('#detail').querySelectorAll('.poster')].every(el=>getComputedStyle(el).visibility==='visible')"));
      await capture(`${w}x${h}-${treatment}-settled`);
      assert.ok(await evaluate(`(()=>{const t=document.querySelector('#detail-title'),r=document.createRange();r.selectNodeContents(t);
        return new Set([...r.getClientRects()].map(x=>Math.round(x.top))).size<=t.textContent.trim().split(/\\s+/).length;})()`),`${w}x${h} ${treatment}: display title wraps only between words`);
      await click('#back');await waitFor(s=>s.phase==='collection','Return restores collection');
    }
    note(`${w}x${h} mechanisms`,'A/B move and settle; C is an immediate distinct-room cut. Explicit input only, visible still content, no horizontal overflow; native return works. Chrome emulation only.');
  }
  await metrics(1024,600);await navigate();await click('input[value="context"]');await click('#play');await sleep(120);await click('#pause');
  await evaluate('Promise.all(document.getAnimations().map(animation=>animation.ready)).then(()=>true)');
  const paused=await waitFor(s=>s.phase==='paused','Pause holds motion');await sleep(140);const held=await state();
  assert.equal(held.running,0);assert.ok(Math.abs(paused.flight.x-held.flight.x)<.5 && Math.abs(paused.flight.y-held.flight.y)<.5);
  await capture('paused-context');await click('#pause');assert.ok((await state()).running>0);
  await click('#finish');assert.equal((await state()).animations,0);assert.equal((await state()).clones,0);
  note('Pause / resume / finish','Real input pauses geometry, resumes and finishes with no surviving animation or overlay.');
  for(let i=0;i<5;i++){await click('#play');}
  assert.ok((await state()).animations<=4);assert.ok((await state()).clones<=3);
  await click('input[value="hold"]');assert.equal((await state()).phase,'collection');assert.equal((await state()).animations,0);
  await click('#play');await click('#back');await waitFor(s=>s.phase==='collection','Interrupted return');
  assert.equal((await state()).animations,0);assert.equal((await state()).clones,0);
  note('Rapid replay / treatment / return','Repeated plays replace owned work; changing treatment or returning clears in-flight geometry.');
  await click('input[value="context"]');await click('#play');await sleep(80);await metrics(390,844);
  await waitFor(s=>s.phase==='settled','Resize settles in new layout');assert.equal((await state()).animations,0);assert.equal((await state()).overflow,false);
  await capture('resize-recovery');note('Resize recovery','A mid-opening resize finishes safely into the phone composition.');
  await navigate();await click('#play');await click('#motion');assert.equal((await state()).animations,0);assert.equal((await state()).phase,'settled');
  await click('#motion');assert.equal((await state()).animations,0,'Re-enabling does not autoplay');
  await click('#play');assert.ok((await state()).running>0);await click('#finish');
  note('Still toggle','Disabling movement settles immediately; re-enabling requires another explicit replay.');
  await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});await navigate();
  assert.equal((await state()).motion,false);await click('input[value="context"]');await click('#play');assert.equal((await state()).animations,0);
  await capture('reduced-motion-still');
  await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'no-preference'}]});await navigate();
  await click('#play');await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});
  await waitFor(s=>s.animations===0 && !s.motion,'Preference change stops motion');
  note('Reduced-motion preference','Initial preference selects stillness and a live change cancels active movement.');
  await call('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'no-preference'}]});await navigate('#structure');
  assert.equal((await state()).title,'Soft Structure');assert.equal((await state()).animations,0);
  await click('#back');assert.equal((await state()).view,'collection');
  await click('#play');await click('#finish');const history=await call('Page.getNavigationHistory');
  await click('#back');await waitFor(s=>s.view==='collection' && s.hash==='#collection','History back');
  await call('Page.navigateToHistoryEntry',{entryId:history.entries[history.currentIndex].id});
  await waitFor(s=>s.view==='detail' && s.href===history.entries[history.currentIndex].url,'History forward');assert.equal((await state()).animations,0);
  note('Direct entry / Back / Forward','Case hashes load settled content; native history navigation does not invent another arrival.');
  await navigate();await key('Tab','Tab',9);assert.equal(await evaluate('document.activeElement.className'),'skip');await key('Enter','Enter',13);
  await call('DOM.focus',{nodeId:await node('.project[data-work="intervals"]')});await key('Enter','Enter',13);
  assert.equal((await state()).title,'Intervals');assert.equal((await state()).focus,'back');
  await key('Enter','Enter',13);await waitFor(s=>s.view==='collection','Keyboard back');assert.equal((await state()).focus,'intervals');
  note('Keyboard and focus','Skip link and project anchors work with Enter; opening/return preserve useful focus.');
  await call('Emulation.setTouchEmulationEnabled',{enabled:true});await navigate();await click('.project[data-work="afterimage"]',true);await click('#finish',true);
  assert.equal((await state()).phase,'settled');await call('Emulation.setTouchEmulationEnabled',{enabled:false});
  note('Touch','Chrome touch input opens and finishes a work. Not physical-device evidence.');
  await navigate();await click('input[value="context"]');await click('#play');
  const background=await call('Target.createTarget',{url:'about:blank'});await call('Target.activateTarget',{targetId:background.targetId});
  await waitFor(s=>s.phase==='paused','Hidden tab pauses');await call('Target.activateTarget',{targetId:tab.id});
  assert.equal((await state()).phase,'paused');await call('Target.closeTarget',{targetId:background.targetId});await click('#finish');
  note('Hidden-tab lifecycle','Activating another isolated tab pauses active motion; returning does not autoplay.');
  await metrics(360,640);await navigate();await call('CSS.setEffectivePropertyValueForNode',{nodeId:await node('html'),propertyName:'font-size',value:'200%'});
  await click('#motion');await click('#play');assert.equal((await state()).overflow,false);await capture('enlarged-text');
  note('Enlarged text','200% root text reflows without page horizontal overflow; no assistive-technology certification.');
  await navigate();await call('DOM.focus',{nodeId:await node('#reaction')});await call('Input.insertText',{text:'B rearranges the work; I want more reading time. <img src=x>'});
  await click('#copy');assert.ok(await evaluate("document.querySelector('#summary').value.includes('not approval') && document.querySelector('#summary').selectionEnd===document.querySelector('#summary').value.length"));
  assert.equal(await evaluate("document.querySelectorAll('img').length"),0);
  note('Reaction notes','Native input remains literal text; the copyable summary explicitly grants no approval.');
  const tree=await call('Accessibility.getFullAXTree');assert.ok(tree.nodes.some(n=>!n.ignored && n.name?.value==='Pause'));
  note('Accessibility structure','Browser tree exposes native playback controls and labels; not a complete accessibility audit.');
  await call('Emulation.setScriptExecutionDisabled',{value:true});await navigate('',false);
  assert.equal(await evaluate("document.querySelector('#controls').hidden"),true);
  assert.ok(await evaluate("[...document.querySelectorAll('.static-case')].every(el=>el.getBoundingClientRect().height>0)"));
  await click('.project[data-work="structure"]');assert.equal(await evaluate('location.hash'),'#case-structure');await capture('no-script',false);
  note('No script','Native project links lead to readable still cases; playback is not falsely exposed.');
  await call('Emulation.setScriptExecutionDisabled',{value:false});
  assert.equal(requests.some(url=>/^https?:/.test(url)),false);assert.equal(errors.length,0,JSON.stringify(errors));
  note('Local delivery and console','No page HTTP(S) requests, captured warnings/errors or uncaught exceptions.');
} catch(error){report.failure=error.message;report.failureStack=error.stack;process.exitCode=1;}
finally{
  report.recordedAt=new Date().toISOString();
  await writeFile(resolve(output,'observations.json'),JSON.stringify(report,null,2)+'\n');
  ws?.close();chrome.kill('SIGTERM');await sleep(300);
  await rm(profile,{recursive:true,force:true,maxRetries:5,retryDelay:150});
}
console.log(JSON.stringify({checks:checks.length,failure:report.failure || null,output}));
