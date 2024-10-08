import math
from display import *

def newton(f, df, x0, tolerance):
    table = Table()
    table.add_column("k")
    table.add_column("x_k")
    table.add_column("f(x_k)")
    table.add_column("f'(x_k)")
    table.add_column("ER_k")

    k = 0

    current_xk = x0
    ek = math.inf

    table.add_row([
        str(k),
        scientific(current_xk),
        scientific(f(current_xk)),
        scientific(df(current_xk)),
        "-"
    ])

    while ek >= tolerance:
        k += 1

        previous_xk = current_xk
        current_xk = current_xk - f(current_xk) / df(current_xk)

        ek = abs(current_xk - previous_xk) / abs(current_xk)

        table.add_row([
            str(k),
            scientific(current_xk),
            scientific(f(current_xk)),
            scientific(df(current_xk)),
            scientific(ek)
        ])
    
    print(header("Método de Newton", "Determinação da raíz $z_2$"))

    print(table)
    print(f"$$\\text{{Raíz }} z_2 = {scientific(current_xk)}$$\n")
    print("\\newpage \n")
