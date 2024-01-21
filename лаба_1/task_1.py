import doctest


class Car:
    def __init__(self, brand: str, color: str):
        """
        Создание и подготовка к работе объекта "Машина"

        :param brand: Марка машины
        :param color: Цвет машины

        Примеры:
        >>> car = Car("BMW", "красный")
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть типа str")
        self.brand = brand
        if not isinstance(color, str):
            raise TypeError("Цвет автомобиля должен быть типа str")
        self.color = color

    def start_engine(self) -> None:
        """
        Запуск двигателя транспортного средства.

        :return: None

        Примеры:
        >>> car = Car("BMW", "красный")
        >>> car.start_engine()
        """
        ...

    def stop_engine(self) -> None:
        """
        Остановка двигателя транспортного средства.

        :return: None

        Примеры:
        >>> car = Car("BMW", "красный")
        >>> car.stop_engine()
        """
        pass


class Furniture:
    def __init__(self, material: str, color: str):
        """
        Создание и подготовка к работе объекта "Мебель".

        :param material: Материал, из которого изготовлена мебель
        :param color: Цвет мебели

        Примеры:
        >>> chair = Furniture("Дерево", "Коричневый")
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        self.material = material
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        self.color = color

    def move_furniture(self, new_location: str) -> None:
        """
        Перемещение мебели в новое место.

        :param new_location: Новое местоположение мебели

        :raise ValueError: Если новое место не типа str, то вызываем ошибку

        :return: None

        Примеры:
        >>> chair = Furniture("Дерево", "Коричневый")
        >>> chair.move_furniture("Гостиная")
        """
        ...

    def change_color(self, new_color: str) -> None:
        """
        Изменение цвета мебели.

        :param new_color: Новый цвет мебели

        :raise ValueError: Если новый цвет не типа str, то вызываем ошибку

        :return: None

        Примеры:
        >>> chair = Furniture("Дерево", "Коричневый")
        >>> chair.change_color("Белый")
        """
        ...


class Book:
    def __init__(self, title: str, author_full_name: str, page_count: int):
        """
        Создание объекта "Книга".

        :param title: Название книги
        :param author_full_name: Полное имя автора книги (включая отчество)
        :param page_count: Количество страниц в книге

        :raise TypeError: Если название книги или полное имя автора не являются строками.
        :raise ValueError: Если количество страниц не является положительным целым числом
                           или если полное имя автора не содержит как минимум имя и фамилию.

        Примеры:
        >>> book = Book("Преступление и наказание", "Федор Михайлович Достоевский", 400)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        self.title = title
        if not isinstance(author_full_name, str):
            raise TypeError("Полное имя автора должно быть строкой")
        self.author_full_name = author_full_name
        if not isinstance(page_count, int) or page_count <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self.page_count = page_count

        self.current_page = 1

        name_parts = author_full_name.split()
        if len(name_parts) < 2:
            raise ValueError("Полное имя автора должно содержать как минимум имя и фамилию")
        self.author_first_name = name_parts[0]
        self.author_middle_name = name_parts[1] if len(name_parts) > 1 else ""
        self.author_last_name = name_parts[-1]

    def read_page(self, page_number: int) -> str:
        """
        Чтение страницы книги.

        :param page_number: Номер страницы
        :return: Текст на странице

        :raise ValueError: Если номер страницы не является положительным целым числом
                           или превышает общее количество страниц в книге.

        Примеры:
        >>> book = Book("Преступление и наказание", "Федор Михайлович Достоевский", 400)
        >>> book.read_page(1)
        """
        if not isinstance(page_number, int) or page_number < 1 or page_number > self.page_count:
            raise ValueError("Некорректный номер страницы")
        ...

    def bookmark_page(self, page_number: int) -> None:
        """
        Добавление закладки на определенную страницу книги.

        :param page_number: Номер страницы для закладки

        :raise ValueError: Если номер страницы для закладки не является положительным целым числом
                           или превышает общее количество страниц в книге.

        Примеры:
        >>> book = Book("Преступление и наказание", "Федор Михайлович Достоевский", 400)
        >>> book.bookmark_page(50)
        """
        if not isinstance(page_number, int) or page_number < 1 or page_number > self.page_count:
            raise ValueError("Некорректный номер страницы для закладки")

        ...


if __name__ == "__main__":
    doctest.testmod()
