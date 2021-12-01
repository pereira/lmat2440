import json
import time
from gmpy2 import is_square, isqrt


def fermat(n):
    assert n % 2 == 1
    if is_square(n) == 1:
        return isqrt(n)
    isqrtn = isqrt(n)
    b2 = (isqrtn + 1)**2 - n
    for a in range(isqrtn + 1, (n + 9)//6 + 2):
        if is_square(b2):
            return a - isqrt(b2)
        b2 = b2 + 2*a + 1
    return -1  # We have a prime number


with open("composite_list.json") as file:
    composite_list = json.load(file)

print("Factoring with the Fermat algorithm.")
print("The test runs on a list of composites that are the product of primes of identical bit lengths.")

for n in composite_list:
    tic = time.perf_counter()
    factor = fermat(n)
    toc = time.perf_counter()
    if factor != -1:
        print(f"{factor} divides {n}. (took {toc - tic:0.2} sec.)")
    else:
        print(f"{n} is prime (took {toc - tic:0.2} sec.)")
