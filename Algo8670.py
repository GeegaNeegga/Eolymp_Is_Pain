def dfs(v):
    """Рекурсивный обход графа в глубину начиная с вершины v."""
    print(v, end=' ')
    used[v] = True
    for neighbor in g[v]:
        if not used[neighbor]:
            dfs(neighbor)

# Считывание количества вершин и рёбер
n, m = map(int, input().split())

# Инициализация списка смежности
g = [[] for _ in range(n + 1)]

# Инициализация массива посещений
used = [False] * (n + 1)

# Считывание рёбер графа
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# Считывание стартовой вершины и запуск обхода
start_vertex = int(input())
dfs(start_vertex)

