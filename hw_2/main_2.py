import math
class Patient:
    """
    По классу Patient можно создавать объект(пациент). В котором будет описано его ФИО,Болезнь. И благодаря методам,
    можно будет записаться на прием.
    """
    def __init__(self, first_name: str, second_name: str, patronymic: str, age: int, condition: str):
        self.first_name = first_name
        self.second_name = second_name
        self.patronymic = patronymic
        self.age = age
        self.condition = condition
        self.appointments = []


    def make_appointment(self, date_time:int):
        """
        Добавление элементов в self.appointments
        :param date_time: Принимает время как аргумент
        :return: Возвращает, а ничего не возвращает. Просто записывает данные в список.
        """
        if date_time in self.appointments:
            print('Вы уже записаны')
        else:
            self.appointments.append(date_time)
            print(f"{self.first_name} ,вы успешно записались на : {date_time}")

    def __str__(self):
        """

        :return: Информацию о пациенте,полную
        """
        return f"""
                Имя: {self.first_name}
                Фамилия: {self.second_name}
                Отчество: {self.patronymic}
                Возраст: {self.age}
                Заболевание: {self.condition}
                Запись на приём: {self.appointments}
                
        """


class TouristSpot:
    """
    Класс TouristSpot подразумевает под собой создание объекта TouristSpot, в котором описывается страна,тип и сама
    достопримечательность.Так же благодаря методам можно "посетить" место, и узнать полную информацию
    о достопримечательности.
    """
    def __init__(self, name:str, country:str, type:str):
        self.name = name
        self.country = country
        self.type = type

    def visit(self, visitor_name):
        """

        :param visitor_name: Принимает строку как аргумент
        :return: Возвращает извещение о том,какой человек посетил достопримечательность
        """
        print(f"{visitor_name} посетил(а) {self.name} в {self.country}.")

    def __str__(self):
        """

        :return: Возвращает полную инфу о месте
        """
        return f"""
            Название места: {self.name}
            Страна расположения: {self.country}
            Тип достопримечательности: {self.type}
        """

class ModelWindow:
    """
    По классу ModelWindow можно создать объект окно с определенными координатами и благодаря методам "играться"
    с состоянием окна и его размером,цветом и тп.
    """
    def __init__(self, title:str, x:int, y:int, width:int, height:int, color:str, visible:bool, framed:bool):
        self.title = title
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.visible = visible
        self.framed = framed

    def move_horizontally(self,dx: int):
        """

        :param dx: Принмает от человека координату
        :return: Перемещает окно по выбранной координате, в горизонтальной плоскости,
        если это возможно и информирует об этом
        """
        if 0 <= self.x + dx + self.width <= 1960:
            self.x += dx
            print(f'Окно перемещено по-горизонтали на координату {self.x}')

    def move_vertically(self, dy:int):
        """

        :param dy: Принимает от человека координату
        :return: Перемещает окно по выбранной координате, в вертикальной плоскости,
        если это возможно и информирует об этом
        """
        if 0 <= self.y + dy + self.height <= 1080:
            self.y += dy
            print(f'Окно перемещено по-вертикали на координату {self.y}')

    def resize_horizontally(self, dw:int):
        """

        :param dw: принимает от человека размер по ширине
        :return: Изменяет размер по ширине до введеного человеком,если это возможно и сообщает об этом
        """
        if 0 <= self.width + dw <= 1960:
            self.width += dw
            print(f'Окно расширено до {self.width}')
        else:
            print('Не получится дальше 1960px.')

    def resize_vertically(self, dh:int):
        """

        :param dh: ринимает от человека размер по высоте
        :return: Изменяет высоту окна,если это возможно, и сообщает об этом
        """
        if 0 <= self.height + dh <= 1080:
            self.height += dh
            print(f'Высота окна теперь {self.height}')
        else:
            print('Больше 1080px не расширить.')

    def change_color(self, color:str):
        """

        :param color: Принимает строку в виде аргумента,строка представляет собой цвет
        :return:Изменяет цвет окна на выбранный пользователем
        """

        self.color = color
        print(f'Цвет окна теперь {self.color}')

    def toggle_visibility(self):
        """

        :return: Меняет видимость\скрытость окна
        """
        self.visible = not self.visible
        print(f'Вы изменили видимость на {self.visible}')

    def toggle_frame(self):
        """

        :return: Изменяет тип окна в окне\развернуто
        """
        self.framed = not self.framed
        print(f'Тип окна теперь {self.framed}')

    def is_visible(self):
        """

        :return: Возвращает текущий статус окна
        """
        if self.visible:
            print('Окно видно')
        else:
            print('Окно скрыто')
        return self.visible

    def is_framed(self):
        """

        :return: Возвращает текущий статус окна
        """
        if self.framed:
            print('Окно в окне')
        else:
            print('Окно развернуто')
        return self.framed

    def __str__(self):
        """

        :return: Возвращает полную информацию об окне
        """
        state = "Виден" if self.visible else "Скрыт"
        frame = "В окне" if self.framed else "Не в окне"
        return f"Заголовок: '{self.title}'\n" \
               f"Координаты: ({self.x}, {self.y})\n" \
               f"Размер окна: {self.width}x{self.height}\n" \
               f"Цвет: {self.color}\n" \
               f"Состояние: {state}\n" \
               f"Режим: {frame}"

