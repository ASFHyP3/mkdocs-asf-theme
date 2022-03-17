# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [PEP 440](https://www.python.org/dev/peps/pep-0440/) 
and uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


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
