n = int(input())
coords = list(map(int, input().split()))
coords.sort()

total_length = 0
for i in range(1, n):
    total_length += coords[i] - coords[i - 1]

print(total_length)
