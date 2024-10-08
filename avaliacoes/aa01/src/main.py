import argparse
import sympy

from methods.bisect import bisect
from methods.newton import newton
from methods.secant import secant
from methods.false_position import false_position
from methods.horner import horner

DEFAULT_TOLERANCE = 1e-6

def create_polynomial_lambda(expr):
    return sympy.lambdify("x", expr)

def run_bisect(args):
    bisect(create_polynomial_lambda(args.f), args.a, args.b, args.tolerance)

def run_newton(args):
    newton(
        create_polynomial_lambda(args.f),
        create_polynomial_lambda(args.df),
        args.x0,
        args.tolerance
    )

def run_secant(args):
    secant(create_polynomial_lambda(args.f), args.x0, args.x1, args.tolerance)

def run_false_position(args):
    false_position(create_polynomial_lambda(args.f), args.a, args.b, args.tolerance)

def run_homer(args):
    horner(sympy.Poly(args.f).all_coeffs(), args.x0, args.tolerance)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)

    parser_bisect = subparsers.add_parser("bisect")
    parser_bisect.add_argument("f", type=sympy.sympify)
    parser_bisect.add_argument("a", type=float)
    parser_bisect.add_argument("b", type=float)
    parser_bisect.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE)
    parser_bisect.set_defaults(func=run_bisect)

    parser_newton = subparsers.add_parser("newton")
    parser_newton.add_argument("f", type=sympy.sympify)
    parser_newton.add_argument("df", type=sympy.sympify)
    parser_newton.add_argument("x0", type=float)
    parser_newton.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE)
    parser_newton.set_defaults(func=run_newton)

    parser_secant = subparsers.add_parser("secant")
    parser_secant.add_argument("f", type=sympy.sympify)
    parser_secant.add_argument("x0", type=float)
    parser_secant.add_argument("x1", type=float)
    parser_secant.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE)
    parser_secant.set_defaults(func=run_secant)

    parser_false_position = subparsers.add_parser("false_position")
    parser_false_position.add_argument("f", type=sympy.sympify)
    parser_false_position.add_argument("a", type=float)
    parser_false_position.add_argument("b", type=float)
    parser_false_position.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE)
    parser_false_position.set_defaults(func=run_false_position)

    parser_homer = subparsers.add_parser("horner")
    parser_homer.add_argument("f", type=sympy.sympify)
    parser_homer.add_argument("x0", type=float)
    parser_homer.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE)
    parser_homer.set_defaults(func=run_homer)

    args = parser.parse_args()
    args.func(args)
