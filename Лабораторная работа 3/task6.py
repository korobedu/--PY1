list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_max = 0
max_num = list_numbers[index_max]
for index, num in enumerate(list_numbers):
    if num > max_num:
        max_num = num
        index_max = index

list_numbers[index_max], list_numbers[-1] = list_numbers[-1], list_numbers[index_max]

print(list_numbers)
