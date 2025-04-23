import math
x = [0] * 1000001
x[0] = 1
for i in range(1, 1000001):
  x[i] = (x[int(i - math.sqrt(i))] +
          x[int(math.log(i))] +
          x[int(i * math.sin(i)**2)]) % 1000000
  
while True:
  n = int(input())
  if n == -1:
    break
  print(x[n])