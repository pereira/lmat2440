from random import randrange, getrandbits
from gmpy2 import mpz

# define length of prime to be found
bit_length = 10


def get_odd_rand(bit_length):
    return mpz(getrandbits(bit_length) | 1 << (bit_length - 1) | 1)


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
            return i + 1
    return -1


print("Counting attempts when running the Miller-Rabin algorithm on random odd integers.")

for _ in range(20):
    n = get_odd_rand(bit_length)
    attempts = miller_rabin(n)
    if attempts == -1:
        print(f"{n} is prime")
    elif attempts == 1:
        print(f"{n} is composite -- 1 attempt")
    else:
        print(f"{n} is composite: it took {attempts} attempts")
