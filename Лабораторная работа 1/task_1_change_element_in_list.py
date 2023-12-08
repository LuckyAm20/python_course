numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
filter_numbers = list(filter(lambda x: x is not None, numbers))
average_num = sum(filter_numbers) / len(numbers)
new_numbers = [el if el is not None else average_num for el in numbers]
print("Измененный список:", new_numbers)
