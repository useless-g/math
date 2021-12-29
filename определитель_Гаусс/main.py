def gauss(a):
    n = len(a[0])
    permutations = 0
    for k in range(n - 1):
        if a[k][k] == 0:
            for _ in range(k + 1, n):
                if a[_][k]:
                    a[_], a[k] = a[k], a[_]
                    permutations += 1
                    break
            else:
                return [[0]], permutations
        for i in range(k + 1, n):
            l = a[i][k] / a[k][k]
            for j in range(k, n):
                a[i][j] -= a[k][j] * l
    return a, permutations


def determinant(array):
    det = 1
    arr, sign = gauss(array)
    for i in range(len(arr[0])):
        det *= arr[i][i]
    return round(det) * ((- 1) ** sign)


A = [[-0.532, 0.653, 2.879],
     [0.653, 2.879, -0.532],
     [2.879, -0.532, 0.653]]
print(determinant(A))

