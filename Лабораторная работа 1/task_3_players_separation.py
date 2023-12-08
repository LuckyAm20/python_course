list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

length = len(list_players)
list_players_1 = list_players[:length // 2]
list_players_2 = list_players[length // 2:]

print(list_players_1, list_players_2, sep="\n")
