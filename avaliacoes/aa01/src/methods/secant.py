from display import *

def secant(f, x0, x1, tolerance):
    table = Table()

    table.add_column("k")
    table.add_column("x_k")
    table.add_column("f(x_k)")
    table.add_column("ER_k")

    k = 0

    previous_xk = x0
    current_xk = x1

    table.add_row([
        str(k),
        scientific(previous_xk),
        scientific(f(previous_xk)),
        "-"
    ])

    while True:
        k += 1
        ek = abs(current_xk - previous_xk) / abs(current_xk)

        table.add_row([
            str(k),
            scientific(current_xk),
            scientific(f(current_xk)),
            scientific(ek)
        ])

        if ek < tolerance:
            break

        alpha = (f(current_xk) - f(previous_xk)) / (current_xk - previous_xk)

        previous_xk = current_xk
        current_xk = current_xk - f(current_xk) / alpha

    print(header("Método da secante", "Determinação da raíz $z_3$"))

    print(table)
    print(f"$$\\text{{Raíz }} z_3 = {scientific(current_xk)}$$\n")
    print("\\newpage \n")
