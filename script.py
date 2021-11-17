import math
import numpy as np


def exp(x):
    # return 1 + x + x**2/2 + x**3/6 ...
    return sum([x ** n / math.factorial(n) for n in range(0, 100)])


def get_primes(n_min, n_max):
    result = []
    for x in range(max(n_min, 2), n_max):
        has_factor = False
        for p in range(2, int(np.sqrt(x)) + 1):
            if x % p == 0:
                has_factor = True
                break
        if not has_factor:
            result.append(x)
    return result


exp1 = exp(complex(0, math.pi))
print(exp1)
primes = get_primes(1000000000, 1000001000)
print(primes)
print(len(primes))
print(1000 / (len(primes)))
