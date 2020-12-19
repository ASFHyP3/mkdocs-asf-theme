# ASF MkDocs Theme

An extension of the [MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/)
for ASF.

## Logos

By default, this theme will provide both the ASF logo and a site logo.

### ASF logo

You can change the ASF logo with
```yaml
theme:
  name: "asf-theme"
  asf_logo: images/asf-altenate-logo.png
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
