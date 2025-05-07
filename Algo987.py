def find_spanning_tree(n, m, edges):
    # Строим список смежности
    adj_list = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = [False] * (n + 1)
    tree_edges = []

    def dfs(v):
        visited[v] = True
        for u in adj_list[v]:
            if not visited[u]:
                tree_edges.append((v, u))
                dfs(u)

    # Начинаем DFS с вершины 1 (или любой другой)
    dfs(1)

    return tree_edges

# Ввод данных
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Находим остовное дерево
tree_edges = find_spanning_tree(n, m, edges)

# Выводим результат
for u, v in tree_edges:
    print(u, v)
