from random import randint

N = int(input("Введите число элементов в массиве: "))
A = [randint(0, 100) for _ in range(N)]


# 1. Копирование массива
def copy(array: list[int]):
    arr = [0] * len(array)
    for i in range(N):
        arr[i] = A[i]
    return arr


# 2. Линейный поиск в массиве
x = int(input("Введите искомое значение в массиве: "))


def array_search(search_item: int, array: list[int]) -> int:
    """Возвращает индекс первого вхождения или -1"""
    for index, item in enumerate(array):
        if search_item == item:
            return index
    return -1


print(array_search(x, [1, 4, 6, 2, 3]))


# 3. Инвертирование массива
def invert_array(array: list[int]):
    n = len(array)
    for j in range(n // 2):
        array[j], array[n - j - 1] = array[n - j - 1], array[j]
    return array


print(f"Массив - {A}")
print(f"Инвертированный массив - {invert_array(copy(A))}")