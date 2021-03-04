# ASF MkDocs Theme

[![PyPI license](https://img.shields.io/pypi/l/mkdocs-asf-theme.svg)](https://pypi.python.org/pypi/mkdocs-asf-theme/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/mkdocs-asf-theme.svg)](https://pypi.python.org/pypi/mkdocs-asf-theme/)
[![PyPI version](https://img.shields.io/pypi/v/mkdocs-asf-theme.svg)](https://pypi.python.org/pypi/mkdocs-asf-theme/)

[![DOI](https://zenodo.org/badge/322375450.svg)](https://zenodo.org/badge/latestdoi/322375450)

An extension of the [MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/)
for ASF.

## Quickstart

This theme is distributed on [PyPI](https://pypi.org/project/mkdocs-asf-theme/) and can be installed into a Python 3.8+ environment using `pip`:
```
python -m pip install mkdocs-asf-theme
```

To use this theme, add the following lines to your `mkdocs.yml`:
```yaml
theme:
  name: asf-theme
```

To see an example of using this theme, see [ASF HyP3's MkDocs repository](https://github.com/ASFHyP3/ASFHyP3)
which generates [ASF HyP3's documentation](https://hyp3-docs.asf.alaska.edu/).

## Customization

This theme has been developed with sensible defaults to be used out-of-the-box by
ASF documentation sites. While sections below describe how to customize the
ASF-specific features of this theme, we hope most users won't need them.

Because this theme is an extension of the [MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/),
advanced customization can be done by following the MkDocs Material Theme
[documentation](https://squidfunk.github.io/mkdocs-material/). **However**, please
consider either:
* [opening an issue](https://github.com/ASFHyP3/mkdocs-asf-theme/issues)
  and requesting any customization you need to be incorporated into this theme
* Opening a pull request to this theme with your customizations so they are available
  to all ASF documentation sites

### Analytics

This theme will provide Google Analytics integration for an ASF documentation site.
However, analytics can be customized in your `mkdocs.yml` with
```yaml
google_analytics:
  - UA-XXXXXXXX-X
  - auto  # or a specific site URL
```

To turn off analytics entirely, remove the site level `google_analytics`
configuration and clear the theme one with
```yaml
theme:
  name: asf-theme
  google_analytics:
```

### Logos

This theme will provide both the ASF logo and a site logo.

#### ASF logo

You can change the ASF logo and/or logo URL with
```yaml
theme:
  name: asf-theme
  asf_logo: images/asf-altenate-logo.png
  asf_logo_url: https://asf.alaska.edu/
```

or remove the ASF logo with
```yaml
theme:
  name: asf-theme
  asf_logo:
```

#### Site logo
With the Material Theme, there are
[two ways to change the site logo](https://squidfunk.github.io/mkdocs-material/setup/changing-the-logo-and-icons/#logo).

1. You can change site logo with a direct link to an image
   ```yaml
   theme:
     name: asf-theme
     logo: images/my-logo.png
   ```

2. or by specifying an icon
   ```yaml
   theme:
     name: asf-theme
     icon:
       logo: material/library
   ```


To remove the site logo, specify an empty icon (and no theme logo)
```yaml
theme:
  name: asf-theme
  icon:
    logo:
```

### Copyright notice

This theme will provide a copyright notice like
```
© [YEAR] Alaska Satellite Facility
```
where `[YEAR]` is replaced with the current year. You can customize the text after
`© [YEAR]` in your `mkdocs.yml` with
```yaml
copyright: Alaska Satellite Facility
```

To turn off the copyright notice entirely, remove the site level `copyright`
configuration and clear the theme one with
```yaml
theme:
  name: asf-theme
  copyright:
```

### Social links

You can add *additional* social links with
```yaml
extra:
  social:
    - icon: fontawesome/brands/gitter
      link: https://gitter.im/ASFHyP3/community
```
 
You can *override* the theme provided social links with
```yaml
theme:
  name: asf-theme
  social:
    - icon: fontawesome/brands/gitter
      link: https://gitter.im/ASFHyP3/community
```
