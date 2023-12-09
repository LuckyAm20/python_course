# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data_json = []
    ...  # TODO считать содержимое csv файла

    with open(INPUT_FILENAME) as file_input:
        rows = csv.DictReader(file_input)
        for row in rows:
            new_data = {}
            for key in rows.fieldnames:
                new_data[key] = row[key]
            data_json.append(new_data)

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode="w",) as file_output:
        json.dump(data_json, file_output, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
