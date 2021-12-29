'''import math

def next_bigger(n):
    n = list(str(n))
    if len(n) < 2 or sorted(n, reverse = True) == n:
        return 0
    for k in range(len(n) - 2, -1, - 1):
        for j in range(len(n) - 1, k - 1, - 1):
            for i in range(j, k - 1, - 1):
                if n[j] > n[i - 1]:
                    n.insert(i - 1, str(n[j]))
                    del n[j + 1]
                    n = n[:i] + sorted(n[i:])
                    return ''.join(n)


for o in range(1):
    N = 9
    s = ''
    for i in range(N):
        s += str(i)
    permutations = [s] * math.factorial(N)
    for i in range(1, math.factorial(N)):
        permutations[i] = next_bigger(permutations[i - 1])
    k = 0
    for perm in permutations:
        A = [[True if int(perm[j]) == i else False for i in range(N)]for j in range(N)]
        flag = True
        for i in range(N):
            if not flag:
                break
            for j in range(N):
                if not flag:
                    break
                if not A[i][j]:
                    continue
                m = i
                n = j
                while m * n > 0:
                    m -= 1
                    n -= 1
                p = -1
                while True:
                    if A[m][n]:
                        p += 1
                    m += 1
                    n += 1
                    if m > N - 1 or n > N - 1:
                        break
                if p:
                   flag = False
                   break
                m = i
                n = j
                while m != N - 1 and n > 0:
                    m += 1
                    n -= 1
                p = -1
                while True:
                    if A[m][n]:
                        p += 1
                    m -= 1
                    n += 1
                    if m < 0 or n > N - 1:
                        break
                if p:
                    flag = False
                    break
            if flag == False:
                break
        if flag:
            k+=1
    print(o, k)

from copy import copy, deepcopy


def getField():
    a = []
    for i in range(N):
        a.append([])
        for j in range(N):
            a[i].append(1)
    return a


def placeFerz(a, i, j):
    res = deepcopy(a)
    length = len(a)
    for k in range(length):
        res[k][j] = 0
    for k in range(length):
        res[i][k] = 0
    k = i
    z = j
    while k >= 0 and z < length:
        res[k][z] = 0
        k += -1
        z += 1
    k = i
    z = j
    while k < length and z < length:
        res[k][z] = 0
        k += 1
        z += 1
    k = i
    z = j
    while k < length and z >= 0:
        res[k][z] = 0
        k += 1
        z += -1
    k = i
    z = j
    while k >= 0 and z >= 0:
        res[k][z] = 0
        k += -1
        z += -1
    return res

def work():
    global counter
    if N == 1:
        counter = 1
        return 1
    field = getField()
    for i in range(N):
        temp = placeFerz(field, 0, i)
        rec(temp, 1, 0)

def rec(field, str, count):
    global counter
    if field[str].count(1) == 0:
        return 0
    elif str == N - 1:
        counter += 1
        return 1
    for i in range(N):
        if field[str][i]:
            rec(placeFerz(field, str, i), str + 1, count)

counter = 0
N = int(input())
# work()
# print(counter)
print()'''
a = 17
c=0
for i in range(4,12):
    a -= 2
    c += a*i*i
print(c*4)