import io

import numpy as np
import matplotlib.pyplot as plt

from display import *

COLORS=["blue", "red", "orange", "green"]

def divided_differences(project, points, z):
    n = points.shape[0]

    points = points[np.argsort(np.abs(np.asarray(points[:,0]).flatten() - z))]

    x = np.asarray(points[:,0]).flatten()
    y = np.asarray(points[:,1]).flatten()

    dd = np.zeros((n, n))
    dd[:, 0] = y

    er = [np.inf]
    p_z = [y[0]]

    best_k = 2

    def pk(k, alpha):
        r = dd[0, 0]

        for i in range(1, k + 1):
            m = dd[0, i]

            for j in range(0, i):
                m *= (alpha - x[j])
            
            r += m
        
        return r

    for k in range(1, n):
        for i in range(n - k):
            dd[i, k] = (dd[i + 1, k - 1] - dd[i, k - 1]) / (x[k + i] - x[i])

    for k in range(1, n):
        p_z.append(pk(k, z))
        er.append(np.abs(p_z[-1] - p_z[-2]) / np.abs(p_z[-1]))
    
    while best_k < n - 1 and er[best_k + 1] < er[best_k]:
        best_k += 1

    dd_table = Table(
        f"Tabela de diferenças divididas $|$ $z = {format_number(z)}$"
    )
    dd_table.add_column("x")
    dd_table.add_column("y")
    
    for k in range(1, n):
        dd_table.add_column(f"DD{k}")

    estimates_table = Table("Tabela de estimativas $|$ $f(z)$")
    estimates_table.add_column("k")
    estimates_table.add_column("P_k(z)")
    estimates_table.add_column("ER_k")

    for k in range(n):
        row = [format_number(x[k])]
        row += [format_number(dd[k, j]) for j in range(0, n - k)]
        row += ["-"] * k
        
        dd_table.add_row(row)

    estimates_table.add_row(["0", format_number(p_z[0]), "-"])
    
    for k in range(1, n):
        estimates_table.add_row([
            str(k),
            format_number(p_z[k]), format_number(er[k])]
        )
    
    project.add_element(dd_table)
    project.add_element(estimates_table)

    project.add_element(
        f"APROXIMAÇÃO MAIS CONFIÁVEL: $k = {best_k}$, $P_k(z) = {format_number(p_z[best_k])}$\n"
    )

    project.add_element("\\begin{figure}[H]")
    project.add_element("\\centering")
    project.add_element("\\caption*{Gráficos}")

    for i in range(1, n // 2):
        k = i * 2

        fig, ax = plt.subplots()

        ax.plot(x, y, "ko")
        x_range = np.linspace(0, 2, 1000)
        y_range = pk(k, x_range)

        ax.set_xlim(0, 2)
        ax.set_ylim(-1, 8)

        ax.set_xlabel("$x$")
        ax.set_ylabel("$y$")

        ax.plot(
            x_range,
            y_range,
            linestyle="solid",
            color=COLORS[(i - 1) % len(COLORS)],
            label=f"$y = P_{k}(x)$"
        )
        ax.legend()

        buffer = io.BytesIO()
        fig.savefig(buffer, format="png", dpi=300, bbox_inches="tight")

        filename = f"P{k}.png"

        project.add_element("\\begin{subfigure}{0.49\\textwidth}")
        project.add_element("\\centering")
        project.add_element("\\includegraphics[width=\\textwidth]")
        project.add_element(f"{{{filename}}}")
        project.add_element("\\end{subfigure}")

        project.add_file(filename, buffer.getvalue())
    
    project.add_element("\\end{figure}")
