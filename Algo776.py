import sys
sys.setrecursionlimit(100000)  # Увеличиваем лимит рекурсии, так как при большом n DFS может быть глубокой

# Функция обхода в глубину (DFS)
def dfs(v, visited, graph):
    visited[v] = True  # Отмечаем текущий город как посещённый
    for neighbor in graph[v]:  # Проходим по соседям текущего города
        if not visited[neighbor]:  # Если сосед еще не посещен
            dfs(neighbor, visited, graph)  # Рекурсивно вызываем DFS для соседа

# Чтение входных данных: количество городов (n) и дорог (m)
n, m = map(int, input().split())

# Инициализация списка смежности для графа
graph = [[] for _ in range(n)]  # graph[i] будет содержать список городов, напрямую связанных с городом i

# Считываем все существующие дороги
for _ in range(m):
    a, b = map(int, input().split())
    # Добавляем дорогу в обе стороны, так как дороги двухсторонние
    graph[a - 1].append(b - 1)  # Преобразуем в 0-индексацию
    graph[b - 1].append(a - 1)

# Массив для отслеживания посещённых городов
visited = [False] * n

components = 0  # Счётчик компонент связности

# Обходим все города
for i in range(n):
    if not visited[i]:  # Если город ещё не посещён
        dfs(i, visited, graph)  # Запускаем DFS из этого города
        components += 1  # Увеличиваем счётчик компонент, т.к. мы начали новую компоненту

# Ответ — минимальное количество дорог, чтобы связать все компоненты
print(components - 1)
