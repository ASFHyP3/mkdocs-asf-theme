# ASF MkDocs Theme

An extension of the [MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/)
for ASF.

## Analytics

By Default this theme will provide correct Google Analytics for ASF documentation site.
However, analytics can be customized in your `mkdocs.yml` with
```yaml
google_analytics:
  - UA-XXXXXXXX-X
  - auto  # or a specific site URL
```

Likewise, to turn off analytics entirely, remove the site level `google_analytics`
configuration and clear the theme one with
```yaml
```yaml
theme:
  name: "asf-theme"
  google_analytics:
```


## Logos

By default, this theme will provide both the ASF logo and a site logo.

### ASF logo

You can change the ASF logo and/or logo URL with
```yaml
theme:
  name: "asf-theme"
  asf_logo: images/asf-altenate-logo.png
  asf_logo_url: https://asf.alaska.edu/
```

or remove the ASF logo with
```yaml
theme:
  name: "asf-theme"
  asf_logo:
```

### Site logo
With the Material Theme, there are
[two ways to change the site logo](https://squidfunk.github.io/mkdocs-material/setup/changing-the-logo-and-icons/#logo).

1. You can change site logo with a direct link to an image
   ```yaml
   theme:
     name: "asf-theme"
     logo: images/my-logo.png
   ```

2. or by specifying an icon
   ```yaml
   theme:
     name: "asf-theme"
     icon:
       logo: material/library
   ```


To remove the site logo, specify an empty icon (and no theme logo)
```yaml
theme:
  name: "asf-theme"
  icon:
    logo:
```

## Copyright notice

By default, this theme will provide a copyright notice like
```
© [YEAR] Alaska Satellite Facility
```
where `[YEAR]` is replaced with the current year. You can customize the text after
`© [YEAR]` in your `mkdocs.yml` with
```yaml
copyright: Alaska Satellite Facility
```

Likewise, to turn off analytics entirely, remove the site level `copyright`
configuration and clear the theme one with
```yaml
theme:
  name: "asf-theme"
  copyright:
```

## Social links

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
  name: "asf-theme"
  social:
    - icon: fontawesome/brands/gitter
      link: https://gitter.im/ASFHyP3/community
```
