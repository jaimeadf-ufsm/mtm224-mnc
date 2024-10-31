import argparse
import numpy as np

from methods.gauss_elimination_partial_pivoting import gauss_elimination_partial_pivoting
from methods.gauss_elimination_total_pivoting import gauss_elimination_total_pivoting
from methods.jacobi import jacobi
from methods.gauss_seidel import gauss_seidel

DEFAULT_TOLERANCE = 1e-5

def run_gauss_elimination_partial_pivoting(args):
    section = gauss_elimination_partial_pivoting(
        args.A.astype(float),
        args.b.astype(float)
    )

    print(section)

def run_gauss_elimination_total_pivoting(args):
    section = gauss_elimination_total_pivoting(
        args.A.astype(float),
        args.b.astype(float)
    )

    print(section)

def run_jacobi(args):
    section = jacobi(
        args.C.astype(float),
        args.d.astype(float),
        args.tolerance
    )

    print(section)

def run_gauss_seidel(args):
    section = gauss_seidel(
        args.C.astype(float),
        args.d.astype(float),
        args.tolerance
    )

    print(section)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)

    parser_gauss_partial = subparsers.add_parser("gauss_elimination_partial")
    parser_gauss_partial.add_argument("A", type=np.matrix)
    parser_gauss_partial.add_argument("b", type=np.matrix)
    parser_gauss_partial.set_defaults(func=run_gauss_elimination_partial_pivoting)

    parser_gauss_total = subparsers.add_parser("gauss_elimination_total")
    parser_gauss_total.add_argument("A", type=np.matrix)
    parser_gauss_total.add_argument("b", type=np.matrix)
    parser_gauss_total.set_defaults(func=run_gauss_elimination_total_pivoting)

    parser_jacobi = subparsers.add_parser("jacobi")
    parser_jacobi.add_argument("C", type=np.matrix)
    parser_jacobi.add_argument("d", type=np.matrix)
    parser_jacobi.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE)
    parser_jacobi.set_defaults(func=run_jacobi)

    parser_gauss_seidel = subparsers.add_parser("gauss_seidel")
    parser_gauss_seidel.add_argument("C", type=np.matrix)
    parser_gauss_seidel.add_argument("d", type=np.matrix)
    parser_gauss_seidel.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE)
    parser_gauss_seidel.set_defaults(func=run_gauss_seidel)

    args = parser.parse_args()
    args.func(args)
