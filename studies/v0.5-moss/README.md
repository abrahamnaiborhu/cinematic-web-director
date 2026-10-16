# Moss Studio: one welcoming gesture

Synthetic fixture and isolated motion study, not a production website. [Scope and client authorization](../../evaluations/V0_5_STUDY_PLAN.md).

Open `index.html` in a browser, or serve this folder locally. Compare **Replay welcome** with **Show still version**. Text and the booking placeholder are available throughout. The illustration plays once when reached; reduced motion shows stillness. Study controls are review aids, not approved production UI.

The optional dependency-free browser check was run with Node 24 and local Chrome on macOS:

```bash
node studies/v0.5-moss/check-browser.mjs dist/evaluations/v0.5/study/recheck
```

It launches an isolated temporary Chrome profile, saves captures/JSON, then closes that browser and removes its temporary profile. Set `CINEMATIC_CHROME_BINARY` to an existing Chrome executable when using another installation path. This harness is not a Safari/Firefox or physical-device test; those checks remain separate.

The inline SVG derives from [the supplied illustration](../../evaluations/fixtures/v0.5/landing/assets/ceramics-study.svg): its vessel geometry is preserved and grouped separately from the ground/shadow. No workshop photograph, availability or service facts have been invented. Typography uses local system/Georgia fallbacks; no dependencies or network assets are needed.

Implementation references: [Element.animate](https://developer.mozilla.org/en-US/docs/Web/API/Element/animate), [matchMedia](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia). Observations and remaining validation limits belong in the v0.5 evaluation report; source code alone is not motion evidence.
