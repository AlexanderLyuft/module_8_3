                        # Домашнее задание по теме "Создание исключений".


class Car:
    def __init__(self, model, __vin, __numbers):

        def __is_valid_vin(vin_number):
            if not isinstance(vin_number, int):
                raise IncorrectVinNumber("Некорректный тип vin номер")
            elif not (vin_number in range(1000000, 9999999)):
                raise IncorrectVinNumber("Неверный диапазон для vin номера")
            else:
                return True

        def __is_valid_numbers(numbers):
            if not isinstance(numbers, str):
                raise IncorrectCarNumbers("Некорректный тип данных для номеров")
            elif not len(numbers) == 6:
                raise IncorrectCarNumbers("Неверная длина номера")
            else:
                return True

        self.model = model
        self.__vin = __is_valid_vin(__vin)
        self.__numbers = __is_valid_numbers(__numbers)


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')






