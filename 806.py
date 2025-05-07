n = int(input())
y = list(map(int, input().split()))

if n == 2:
    print((y[1] - y[0]) ** 2)
else:
    prev2 = 0
    prev1 = (y[1] - y[0]) ** 2
    for i in range(2, n):
        curr = min(
            prev1 + (y[i] - y[i - 1]) ** 2,
            prev2 + 3 * (y[i] - y[i - 2]) ** 2
        )
        prev2, prev1 = prev1, curr
    print(prev1)
