import sys

 

def g(n):

  if n == 0:

    return 0

  k = (n + 1) // 2

  return k * k + g(n // 2)

 

for line in sys.stdin:

  n = int(line)

  print(g(n))