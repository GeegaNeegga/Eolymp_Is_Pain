d = [0] * 1000001
d[1] = 0

for i in range(2, 1000001):

  d[i] = d[i - 1]

  if i % 2 == 0 and d[i // 2] < d[i]:

    d[i] = d[i // 2]

  if i % 3 == 0 and d[i // 3] < d[i]:

    d[i] = d[i // 3]

  d[i] += 1

while True:
  try:
    n = int(input())
    print(d[n])
  except EOFError:
    break
  