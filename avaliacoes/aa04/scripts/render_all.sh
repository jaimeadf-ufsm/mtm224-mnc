#!/bin/bash

for script in scripts/render_*.sh; do
    if [ "$script" == "scripts/render_all.sh" ]; then
        continue
    fi

    bash $script
done