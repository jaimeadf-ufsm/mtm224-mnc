import math
from display import *

def false_position(f, a, b, tolerance):
    if f(a) * f(b) > 0:
        raise ValueError("f(a) and f(b) must have different signs")
    
    table = Table()
    table.add_column("k")
    table.add_column("a_k")
    table.add_column("x_k")
    table.add_column("b_k")
    table.add_column("f(x_k)")
    table.add_column("ER_k")

    k = 0

    ak = a
    bk = b

    previous_xk = None
    current_xk = ak - ((bk - ak) / (f(bk) - f(ak))) * f(ak)

    ek = math.inf

    table.add_row([
        str(k),
        scientific(ak),
        scientific(current_xk),
        scientific(bk),
        scientific(f(current_xk)),
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
        current_xk = ak - ((bk - ak) / (f(bk) - f(ak))) * f(ak)

        ek = abs(current_xk - previous_xk) / abs(current_xk)

        table.add_row([
            str(k),
            scientific(ak),
            scientific(current_xk),
            scientific(bk),
            scientific(f(current_xk)),
            scientific(ek)
        ])

    print(header("Método da falsa posição", "Determinação da raíz $z_4$"))

    print(table)
    print(f"$$\\text{{Raíz }} z_4 = {scientific(current_xk)}$$\n")
    print("\\newpage \n")
