# 3D SciVis Model Viewer

Static `<model-viewer>` site for reviewing MATLAB-to-Blender scientific visualization assets in a browser and on AR-capable mobile devices.

The site uses optimized GLB files for inline web viewing and paired USDZ files for Apple Quick Look on iPhone and iPad.

## Local Testing

Run the local server from the repository root:

```bash
python3 scripts/serve_local.py --host 0.0.0.0 --port 8765
```

Open the local page:

```text
http://127.0.0.1:8765/
```

For iPhone testing, put the phone on the same Wi-Fi network and open the Mac's LAN address:

```text
http://<mac-lan-ip>:8765/
```

Verify MIME headers before testing Apple Quick Look:

```bash
curl -I http://127.0.0.1:8765/assets/models/usdz-mobile-globe-detail-fixed/usdz-mobile-globe-detail-fixed.opt.glb
curl -I http://127.0.0.1:8765/assets/models/usdz-mobile-globe-detail-fixed/usdz-mobile-globe-detail-fixed-8k.usdz
```

Expected content types:

```text
model/gltf-binary
model/vnd.usdz+zip
```

## GitHub Pages

This repository is designed to publish from the `main` branch root with GitHub Pages.

Expected project site URL:

```text
https://jimmydx.github.io/3d-scivis-model-viewer/
```

Production AR checks should use HTTPS. WebXR requires HTTPS, while Apple Quick Look requires the USDZ URL to be served with:

```text
Content-Type: model/vnd.usdz+zip
```

If GitHub Pages does not serve USDZ files with that MIME type, use another static host that allows explicit response headers.

## Asset Policy

The initial catalog includes only non-superseded portable assets under the 50 MB soft cap:

- `usdz-mobile-globe-detail-fixed`
- `usdz-mobile-globe-detail-iss-hi`
- `usdz-mobile-globe-detail-awe-disp-light`
- `usdz-mobile-globe-detail-awe-disp-medium`
- `usdz-mobile-globe-detail-awe-disp-high`

Keep each publishable asset as a paired optimized GLB and USDZ:

```text
assets/models/<asset-id>/
  <asset-id>.opt.glb
  <asset-id>-8k.usdz
```

Update `assets/models/catalog.json` whenever assets are added, removed, renamed, or replaced. Each catalog entry should include `id`, `name`, `product`, `description`, `glb`, `usdz`, `glbSize`, and `usdzSize`; `tags` and `initialZoom` are optional. `initialZoom` defaults to `1`; use `2` to start a model at 2x zoom.

Model paths in `glb` and `usdz` are resolved relative to `assets/models/catalog.json`, so colocated assets should use paths such as `usdz-mobile-globe-detail-fixed/usdz-mobile-globe-detail-fixed.opt.glb`. Absolute `https://...` URLs are also supported when a future deployment moves binaries to a CDN or object-storage host.

Do not add superseded provenance files or oversized workflow-test USDZ files to this deployable catalog.

## Browser and AR Behavior

- Desktop and Android browsers render the GLB from `src`.
- iPhone and iPad use the paired USDZ from `ios-src` when launching Apple Quick Look.
- Android AR uses WebXR or Scene Viewer depending on browser and device support.
- Inline USDZ rendering is not expected; USDZ is an Apple Quick Look handoff format in this site.
- The page sets `<model-viewer>`'s glTF cache lower on mobile Apple devices so model switching does not retain several heavy GLB files in Safari memory.
- The viewer captures the current GLB frame before a model switch and uses that image as the temporary poster while the next GLB is fetched and prepared. A lightweight SVG poster is used only for first load and capture fallback.

## License

This repository uses a dual license:

- Website source code, scripts, and documentation: MIT License.
- GLB/USDZ model assets, catalog metadata, visual descriptions, and other non-code scientific visualization content: Creative Commons Attribution 4.0 International License (CC BY 4.0).

See `LICENSE.md` for details.
