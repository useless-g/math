def gcd(a, b):
    while a * b:
        if a >= b:
            a %= b
        else:
            b %= a
    return a + b


def lcm(a, b):
    return abs(a * b) / gcd(a, b)


a, b = map(int, input().split())
c = a
d = b
while a * b:
    if a >= b:
        a %= b
    else:
        b %= a
gcdiv = a + b
print((abs(d * c) // gcdiv))
