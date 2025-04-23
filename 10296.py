m = {}


def f(n):
  if n == 0:
    return 1
  if n in m:
    return m[n]
  m[n] = f(n // 2) + f(n // 3)
  return m[n]

n = int(input())
res = f(n)
print(res)