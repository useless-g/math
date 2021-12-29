s = 1
i = 0
k = 1
while s < 1.5706963267948966:
    i += 1
    k *= (2 * i - 1) / (2 * i)
    k /= 2 * i + 1
    s += k
    k *= 2 * i + 1
    print(s)
print(i)
s = input()
