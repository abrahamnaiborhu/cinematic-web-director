# Device Experience: Design Motion for the Supported Audience

Read this during concept/motion development, responsive treatment and device QA. Use the [creative workflow](CREATIVE_WORKFLOW.md) and [motion direction](MOTION_DIRECTION.md). Apply relevant checks to targeted work; do not reopen an approved design or expand a sprint merely to complete a generic device checklist.

## Establish device coverage before the large-screen design hardens

Use known audience and project constraints. For a new or substantial public-site design, treat phones and compact laptop windows as first-class experiences from concept exploration, then develop larger-screen enhancements. If device priorities or browser support are consequential and unclear, propose a coverage plan and ask one focused question. Do not make clients provide analytics or hardware before creative planning can proceed.

Describe the same important idea or interaction at phone, compact-laptop and larger-screen sizes. Adapt composition and choreography deliberately. A narrow version need not reproduce a desktop pin or 3D scene exactly, but disabling a major moment below a breakpoint is a design decision to explain, not automatic mobile completion. Propose a suitable smaller-screen animated treatment when it serves the approved direction and is feasible. Reduced-motion/static access remains separately available; touch input alone does not imply a reduced-motion preference.

Use CSS viewport dimensions, available height, browser chrome, text size and input capabilities. Physical screen size and device labels do not determine the browser's usable area. Do not assume a small device is slow, a large device is fast, or a wide viewport has hover. Assess support and observed performance rather than inferring hardware capability from width.

## Keep a practical coverage matrix

Adapt these starting points to the audience, actual breakpoints and approved scope. They are representative CSS-pixel viewports, not promises to test every device or mandatory product breakpoints.

| Representative case | Example viewport | What needs deliberate attention |
|---|---|---|
| Narrow/short phone | 360 × 640 | Content, actions, touch controls and motion remain usable in limited space |
| Typical portrait phone | 390 × 844 | Authored composition and motion; browser controls expanding/collapsing |
| Compact laptop window | 1280 × 720 or 1024 × 600 | Short-height composition, pinning budgets, sticky navigation and readable diagrams |
| Larger laptop/desktop | 1440 × 900 or the approved reference size | Larger composition/enhancements without making them the only complete experience |
| Tablet, landscape or hybrid input | Select when relevant | Orientation changes, touch plus mouse, keyboard and layout transitions |

Record browser/OS, input, motion preference, viewport, intended treatment, required evidence and actual result. Include iPhone Safari and Android Chrome for a general mobile audience unless the supported scope says otherwise; add other browsers reported by the client or relevant to the audience. A report affecting iPhone Safari and Chrome needs those environments considered explicitly. Keep device targets distinct from environments actually tested.

Browser emulation is useful for dimensions, layout and some input/media-query behavior. Desktop Chrome resized to a phone width is not an iPhone Safari or Android hardware test. Label it as emulated and leave OS font rendering, browser-specific behavior and hardware performance unverified until observed in the relevant environment. Record client-supplied captures/observations separately from agent-run checks. Missing device access does not prevent planning; do not claim complete QA or silently waive an approved acceptance criterion.

## Author behavior for space, input and change

For each important treatment, decide what persists, reflows, changes trigger or simplifies across the matrix. Preserve story/content, meaningful agency, keyboard access and readable actions. Avoid shrinking a wide diagram until labels become unreadable or removing the main idea from the phone experience.

- Check viewport height as well as width. Inspect pinned/sticky content, text and controls in short windows; avoid hidden exits, overlapping navigation, long empty scroll distances or clipped essential states.
- Provide touch/keyboard equivalents for hover-dependent information or controls. Use actual input capability where relevant; hover and pointer media queries describe capabilities rather than device brands. See [W3C Media Queries](https://www.w3.org/TR/mediaqueries-4/#hover).
- Consider mobile browser controls and safe areas for fixed content. Choose viewport units for the intended stability or resizing behavior; `svh` and `dvh` address different viewport sizes. Verify the result rather than prescribing one unit universally. See [MDN viewport-relative lengths](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#relative_length_units_based_on_viewport).
- Recheck orientation, resize, text enlargement, direct entry and returning to a page where relevant. Responsive changes must not leave duplicate animation instances, stale scroll ranges or an unreadable intermediate state.
- Preserve the core experience when features or resources are unavailable. Distinguish a justified simplified treatment, user-selected reduced motion and an implementation that has only been designed for large screens.

Observe motion over time at required sizes: entry, important intermediate states, settled state, interruptions and exit. Screenshots support composition but cannot establish timing, smoothness, touch control or physical-device performance. Define qualitative acceptance criteria first and measure performance under recorded conditions where tools permit.

## Use deliberate UI icons across platforms

Inspect arrows, checks, menu controls and other functional symbols as well as images and type. Unicode characters such as `↗` and `↘` can receive text or emoji presentation depending on the environment. The screenshot alone cannot identify the OS or exact rendering cause. Confirm the code and reported browser/device before claiming reproduction. [Unicode presentation guidance](https://www.unicode.org/reports/tr51/#Presentation_Style) explains the distinction and text-presentation selector U+FE0E.

For a consistent monochrome UI symbol, prefer the project's existing SVG icon component/set or a small reusable vector component using `currentColor`. Do not add a library for one arrow or replace an established icon language without reason. A text-presentation selector can request text rendering for supported characters, but is not a guarantee of identical glyph design across platforms. Deliberate brand/content emoji remain valid; do not strip them from client content indiscriminately.

For example, this decorative arrow can accompany a link whose visible text already describes the action:

```html
<svg class="ui-icon" viewBox="0 0 24 24" width="16" height="16"
     fill="none" stroke="currentColor" stroke-width="1.5"
     stroke-linecap="round" stroke-linejoin="round"
     aria-hidden="true" focusable="false">
  <path d="M7 17 17 7M7 7h10v10" />
</svg>
```

Keep the icon's size, alignment, stroke and spacing consistent. Decorative icons should not duplicate spoken link text; icon-only controls still need accessible names. See [W3C decorative-image guidance](https://www.w3.org/WAI/tutorials/images/decorative/). Verify the implemented component in the reported environments; a valid SVG example does not prove a live website has been fixed.

## Approval and evidence

Before production, include representative phone and compact-laptop compositions/treatments and the agreed coverage matrix. Scope experiments to the devices/input conditions that will decide the uncertainty. During an approved sprint, fix relevant responsive defects within scope; propose consequential new choreography or scope changes for the affected decision.

Before website release, account for each required row with actual evidence or an explicitly agreed limitation. The preflight checker's desktop/mobile PNG requirement is a technical floor, not full device coverage or cross-browser certification. Passing that check does not prove compact-laptop motion, iPhone icon rendering or real-device performance. Use the project script, treatments and iteration log to retain the actual acceptance/evidence record.
