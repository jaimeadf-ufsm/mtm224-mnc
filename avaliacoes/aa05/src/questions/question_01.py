import io
import numpy as np
import matplotlib.pyplot as plt

from display import *

from methods.linear_fitting import linear_fitting
from methods.polynomial_fitting import polynomial_fitting

def add_steps(project, table, polynomial_results):
    table.add_row(TableCell("\\textbf{TABELA DE DADOS}", 8, "l"))
    table.add_mid_rule()

    table.add_row(
        "$k$",
        "$x_k$",
        "$y_k$",
        "$x_k^2$",
        "$x_k^3$",
        "$x_k^4$",
        "$x_ky_k$",
        "$x_k^2y_k$"
    )

    table.add_mid_rule()

    for k, step in enumerate(polynomial_results["steps"]):
        table.add_row(
            f"${k}$",
            f"${format_number(step['x^i'][1])}$",
            f"${format_number(step['yx^i'][0])}$",
            f"${format_number(step['x^i'][2])}$",
            f"${format_number(step['x^i'][3])}$",
            f"${format_number(step['x^i'][4])}$",
            f"${format_number(step['yx^i'][1])}$",
            f"${format_number(step['yx^i'][2])}$"
        )

    table.add_mid_rule()

    table.add_row(
        "$\\sum$",
        f"${format_number(polynomial_results['sums']['x^i'][1])}$",
        f"${format_number(polynomial_results['sums']['yx^i'][0])}$",
        f"${format_number(polynomial_results['sums']['x^i'][2])}$",
        f"${format_number(polynomial_results['sums']['x^i'][3])}$",
        f"${format_number(polynomial_results['sums']['x^i'][4])}$",
        f"${format_number(polynomial_results['sums']['yx^i'][1])}$",
        f"${format_number(polynomial_results['sums']['yx^i'][2])}$"
    )

def add_linear_answer(project, table, linear_results):
    latex = "$"
    latex += " \\quad ".join(
        [
            f"a_{i} = {format_number(linear_results['coefficients'][i])}"
            for i in range(len(linear_results["coefficients"]))
        ]
    )
    latex += "$"

    table.add_mid_rule()
    table.add_row(TableCell("\\textbf{AJUSTE LINEAR}", 8, "l"))
    table.add_mid_rule()
    table.add_row(TableCell(latex, 8, "l"))

def add_polynomial_answer(project, table, polynomial_results):
    A, b = polynomial_results["system"]

    coefficients_latex = "$"
    coefficients_latex += " \\quad ".join(
        [
            f"a_{i} = {format_number(polynomial_results['coefficients'][i])}"
            for i in range(len(polynomial_results["coefficients"]))
        ]
    )

    coefficients_latex += "$"

    table.add_mid_rule()
    table.add_row(TableCell("\\textbf{AJUSTE QUADRÁTICO}", 8, "l"))
    table.add_mid_rule()
    table.add_row(TableCell("SISTEMA LINEAR", 8, "l"))
    
    for i in range(len(b)):
        equation_latex = "$"
        equation_latex += " + ".join([
            f"{format_number(A[i, j])}a_{j}" for j in range(len(b))
        ])
        equation_latex += f" = {format_number(b[i])}$"
        
        table.add_row(TableCell(equation_latex, 5, "r"))
        
    table.add_mid_rule()
    table.add_row(TableCell("SOLUÇÃO", 8, "l"))
    table.add_row(TableCell(coefficients_latex, 8, "l"))

def add_plots(project, table, x, y, linear_results, polynomial_results):
    filename = "q01_f.png"

    fig, ax = plt.subplots()

    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.plot(x, y, "o", color="tab:orange")

    ax.set_xlim(0, 25)

    x_range = np.linspace(0, 25, 1000)

    linear_y_range = linear_results["function"](x_range)
    polynomial_y_range = polynomial_results["function"](x_range)

    ax.plot(x_range, linear_y_range, linestyle="solid", color="b", label="$y = a_0 + a_1x$")
    ax.plot(x_range, polynomial_y_range, linestyle="solid", color="k", label="$y = a_0 + a_1x + a_2x^2$")

    ax.legend()

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", dpi=300, bbox_inches="tight")

    project.add_file(filename, buffer.getvalue())

    table.add_mid_rule()
    table.add_row(TableCell("\\textbf{GRÁFICO}", 8, "l"))
    table.add_mid_rule()

    table.add_row(TableCell(f"\\includegraphics[width=0.5\\textwidth]{{{filename}}}", 8, "c"))


def question_01(project, values):
    points = np.matrix(values["points"])

    x = np.asarray(points[:, 0]).flatten()
    y = np.asarray(points[:, 1]).flatten()

    linear_results = linear_fitting(x, y)
    polynomial_results = polynomial_fitting(x, y, 2)
    
    table = Table()
    table.add_top_rule()

    add_steps(project, table, polynomial_results)
    add_linear_answer(project, table, linear_results)
    add_polynomial_answer(project, table, polynomial_results)
    add_plots(project, table, x, y, linear_results, polynomial_results)

    table.add_bottom_rule()

    project.add_element("\\noindent \\textbf{QUESTÃO 01} \\\\")
    project.add_element(table)

    project.add_element("\\newpage")





