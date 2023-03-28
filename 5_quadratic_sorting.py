A = [8, 3, 1, 2, 9, 5, 0, 3, 7]


# 1. insert sort(вставками)
def insert_sort(array: list[int]):
    n = len(array)
    for i in range(1, n):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array


# 2. choise sort(выбором)
def choise_sort(array: list[int]):
    n = len(array)
    for i in range(n - 1):
        mn_ind = i
        for j in range(i + 1, n):
            if array[mn_ind] > array[j]:
                mn_ind = j
        array[i], array[mn_ind] = array[mn_ind], array[i]
    return array


# 3. buble sort(сортировка пузырьком)
def buble_sort(array: list[int]):
    n = len(array)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


print(insert_sort(A.copy()))
print(choise_sort(A.copy()))
print(buble_sort(A.copy()))
