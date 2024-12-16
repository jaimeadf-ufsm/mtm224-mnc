import io
from functools import partial

import matplotlib.scale
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from display import *

from methods.linear_fitting import linear_fitting
from methods.polynomial_fitting import polynomial_fitting

def add_steps(project, table, linear_results):
    table.add_row(TableCell("\\textbf{TABELA DE DADOS}", 5, "l"))
    table.add_mid_rule()

    table.add_row(
        "$k$",
        "$\\log{x_k}$",
        "$\\log{y_k}$",
        "$\\log{x_k}^2$",
        "$\\log{y_k} \\log{x_k}$"
    )

    table.add_mid_rule()

    for k, step in enumerate(linear_results["steps"]):
        table.add_row(
            f"${k + 1}$",
            f"${format_number(step['x'])}$",
            f"${format_number(step['y'])}$",
            f"${format_number(step['x^2'])}$",
            f"${format_number(step['xy'])}$"
        )
    
    table.add_mid_rule()

    table.add_row(
        "$\\sum$",
        f"${format_number(linear_results['sums']['x'])}$",
        f"${format_number(linear_results['sums']['y'])}$",
        f"${format_number(linear_results['sums']['x^2'])}$",
        f"${format_number(linear_results['sums']['xy'])}$"
    )

def add_linear_answer(project, table, linear_results):
    latex = "$"
    latex += f"a_0 = {format_number(linear_results['coefficients'][0])}"
    latex += " \\quad "
    latex += f"a_1 = {format_number(linear_results['coefficients'][1])}"
    latex += "$"

    table.add_mid_rule()
    table.add_row(TableCell("\\textbf{AJUSTE LINEAR}", 5, "l"))
    table.add_mid_rule()
    table.add_row(TableCell(latex, 5, "l"))

def add_exponential_answer(project, table, a, b):
    latex = "$"
    latex += f"a = e^{{a_0}} = {format_number(a)}"
    latex += " \\quad "
    latex += f"b = a_1 = {format_number(b)}"
    latex += "$"

    table.add_mid_rule()
    table.add_row(TableCell("\\textbf{AJUSTE POTÊNCIA}", 5, "l"))
    table.add_mid_rule()
    table.add_row(TableCell(latex, 5, "l"))


def add_plots(project, table, x, y, a, b):
    filename = "q02b_f.png"

    fig, ax = plt.subplots()

    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.plot(x, y, "o", color="tab:orange")

    ax.set_xlim(10, 45)

    ax.set_xscale("log", base=np.e)
    ax.set_yscale("log", base=np.e)

    ax.set_xticks([10, 15, 20, 30, 45])
    # ax.set_yticks([20, 30, 50, 70, 100, 150])

    # ax.xaxis.set_major_locator(matplotlib.ticker.KL())
    # ax.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(50))

    # ax.xaxis.set_major_locator(matplotlib.ticker.LogLocator(base=np.e, subs=[1.0, 1.5, 2.0]))

    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

    x_range = np.linspace(10, 45, 1000)
    y_range = a * np.power(x_range, b)

    ax.plot(x_range, y_range, linestyle="solid", color="b", label="$y = ax^b$")

    ax.legend()

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", dpi=300, bbox_inches="tight")

    project.add_file(filename, buffer.getvalue())

    table.add_mid_rule()
    table.add_row(TableCell("\\textbf{GRÁFICO}", 5, "l"))
    table.add_mid_rule()

    table.add_row(TableCell(f"\\includegraphics[width=0.5\\textwidth]{{{filename}}}", 5, "c"))

def question_02b(project, values):
    points = np.matrix(values["points"])

    x = np.asarray(points[:, 0]).flatten()
    y = np.asarray(points[:, 1]).flatten()

    log_x = np.log(x)
    log_y = np.log(y)

    linear_results = linear_fitting(log_x, log_y)

    a = np.exp(linear_results["coefficients"][0])
    b = linear_results["coefficients"][1]
    
    table = Table()
    table.add_top_rule()

    add_steps(project, table, linear_results)
    add_linear_answer(project, table, linear_results)
    add_exponential_answer(project, table, a, b)
    add_plots(project, table, x, y, a, b)

    table.add_bottom_rule()

    project.add_element("\\noindent \\textbf{QUESTÃO 02} $|$ \\textbf{AJUSTE POTÊNCIA} \\\\")
    project.add_element(table)

    project.add_element("\\newpage")




