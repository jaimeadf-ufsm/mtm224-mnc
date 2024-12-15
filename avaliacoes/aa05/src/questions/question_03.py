import io
import numpy as np
import matplotlib.pyplot as plt

from methods.legendre_approximation import legendre_approximation
from methods.trigonometric_approximation import trigonometric_approximation

from display import *

def add_parameters(project, table, c):
    latex = "$"
    latex += " \\quad ".join(
        [f"c_{i} = {format_number(c[i])}" for i in range(len(c))]
    )
    latex += "$"

    table.add_row(TableCell("\\textbf{PARÂMETROS DA FUNÇÃO}", 9, "l"))
    table.add_mid_rule()
    table.add_row(TableCell(latex, 9, "l"))

def add_steps(project, table, legendre_results, trigonometric_results):
    table.add_mid_rule()

    table.add_row(
        TableCell("\\textbf{POLINÔMIOS DE LEGENDRE}", 4, "l"),
        TableCell("\\textbf{POLINÔMIOS TRIGONOMÉTRICOS}", 5, "l")
    )

    table.add_mid_rule()

    table.add_row(
        "$k$",
        "$a_k$",
        "$EA_k^{(g)}$",
        "$ER_k^{(g)}$",
        TableCell("$k$", 1, "|r"),
        "$a_k$",
        "$b_k$",
        "$EA_k^{(g)}$",
        "$ER_k^{(g)}$"
    )

    table.add_mid_rule()

    for k in range(0, len(legendre_results["steps"])):
        legendre_step = legendre_results["steps"][k]

        table.add_row(
            f"${k}$",
            f"${format_number(legendre_step["a"])}$",
            f"${"-" if legendre_step["EA"] == np.inf else format_number(legendre_step["EA"])}$",
            f"${"-" if legendre_step["ER"] == np.inf else format_number(legendre_step["ER"])}$",
            TableCell(f"${k}$", 1, "|r"),
            f"${format_number(trigonometric_results['steps'][k]['a'])}$",
            f"${format_number(trigonometric_results['steps'][k]['b'])}$",
            f"${"-" if trigonometric_results['steps'][k]['EA'] == np.inf else format_number(trigonometric_results['steps'][k]['EA'])}$",
            f"${"-" if trigonometric_results['steps'][k]['ER'] == np.inf else format_number(trigonometric_results['steps'][k]['ER'])}$"
        )


def add_plots(project, f, approximation_functions, letter, color):    
    project.add_element("\\begin{figure}[H]")
    project.add_element("\\centering")

    for i in range(0, len(approximation_functions) // 2 + 1):
        k = i * 2

        g = approximation_functions[k]

        fig, ax = plt.subplots()

        x_range = np.linspace(-1, 1, 1000)

        f_y_range = f(x_range)
        g_y_range = g(x_range)

        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 2)

        ax.set_xlabel("$x$")
        ax.set_ylabel("$y$")

        ax.plot(
            x_range,
            f_y_range,
            linestyle="solid",
            color="blue",
            label="$y = f(x)$"
        )

        ax.plot(
            x_range,
            g_y_range,
            linestyle="solid",
            color=color,
            label=f"$y = {letter}_{k}(x)$"
        )
        ax.legend()

        buffer = io.BytesIO()
        fig.savefig(buffer, format="png", dpi=300, bbox_inches="tight")

        filename = f"q03_{letter}{k}.png"

        project.add_element("\\begin{subfigure}{0.32\\textwidth}")
        project.add_element("\\centering")
        project.add_element("\\includegraphics[width=\\textwidth]")
        project.add_element(f"{{{filename}}}")
        project.add_element("\\end{subfigure}")

        project.add_file(filename, buffer.getvalue())
    
    project.add_element("\\end{figure}")

def question_03(project, values):
    c = values["c"]

    def f(x):
        return np.cos(c[0] + np.sin(c[1] * x) / (x ** 2 + 1)) + np.sin(c[2] * x ** 2)
    
    order = 10

    legendre_results = legendre_approximation(f, order)
    trigonometric_results = trigonometric_approximation(f, order)

    table = Table()
    table.add_top_rule()

    add_parameters(project, table, c)
    add_steps(project, table, legendre_results, trigonometric_results)

    table.add_bottom_rule()

    project.add_element("\\noindent \\textbf{QUESTÃO 03} \\\\")
    project.add_element(table)

    project.add_element("\\noindent \\textbf{GRÁFICOS $|$ POLINÔMIOS DE LEGENDRE}")
    add_plots(
        project,
        f,
        [s["P"] for s in legendre_results["steps"]],
        "P",
        "tab:orange"
    )

    project.add_element("\\noindent \\textbf{GRÁFICOS $|$ POLINÔMIOS TRIGONOMÉTRICOS}")
    add_plots(
        project,
        f,
        [s["S"] for s in trigonometric_results["steps"]],
        "S",
        "red"
    )

    project.add_element("\\newpage")
