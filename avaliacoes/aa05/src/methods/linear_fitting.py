import numpy as np

def linear_fitting(x, y):
    n = len(x)

    steps = []
    sums = {
        "x": 0,
        "y": 0,
        "xy": 0,
        "x^2": 0
    }

    for k in range(n):
        xk = x[k]
        yk = y[k]
        ykxk = xk * yk
        xk2 = xk ** 2

        sums["x"] += xk
        sums["y"] += yk
        sums["xy"] += ykxk
        sums["x^2"] += xk2

        steps.append({
            "x": xk,
            "y": yk,
            "xy": ykxk,
            "x^2": xk2
        })
    
    x_sum = sums["x"]
    y_sum = sums["y"]
    xy_sum = sums["xy"]
    x2_sum = sums["x^2"]

    a0 = (x2_sum * y_sum - xy_sum * x_sum) / (n * x2_sum - x_sum ** 2)
    a1 = (n * xy_sum - x_sum * y_sum) / (n * x2_sum - x_sum ** 2)

    return {
        "steps": steps,
        "sums": sums,
        "coefficients": (a0, a1),
        "function": lambda x: a0 + a1 * x
    }