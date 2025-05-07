n = int(input())
y = list(map(int, input().split()))

# Минимальная энергия до каждой платформы
dp = [0] * n
# Предыдущая платформа для восстановления пути
prev = [-1] * n

# Начальные значения
dp[0] = 0
dp[1] = abs(y[1] - y[0])
prev[1] = 0

# Основной цикл
for i in range(2, n):
    cost1 = dp[i-1] + abs(y[i] - y[i-1])
    cost2 = dp[i-2] + 3 * abs(y[i] - y[i-2])
    
    if cost1 <= cost2:
        dp[i] = cost1
        prev[i] = i - 1
    else:
        dp[i] = cost2
        prev[i] = i - 2

# Восстановление пути
path = []
cur = n - 1
while cur != -1:
    path.append(cur + 1)  # +1 для человеческой нумерации
    cur = prev[cur]

path.reverse()

# Вывод
print(dp[n - 1])
print(len(path))
print(*path)
