#!/bin/bash

CONTENT="$(< /dev/stdin)"
export CONTENT

envsubst '$CONTENT' < template.txt
