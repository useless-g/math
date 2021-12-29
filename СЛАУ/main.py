def Gauss(a, n, m):
    for k in range(min(n, m)):
        if a[k][k] == 0:
            for _ in range(k + 1, n):
                if a[_][k]:
                    a[_], a[k] = a[k], a[_]
                    break
            else:
                stolb = [a[l][k] for l in range(n)]
                stolb = list(map(lambda x: x if abs(round(x) - x) > 0.00001 else round(x), stolb))
                if stolb.count(0) == len(stolb):
                    for l in range(n):
                        del a[l][k]
                    m -= 1
                continue
        for i in range(n):
            if i == k:
                continue
            l = a[i][k] / a[k][k]
            for j in range(k, m + 1):
                a[i][j] -= a[k][j] * l
    for i in range(n):
        a[i] = list(map(lambda x: x if abs(round(x) - x) > 0.00001 else round(x), a[i]))
    for i in range(n):
        if m == a[i].count(0) and a[i][m]:
            print('NO')
            return ''
        elif m == a[i].count(0):
            n -= 1
    if n > m:
        print('NO')
        return ''
    elif n < m:
        print('INF')
        return ''
    else:
        print('YES')
        b = [0] * m
        for i in range(m):
            b[i] = a[i][m] / a[i][i] if a[i][i] else 0
        return list(map(lambda x: x if abs(round(x) - x) > 0.00001 else round(x), b))

print(7**2017%1000)
n, m = tuple(map(int, input().split()))
A = [[] for i in range(n)]
for i in range(n):
    A[i] = list(map(float, input().split()))
print(*Gauss(A, n, m))
