import random


def get_digits_frequency(s: str) -> None:
    """Функция принимает строку, состоящую из цифр и печатает сколько раз
    встречалась каждая цифра
    """
    array = [0] * 10
    for num in s:
        array[int(num)] += 1

    for ind, item in enumerate(array):
        print(f"{ind} - {item}")


def counting_sort(array: list[int]) -> None:
    """Функция сортирует список с значениями в диапазоне [-100; 100] методом подсчета
    и выводит отсортированные значения на экран"""
    values = [0] * 201

    for item in array:
        values[item + 100] += 1

    for i, elem in enumerate(values, -100):
        if elem > 0:
            print(elem * f"{i} ", end="")


get_digits_frequency(input("Введите число: "))
counting_sort([random.randint(-100, 100) for _ in range(100)])
