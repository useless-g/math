import math
import itertools


def solveKTO(B, M, n) -> int:
    solutions_array = []
    if math.gcd(*m) != 1:
        print('не решается кто')
    for i in range(n):
        xi = 1
        for j in range(n):
            xi *= M[j]
        xi //= M[i]
        solutions_array.append(solve(xi, B[i], M[i], n)[0] * xi)
    solution = sum(solutions_array)
    return solution


def solve(AA, BB, MM, n) -> list:
    """решает одно линейное сравнение и возвращает массив решений"""
    while BB < 0:
        BB += MM
    ans = 1
    g = math.gcd(AA, MM)  # НОД коэффициента и модуля
    Ak = AA
    ans_array = []
    while Ak != BB:  # ищем решение уравнения
        Ak += AA
        ans += 1
        if Ak >= MM:
            Ak %= MM
    for j in range(n):  # ищем все решения не равные по модулю M
        if int((ans + MM / g * j) % MM) not in ans_array:  # добавляем все решения в список без повторов
            ans_array.append(int((ans + MM / g * j) % MM))
    return ans_array


n = int(input('количество уранений в системе: '))
a = [0] * n
b = [0] * n
m = [0] * n
k = [[] for i in range(n)]  # список списков решений
for i in range(n):
    a[i], b[i], m[i] = tuple(map(int, (input()).split()))  # считали систему
for i in range(n):
    k[i] = solve(a[i], b[i], m[i], n)

k = list(map(set, k))
print(k)
decart = list()  # список декартово произведение
for element in itertools.product(*k):
    decart.append(element)
print(decart)
kkk = []  # список решений для каждой системы через КТО
'''теперь нужно через кто решить каждую систему'''
# if math.gcd(*m) != 1:
    # print('нет решений')
for i in range(len(decart)):
    kkk.append(solveKTO(decart[i], m, n))
print(kkk)
