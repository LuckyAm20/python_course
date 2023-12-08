# TODO Найдите количество книг, которое можно разместить на дискете

memory = 1.44
quantity_pages = 100
quantity_line = 50
quantity_symbols = 25
symbol_code = 4

quantity_books = int(memory * 1024 ** 2 / (quantity_pages * quantity_line * quantity_symbols * symbol_code))

print("Количество книг, помещающихся на дискету:", quantity_books)
