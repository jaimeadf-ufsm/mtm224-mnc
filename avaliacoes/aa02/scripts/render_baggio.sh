#!/bin/bash

A="\
95 98 28 69 8 -69 -37; \
82 -41 -56 -79 25 -66 -6; \
-24 81 -60 -23 -38 70 -43; \
49 30 -8 6 0 -81 -91; \
73 -55 -80 70 -81 -68 77; \
41 -8 -39 92 79 -18 -54; \
58 -13 50 33 32 -52 62 \
"

b="\
63; \
6; \
9; \
58; \
-78; \
-79; \
-77 \
"

C="\
-577 -100 20 10 1 56 219; \
-56 -978 105 301 33 -13 -1; \
-106 -277 632 -16 23 -8 -60; \
-95 267 -30 799 4 19 54; \
-51 -172 156 -19 568 31 -7; \
0 10 158 -178 -76 526 -28; \
47 4 -251 -37 14 132 -611 \
"

d="\
-24; \
-45; \
-60; \
100; \
90; \
-62; \
-28 \
"

./scripts/render.sh "Gabriel Souza Baggio" "$A" "$b" "$C" "$d"
