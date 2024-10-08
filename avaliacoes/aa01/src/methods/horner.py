import math
from display import *

def horner(coeffs, x_0, tolerance):
    coeffs = coeffs[::-1]

    b_table = Table("Coeficientes $b_i$ do Polinômio $f(x)$")
    b_table.add_column("k")

    for i in range(len(coeffs) - 1, -1, -1):
        b_table.add_column(f"b_{{{i},k}}")
    
    c_table = Table("Coeficientes $c_i$ do Polinômio $f'(x)$")
    c_table.add_column("k")

    for i in range(len(coeffs) - 1, 0, -1):
        c_table.add_column(f"c_{{{i},k}}")

    estimates_table = Table("Estimativas")
    estimates_table.add_column("k")
    estimates_table.add_column("x_k")
    estimates_table.add_column("f(x_k)")
    estimates_table.add_column("f'(x_k)")
    estimates_table.add_column("ER_k")
    
    k = 0

    previous_xk = None
    current_xk = x_0

    ek = math.inf

    while ek >= tolerance:
        bk = [0] * len(coeffs)
        ck = [0] * len(coeffs)

        bk[-1] = coeffs[-1]
        ck[-1] = coeffs[-1]

        for i in range(len(coeffs) - 2, -1, -1):
            bk[i] = coeffs[i] + bk[i + 1] * current_xk
        
        for i in range(len(coeffs) - 2, -1, -1):
            ck[i] = bk[i] + ck[i + 1] * current_xk

        estimates_table.add_row([
            str(k),
            scientific(current_xk),
            scientific(bk[0]),
            scientific(ck[1]),
            "-" if ek == math.inf else scientific(ek)
        ])

        b_table.add_row([str(k)] + list(map(scientific, reversed(bk))))
        c_table.add_row([str(k)] + list(map(scientific, reversed(ck[1:]))))

        k += 1
        
        previous_xk = current_xk
        current_xk = current_xk - bk[0] / ck[1]

        ek = abs(current_xk - previous_xk) / abs(current_xk)

    estimates_table.add_row([
        str(k),
        scientific(current_xk),
        "-",
        "-",
        scientific(ek)
    ])
    
    print(header("Método de Horner", "Determinação da raíz $z_5$"))

    print(b_table)
    print(c_table)
    print(estimates_table)
    print(f"$$\\text{{Raíz }} z_5 = {scientific(current_xk)}$$\n")
    print("\\newpage \n")
