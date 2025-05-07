n = int(input())
a, b, c = [], [], []

for _ in range(n):
    ai, bi, ci = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)

INF = float('inf')
dp = [INF] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    # один человек сам за себя
    dp[i] = min(dp[i], dp[i - 1] + a[i - 1])
    # двое подряд (если можно)
    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + b[i - 2])
    # трое подряд (если можно)
    if i >= 3:
        dp[i] = min(dp[i], dp[i - 3] + c[i - 3])

print(dp[n])
