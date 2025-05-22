#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

ruff format
ruff check --fix
