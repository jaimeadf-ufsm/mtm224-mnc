#!/bin/bash

A="\
37 19 -78 -68 -31 -91 -83; \
-68 48 76 -36 80 -18 43; \
-41 -89 -84 -92 -69 -1 -86; \
-58 47 -43 54 64 0 -74; \
-12 8 13 -39 25 -62 -67; \
41 -47 78 -19 -14 73 -24; \
-47 54 -87 -34 -48 10 -67 \
"

b="\
-69; \
8; \
-45; \
-62; \
-94; \
-40; \
63 \
"

C="\
525 10 113 -280 -61 -28 -1; \
73 472 19 -164 -37 155 6; \
37 -10 -407 -62 -10 88 -168; \
69 160 10 -605 -166 29 3; \
35 126 205 -5 -607 -13 -51; \
108 -275 -30 -11 -8 917 62; \
142 17 -3 234 -49 26 -808 \
"

d="\
-41; \
2; \
19; \
89; \
28; \
91; \
27
"

./scripts/render.sh "Gabriel Stiegemeier" "$A" "$b" "$C" "$d"