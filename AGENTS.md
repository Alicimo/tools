# AGENTS

This repository is a collection of single-file HTML tools with inline page-specific CSS/JS. All pages share the Editorial theme in `resources/tools.css`.
Use these notes to keep edits consistent and low-friction for future agents.

## Repo map
- `index.html` is the catalog page that links to each tool.
- Each tool lives in a single `.html` file at repo root.
- `resources/` holds the shared stylesheet, local data files, and any required vendored assets.
- There is no build system or package manager configured.

## Commands (build/lint/test)
There are no configured build, lint, or test commands in this repo.
Use manual checks and a static server when needed.

Common dev commands:
- `python3 -m http.server` (serve the repo at `http://localhost:8000`).
- `open index.html` (macOS: open the catalog in the browser).
- `open <tool>.html` (open a specific tool page).
- `uv run resources/fetch_podcast.py --rss-url <url> --out resources/episodes.json` (refresh podcast dataset).

Single-test equivalents:
- No automated tests exist, so there is no single-test command.
- For manual verification, open the specific HTML file in a browser.

## HTML structure
- Use `<!doctype html>` and a simple `<html lang="en">` layout.
- Keep `<meta charset>` and viewport in the head (or top of file for minimal pages).
- Every tool must link `resources/tools.css` before its inline `<style>` block.
- Include the shared `.tool-nav` navigation with the `Personal tools` brand and an `All tools` link to `index.html`. Use `.tool-shell` for the main content container where appropriate.
- Keep page-specific layout and third-party integration CSS in an inline `<style>` block near the top.
- Inline JS in a `<script>` block at the end of the document.
- Prefer semantic tags (`header`, `main`, `section`, `article`).
- Keep each tool self-contained, with `resources/tools.css` as the shared-style exception.

## Formatting
- Indentation: 2 spaces.
- HTML attributes use double quotes.
- JS uses no trailing semicolons.
- Use single quotes for JS strings unless HTML requires double quotes.
- Keep lines reasonably short; wrap long attribute lists or gradients.
- Align multi-line attributes with the opening tag (see `index.html`).

## CSS conventions
- Prefer CSS variables on `:root` or `html` for shared colors.
- The selected Editorial theme uses a white background, warm gray accents, Georgia headings, and system sans-serif controls. Keep the interface light even when the device prefers dark mode.
- Use the `--tool-*` tokens in `resources/tools.css` for interface colors and fonts. Keep shared controls, typography, focus states, and spacing in that stylesheet; do not duplicate them in each tool.
- Use simple class names; avoid deeply nested selectors.
- Keep animations and transitions explicit and short.
- Use `@media (hover)` to gate hover styles for touch devices.
- Do not introduce Bootstrap, desktop window chrome, or a second global UI theme.
- Charts, canvases, editor content, and annotation output may retain task-specific colors and typography. Their surrounding navigation and controls must still use the shared theme. Document the rationale near specialized styles.
- Prefer whitespace, thin dividers, and underlined active tabs over nested cards, shadows, and rounded panels.
- Design for mobile first: 16px editable text, controls at least 44px tall, wrapping toolbars, and stacked forms. Contain necessary wide-table scrolling inside the table wrapper; the page itself must not overflow at 320px.
- Scope third-party integrations (Leaflet, Tabulator, FullCalendar, Mermaid) so shared styles do not break their geometry or generated output.

## JavaScript style
- Use `const` by default; use `let` only when reassigning.
- Use arrow functions for callbacks; use named functions for reusable logic.
- Prefer `addEventListener` over inline event attributes.
- Keep globals minimal; if unavoidable, declare them once near the top.
- Keep DOM queries near usage and cache when reused.
- Use `async`/`await` for async flows; avoid mixing with `.then()`.
- Prefer early returns for guard clauses.

