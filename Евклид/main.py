def gcd(a, b):
    while a * b:
        if a >= b:
            a %= b
        else:
            b %= a
    return a + b
import math
print(math.gcd(39,3))