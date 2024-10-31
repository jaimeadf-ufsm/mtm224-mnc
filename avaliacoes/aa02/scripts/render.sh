#!/bin/bash

STUDENT=$1
A=$2
b=$3
C=$4
d=$5

DATE=$(date '+%d/%m/%Y')
GAUSS_ELIMINATION_PARTIAL=$(python src/main.py gauss_elimination_partial "$A" "$b")
GAUSS_ELIMINATION_TOTAL=$(python src/main.py gauss_elimination_total "$A" "$b")
JACOBI=$(python src/main.py jacobi "$C" "$d")
GAUSS_SEIDEL=$(python src/main.py gauss_seidel "$C" "$d")

export STUDENT
export DATE
export GAUSS_ELIMINATION_PARTIAL
export GAUSS_ELIMINATION_TOTAL
export JACOBI
export GAUSS_SEIDEL

envsubst '$STUDENT:$DATE:$GAUSS_ELIMINATION_PARTIAL:$GAUSS_ELIMINATION_TOTAL:$JACOBI:$GAUSS_SEIDEL' \
    < assets/template.tex
