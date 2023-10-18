from time import time


def fast_pow_mod(a: int, n: int, m: int) -> int:
    """
    :param a: number
    :param n: degree
    :param m: modulo
    :return: (a**n) % m
    """
    c = 1
    while n > 1:
        if n % 2 == 0:
            a = (a ** 2) % m
            n //= 2
        else:
            c = (c * a) % m
            n -= 1
    return c * a % m


def fast_pow(a: int, n: int) -> int:
    """
    :param a: number
    :param n: degree
    :return: a**n
    """
    c = 1
    while n > 1:
        if n % 2 == 0:
            a *= a
            n //= 2
        else:
            c *= a
            n -= 1
    return c * a


if __name__ == "__main__":
    print("pow mod")    
    t = time()
    print((11 ** 2878063) % 3472094802933740923740923742322323237)
    print(time() - t)
    print()
    
    print("fast pow mod")
    t = time()
    print(fast_pow_mod(11, 2878063, 3472094802933740923740923742322323237))
    print(time() - t)
    print()
    
    print("pow")
    t = time()
    print(11 ** 2878063)
    print(time() - t)
    print()
    
    print("fast pow")
    t = time()
    print(fast_pow(11, 2878063))
    print(time() - t)
    print()


