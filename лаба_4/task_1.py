if __name__ == "__main__":
    class Car:
        """
        Базовый класс для представления автомобилей.
        """

        def __init__(self, brand: str, model: str, year: int):
            """
            Конструктор класса Car.

            :param brand: Марка автомобиля.
            :param model: Модель автомобиля.
            :param year: Год выпуска автомобиля.

            :raise TypeError: Если типы входных данных не соответствуют ожидаемым.
            """
            if not isinstance(brand, str) or not isinstance(model, str) or not isinstance(year, int):
                raise TypeError("Некорректный тип входных данных")

            self.brand = brand
            self.model = model
            self.year = year

        def start_engine(self) -> str:
            """
            Метод для запуска двигателя автомобиля.

            :return: Сообщение о запуске двигателя.
            """
            return f"{self.brand} {self.model} двигатель запущен"

        def drive(self, distance: float) -> str:
            """
            Метод для имитации поездки на автомобиле.

            :param distance: Пройденное расстояние.
            :return: Сообщение о пройденном расстоянии.

            :raise TypeError: Если тип входных данных для distance не соответствует ожидаемому.
            """
            if not isinstance(distance, (int, float)):
                raise TypeError("Некорректный тип входных данных для distance")

            return f"{self.brand} {self.model} проехал(а) {distance} км"

        def __str__(self) -> str:
            """
            Магический метод для представления объекта в виде строки.

            :return: Строковое представление объекта.
            """
            return f"{self.year} {self.brand} {self.model}"

        def __repr__(self) -> str:
            """
            Магический метод для представления объекта в виде строки при вызове repr().

            :return: Строковое представление объекта.
            """
            return f"Car('{self.brand}', '{self.model}', {self.year})"


    class GasolineCar(Car):
        """
        Дочерний класс для представления бензиновых автомобилей.
        """

        def __init__(self, brand: str, model: str, year: int, fuel_efficiency: float):
            """
            Конструктор класса GasolineCar.

            :param brand: Марка автомобиля.
            :param model: Модель автомобиля.
            :param year: Год выпуска автомобиля.
            :param fuel_efficiency: Расход топлива автомобиля (л/100 км).

            :raise TypeError: Если типы входных данных не соответствуют ожидаемым.
            """
            super().__init__(brand, model, year)

            if not isinstance(fuel_efficiency, (int, float)):
                raise TypeError("Некорректный тип входных данных для fuel_efficiency")

            self.fuel_efficiency = fuel_efficiency

        def refuel(self, amount: float) -> str:
            """
            Метод для заправки бензинового автомобиля.

            :param amount: Количество заправленного топлива (в литрах).
            :return: Сообщение о заправке топлива.

            :raise TypeError: Если тип входных данных для amount не соответствует ожидаемому.
            """
            if not isinstance(amount, (int, float)):
                raise TypeError("Некорректный тип входных данных для amount")

            return f"{self.brand} {self.model} заправлен(а) {amount} л бензина"

        def drive(self, distance: float) -> str:
            """
            Перегруженный метод для имитации поездки на бензиновом автомобиле.
            Перегрузка нужна, чтобы указать количество потраченного топлива

            :param distance: Пройденное расстояние.
            :return: Сообщение о пройденном расстоянии с учетом расхода топлива.

            :raise TypeError: Если тип входных данных для distance не соответствует ожидаемому.
            """
            if not isinstance(distance, (int, float)):
                raise TypeError("Некорректный тип входных данных для distance")

            fuel_needed = distance / self.fuel_efficiency
            return f"{self.brand} {self.model} проехал(а) {distance} км, потратив {fuel_needed:.2f} л бензина"

        def __repr__(self) -> str:
            """
            Перегруженный магический метод для представления объекта в виде строки при вызове repr().

            :return: Строковое представление объекта.
            """
            return f"GasolineCar('{self.brand}', '{self.model}', {self.year}, {self.fuel_efficiency})"


    class ElectricCar(Car):
        """
        Дочерний класс для представления электрических автомобилей.
        """

        def __init__(self, brand: str, model: str, year: int, battery_capacity: float):
            """
            Конструктор класса ElectricCar.

            :param brand: Марка автомобиля.
            :param model: Модель автомобиля.
            :param year: Год выпуска автомобиля.
            :param battery_capacity: Емкость батареи автомобиля (в кВтч).

            :raise TypeError: Если типы входных данных не соответствуют ожидаемым.
            """
            super().__init__(brand, model, year)

            if not isinstance(battery_capacity, (int, float)):
                raise TypeError("Некорректный тип входных данных для battery_capacity")

            self.battery_capacity = battery_capacity

        def charge(self, hours: int) -> str:
            """
            Метод для зарядки электрического автомобиля.

            :param hours: Количество часов зарядки.
            :return: Сообщение о зарядке батареи.

            :raise TypeError: Если тип входных данных для hours не соответствует ожидаемому.
            """
            if not isinstance(hours, int):
                raise TypeError("Некорректный тип входных данных для hours")

            return f"{self.brand} {self.model} заряжен(а) в течение {hours} часов"

        def __repr__(self) -> str:
            """
            Перегруженный магический метод для представления объекта в виде строки при вызове repr().

            :return: Строковое представление объекта.
            """
            return f"ElectricCar('{self.brand}', '{self.model}', {self.year}, {self.battery_capacity})"
