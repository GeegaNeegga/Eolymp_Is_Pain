n, m = map(int, input().split())

a = [[0] * (m + 1) for _ in range(n + 1)]
s = [[0] * (m + 1) for _ in range(n + 1)]

# Ввод матрицы
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, m + 1):
        a[i][j] = row[j - 1]

# Вычисление префиксных сумм
for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i][j]

# Выводим массив префиксных сумм
for i in range(1, n + 1):
    print(*s[i][1:])
