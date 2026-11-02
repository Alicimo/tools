# Tool icons

Each root HTML page links to its own SVG favicon and opaque 180 × 180 PNG
Apple touch icon. The original drawings use a shared line style, warm ink colors,
and generous margins. Backgrounds extend to the edges; iOS applies its own mask.

Edit the SVG source, then regenerate its PNG with ImageMagick (development only):

```sh
magick -background white -density 384 resources/icons/notepad.svg -resize 180x180 -alpha off PNG24:resources/icons/notepad-apple-touch-icon.png
```

Use the same filename pattern and both links when adding a tool. No runtime
library, manifest, or build step is required for these icons.

Apple reference: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html
