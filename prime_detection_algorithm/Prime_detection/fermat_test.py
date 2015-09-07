__author__ = 'ZK'

'''

    Using Fermat's Theorem:
        (a^p) − 1 ≡ 1(mod p)

    As for the false positive (ie a composite number is judged
    to be a prime number) probability, studies show that with
    the integer tends to infinity, this probability tends to zero,
    in the case of base 2, 512 encountered false positive integer
    the probability is 1/10 ^ 20, and in 1024 integers, encountered
    false positive probability is 1/10 ^ 41. So if the same method to
    detect a sufficiently large number, the possibility of errors
    encountered reaches its minimum.


'''


def compute_power(base, power, moduler):
    result = 1
    power_binary = bin(power)[2:]
    length = len(power_binary)

    for i in range(2, length):
        result = result ** 2 % moduler
        if power_binary[i] == '1':
            result = result * base % moduler

    return result


def prime_fermat_test(n):
    if n == 1:
        return False

    if n == 2:
        return True

    d = compute_power(2, n - 1, n)
    if d == 1:
        return True
    else:
        return False
