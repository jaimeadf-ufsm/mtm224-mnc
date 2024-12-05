import numpy as np

def gaussian_quadrature(f, a, b, tolerance, nodes, weight):
    iterations = []

    k = 0

    Ak = 0
    previous_Ak = 0

    ek = np.inf

    while ek >= tolerance:
        n = 2**k
        h = (b - a) / n

        Ak = 0

        for i in range(1, n + 1):
            a_prime = a + (i - 1) * h
            b_prime = a + i * h

            def transform(x):
                return (a_prime + b_prime + x * h) / 2

            for j in range(0, len(weight)):
                Ak += weight[j] * f(transform(nodes[j]))
        
        Ak *= h / 2

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

def gaussian_quadrature_2pts(f, a, b, tolerance):
    return gaussian_quadrature(
        f,
        a,
        b,
        tolerance,
        [-1 / np.sqrt(3), 1 / np.sqrt(3)],
        [1, 1]
    )

def gaussian_quadrature_3pts(f, a, b, tolerance):
    return gaussian_quadrature(
        f,
        a,
        b,
        tolerance,
        [-np.sqrt(3 / 5), 0, np.sqrt(3 / 5)],
        [5 / 9, 8 / 9, 5 / 9]
    )
