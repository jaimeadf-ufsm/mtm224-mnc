import numpy as np
from display import *

def gaussian_elimination_partial_pivoting(A, b):
    n = len(b)
    M = np.column_stack((A, b))

    matrix_block = MatrixBlock()
    matrix_block.add_matrix(M, "A_0")

    for i in range(n - 1):
        max_row = np.argmax(np.abs(M[i:, i])) + i
        M[[i, max_row]] = M[[max_row, i]]

        for j in range(i + 1, n):
            M[j] -= M[i] * M[j, i] / M[i, i]

        matrix_block.add_matrix(M, f"A_{i + 1}")

    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        residual = np.sum(np.multiply(M[i, i:n], x[i:n]))
        x[i] = (M[i, n] - residual) / M[i, i]

    section = Section()
    section.add_title("ELIMINAÇÃO GAUSSIANA: PIVOTAMENTO PARCIAL")
    section.add_matrix_block(matrix_block)

    section.add_subtitle("SOLUÇÃO $|$ RETROSUBSTITUIÇÃO")

    section.add_statement("$$")
    section.add_statement('\\;\\;\\;\\;'.join(
        f'x_{i + 1} = {format_number(x[i])}' for i in range(n - 1, -1, -1)
    ))
    section.add_statement("$$")

    return section




    

