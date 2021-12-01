import json
import time
from random import randrange
from gmpy2 import gcd


def prho(n):
    a = randrange(1, n)
    u = randrange(1, n)
    v = u
    while True:
        u = (u*u + a) % n
        v = (v*v + a) % n
        v = (v*v + a) % n
        d = gcd(u - v, n)
        if d != 1 and d != n:
            return d
        if d == n:
            return -1


print("Factoring with the Pollard rho algorithm.")

with open("composite_list.json") as file:
    composite_list = json.load(file)

for n in composite_list:
    tic = time.perf_counter()
    factor = prho(n)
    toc = time.perf_counter()
    if factor == -1:
        print(f"Failed to factor {n} (took {toc - tic:0.2} sec.)")
    else:
        print(f"{factor} divides {n} (took {toc - tic:0.2} sec.)")
