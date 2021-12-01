import json
import time
from random import randrange


def test_strong_prime(n, s, t):
    a = randrange(2, n - 1)
    b = pow(a, t, n)
    if (b == 1) or (b == n - 1):
        return True
    for r in range(s):
        b = pow(b, 2, n)
        if b == 1:
            return False
        if b == n - 1:
            return True
    return False


def miller_rabin(n):
    # compute s and t
    s = 0
    t = n - 1
    while t % 2 == 0:
        s = s + 1
        t = t // 2
    # repeat strong primality test
    for i in range(50):
        if not test_strong_prime(n, s, t):
            return False
    return True


with open("mixed_list.json") as file:
    mixed_list = json.load(file)

print("Testing primality with the Miller-Rabin algorithm:")

for n in mixed_list:
    tic = time.perf_counter()
    prime = miller_rabin(n)
    toc = time.perf_counter()
    if prime:
        print(f"{n} is prime (took {toc - tic:0.2} sec.)")
    else:
        print(f"{n} is composite (took {toc - tic:0.2} sec.)")
