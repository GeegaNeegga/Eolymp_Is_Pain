x, y = map(int, input().split())

def f(x, y):
  if x <= 0 or y <= 0: return 0
  if dp[x][y] != -1: return dp[x][y]
  if x <= y:
    dp[x][y] = f(x - 1, y - 2) + f(x - 2, y - 1) + 2
  else:
    dp[x][y] = f(x - 2, y - 2) + 1
  return dp[x][y]
dp = [[-1] * 51 for _ in range(51)]
print(f(x, y))