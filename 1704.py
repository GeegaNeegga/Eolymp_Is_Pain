m, n = map(int,input().split())
dp = [[0] * (n + 1) for i in range(m + 1)]
for i in range(1, m + 1): dp[i][1] = 1
for j in range(1, n + 1): dp[1][j] = 1
for i in range(2, m + 1):
  for j in range(2, n + 1):
    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[m][n])