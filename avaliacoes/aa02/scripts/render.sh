#!/bin/bash

STUDENT=$1
A=$2
b=$3
C=$4
d=$5

DATE=$(date '+%d/%m/%Y')
GAUSSIAN_ELIMINATION_PARTIAL=$(python src/main.py gaussian_elimination_partial "$A" "$b")
GAUSSIAN_ELIMINATION_TOTAL=$(python src/main.py gaussian_elimination_total "$A" "$b")
JACOBI=$(python src/main.py jacobi "$C" "$d")
GAUSS_SEIDEL=$(python src/main.py gauss_seidel "$C" "$d")

export STUDENT
export DATE
export GAUSSIAN_ELIMINATION_PARTIAL
export GAUSSIAN_ELIMINATION_TOTAL
export JACOBI
export GAUSS_SEIDEL

envsubst '$STUDENT:$DATE:$GAUSSIAN_ELIMINATION_PARTIAL:$GAUSSIAN_ELIMINATION_TOTAL:$JACOBI:$GAUSS_SEIDEL' \
    < assets/template.tex
