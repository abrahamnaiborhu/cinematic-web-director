(() => {
  const vessel = document.querySelector('#vessel');
  const shadow = document.querySelector('#shadow');
  const replay = document.querySelector('#replay');
  const settle = document.querySelector('#settle');
  const status = document.querySelector('#motion-status');
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (!vessel.animate || !window.IntersectionObserver) return;

  let animations = [];
  let played = false;

  function showStill() {
    for (const animation of animations) {
      animation.onfinish = null;
      animation.cancel();
    }
    animations = [];
    status.textContent = preference.matches ? 'Reduced motion · still composition' : 'Still composition';
  }

  function play() {
    showStill();
    if (preference.matches) return;
    played = true;
    status.textContent = 'Welcome playing';
    const timing = { duration: 1100, easing: 'cubic-bezier(.22,.61,.36,1)' };
    animations = [
      vessel.animate([{ transform: 'translateY(-12px)' }, { transform: 'translateY(0)' }], timing),
      shadow.animate([{ transform: 'scale(.94)', opacity: .65 }, { transform: 'scale(1)', opacity: 1 }], timing),
    ];
    animations[0].onfinish = showStill;
  }

  document.querySelector('#controls').hidden = false;
  replay.addEventListener('click', play);
  settle.addEventListener('click', () => { played = true; showStill(); });
  preference.addEventListener('change', () => {
    replay.disabled = preference.matches;
    showStill();
  });
  replay.disabled = preference.matches;
  showStill();

  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (entry.isIntersecting && !played) play();
      if (!entry.isIntersecting && animations.length) showStill();
    }
  }, { threshold: .35 });
  observer.observe(document.querySelector('#illustration'));
  window.addEventListener('resize', showStill);
  document.addEventListener('visibilitychange', () => { if (document.hidden) showStill(); });
})();
