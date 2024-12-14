import argparse
import yaml
import numpy as np

from display import *

from methods.trapezoidal_rule import trapezoid_rule
from methods.simpson_rule import simpson_rule
from methods.gaussian_quadrature import gaussian_quadrature_2pts, gaussian_quadrature_3pts

DEFAULT_TOLERANCE = 1e-6

def solve(project, a, b, c, tolerance):
    def g(x):
        return 2 * np.cos(2 * np.pi * x * (c[2] - c[3] * x))

    def f(x):
        return np.sin(2 * np.pi * (x * (c[0] - c[1] * x) + g(x)))
    
    def u(x):
        return f(x) * np.exp(-x)

    r = (b - a) / 4

    results = [
        trapezoid_rule(u, a, a + r, tolerance),
        simpson_rule(u, a + r, a + 2 * r, tolerance),
        gaussian_quadrature_2pts(u, a + 2 * r, a + 3 * r, tolerance),
        gaussian_quadrature_3pts(u, a + 3 * r, b, tolerance)
    ]

    table = Table()

    table.add_top_rule()
    table.add_row([
        "",
        "",
        "TRAPÉZIO",
        "",
        "SIMPSON",
        "",
        "GAUSS 2PTS",
        "",
        "GAUSS 3PTS",
    ])
    table.add_mid_rule()

    table.add_row(["$k$"] + ["$A_k$", "$ER_k$"] * len(results))

    k = 0

    while any(len(result["iterations"]) > k for result in results):
        row = [str(k)]

        for result in results:
            if k < len(result["iterations"]):
                row += [
                    f"${format_number(result['iterations'][k]['ak'])}$",
                    f"${format_number(result['iterations'][k]['ek'])}$"
                ]
            else:
                row += ["$-$", "$-$"]

        table.add_row(row)

        k += 1

    table.add_bottom_rule()

    A = sum(result["answer"] for result in results)

    project.add_element("\\noindent \\textbf{PARÂMETROS DA INTEGRAL DEFINIDA} \\\\")
    project.add_element("$$")
    project.add_element("\\begin{array}{ll}")
    project.add_element(f"\\text{{INTERVALO DE INTEGRAÇÃO}} & I = [a, b] = [{a}, {b}] \\\\")
    project.add_element(f"\\text{{COEFICIENTES DA FUNÇÃO}} & \\{{c_1, c_2, c_3, c_4\\}} = \\{{{c[0]}, {c[1]}, {c[2]}, {c[3]}\\}} \\\\")
    project.add_element("\\end{array}")
    project.add_element("$$ \\\\")

    project.add_element("\\noindent \\textbf{MÉTODOS DE INTEGRAÇÃO COMPOSTA COM MULTIRESOLUÇÃO} \\")
    project.add_element(table)

    project.add_element("\\noindent INTEGRAL NUMÉRICA")
    project.add_element("$$")
    project.add_element(f"A = {format_number(A)}")
    project.add_element("$$ \\\\")

def run(args):
    with open(args.values, "r") as values_file:
        values = yaml.safe_load(values_file)

        name = values["name"]
        date = values["date"]

        a = values["variables"]["a"]
        b = values["variables"]["b"]
        c = values["variables"]["c"]

        tolerance = values["variables"].get("tolerance", DEFAULT_TOLERANCE)
        
        project = Project()
        project.add_element(Header(
            "AA04",
            "MTM224 - Métodos Numéricos Computacionais",
            name,
            date
        ))

        solve(project, a, b, c, tolerance)

        project.save(args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("values")
    parser.add_argument("-o", "--output")
    parser.set_defaults(func=run)

    args = parser.parse_args()
    args.func(args)
