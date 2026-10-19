import { mountPoster } from './preview.js';

export function createPosterRoute() {
  let dispose;
  return {
    show(root) {
      dispose?.();
      dispose = mountPoster(root);
    },
    leave() {
      dispose?.();
      dispose = undefined;
    },
  };
}
