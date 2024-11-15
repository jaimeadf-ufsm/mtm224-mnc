#!/bin/bash

input_filename=$1
output_filename=$2

tmp=$(mktemp -d)

python src/main.py "$input_filename" -o "$tmp"
pdflatex -interaction=nonstopmode -output-directory="$tmp" "$tmp/main.tex"

mv "$tmp/main.pdf" "$output_filename"

rm -rf "$tmp"