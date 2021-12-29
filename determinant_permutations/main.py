from math import factorial

def next_bigger(n):
    n = list(str(n))
    if len(n) < 2 or sorted(n, reverse=True) == n:
        return 0
    for k in range(len(n) - 2, -1, - 1):
        for j in range(len(n) - 1, k - 1, - 1):
            for i in range(j, k - 1, - 1):
                if n[j] > n[i - 1]:
                    n.insert(i - 1, str(n[j]))
                    del n[j + 1]
                    n = n[:i] + sorted(n[i:])
                    return ''.join(n)

def determinant(arr, permutations):
    det = 0
    for perm in (permutations):
        disorder = 0
        for j in range(len(perm)):
            for k in range(j, len(perm)):
                if perm[j] > perm[k]:
                    disorder += 1
        mult = 1
        for i in range(len(perm)):
            mult *= arr[i][int(perm[i]) - 1]
        if disorder % 2 == 0:
            det += mult
        else:
            det -= mult
    return det


N = '123'
lenght = len(N)
array = [''] * factorial(lenght)
for i in range(factorial(lenght)):
    disorder = 0
    for j in range(lenght):
        for k in range(j, lenght):
            if N[j] > N[k]:
                disorder += 1
    print(i + 1, N, disorder % 2)
    array[i] = N
    N = next_bigger(N)
A =[[-0.532, 0.653, 2.879],
    [0.653, 2.879, -0.532],
    [2.879, -0.532, 0.653]]

print(f'det A = {determinant(A, array)}')





















