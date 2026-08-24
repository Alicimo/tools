# AGENTS

This repository is a collection of single-file HTML tools with inline page-specific CSS/JS. Vendored shared `98.css` is the default exception for the tool surface.
Use these notes to keep edits consistent and low-friction for future agents.

## Repo map
- `index.html` is the catalog page that links to each tool.
- Each tool lives in a single `.html` file at repo root.
- `resources/` holds local data files and vendored assets used by tools (including `98.css`, SE98 icons, BibTeX, and ICS).
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
- New tools should link `resources/98-css/98.css` and use semantic 98.css structures for one primary application window and its controls.
- Keep page-specific layout and third-party integration CSS in an inline `<style>` block near the top; there is no repository wrapper stylesheet.
- Inline JS in a `<script>` block at the end of the document.
- Prefer semantic tags (`header`, `main`, `section`, `article`).
- Keep each tool self-contained, with the vendored 98.css link as the shared-style exception.

## Formatting
- Indentation: 2 spaces.
- HTML attributes use double quotes.
- JS uses no trailing semicolons.
- Use single quotes for JS strings unless HTML requires double quotes.
- Keep lines reasonably short; wrap long attribute lists or gradients.
- Align multi-line attributes with the opening tag (see `index.html`).

## CSS conventions
- Prefer CSS variables on `:root` or `html` for shared colors.
- Prefer light/dark theme handling with `prefers-color-scheme` when used.
- Use simple class names; avoid deeply nested selectors.
- Keep animations and transitions explicit and short.
- Use `@media (hover)` to gate hover styles for touch devices.
- Use 98.css by default for new tools. Do not combine Bootstrap and 98.css; new themed pages should not use Bootstrap.
- Specialized surfaces may keep local styles when the core surface is a chart, canvas, editor, game, or is otherwise materially harmed by 98.css; record or preserve that rationale. Current exception files are `calories.html`, `swipe.html`, `golden-sun-class-explorer.html`, `text-annotator.html`, `notepad.html`, and `vim-snake.html`.
- Responsive/mobile usability may override authentic 98.css dimensions. Do not add nonfunctional window controls.

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
- `index.html` is an Explorer-style 98.css catalog that uses the vendored SE98 icon subset.
- Maintain the responsive icon grid and total count when adding/removing tools.
- `notepad.html` and the other listed exception files are intentionally standalone specialized surfaces.

## When adding a new tool
- Create a new `<tool>.html` at repo root.
- Add a corresponding icon-grid entry to `index.html` with a short description.
- Link `resources/98-css/98.css` and build one primary application window with semantic 98.css structures and functional controls.
- Keep page-specific and integration CSS inline. Use the specialized-surface exception only with a clear rationale; do not use Bootstrap on a new themed page.
- Keep the tool self-contained; no build steps required.

## Testing checklist (manual)
- Open the tool in a browser and exercise primary flows.
- Verify the vendored 98.css and any vendored icon resources load, and that every displayed window control is functional.
- Check layout on narrow/mobile widths.
- Reload to verify persistence if localStorage is used.
- Verify any external resources load without console errors.

## Git hygiene for agents
- Do not modify unrelated tools unless requested.
- Avoid reformatting entire files; limit edits to relevant sections.
- Preserve existing visual language of each tool.

## Examples from this repo
- Multi-line attribute formatting in `index.html`.
- Explorer-style catalog and vendored SE98 icons in `index.html`.
- Inline scripting and async helpers in `notepad.html`.
- CSS theming with `prefers-color-scheme` in `notepad.html`.

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
