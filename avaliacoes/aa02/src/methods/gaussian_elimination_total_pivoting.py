import numpy as np
from display import *

def gaussian_elimination_total_pivoting(A, b):
    M = np.column_stack((A, b))
    n = len(b)

    xi = np.arange(n)

    matrix_block = MatrixBlock()
    matrix_block.add_matrix(M, "A_0")

    for i in range(n - 1):
        max_index = np.argmax(np.abs(M[i:, i:n]))
        max_row, max_column = np.unravel_index(max_index, (n - i, n - i))

        max_row += i
        max_column += i

        M[[i, max_row]] = M[[max_row, i]]
        M[:, [i, max_column]] = M[:, [max_column, i]]

        xi[[i, max_column]] = xi[[max_column, i]]

        for j in range(i + 1, n):
            M[j] -= M[i] * M[j, i] / M[i, i]
        
        matrix_block.add_matrix(M, f"A_{i + 1}")

    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        residual = np.sum(np.multiply(M[i, i:n], x[i:n]))
        x[i] = (M[i, n] - residual) / M[i, i]

    section = Section()
    section.add_title("ELIMINAÇÃO GAUSSIANA: PIVOTAMENTO TOTAL")
    section.add_matrix_block(matrix_block)

    section.add_subtitle("SOLUÇÃO $|$ RETROSUBSTITUIÇÃO")

    section.add_statement("$$")
    section.add_statement('\\;\\;\\;\\;'.join(
        f'x_{xi[i] + 1} = {format_number(x[i])}' for i in range(n - 1, -1, -1)
    ))
    section.add_statement("$$")

    return section




    

