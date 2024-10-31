import numpy as np

from display import *

def gauss_seidel(C, d, tolerance):
    n = len(d)

    x_table = Table()
    x_table.add_column("k")
    
    for i in range(n):
        x_table.add_column(f"x_{{{i + 1},k}}")

    e_table = Table()
    e_table.add_column("k")
    
    for i in range(n):
        e_table.add_column(f"ER_{{{i + 1},k}}")

    k = 0

    xk = np.zeros(n)
    ek = np.full(n, np.inf)
    
    x_table.add_row([str(k)] + list(map(format_number, xk)))
    e_table.add_row([str(k)] + list("-" for _ in range(n)))

    while np.max(ek) >= tolerance:
        k += 1
        previous_xk = xk.copy()
        
        for i in range(0, n):
            theta = 0
            alpha = 0

            for j in range(0, i):
                theta -= C[i, j] * xk[j]

            for j in range(i + 1, n):
                alpha -= C[i, j] * previous_xk[j]
            
            xk[i] = (theta + alpha + d[i]) / C[i, i]

        ek = np.abs(xk - previous_xk) / np.abs(xk)

        x_table.add_row([str(k)] + list(map(format_number, xk)))
        e_table.add_row([str(k)] + list(map(format_number, ek)))

    section = Section()
    section.add_title("MÉTODO DE GAUSS SEIDEL")

    section.add_statement("$$")
    section.add_statement(f"C = {format_matrix(C)}")
    section.add_statement("\\;\\;\\;\\;")
    section.add_statement(f"\\mathbf{{d}} = {format_matrix(d)}")
    section.add_statement("$$")

    section.add_table(x_table)
    section.add_table(e_table)
    
    return section