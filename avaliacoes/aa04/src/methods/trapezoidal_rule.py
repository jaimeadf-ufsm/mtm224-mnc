import numpy as np

def trapezoid_rule(f, a, b, tolerance):
    iterations = []

    k = 0

    Ak = 0
    previous_Ak = 0

    ek = np.inf

    h = b - a

    while ek >= tolerance:
        n = 2 ** k
        h = (b - a) / n

        alpha = 0

        for i in range(1, n):
            alpha += f(a + i * h)

        Ak = h / 2 * (f(a) + f(b) + 2 * alpha)
        ek = np.abs(Ak - previous_Ak) / np.abs(Ak)

        previous_Ak = Ak

        iterations.append({
            'ak': Ak,
            'ek': ek
        })

        k += 1
    
    return {
        'answer': Ak,
        'iterations': iterations
    }