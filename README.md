# AI_Course
## sli.dev
- Offers a lot, but has some rough edges.
- Start up `devcontainer`
- Run `npx slidev`
- Sub-pages do not cause auto-reloads.
    - Have to either trigger a page reflow in the top-level `slides.md` (via an error like adding a character to the page path or toggling the `hide` attribute)
    - Best to develop subpages/sections separately
        - Can bring up via: `npx slidev {markdown_file}`
