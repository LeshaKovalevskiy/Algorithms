def quick_merge(list1: list[int], list2: list[int]) -> list[int]:
    """Принимает в качестве аргументов два отсортированных по возрастанию списка,
    состоящих из целых чисел, и объединяет их в один отсортированный список"""
    p1, p2 = 0, 0
    res_lst = []
    n = len(list1)
    m = len(list2)

    while p1 < n and p2 < m:
        if list1[p1] < list2[p2]:
            res_lst.append(list1[p1])
            p1 += 1
        else:
            res_lst.append(list2[p2])
            p2 += 1
    return res_lst + list1[p1:] + list2[p2:]


lst1 = [1, 2, 2, 3, 5, 6, 7, 9]
lst2 = [2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 10]
print(quick_merge(lst1, lst2))
