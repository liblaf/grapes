#!/bin/bash

args=()
if [[ -t 2 ]]; then args+=("--color=always"); fi # workaround for colorful output
eval "$(pixi shell-hook "${args[@]}")"
