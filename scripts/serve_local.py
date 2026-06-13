#!/usr/bin/env python3
"""Serve the static viewer with GLB/USDZ MIME types for device testing."""

from __future__ import annotations

import argparse
import mimetypes
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1", help="Bind host, for example 0.0.0.0 for LAN testing.")
    parser.add_argument("--port", default=8765, type=int, help="Bind port.")
    parser.add_argument("--directory", default=Path(__file__).resolve().parents[1], type=Path, help="Static site root.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    mimetypes.add_type("model/gltf-binary", ".glb")
    mimetypes.add_type("model/vnd.usdz+zip", ".usdz")

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *handler_args, **handler_kwargs):
            super().__init__(*handler_args, directory=str(args.directory), **handler_kwargs)

    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Serving {args.directory} at http://{args.host}:{args.port}/")
    print("MIME mappings: .glb -> model/gltf-binary, .usdz -> model/vnd.usdz+zip")
    server.serve_forever()


if __name__ == "__main__":
    main()
