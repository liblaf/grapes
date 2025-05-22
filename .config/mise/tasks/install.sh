#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

if [[ -f "pixi.lock" ]]; then
  pixi install
fi

if [[ -f "uv.lock" ]]; then
  uv sync
fi
