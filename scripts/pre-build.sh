#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

wget --output-document="docs/favicon.png" "https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Grapes/3D/grapes_3d.png"
wget --output-document="docs/logo.png" "https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Grapes/3D/grapes_3d.png"
