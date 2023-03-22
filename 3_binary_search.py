arr = [-1, 2, 3, 4, 5, 8, 9, 12]
n = len(arr)

left, right = 0, n - 1
search_v = int(input())

while left <= right:
    middle = (right + left) // 2
    value = arr[middle]
    if value == search_v:
        print(f"Индекс - {middle}")
        break
    elif value > search_v:
        right = middle - 1
    else:  # value < search_v
        left = middle + 1
else:
    print("Значение не найдено")
