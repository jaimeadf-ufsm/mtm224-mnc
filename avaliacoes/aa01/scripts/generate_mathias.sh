#!/bin/bash

f="x**5 - 2.79201*x**4 - 3.2732*x**3 + 10.7548*x**2 - 2.53959*x - 2.41684"
df="5*x**4 - 2.79201*4*x**3 - 3.2732*3*x**2 + 10.7548*2*x - 2.53959"

python3 src/main.py "bisect" "$f" "-2" "-1"
python3 src/main.py "newton" "$f" "$df" "-0.5"
python3 src/main.py "secant" "$f" "1" "0.5"
python3 src/main.py "false_position" "$f" "1" "2"
python3 src/main.py "horner" "$f" "2.5"