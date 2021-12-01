import json
import time
from math import log
from gmpy2 import next_prime, gcd

# Setting bound
B = 1000000


# Building list of primes
def make_prime_list():
    prime_list = []
    power_list = []
    b = 1
    while b <= B:
        b = next_prime(b)
        prime_list.append(b)
        power_list.append(int(log(B)/log(b)))
    return prime_list, power_list


def pm1(n, prime_list, power_list):
    c = 2
    for i in range(len(prime_list)):
        for j in range(power_list[i]):
            c = pow(c, prime_list[i], n)
            out = gcd(c - 1, n)
            if out != 1 and out != n:
                return out
    return -1


print("Factoring with the Pollard p-1 algorithm.")

tic = time.perf_counter()
prime_list, power_list = make_prime_list()
toc = time.perf_counter()

print(f"Prime list generation: {toc - tic:0.2} sec.")

with open("composite_list.json") as file:
    composite_list = json.load(file)

for n in composite_list:
    tic = time.perf_counter()
    factor = pm1(n, prime_list, power_list)
    toc = time.perf_counter()
    if factor == -1:
        print(f"Failed to factor {n} (took {toc - tic:0.2} sec.)")
    else:
        print(f"{factor} divides {n} (took {toc - tic:0.2} sec.)")
