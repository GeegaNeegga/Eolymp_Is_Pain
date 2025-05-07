n = int(input())
res = [0] * (n + 1)
res[1] = 1  # минимально операций, чтобы получить 1 — это 1 (начальная точка)

for i in range(2, n + 1):
    res[i] = i  # по умолчанию: складываем единицы i раз

    # Попробуем получить i как сумму двух меньших чисел
    for j in range(1, i // 2 + 1):
        res[i] = min(res[i], res[j] + res[i - j])

    # Попробуем получить i как произведение двух множителей
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            res[i] = min(res[i], res[j] + res[i // j])

print(res[n])
