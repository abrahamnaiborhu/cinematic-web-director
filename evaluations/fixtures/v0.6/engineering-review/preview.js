export function mountPoster(root, preference = window.matchMedia('(prefers-reduced-motion: reduce)')) {
  const button = root.querySelector('[data-open]');
  const artwork = root.querySelector('[data-artwork]');
  let animation;
  const settle = () => {
    animation?.cancel();
    animation = undefined;
  };
  const open = () => {
    settle();
    if (preference.matches) return;
    animation = artwork.animate([
      { transform: 'rotate(-7deg) scale(.95)', offset: 0 },
      { transform: 'rotate(-7deg) scale(.94)', offset: .2 },
      { transform: 'rotate(0deg) scale(1)', offset: 1 },
    ], { duration: 650, easing: 'cubic-bezier(.22,.61,.36,1)' });
  };
  button.addEventListener('click', open);
  window.addEventListener('resize', settle);
  preference.addEventListener('change', settle);
  return () => {
    button.removeEventListener('click', open);
    settle();
  };
}
