import math
from functools import reduce

def min_students(A, B, C, D):
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    percentages = [A, B, C, D]
    denominators = [100 // math.gcd(100, p) for p in percentages]
    return reduce(lcm, denominators)

# Ввод
A, B, C, D = map(int, input().split())
print(min_students(A, B, C, D))
