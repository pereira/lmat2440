import json
import time
from math import sqrt


def primes_division(n):
    if n % 2 == 0:
        return False
    div = 3
    maxdiv = sqrt(n)
    while div <= maxdiv:
        if n % div == 0:
            return False
        div = div + 2
    return True

with open("mixed_list.json") as file:
    mixed_list = json.load(file)

print("Testing primality through trial division.")

for n in mixed_list:
    tic = time.perf_counter()
    prime = primes_division(n)
    toc = time.perf_counter()
    if prime:
        print(f"{n:25} is prime     (took {toc - tic:4.2} sec.)")
    else:
        print(f"{n:25} is composite (took {toc - tic:4.2} sec.)")
