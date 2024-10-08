#!/bin/bash

f="x^5 + 28.3001*x^4 + 308.576*x^3 + 1614.77*x^2 + 4044.8*x + 3880.73"
df="5*x^4 + 113.2*x^3 + 925.728*x^2 + 3229.54*x + 4044.8"

python3 src/main.py "bisect" "$f" "-9" "-8"
python3 src/main.py "newton" "$f" "$df" "-7.5"
python3 src/main.py "secant" "$f" "-5.5" "-5"
python3 src/main.py "false_position" "$f" "-4" "-3"
python3 src/main.py "horner" "$f" "-2"

