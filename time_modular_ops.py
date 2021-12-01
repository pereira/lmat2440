from gmpy2 import next_prime, legendre, mpz
from random import getrandbits
import time

n_list = [1024, 2048, 4096, 8192]


def print_table(result):
    table_format = " {:>24}"
    table_headers = ["Bit length"]
    for n in n_list:
        table_format += " {:>8}"
        table_headers.append(str(n))

    print(table_format.format(*table_headers))
    for row in result:
        print(table_format.format(*row))


def get_rand(bit_length):
    return mpz(getrandbits(bit_length) | 1 << (bit_length - 1))


def get_rand_array(bit_length, len_array):
    """:returns an array of len_array integers of len_int bits
    """
    return [mpz(getrandbits(bit_length) | 1 << (bit_length - 1)) for _ in range(len_array)]


def get_prime_list():
    """:returns an array of primes of lengths specified in n_list
    """
    print("Getting list of primes...")
    prime_list = [next_prime(get_rand(n)) for n in n_list]
    print("Done.")
    return prime_list


def time_multiply():
    """:performs op_number modular multiplications of random integers of length in n_list
    :returns an array with the time needed for each integer length"""
    op_number = 1000
    result = ["Multiplication (" + str(op_number) + ")"]
    for n in n_list:
        a_array = get_rand_array(n, op_number)
        b_array = get_rand_array(n, op_number)
        c_array = get_rand_array(n, op_number)
        tic = time.perf_counter()
        _ = [a * b % c for a, b, c in zip(a_array, b_array, c_array)]
        toc = time.perf_counter()
        result.append(f"{toc - tic:0.3}")
    return result


def time_legendre():
    """:performs op_number legendre symbol evaluation for random integers of length in n_list
        modulo a prime of the same length
    :returns an array with the time needed for each integer length"""
    op_number = 1000
    result = ["Legendre (" + str(op_number) + ")"]
    for n, p in zip(n_list, prime_list):
        b_array = get_rand_array(n, op_number)
        tic = time.perf_counter()
        _ = [legendre(b, p) for b in b_array]
        toc = time.perf_counter()
        result.append(f"{toc - tic:0.3}")
    return result


def time_pow():
    """:performs op_number modular exponentiations on random integers of length in n_list
        modulo a prime of the same length
    :returns an array with the time needed for each integer length"""
    op_number = 1000
    result = ["Exponentiation (" + str(op_number) + ")"]
    for n, p in zip(n_list, prime_list):
        a_array = get_rand_array(n, op_number)
        b_array = get_rand_array(n, op_number)
        tic = time.perf_counter()
        _ = [pow(a, b, p) for a, b in zip(a_array, b_array)]
        toc = time.perf_counter()
        result.append(f"{toc - tic:0.3}")
    return result


prime_list = get_prime_list()

result_array = list()
result_array.append(time_multiply())
result_array.append(time_legendre())
result_array.append(time_pow())

print_table(result_array)
print("Times are in seconds.")
