list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number = 0

for number in list_numbers:
    if number > max_number:
        max_number = number

max_number_index = 0

for i in range(len(list_numbers)):
    max_number = list_numbers[max_number_index]
    if number > max_number:
        max_number_index = i
list_numbers[max_number_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_number_index]


print(list_numbers)
