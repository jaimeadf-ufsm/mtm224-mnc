import scipy
import numpy as np

def trigonometric_approximation(f, n):
    steps = []

    for k in range(0, n + 1):
        actual_k = k

        a0 = scipy.integrate.quad(lambda x: f(x / np.pi), -np.pi, np.pi)[0] / np.pi

        a_integrand = lambda x: np.cos(actual_k * x) * f(x / np.pi)
        a = scipy.integrate.quad(a_integrand, -np.pi, np.pi)[0] / np.pi

        b_integrand = lambda x: np.sin(actual_k * x) * f(x / np.pi)
        b = scipy.integrate.quad(b_integrand, -np.pi, np.pi)[0] / np.pi

        step = {
            "a": a,
            "b": b,
            "EA": np.inf,
            "ER": np.inf,
            "S": lambda x, a0=a0, k=k: a0 / 2 + np.zeros_like(x) + sum([
                steps[j]["a"] * np.cos(j * x * np.pi) + steps[j]["b"] * np.sin(j * x * np.pi) for j in range(1, k + 1)
            ])
        }

        steps.append(step)

        if k > 0:
            beta = sum([steps[m]["a"] ** 2 + steps[m]["b"] ** 2 for m in range(1, k + 1)])

            step["EA"] = a ** 2 + b ** 2
            step["ER"] = (a ** 2 + b ** 2) / (a0 ** 2 / 4 + beta)

            # ea = scipy.integrate.quad(lambda x: (steps[-1]["S"](x) - steps[-2]["S"](x)) ** 2, -1, 1)[0]
            # er = ea / scipy.integrate.quad(lambda x: steps[-1]["S"](x) ** 2, -1, 1)[0]

            # step["EA"] = ea
            # step["ER"] = er

    return {
        "steps": steps
    }