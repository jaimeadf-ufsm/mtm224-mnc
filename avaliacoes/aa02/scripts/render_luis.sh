#!/bin/bash

A="\
-46 15 -88 16 -66 -14 74; \
-48 43 -100 21 48 -60 -86; \
-60 77 -34 -32 17 8 -69; \
72 -50 43 -92 10 24 -33; \
76 -11 -73 31 -46 66 90; \
52 43 14 22 -99 -12 12; \
-30 -57 -23 46 -18 4 70 \
"

b="\
20; \
64; \
-35; \
87; \
9; \
-58; \
-39 \
"

C="\
-818 192 -11 -9 -149 -24 42; \
3 388 25 -17 -60 -84 186; \
23 -102 594 5 14 -54 -198; \
281 -89 -77 566 35 7 -16; \
-9 -16 40 38 -867 128 -249; \
157 -32 19 -240 40 994 10; \
-204 -70 11 31 -89 4 583 \
"

d="\
-17; \
-49; \
-54; \
-81; \
83; \
-79; \
-100 \
"

./scripts/render.sh "Luís Gustavo Werle Tozevich" "$A" "$b" "$C" "$d"