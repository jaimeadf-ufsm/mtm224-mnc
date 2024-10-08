#!/bin/bash

f="x^5 + 32.2994*x^4 + 407.148*x^3 + 2500.89*x^2 + 7478.64*x + 8700.01"
df="5*x^4 + 129.1976*x^3 + 1221.444*x^2 + 5001.78*x + 7478.64"

python3 src/main.py "bisect" "$f" "-10" "-9"
python3 src/main.py "newton" "$f" "$df" "-8"
python3 src/main.py "secant" "$f" "-6.5" "-6"
python3 src/main.py "false_position" "$f" "-5.5" "-4.5"
python3 src/main.py "horner" "$f" "-4"
