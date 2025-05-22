#!/bin/bash
#MISE depends_post=["lint"]
set -o errexit
set -o nounset
set -o pipefail

if [[ -f "pixi.lock" ]]; then
  pixi upgrade
fi

if [[ -f "uv.lock" ]]; then
  uv sync --upgrade
fi