class ArrayUtils:
    @staticmethod
    def sum_array(array: list):
        """

        :param array: Принимает массив как аргумент
        :return: Возвращает сумму всех чисел массива
        """
        sum = 0

        for i in range(0, len(array),1):
            sum += array[i]

        return sum

    @staticmethod
    def composition(array: list):
        """

        :param array: Принимает массив как аргумент
        :return: Возвращает произведение всех чисел массива
        """
        com = 1

        for i in range(0,len(array), 1):
            com *= array[i]

        return com

    @staticmethod
    def inversion_arr(array: list):
        """

        :param array: Принимает массив как аргумент
        :return: Возвращает развернутый массив,созданный на базе принятого массива
        """
        inversed_array = []

        for i in range(len(array) -1, -1, -1):
            inversed_array.append(array[i])

        return inversed_array

    @staticmethod
    def max(array: list):
        """

        :param array: Принимает массив как аргумент
        :return: Возвращает максималочку
        """
        max = array[0]

        for i in range(0, len(array), 1):
            if max < array[i]:
                max = array[i]

        return max

    @staticmethod
    def min(array: list):
        """

        :param array: Принимает массив как аргумент
        :return: Возвращает минималочку
        """
        min = array[0]

        for i in range(0, len(array), 1):
            if min > array[i]:
                min = array[i]

        return min

