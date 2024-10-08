import math
from display import *

def bisect(f, a, b, tolerance):
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have different signs")
    
    table = Table()
    table.add_column("k")
    table.add_column("a_k")
    table.add_column("x_k")
    table.add_column("b_k")
    table.add_column("f(a_k)")
    table.add_column("f(x_k)")
    table.add_column("f(b_k)")
    table.add_column("ER_k")

    k = 0

    ak = a
    bk = b

    previous_xk = None
    current_xk = (a + b) / 2

    ek = math.inf

    table.add_row([
        str(k),
        scientific(ak),
        scientific(current_xk),
        scientific(bk),
        scientific(f(ak)),
        scientific(f(current_xk)),
        scientific(f(bk)),
        "-"
    ])

    while ek >= tolerance:
        k += 1

        if f(ak) * f(current_xk) > 0:
            ak = current_xk
        elif f(bk) * f(current_xk) > 0:
            bk = current_xk
        else:
            break

        previous_xk = current_xk
        current_xk = (ak + bk) / 2

        ek = abs(current_xk - previous_xk) / abs(current_xk)

        table.add_row([
            str(k),
            scientific(ak),
            scientific(current_xk),
            scientific(bk),
            scientific(f(ak)),
            scientific(f(current_xk)),
            scientific(f(bk)),
            scientific(ek)
        ])

    print(header("Método da bissecção", "Determinação da raíz $z_1$"))

    print(table)
    print(f"$$\\text{{Raíz }} z_1 = {scientific(current_xk)}$$\n")
    print("\\newpage \n")
