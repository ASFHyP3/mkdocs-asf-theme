# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [PEP 440](https://www.python.org/dev/peps/pep-0440/) 
and uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [0.3.2]

### Changed
* Tables are now displayed at maximum width.
* Announcement banner style has been improved.

## [0.3.1]

### Changed
* `mkdocs-asf-theme` now uses a `src` layout per this [recommendation](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).
* `mkdocs-asf-theme` now only uses `pyproject.toml` for package creation now that `setuptools` recommends [not using setup.py](https://setuptools.pypa.io/en/latest/userguide/quickstart.html#setuppy-discouraged).
- The contents of `main.html` have been moved to `partials/main.html` and `main.html` now extends from `partials/main.html`. This allows any project using this theme to override `main.html` and extend from `partials/main.html`, which allows projects to override blocks defined in [`base.html`](https://github.com/squidfunk/mkdocs-material/blob/9.4.2/src/templates/base.html).

## [0.3.0]

### Changed
- Upgraded `mkdocs-material` to v9.4.2. We have updated our templates in [asf_theme/partials](./asf_theme/partials) to match the [upstream versions](https://github.com/squidfunk/mkdocs-material/tree/9.4.2/src/templates/partials) as closely as possible. This introduces breaking changes. In particular:
    - If you want a footer, you should make the following change to your website's `mkdocs.yml` file:
      ```diff
      theme:
        features:
      +    - navigation.footer
      ```
    - You should carefully review your website to confirm that everything still renders and functions as expected.
    - If anything does not work as expected, you may want to read the [`mkdocs-material` upgrade guide](https://squidfunk.github.io/mkdocs-material/upgrade/) starting at [Upgrading from 6.x to 7.x](https://squidfunk.github.io/mkdocs-material/upgrade/#upgrading-from-6x-to-7x) for any other important changes that may apply to your website.

### Removed
- Analytics is no longer provided by default. You should follow <https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-analytics/> to enable analytics for your website.

### Fixed
- Fixed <https://github.com/ASFHyP3/mkdocs-asf-theme/issues/27> by upgrading `mkdocs-material`.

## [0.2.4](https://github.com/ASFHyP3/mkdocs-asf-theme/compare/v0.2.3...v0.2.4)

### Fixed
- MkDocs Material theme 6.2.0 breaks site generation, so the dependency is now pinned to `mkdocs-material>=6.2.1,<7.0`

## [0.2.3](https://github.com/ASFHyP3/mkdocs-asf-theme/compare/v0.2.2...v0.2.3)

### Fixed
- ASF logo and background map now appear correctly in "Project" or repo level sites

## [0.2.2](https://github.com/ASFHyP3/mkdocs-asf-theme/compare/v0.2.1...v0.2.2)

### Changed
- MkDocs Material theme 7 breaks the theme header, so the dependency is now pinned to `mkdocs-material>=6.0,<7.0`

## [0.2.1](https://github.com/ASFHyP3/mkdocs-asf-theme/compare/v0.2.0...v0.2.1)

### Changed
- HTML in partials footer no longer calls document.write() should fix bug where page gets deleted and replaced by current year
- Renamed github repository to `mkdocs-asf-theme` to mirror PyPI

## [0.2.0](https://github.com/ASFHyP3/mkdocs-asf-theme/compare/v0.1.0...v0.2.0)

### Added
- Social links to the footer
- Default Google Analytics settings

### Changed
- Added search functionality uses the `search.html` partial instead of being directly
  inserted into the header
- Now includes two logos for a site - the ASF logo (linking back to ASF), and the
  site logo (linking back to the site home page)
- Copyright in footer is now dynamic (provides `© YEAR `) and can be customized
  or removed

## [0.1.0](https://github.com/ASFHyP3/mkdocs-asf-theme/compare/v0.0.0...v0.1.0)

### Added
- MkDocs theme based on material to match ASF branding
