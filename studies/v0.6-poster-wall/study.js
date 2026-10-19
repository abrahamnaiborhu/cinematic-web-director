(() => {
  const preference = matchMedia('(prefers-reduced-motion: reduce)');
  const comparison = document.querySelector('#comparison');
  const status = document.querySelector('#motion-status');
  const replay = document.querySelector('#replay');
  const details = [...document.querySelectorAll('.detail')];
  const collection = document.querySelector('.collection');
  let variant = 'a';
  let selected;
  let lastStudy = 'sideways';
  let collectionScroll = 0;
  let animations = [];
  let generation = 0;

  const canMove = () => !preference.matches && variant !== 'still' && typeof Element.prototype.animate === 'function';
  const describe = () => {
    replay.disabled = !selected || !canMove();
    status.textContent = preference.matches ? 'Reduced motion: complete still artwork.'
      : !selected ? 'Choose a poster. Then compare A, B and stillness.'
      : variant === 'still' ? 'Still: the same work, without the handoff.'
      : !canMove() ? 'Animation unavailable: complete still artwork.'
      : variant === 'a' ? 'A · Choose — shove — still.'
      : 'B · Choose — sweep — correct — still.';
  };
  const settle = () => {
    generation++;
    animations.forEach(animation => animation.cancel());
    animations = [];
    document.querySelectorAll('.companion').forEach(image => image.remove());
    describe();
  };
  const play = () => {
    settle();
    if (!selected || !canMove()) return;
    const artwork = selected.querySelector('.artwork');
    const other = details.find(detail => detail !== selected).querySelector('.artwork');
    const companion = other.cloneNode();
    companion.className = 'companion';
    companion.alt = '';
    companion.setAttribute('aria-hidden', 'true');
    selected.querySelector('.stage').prepend(companion);
    const compact = innerWidth <= 700;
    const distance = compact ? 28 : innerWidth <= 1100 ? 54 : 76;
    const duration = variant === 'a' ? 510 : 840;
    const move = (x, y = 0, angle = 0) => `translate(${x}px, ${y}px) rotate(${angle}deg)`;
    const frames = variant === 'a' ? [
      {transform:move(distance, 6, 2),offset:0,easing:'cubic-bezier(.12,.8,.2,1)'},
      {transform:move(1),offset:.86,easing:'ease-out'},
      {transform:move(0),offset:1},
    ] : [
      {transform:move(distance, 8, 3),offset:0,easing:'ease-in'},
      {transform:move(distance * .9, 6, 2),offset:.18,easing:'cubic-bezier(.16,.8,.24,1)'},
      {transform:move(compact ? -7 : -13, -2, -.7),offset:.75,easing:'ease-out'},
      {transform:move(0),offset:1},
    ];
    const run = generation;
    animations = [
      artwork.animate(frames, {duration,fill:'none'}),
      companion.animate([
        {transform:move(-distance * .45, 0, -2),opacity:1,offset:0},
        {transform:move(-distance * 1.3, 3, -3),opacity:1,offset:.6},
        {transform:move(-distance * 2.8, 8, -5),opacity:0,offset:1},
      ], {duration:duration - 90,delay:variant === 'a' ? 70 : 90,fill:'both',easing:variant === 'a' ? 'cubic-bezier(.22,.75,.3,1)' : 'ease-in-out'}),
    ];
    status.textContent = variant === 'a' ? 'A · Shove and hold — playing.' : 'B · Overshoot and correct — playing.';
    // Cancellation rejects finished; a departed run must never clear a newer one.
    Promise.all(animations.map(animation => animation.finished)).then(() => {
      if (generation === run) settle();
    }).catch(() => {});
  };
  const render = (hash, {animate = false, focus = false} = {}) => {
    settle();
    selected = details.find(detail => `#${detail.id}` === hash);
    document.body.dataset.view = selected ? 'detail' : 'collection';
    details.forEach(detail => { detail.hidden = !!selected && detail !== selected; });
    if (selected) {
      lastStudy = selected.id;
      selected.querySelector('.detail-heading').append(comparison);
      if (focus) {
        selected.querySelector('h2').focus({preventScroll:true});
        comparison.scrollIntoView({block:'start'});
        window.scrollBy(0, selected.querySelector('h2').getBoundingClientRect().top - 8);
      }
      if (animate) play();
    } else if (hash === '#contact-note') {
      document.querySelector('.intro').after(comparison);
      document.querySelector('#contact-note').focus({preventScroll:true});
      document.querySelector('#contact-note').scrollIntoView({block:'start'});
    } else if (focus) {
      document.querySelector('.intro').after(comparison);
      window.scrollTo(0, collectionScroll);
      document.querySelector(`#choose-${lastStudy}`).focus({preventScroll:true});
    }
    if (!animate) describe();
  };
  document.body.classList.add('enhanced');
  comparison.hidden = false;
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href^="#"]');
    if (!link || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const hash = link.getAttribute('href');
    if (!['#work','#after-hours','#sideways','#contact-note'].includes(hash)) return;
    event.preventDefault();
    if (document.body.dataset.view === 'collection' && hash !== '#work') collectionScroll = scrollY;
    if (location.hash !== hash) history.pushState(null, '', hash);
    render(hash, {animate:hash === '#after-hours' || hash === '#sideways',focus:true});
  });
  comparison.addEventListener('change', event => {
    if (event.target.name !== 'treatment') return;
    variant = event.target.value;
    settle();
  });
  replay.addEventListener('click', () => {
    selected?.querySelector('.stage').scrollIntoView({block:'nearest'});
    play();
  });
  // One document owns these listeners; routes do not register additional copies.
  window.addEventListener('hashchange', () => render(location.hash, {focus:true}));
  window.addEventListener('resize', settle);
  window.addEventListener('pagehide', settle);
  preference.addEventListener('change', settle);
  render(location.hash);
})();
