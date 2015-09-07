from random import randint
from math import floor, log

__author__ = 'ZK'


def compute_power(base, power, moduler):
    result = 1
    power_binary = bin(power)[2:]
    length = len(power_binary)

    for i in range(2, length):
        result = result ** 2 % moduler
        if power_binary[i] == '1':
            result = result * base % moduler

    return result


def miller_rabin_witness(a, p):
    if p == 1:
        return False

    if p == 2:
        return True

    n = p - 1
    t = int(floor(log(n, 2)))
    u = 1
    while t > 0:
        u = n / 2 ** t
        if n % 2 ** t == 0 and u % 2 == 1:
            break
        t = t - 1

    b1 = b2 = compute_power(a, u, p)
    for i in range(1, t + 1):
        b2 = b1 ** 2 % p
    if b2 == 1 and b1 != 1 and b1 != (p - 1):
        return False
    b1 = b2
    if b1 != 1:
        return False

    return True


def prime_test_miller_rabin(p, k):
    while k > 0:
        a = randint(1, p - 1)

        if not miller_rabin_witness(a, p):
            return False
        k = k - 1

    return True
