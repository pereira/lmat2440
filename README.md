# LMAT2440 - Number Theory @UCLouvain

The following files are provided in support for the lectures discussing primality test algorihtms and factorization methods. 

They offer a playground for testing some of the algorithms discussed in the class. 
Documentation is largely missing, but the algorithms closely follow their description from the slides.

Each Python file can be executed by running `python3 filename.py`. 
The files are organised as follows.  

## Modular arithmetic

- `time_modular_ops.py` measures the time that is needed to perform basic modular arithmetic operations with integers of different lengths: multiplication, Legendre symbol evaluation, modular exponentiation.

## Primality

- `prime_division.py` tests whether the integers in `mixed_list.json` are primes, by performing trial division until reaching the square root of the tested integer. 
- `miller-rabin.py` applies the Miller-Rabin primality test to the integers listed in `mixed_list.json`.
- `miller-rabin-count.py` counts the number of bases that are tested when applying the Miller-Rabin test to randomly selected integers. 

## Factoring

- `fermat.py` applies the Fermat factoring method to the composite numbers in `composite_list.py`
- `pollard-pm1.py` applies Pollard's p-1 factoring method to the composite numbers in `composite_list.py`
- `pollard-rho.py` applies Pollard's rho factoring method to the composite numbers in `composite_list.py`

## Utils

- `make_int_list.py` generates lists of integers of various lengths that are used in some algorithms. In particular, it produces the files `composite_list.json`, `mixed_list.json` and `prime_list.json`. 
