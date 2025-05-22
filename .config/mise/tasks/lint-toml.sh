#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

sort-toml .ruff.toml pyproject.toml
