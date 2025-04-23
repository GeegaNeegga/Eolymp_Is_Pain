n = int(input())

res = [1,3]

for i in range(2,46):

  res += [3 * res[i-1] - res[i-2]]

print (res[n])