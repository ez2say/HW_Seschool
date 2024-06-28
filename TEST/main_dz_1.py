from decimal import Decimal
import math

###################################################ЗАДАНИЕ_1###########################################################
def input_coefficient(coefficient: str):
    while True:
        number = input(f'Введите число {coefficient}: ')
        try:
            number = float(number)
            return number
        except ValueError:
            print('Не правильный тип данных')


def calculate_discriminant(a: float, b: float, c: float):
    if isinstance(a, float) and isinstance(b, float) and isinstance(c, float):
        discriminant = b * b - 4 * a * c
        return discriminant
    else:
        raise ValueError


def calculate_roots(discriminant: float, a: float, b: float):

    if discriminant > 0:
        try:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        except ZeroDivisionError:
            result = 'Че то ек туда'
        else:
            result = root1, root2

    elif discriminant == 0:
        root1 = -b / (2 * a)
        result = root1
    else:
        result = f'Действительных корней нет'

    return result


print('Введите коэффициенты a, b и c: ')

a = input_coefficient('a')
b = input_coefficient('b')
c = input_coefficient('c')

discriminant = calculate_discriminant(a, b, c)
result = calculate_roots(discriminant, a, b)
print(discriminant)
print(f'Корни уравнения: {a}x^2 + {b}x + {c} = 0 Ответ: {result}')

#####################################################ЗАДАНИЕ_2#########################################################

# def input_side_length(side: str):
#     while True:
#         value = input(f"Введите длину стороны {side}: ")
#         try:
#             value = float(value)
#             if value > 0:
#                 return value
#             else:
#                 print('Минус нельзя, ноль нельзя,че не понятного!')
#         except ValueError:
#             print('Неверно')
#
#
# def check_exist_triangle(a: float, b: float, c: float):
#     if a + b > c and a + c > b and b + c > a:
#         return True
#     else:
#         return False
#
# def calculate_perimeter(a: float, b: float, c: float):
#     perimeter = a + b + c
#     return perimeter
#
# def calculate_square(a: float, b: float, c: float):
#     if check_exist_triangle(a, b, c):
#         half_perimeter = calculate_perimeter(a, b, c) / 2
#         square = math.sqrt(half_perimeter * (half_perimeter - a) *\
#                            (half_perimeter - b) * (half_perimeter - c))
#     else:
#         square = f'Треугольник с такими сторонами не существует.'
#
#     return square
#
#
# a = input_side_length('a')
# b = input_side_length('b')
# c = input_side_length('c')
# print(a, b, c)
#
# print(f'Площадь треугольника со сторанами: {a}, {b}, {c} равна: ', end='')
# print(calculate_square(a, b, c))
#
#
# # task 3
#
# def choice_option():
#     while True:
#         try:
#             choice = int(input('Введите опцию:\n'
#                                '1- Ковертировать Цельсий в Фаренгейт\n'
#                                '2- Конвертировать Фаренгейт в Цельсий\n'))
#         except ValueError:
#             print('Неверная опция')
#         else:
#             if choice == 1 or choice == 2:
#                 return choice
#             else:
#                 print('Неверная опция')
#
#
# def input_temperature(parameter: str):
#     while True:
#         try:
#             temperature = float(input(f'Введите температуру в градусах {parameter}: '))
#         except ValueError:
#             print('Неверное значение')
#         else:
#             if parameter == 'Цельсия' and temperature >= -273.15 or parameter == 'Фаренгейта' and temperature >= -459.67:
#                 return temperature
#             else:
#                 print('Показания не могут быть ниже абсолютного нуля!')
#
#
# def output_result(temperature, param: str):
#     print(f'Температура в градусах {param}: {temperature}')
#
#
# def conversion():
#
#     choice = choice_option()
#     if choice == 1:
#         temperature = Decimal(str(input_temperature('Цельсия'))) * 9 / 5 + 32
#         output_result(temperature, 'Цельсия')
#
#     elif choice == 2:
#         temperature = (Decimal(str(input_temperature('Фаренгейта'))) - 32) * 5 / 9
#         output_result(temperature, 'Фаренгейта')


# conversion()

