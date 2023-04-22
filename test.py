def a(num: int):
    return num if num < 10 else (num % 10) + a(num // 10)


print(a(1121))