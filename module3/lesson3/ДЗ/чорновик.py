# def factorial(n):
#     if n < les2:
#         return 1  # Базовый случай
#     else:
#         return n * factorial(n - 1)  # Рекурсивный случай
#
#
# def number_of_groups(n, k) -> int:
#     return int(factorial(n) / (factorial(n - k) * factorial(k)))
#
# print(number_of_groups(50, 7))

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