## Naming conventions
- Functions: verbs or verb phrases (`loadData`, `renderChart`).
- Variables: camelCase (`toolState`, `activeIndex`).
- Constants: camelCase for values, SCREAMING_SNAKE_CASE only for fixed config.
- CSS classes: kebab-case (`tool-card`, `hero-title`).
- IDs: kebab-case or lowerCamelCase, but stay consistent within a file.

## Error handling
- Favor resilient UI behavior; avoid throwing in event handlers.
- Wrap storage or network access in `try/catch` and degrade gracefully.
- When a failure is user-visible, update the UI instead of `alert()`.
- Use `console.error` for unexpected failures; keep logs minimal.

## Data and assets
- Use relative paths for local resources (see `resources/`).
- Large data should live in `resources/` instead of inline strings.
- Preserve licenses and source metadata for vendored styles and icons.
- If using external CDN assets, keep versions pinned in URLs.
- `resources/fetch_podcast.py` uses uv inline script metadata for dependencies (no requirements.txt).

## Accessibility
- Provide labels for inputs and controls.
- Ensure focus states are visible for interactive elements.
- Avoid color-only cues; include text or icons.

## Performance
- Avoid heavy libraries; these pages are meant to be lightweight.
- Debounce expensive input handlers when needed.
- Prefer `requestAnimationFrame` for canvas or animation loops.

## File-specific notes
- `index.html` is a text-first Editorial catalog with a responsive two-column list.
- Maintain the catalog links and total count when adding/removing tools.
- `notepad.html` exports self-contained notes by embedding the shared stylesheet. Preserve that behavior when changing styles or export code.
- `text-annotator.html` hides navigation and controls in screenshot mode; preserve its user-selected output fonts and highlight colors.
- `vim-snake.html` uses native dialogs and touch direction controls; its dark canvas is a contrast aid, not a separate page theme.

## When adding a new tool
- Create a new `<tool>.html` at repo root.
- Add a corresponding catalog entry to `index.html` with a short description and update the count.
- Link `resources/tools.css`, add the shared navigation and one descriptive `h1`, and use native labeled controls.
- Keep page-specific layout and integration CSS inline. Extend the shared stylesheet only for patterns useful across tools.
- Keep the tool self-contained; no build steps required.

## Testing checklist (manual)
- Open the tool in a browser and exercise primary flows.
- Verify `resources/tools.css` loads and shared navigation works.
- Check desktop and narrow/mobile widths, including 320px, for page overflow, readable forms, and usable touch targets.
- Reload to verify persistence if localStorage is used.
- Verify any external resources load without console errors.

## Git hygiene for agents
- Do not modify unrelated tools unless requested.
- Avoid reformatting entire files; limit edits to relevant sections.
- Preserve the shared Editorial visual language and each tool's task-specific behavior.

## Examples from this repo
- Multi-line attribute formatting in `index.html`.
- Editorial catalog and shared navigation in `index.html`.
- Inline scripting and async helpers in `notepad.html`.
- Shared theme tokens and control styles in `resources/tools.css`.

## Out of scope
- No TypeScript or build tooling is present.
- No linting or formatting tools are configured.
- No unit tests or test runner is configured.

## If you add tooling
- Document the new commands here.
- Add a single-test example (e.g., per-file or per-suite).
- Prefer lightweight tools that do not require a bundler.

## Writing conventions
- Keep copy concise and functional.
- Use sentence case for headings and labels.
- Avoid excessive marketing language.

## Security and privacy
- Do not add tracking or analytics by default.
- Avoid fetching remote data unless required for the tool.

## Browser support
- Target modern evergreen browsers.
- Use feature detection (`if ('serviceWorker' in navigator)`) when needed.

## Notes for agentic coding
- These pages ship as-is; there is no compilation step.
- Read the target HTML file fully before making structural changes.
- Match the surrounding style and spacing to avoid visual churn.

## Maintainer preferences
- Keep tools single-file unless a strong reason exists.
- Favor clarity over abstraction; readable code beats cleverness.

## Contact
- No explicit maintainer contact info in this repo.
