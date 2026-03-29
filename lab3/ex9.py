list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

def sum_lists(l1, l2):
    return list(map(lambda x: x[0] + x[1], zip(l1, l2)))

result = sum_lists(list1, list2)
print(result)  # [11, 22, 33, 44, 55]