import numpy as np

def polynomial_fitting(x, y, order):
    n = len(x)

    steps = []
    sums = {
        "x^i": np.zeros(order * 2 + 1),
        "yx^i": np.zeros(order + 1)
    }

    for k in range(n):
        xi = np.array([x[k] ** i for i in range(order * 2 + 1)])
        yxi = np.array([y[k] * x[k] ** i for i in range(order + 1)])

        sums["x^i"] += xi
        sums["yx^i"] += yxi

        steps.append({
            "x^i": xi,
            "yx^i": yxi
        })

    A = np.zeros((order + 1, order + 1))
    b = np.zeros(order + 1)

    for i in range(order + 1):
        for j in range(order + 1):
            A[i, j] = sums["x^i"][i + j]

        b[i] = sums["yx^i"][i]

    coefficients = np.linalg.solve(A, b)

    return {
        "steps": steps,
        "sums": sums,
        "system": (A, b),
        "coefficients": coefficients,
        "function": lambda x: sum([coefficients[i] * x ** i for i in range(order + 1)])
    }




