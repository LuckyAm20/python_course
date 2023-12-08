# TODO Напишите функцию find_common_participants
from typing import List


def find_common_participants(group_1: str, group_2: str, separation=",") -> List[str]:
    return sorted(list(set(group_1.split(sep=separation)) & set(group_2.split(sep=separation))))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
