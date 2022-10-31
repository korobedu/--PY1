import random

def get_unique_list_numbers() -> list[int]:
    # TODO написать функцию для получения списка уникальных целых чисел
    len_ = 16
    list_ = []
    for _ in range(len_):
        while True:
            num = random.randint(-10, 10)
            if num in list_:
                continue
            list_.append(num)
            break

    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
