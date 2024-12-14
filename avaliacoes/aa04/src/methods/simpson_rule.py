import numpy as np

def simpson_rule(f, a, b, tolerance):
    iterations = []

    k = 1

    Ak = 0
    previous_Ak = 0

    ek = np.inf

    while ek >= tolerance:
        n = 2 ** k
        h = (b - a) / n

        alpha = 0
        beta = 0
        
        for i in range(1, n // 2):
            alpha += f(a + 2 * i * h)

        for i in range(1, n // 2 + 1):
            beta += f(a + (2 * i - 1) * h)

        Ak = h / 3 * (f(a) + f(b) + 2 * alpha + 4 * beta)
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