# Image Compressor (Client-side)

A tiny, dependency-free tool to compress and resize images in the browser.  
- Choose an image
- Set quality and max dimensions
- Preview original vs compressed
- Download the result (WEBP if supported, otherwise JPEG)

## Run
Just open `index.html` in a browser (no build step).

## Files
- `index.html` – markup and controls
- `styles.css` – minimal UI
- `script.js` – compression logic (Canvas API)

## How it works
1. Read the file with an `<input type="file">`
2. Draw to `<canvas>` (optionally scaled down)
3. Export via `canvas.toBlob(type, quality)` to WEBP/JPEG
4. Trigger a download with an `<a download>` link

## Notes
- Uses `URL.createObjectURL` to preview and download.
- Chooses WEBP when supported; falls back to JPEG.
- No external libraries.
