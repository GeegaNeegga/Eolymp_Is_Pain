import sys
sys.setrecursionlimit(1000)  # с запасом, т.к. n ≤ 100

# Считываем вход
n, m = map(int, input().split())

# Инициализация графа
graph = [[] for _ in range(n + 1)]  # вершины от 1 до n

# Считываем рёбра
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# Считываем стартовую вершину
start = int(input())

# Сортируем соседей для корректного порядка обхода (по возрастанию)
for neighbors in graph:
    neighbors.sort()

# Метки входа и выхода
d = [0] * (n + 1)  # время входа
f = [0] * (n + 1)  # время выхода
visited = [False] * (n + 1)

time = 1  # глобальное время

def dfs(v):
    global time
    visited[v] = True
    d[v] = time
    time += 1
    for u in graph[v]:
        if not visited[u]:
            dfs(u)
    f[v] = time
    time += 1

# Запуск DFS
dfs(start)

# Вывод результата
for v in range(1, n + 1):
    print(d[v], f[v])

