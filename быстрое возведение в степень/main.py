'''a, n, m = tuple(map(int, input('введите число, степень и модуль').split()))
b = a
c = 1
for i in range(n-1):
    b *= a
    b %= m
    print(i + 2, b)
print('check', a**n % m)
while n > 1:
    if n % 2 == 0:
        a *= a
        n //= 2
    else:
        c *= a
        n -= 1
print(c*a % m)'''
