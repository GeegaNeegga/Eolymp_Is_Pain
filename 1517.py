def g(n):

  if n <= 0: return 0

  t = n % 10

  return (n // 10) * 45 + (t * (t + 1) // 2) + g(n // 10)

while True:

  p, q = map(int, input().split())

  if p < 0 and q < 0: break

  print(g(q) - g(p - 1))