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

> [!WARNING]
> You should NOT include the `navigation.instant` feature in your `mkdocs.yml`.
> See <https://github.com/ASFHyP3/hyp3-docs/pull/371> for more information.

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

You can follow <https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-analytics/>
to enable analytics for your site.

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

## Development

### Upgrading `mkdocs-material` to a new major version

When upgrading the `mkdocs-material` dependency to a new major version,
you should reference the [upgrade guide](https://squidfunk.github.io/mkdocs-material/upgrade/)
for any important changes.

In particular, you should update each template `.html` file in [asf_theme/partials](./asf_theme/partials)
to match the latest upstream version as closely as possible.
Each template file should include a comment near the top of the file
with a link to the upstream version upon which it was based.
When updating a particular template file,
you can `diff` it against the linked upstream version to see what changes were made.
Then you can apply those changes to the *latest* upstream version of the file.

For example, when updating `header.html` from major version 9 to 10,
you can `diff` our version of `header.html` against the `9.x.x` upstream version linked near the top of the file.
Then you can download the latest `10.x.x` upstream version from <https://github.com/squidfunk/mkdocs-material>
and apply the `diff` changes, adapting them as necessary for the latest version of `mkdocs-material`.

You may also have to update
[asf_theme/assets/stylesheets/asf.css](./asf_theme/assets/stylesheets/asf.css),
[asf_theme/partials/main.html](./asf_theme/partials/main.html),
and [asf_theme/mkdocs_theme.yml](./asf_theme/mkdocs_theme.yml) as appropriate.
