import json
from gmpy2 import is_prime, mpz
from random import getrandbits

# list of lengths of integers that we want to obtain
# Lengths must all be even
n_list = list(range(8, 81, 4))


def mpz_to_int(x):
    if isinstance(x, mpz):
        return int(x)
    raise TypeError


def get_rand(bit_length):
    return mpz(getrandbits(bit_length) | 1 << (bit_length - 1))


def get_odd_rand(bit_length):
    return mpz(getrandbits(bit_length) | 1 << (bit_length - 1) | 1)


def get_prime(bit_length):
    p = 1
    while not is_prime(p):
        p = get_odd_rand(bit_length)
    return p


def get_prime_list():
    return [get_prime(n) for n in n_list]


def get_composite(bit_length):
    assert bit_length % 2 == 0
    pq = 1
    while pq.bit_length() != bit_length:
        while pq.bit_length() != bit_length:
            p = get_odd_rand(bit_length // 2)
            q = get_odd_rand(bit_length // 2)
            pq = p * q
        if not is_prime(p) or not is_prime(q):
            pq = 1
    return pq


def get_composite_list():
    return [get_composite(n) for n in n_list]


def get_mixed_list():
    mixed_list = []
    for i, n in enumerate(n_list):
        if i % 2 == 0:
            mixed_list.append(get_prime(n))
        else:
            mixed_list.append(get_composite(n))
    return mixed_list


prime_list = get_prime_list()
composite_list = get_composite_list()
mixed_list = get_mixed_list()

with open("prime_list.json", 'w') as file:
    json.dump(prime_list, file, default=mpz_to_int)
with open("composite_list.json", 'w') as file:
    json.dump(composite_list, file, default=mpz_to_int)
with open("mixed_list.json", 'w') as file:
    json.dump(mixed_list, file, default=mpz_to_int)
