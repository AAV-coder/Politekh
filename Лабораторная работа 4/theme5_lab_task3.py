from random import sample

def get_unique_list_numbers() -> list[int]:
    list_unique_numbers = sample(range(-10, 10), 15)
    return list_unique_numbers

    # функция для получения списка уникальных целых чисел

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
