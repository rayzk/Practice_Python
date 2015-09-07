from math import sqrt, floor

__author__ = 'ZK'


def prime_factor_test(n):
    if n == 1:
        return False
    for i in range(2, int(floor(sqrt(n)))):
        if n % i == 0:
            return False

    return True
