orig_list = [1,2,3,4,5,6,7,8,9,10]

even_list = list(filter(lambda x: x % 2 == 0, orig_list))
odd_list = list(filter(lambda x: x % 2 != 0, orig_list))

print(even_list)  # [2, 4, 6, 8, 10]
print(odd_list)   # [1, 3, 5, 7, 9]