class Vector:
    def __init__(self, x:float, y:float, z:float):
        """

        :param x: Принимает координату х
        :param y: Принимает координату у
        :param z: Принимает координату z
        """
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        """

        :return: выводит информацию о текущем положении точки
        """
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        """
        Метод для сложения векторов
        :param other: Принимает набор координат(Other) как аргумент
        :return: Возвращает сумму векторов
        """
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return Vector(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        """

        :param other: Принимает набор координат(Other) как аргумент
        :return:  Возвращает разность векоторв
        """
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return Vector(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other):
        """

        :param other: Принимает набор координат(Other) как аргумент
        :return: Возвращает произведение векторов
        """
        if isinstance(other, Vector):
            return self.dot_product(other)
        else:
            return Vector(self.x * other, self.y * other, self.z * other)

    def cross_product(self, other):
        """

        :param other: Принимает набор координат(Other) как аргумент
        :return: Возвращает векторное произведение
        """
        if isinstance(other, Vector):
            return Vector(self.y*other.z - self.z*other.y,
                            self.z*other.x - self.x*other.z,
                            self.x*other.y - self.y*other.x)
        else:
            raise TypeError("Векторное произведение возможно только между векторами")

    def dot_product(self, other):
        """

        :param other: Принимает набор координат(Other) как аргумент
        :return: Возвращает скалярное произведение
        """
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Скалярное произведение возможно только между векторами")

    def norm(self):
        """

        :return: Возвращает норму(длину) вектора
        """
        return (self.x**2 + self.y**2 + self.z**2)**0.5

class Fraction:

    def __init__(self,numerator:int, denominator:int):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть нулевым")
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        """

        :param other:Принимает числитель и знаменатель в виде целой дроби (other)
        :return: Сумму дробей
        """
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            return self + Fraction(other, 1)

    def __sub__(self, other):
        """

        :param other: Принимает числитель и знаменатель в виде целой дроби (other)
        :return: Возвращает разность дробей
        """
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            return self - Fraction(other, 1)

    def __mul__(self, other):
        """

        :param other: Принимает числитель и знаменатель в виде целой дроби (other)
        :return: Возвращает произведение дробей
        """
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            return self * Fraction(other, 1)

    def __str__(self):
        """

        :return: Возвращает значения числителя и знаменателя текущей дроби
        """
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

class GeometryUtils:

    @staticmethod
    def calculate_circle_area(circle_radius: float):
        """
        Метод для расчета площади круга с помощью радиуса
        :param circle_radius: Принимает радиус круга как аргумент
        :return: Возвращает площадь круга
        """
        area_of_circle = math.pi * (circle_radius ** 2)

        return area_of_circle

    @staticmethod
    def calculate_circle_perimeter(circle_radius: float):
        """
        Метод для расчета периметра круга с помощью радиуса
        :param circle_radius: Принимает радиус круга как аргумент
        :return: Возвращает периметр круга
        """
        perimeter_of_circle = (2 * math.pi) * circle_radius

        return perimeter_of_circle

    @staticmethod
    def calculate_rectangle_area(length: float, width: float):
        """

        :param length: Принимает длину прямоугольника как аргумент
        :param width: Принимает ширину треугольника как аргумент
        :return: Возвращает площадь прямоугольника
        """
        area_of_rectangle = length * width

        return area_of_rectangle

    @staticmethod
    def calculate_rectangle_perimeter(length: float, width: float):
        """

        :param length: Принимает длину прямоуголника как аргумент
        :param width: Принимает ширину прямоугольника как аргумент
        :return: Возвращает Периметр прямоугольника
        """
        perimeter_of_rectangle = 2 * (length + width)

        return perimeter_of_rectangle

    @staticmethod
    def Heron_area_formula_for_triangle(a: float, b: float, c: float):
        """

        :param a:Принимает сторону А треугольника как аргумент
        :param b:Принимает сторону B треугольника как аргумент
        :param c:Принимает сторону C треугольника как аргумент
        :return: возвращает площадь треугольника ,расчитанную с помощью формулы Херона(че!? ,а что ,так нельзя
        посчитать,без Херонов всяких?)
        """
        half_of_perimetr = 0.5 * (a + b + c)

        area_of_triangle = (half_of_perimetr * (half_of_perimetr - a) * (half_of_perimetr - b) * (half_of_perimetr - c)) ** 0.5

        return area_of_triangle


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Program:
    @staticmethod
    def main():

#############################################Задание_1############################################################
        #name = input('Введите имя: ')
        #second_name = input('Введите фамилию: ')
        #third_name = input('Введите отчество: ')
        #age = input('Введите возраст: ')
        #bolezn = input('Введите че болит: ')
        #patient_1 = Patient(name,second_name,third_name,age,bolezn)

        # while True:
        #     chs = int(input('Введите цифру для продолжения:'
        #                     '\n[1]Информация о пациенте'
        #                     '\n[2]Добавить запись на прием'
        #                     '\n[3]Выход'
        #                     '\n>>> '))
        #     if chs == 1:
        #         print(patient_1)
        #     elif chs == 2:
        #         date = input('Введите дату и время:')
        #         patient_1.make_appointment(date)
        #     elif chs == 3:
        #         break
        #     else:
        #         print('Такой команды нема')
    ##############################################Конец_задания_1#######################################################
    ##############################################Задание_2#############################################################
        # name = input('Введите название достопримечательности >: ')
        # country = input('Введите страну,где оно находится >: ')
        # type = input('Введите тип этого самого >: ')
        # spot = TouristSpot(name, country, type)
        #
        # while True:
        #     chs = int(input('Введите цифру для продолжения:'
        #                     '\n[1]Информация о достопримечательности'
        #                     '\n[2]Посетить место'
        #                     '\n[3]Выход'
        #                     '\n>>> '))
        #     if chs == 1:
        #         print(spot)
        #     elif chs == 2:
        #         name = input('Введите имя туриста >: ')
        #         spot.visit(name)
        #     elif chs == 3:
        #         break
    ############################################Конец_задания_2#########################################################
    ############################################Задание_3##############################################################
        # title = input('Введите заголовок окна: ')
        # x = int(input('Введите координату X: '))
        # y = int(input('Введите координату Y: '))
        # width = int(input('Введите ширину: '))
        # height = int(input('Введите высоту: '))
        # color = input('Введите цвет: ')
        # state_visible = input('Введите состояние видимости(visible/hidden):') == 'visible'
        # state_frame = input('Введите состояние окна(framed/frameless):') == 'framed'
        # window = ModelWindow(title,x,y,width,height,color,state_visible,state_frame)
        #
        # while True:
        #     chs = int(input('Введите цифру для продолжения:'
        #                     '\n[1]Переместить окно по горизонтали '
        #                     '\n[2]Переместить окно по вертикали '
        #                     '\n[3]Изменить ширину окна '
        #                     '\n[4]Изменить высоту окна '
        #                     '\n[5]Изменить цвет окна '
        #                     '\n[6]Изменить состояние окна '
        #                     '\n[7]Вывод состояния окна'
        #                     '\n[8]Выход'
        #                     '\n>>> '))
        #     if chs == 1:
        #         dx = int(input('Введите куда сместиться по-горизонтали: '))
        #         window.move_horizontally(dx)
        #     elif chs == 2:
        #         dy = int(input('Введите куда сместиться по-вертикали: '))
        #         window.move_vertically(dy)
        #     elif chs == 3:
        #         dw = int(input('Введите размер изменения окна по-ширине: '))
        #         window.resize_vertically(dw)
        #     elif chs == 4:
        #         dh = int(input('Введите размер изменения окна по-высоте: '))
        #         window.resize_horizontally(dh)
        #     elif chs == 5:
        #         new_color = input('Введите цвет окна: ')
        #         window.change_color(new_color)
        #     elif chs == 6:
        #         while True:
        #             print("[1]Изменить тип окна(в окне\развернуто)"
        #                   "\n[2]Изменить видимость окна(видно\скрыто)"
        #                   "\n[3]Назад")
        #             choose = int(input('Введите цифру для продолжения: '))
        #             if choose == 1:
        #                 window.toggle_frame()
        #             elif choose == 2:
        #                 window.toggle_visibility()
        #             elif choose == 3:
        #                 break
        #     elif chs == 7:
        #         window.is_visible()
        #         window.is_framed()
        #     elif chs == 8:
        #         break
#############################################################Конец_задания_3###########################################
#############################################################Задание_4#################################################
        # numbers = list(map(int, input("Введите массив чисел, разделенных пробелами: ").split()))
        # while True:
        #     print(f'Ваш первоначальный массив:{numbers}')
        #     chs = int(input('Введите цифру для продолжения:'
        #                     '\n[1]Сумма чисел введенного массива '
        #                     '\n[2]Произведение чисел введенного массива '
        #                     '\n[3]Развернутый массив'
        #                     '\n[4]Максимальное число массива '
        #                     '\n[5]Минимальное число массива'
        #                     '\n[6]Выход'
        #                     '\n>>> '))
        #     if chs == 1:
        #         print("Сумма :", ArrayUtils.sum_array(numbers))
        #     elif chs == 2:
        #         print('Произведение:', ArrayUtils.composition(numbers))
        #     elif chs == 3:
        #         print('Развернутый массив:', ArrayUtils.inversion_arr(numbers))
        #     elif chs == 4:
        #         print('Максимальное число:', ArrayUtils.max(numbers))
        #     elif chs == 5:
        #         print('Минимальное число:', ArrayUtils.min(numbers))
        #     elif chs == 6:
        #         break
############################################################Конец_задания_4#############################################
############################################################Задание_5###################################################
        # x1 = float(input('Введите координату х первого вектора: '))
        # y1 = float(input('Введите координату y первого вектора: '))
        # z1 = float(input('Введите координату z первого вектора: '))
        #
        # x2 = float(input('Введите координату х второго вектора: '))
        # y2 = float(input('Введите координату y второго вектора: '))
        # z2 = float(input('Введите координату z второго вектора: '))
        #
        # vec1 = Vector(x1, y1, z1)
        # vec2 = Vector(x2, y2, z2)
        #
        # while True:
        #
        #     chs = int(input('Введите цифру для продолжения:'
        #                     '\n[1]Информация о векторах '
        #                     '\n[2]Cумма векторов '
        #                     '\n[3]Разность векторов'
        #                     '\n[4]Скалярное произведение векторов '
        #                     '\n[5]Векторное произведение'
        #                     '\n[6]Норма(длина)вектора'
        #                     '\n[7]Выход'
        #                     '\n>>> '))
        #     if chs == 1:
        #         print(vec1)
        #         print(vec2)
        #     elif chs == 2:
        #         print(vec1 + vec2)
        #     elif chs == 3:
        #         print(vec1 - vec2)
        #     elif chs == 4:
        #         print(vec1.dot_product(vec2))
        #     elif chs == 5:
        #         print(vec1.cross_product(vec2))
        #     elif chs == 6:
        #         print(vec1.norm())
        #         print(vec2.norm())
        #     elif chs == 7:
        #         break
###########################################################Конец_задания_5#############################################
##########################################################Задание_6####################################################
        # chs1 = int(input('Введите числитель первой дроби: '))
        # znm1 = int(input('Введите знаменатель первой дроби(он не может быть равен нулю): '))
        #
        # chs2 = int(input('Введите числитель второй дроби: '))
        # znm2 = int(input('Введите знаменатель второй дроби(он не может быть равен нулю): '))
        #
        # drob_1 = Fraction(chs1, znm1)
        # drob_2 = Fraction(chs2, znm2)
        #
        # while True:
        #     chs = int(input('Введите цифру для продолжения:'
        #                     '\n[1]Информация дробях '
        #                     '\n[2]Cумма дробей '
        #                     '\n[3]Разность дробей'
        #                     '\n[4]Произведение дробей'
        #                     '\n[5]Выход'
        #                     '\n>>> '))
        #     if chs == 1:
        #         print(drob_1)
        #         print(drob_2)
        #     elif chs == 2:
        #         print(drob_1 + drob_2)
        #     elif chs == 3:
        #         print(drob_1 - drob_2)
        #     elif chs == 4:
        #         print(drob_1 * drob_2)
        #     elif chs == 5:
        #         break
#############################################################Конец_задания_6###########################################
################################################################Задани_7###############################################
        while True:
            chs = int(input('Введите цифру для продолжения:'
                            '\n[1]Рассчет площади круга '
                            '\n[2]Рассчет периметра круга '
                            '\n[3]Рассчет площади прямоугольника'
                            '\n[4]Рассчет периметра прямоугольника'
                            '\n[5]ПЛОЩАДЬ ХЕРОНА ТРЕУГОЛЬНИКА'
                            '\n[6]Выход'
                            '\n>>> '))
            if chs == 1:
                misha_krug = float(input('Введите радиус круга: '))
                print(GeometryUtils.calculate_circle_area(misha_krug))
            elif chs == 2:
                misha_krug = float(input('Введите радиус круга: '))
                print(GeometryUtils.calculate_circle_perimeter(misha_krug))
            elif chs == 3:
                dlina_pryamougol = float(input('Введите длину прямоугольника: '))
                shirina_priamougol = float(input('Введите ширину прямоугольника: '))
                print(GeometryUtils.calculate_rectangle_area(dlina_pryamougol, shirina_priamougol))
            elif chs == 4:
                dlina_pryamougol = float(input('Введите длину прямоугольника: '))
                shirina_priamougol = float(input('Введите ширину прямоугольника: '))
                print(GeometryUtils.calculate_rectangle_perimeter(dlina_pryamougol, shirina_priamougol))
            elif chs == 5:
                a = float(input('Введите длину стороны А треугольника: '))
                b = float(input('Введите длину стороны B треугольника: '))
                c = float(input('Введите длину стороны C треугольника: '))
                print(GeometryUtils.Heron_area_formula_for_triangle(a, b, c))
            elif chs == 6:
                break




        dlina_pryamougol = float(input('Введите радиус круга: '))
        shirina_priamougol = float(input('Введите радиус круга: '))


Program.main()




