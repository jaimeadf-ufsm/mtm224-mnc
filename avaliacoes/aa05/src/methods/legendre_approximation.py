import scipy
import numpy as np

def legendre_approximation(f, n):
    steps = []

    legendre = [scipy.special.legendre(k) for k in range(n + 1)]

    for k in range(0, n + 1):
        integrand = lambda x: f(x) * legendre[k](x)
        integral = scipy.integrate.quad(integrand, -1, 1)[0]

        a = (2 * k + 1) / 2 * integral

        step = {
            "a": a,
            "EA": np.inf,
            "ER": np.inf,
            "P": lambda x, k=k: sum([
                steps[j]["a"] * legendre[j](x) for j in range(0, k + 1)
            ])
        }

        steps.append(step)

        if k > 0:
            beta = sum([2 * steps[j]["a"] ** 2 / (2 * j + 1) for j in range(0, k + 1)])

            step["EA"] = 2 * a ** 2 / (2 * k + 1)
            step["ER"] = step["EA"] / beta
    
    return {
        "steps": steps
    }