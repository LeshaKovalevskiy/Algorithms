# 1. Рекурсивный способ
def fib1(x):
    return x if x <= 1 else fib1(x - 1) + fib1(x - 2)


# 2. Рекурсивный способ c кешированием
_cashe = {}


def fib2(x):
    if x not in _cashe:
        _cashe[x] = x if x <= 1 else fib2(x - 1) + fib2(x - 2)
    return _cashe[x]


# 3. Кеширование с использованием декоратора вместо глобального словаря
def memo(func):
    cashe = {}

    def wrapper(x):
        if x not in cashe:
            cashe[x] = func(x)
        return cashe[x]

    return wrapper


# 4. Цикл
def fib3(x):
    a, b = 1, 1
    for _ in range(x - 1):
        a, b = b, a + b
    return a
