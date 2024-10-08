#!/bin/bash

f="x**5 - 7.22984*x**4 -4.72769*x**3 + 92.1905*x**2 - 67.6756*x - 84.3088"
df="5*x**4 - 4*7.22984*x**3 - 3*4.72769*x**2 + 2*92.1905*x - 67.6756"

python3 src/main.py "bisect" "$f" "-4" "-3"
python3 src/main.py "newton" "$f" "$df" "0"
python3 src/main.py "secant" "$f" "1" "2"
python3 src/main.py "false_position" "$f" "3.5" "4.5"
python3 src/main.py "horner" "$f" "6"