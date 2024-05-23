class Spell:
    def __init__(self, name:str, difficult:int, type:str, description:str):
        self.__name = name
        self.__difficult = difficult
        self.__type = type
        self.__description = description

    def get_name(self):
        return f'Название заклинания: {self.__name}'

    def get_difficult(self):
        return f'Сложность заклинания: {self.__difficult}'

    def get_type(self):
        return f'Тип заклинания {self.__type}'

    def get_description(self):
        return (f'Заклинание --*{self.__name}*-- имеет эффект :'
                f'\n{self.__description}')

    def set_name(self,new_name:str):
        if not isinstance(new_name, str):
            raise TypeError
        else:
            self.__name = new_name
            print(f'Название заклинания сменено на {self.__name}')

    def set_difficult(self, new_dfficult:int):
        if not isinstance(new_dfficult, int):
            raise TypeError
        else:
            if new_dfficult >= 1 and new_dfficult <= 10:
                self.__difficult = new_dfficult
                print(f'Сложность заклинания {self.__name} изменена на {self.__difficult}')
            else:
                raise ValueError

    def set_type(self, new_type:str):
        if not isinstance(new_type, str):
            raise TypeError
        else:
            self.__type = new_type
            print(f'Тип заклинания {self.__name} изменен на {self.__type}')

    def set_description(self, new_desc:str):
        if not isinstance(new_desc, str):
            raise TypeError
        else:
            self.__description = new_desc
            print(f'Теперь описание способности {self.__name} -->'
                  f'\n{self.__description}')

    def __str__(self):
        return f"""
                Название: {self.__name}
                Сложность:{self.__difficult}
                Тип заклинания: {self.__type}
                Описание заклинания: {self.__description}
                """


class Wizard:
    def __init__(self, name:str, faculty:str, spellforce:int, spells:list = None, status:str = 'В Хогвартсе'):
        self.__name = name
        self.__faculty = faculty
        self.__spellforce = spellforce
        self.__spellbook = spells
        self.__status = status

    def get_name(self):
        return f'Имя волшебника >>>  {self.__name}'

    def get_faculty(self):
        return f'Факультет волшебника {self.__name} >>> {self.__faculty}'

    def get_spellforce(self):
        return f'Уровень магической силы у волшебника {self.__name} >>> {self.__spellforce}'

    def get_spellbook(self):
        return f"Заклинания>>>> {'\n'.join(str(spell) for spell in self.__spellbook)}"

    def get_status(self):
        return f'Статус волшебника {self.__name} >>> {self.__status}'

    def set_faculty(self, faculty:str):
        if not isinstance(faculty,str):
            raise TypeError
        else:
            self.__faculty = faculty
            print(f'Факультет сменён на: {self.__faculty}')


    def set_status(self, status:str):
        self.__status = status
        print(f'Статус изменен на: {self.__status}')

    def add_spell(self, spell: Spell):
        self.__spellbook.append(spell)
        print(f'Заклинание {spell} добавлено')

    def remove_spell(self, spell: Spell):
        self.__spellbook.remove(spell)
        print(f'Заклинание {spell} удалено из списка заклинаний.')

    def increase_spellforce(self, amount:int):
        if not isinstance(amount, int):
            raise TypeError
        else:
            if not amount >= 0:
                raise ValueError
            else:
                self.__spellforce = amount
                print(f'Теперь сила волшебника: {self.__spellforce}')

    def __str__(self):
        return f"""
                Имя: {self.__name}
                Факультет: {self.__faculty}
                Уровень магической силы: {self.__spellforce}
                Заклинания:{'\n'.join(str(spell) for spell in self.__spellbook)}
                Статус: {self.__status}"
                
               """


class Employee:
    def __init__(self, name: str, position: str, department: str, salary: float, experience: int, completed_projects: list = None):
        self.__name = name
        self.__position = position
        self.__department = department
        self.__salary = salary
        self.__experience = experience
        self.__completed_projects = completed_projects

    def get_name(self):
        return f'Имя: {self.__name}'

    def get_position(self):
        return f'Должность {self.__name} : {self.__position}'

    def get_department(self):
        return f'Отдел работника {self.__name} - {self.__department}'

    def get_salary(self):
        return f'Зарплата сотрудника {self.__name} - {self.__salary}'

    def get_experience(self):
        return f'Стаж работы сотрудника {self.__name} - {self.__experience}'

    def get_completed_projects(self):
        return f"Законченные проекты >>>> {'\n'.join(str(project) for project in self.__completed_projects)}"

    def set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError
        else:
            self.__name = name
            print(f'Имя изменено на {self.__name}')

    def set_position(self, position: str):
        if not isinstance(position, str):
            raise TypeError
        else:
            self.__position = position
            print(f'Должность изменена на {self.__position}')

    def set_department(self, department: str):
        if not isinstance(department, str):
            raise TypeError
        else:
            self.__department = department
            print(f'Отдел сменен на {self.__department} ')

    def set_salary(self, salary: float):
        if not isinstance(salary, float):
            raise TypeError
        else:
            self.__salary = salary
            print(f'Зарплата теперь {salary} такая вот ')

    def set_experience(self, experience: int):
        if not isinstance(experience, int):
            raise TypeError
        else:
            self.__experience = experience
            print(f'Стаж изменен на {self.__experience}')

    def add_project(self, project: str):
        self.__completed_projects.append(project)

    def remove_project(self, project: str):
        if project in self.__completed_projects:
            self.__completed_projects.remove(project)
        else:
            print(f"Проект '{project}' отсутствует в списке выполненных проектов.")

    def increase_salary(self, percent: float):
        self.__salary *= (1 + percent / 100)

    def __str__(self):
        return f"""
                 Имя: {self.__name}
                 Должность: {self.__position}
                 Отдел: {self.__department}
                 Зарплата: {self.__salary}
                 Стаж работы: {self.__experience} лет
                 Выполненные проекты: {', '.join(self.__completed_projects)}
                """


class Robot:
#####################я три класса сделал с print в гетах,чет я как то не понимаю,а нужны ли они вообще))##########
    def __init__(self, serial_number: str, model: str, current_task: str = None, battery_level: int = 100, state: str = "на перерыве"):
        self.__serial_number = serial_number
        self.__model = model
        self.__current_task = current_task
        self.__battery_level = battery_level
        self.__state = state

    def get_serial_number(self):
        return self.__serial_number

    def get_model(self):
        return self.__model

    def get_current_task(self):
        return self.__current_task

    def get_battery_level(self):
        return self.__battery_level

    def get_state(self):
        return self.__state

    def set_serial_number(self, serial_number: str):
        if not isinstance(serial_number, str):
            raise TypeError
        else:
            self.__serial_number = serial_number

    def set_model(self, model: str):
        if not isinstance(model, str):
            raise TypeError
        else:
            self.__model = model

    def set_current_task(self, current_task: str):
        if not isinstance(current_task, str):
            raise TypeError
        else:
            self.__current_task = current_task

    def set_battery_level(self, battery_level: int):
        if not isinstance(battery_level, int):
            raise TypeError
        else:
            self.__battery_level = battery_level

    def set_state(self, state: str):
        if not isinstance(state, str):
            raise TypeError
        else:
            self.__state = state

    def assign_task(self, task: str):
        self.__current_task = task
        print(f"Роботу {self.__serial_number} назначена задача: {task}")

    def change_battery_level(self, level: int):
        self.__battery_level += level
        print(f"Уровень заряда батареи робота {self.__serial_number} изменен на {level}. Текущий уровень: {self.__battery_level}%")

    def start_working(self):
        if self.__state == "на перерыве":
            self.__state = "в работе"
            print(f"Робот {self.__serial_number} приступил к работе.")
        else:
            print(f"Робот {self.__serial_number} уже в работе.")

    def take_break(self):
        if self.__state == "в работе":
            self.__state = "на перерыве"
            print(f"Робот {self.__serial_number} взял перерыв.")
        else:
            print(f"Робот {self.__serial_number} уже на перерыве.")

    def __str__(self):
        return f"""
                 Серийный номер: {self.__serial_number}
                 Модель: {self.__model}
                 Текущая задача: {self.__current_task}
                 Уровень заряда батареи: {self.__battery_level}%
                 Состояние: {self.__state}
                """


class Achievement:
    def __init__(self, competition: str, year: int, result: str):
        self.competition = competition
        self.year = year
        self.result = result

    def __str__(self):
        return f"{self.competition} ({self.year}): {self.result}"


class Athlete:
    def __init__(self, name: str, age: int, sport: str, achievements: list = [], status: str = "активен"):
        self.__name = name
        self.__age = age
        self.__sport = sport
        self.__achievements = achievements
        self.__status = status

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_sport(self):
        return self.__sport

    def get_achievements(self):
        return self.__achievements

    def get_status(self):
        return self.__status

    def set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError
        else:
            self.__name = name

    def set_age(self, age: int):
        if not isinstance(age, int):
            raise TypeError
        else:
            self.__age = age

    def set_sport(self, sport: str):
        if not isinstance(sport, str):
            raise TypeError
        else:
            self.__sport = sport

    def set_status(self, status: str):
        if not isinstance(status, str):
            raise TypeError
        else:
            self.__status = status

    def add_achievement(self, achievement: Achievement):
        self.__achievements.append(achievement)
        print(f"Достижение '{achievement.competition}' добавлено в список атлета '{self.__name}'.")

    def remove_achievement(self, achievement: Achievement):
        if achievement in self.__achievements:
            self.__achievements.remove(achievement)
            print(f"Достижение '{achievement.competition}' удалено из списка атлета '{self.__name}'.")
        else:
            print(f"Достижение '{achievement.competition}' отсутствует в списке атлета '{self.__name}'.")

    def __str__(self):
        achievement_str = "\n".join(str(achievement) for achievement in self.__achievements)
        return f"""
                 Имя: {self.__name}
                 Возраст: {self.__age}
                 Вид спорта: {self.__sport}
                 Достижения:\n{achievement_str if achievement_str else 'Нет достижений'}
                 Статус: {self.__status}
                """

class Program:

    @staticmethod
    def main():
####################################################ЗАДАНИЕ 1(и 1.2)####################################################
#####################################################ТАНЯ_ГРОТТЕР#######################################################

        new_wizard = Wizard('Никитос Пылесос', 'Нормальный-такой', 666, [], 'В Хогвартсе')
        bird_tornado = Spell('Птичья буря',5, 'Наносит урон', 'Вихрь состояший из тысяч птиц начинает кружить вокруг цели,нанося урон ценой жизни')
        healing_leaf = Spell('Лечащий лист', 3, 'Лечение', 'Призывает с близжайшей обочины лист подорожника,вроде лечит даже')

#############GET_методы объекта класса Wizard###########################################################################

        new_wizard.get_name()
        new_wizard.get_status()
        new_wizard.get_spellbook()
        new_wizard.get_faculty()
        new_wizard.get_spellforce()

############SET_методы объекта класса Wizard############################################################################

        status = 'Выпущен'
        new_wizard.set_status(status)
        faculty = 'Другой, но тоже ничего такой,пойдет'
        new_wizard.set_faculty(faculty)

##########OTHER_методы объекта класса Wizard############################################################################

        new_wizard.add_spell(bird_tornado)
        new_wizard.add_spell(healing_leaf)
        new_wizard.get_spellbook()
        new_wizard.remove_spell(bird_tornado)
        spelforce = 4
        new_wizard.increase_spellforce(spelforce)
        print(new_wizard)

#################################################АБРАКАДАБРА############################################################
###########GET_методы объекта класаса SPELL#############################################################################

        bird_tornado.get_name()
        bird_tornado.get_type()
        bird_tornado.get_difficult()
        bird_tornado.get_description()

###########SET_методы объекта класса SPELL##############################################################################

        print(bird_tornado) #Типа шо было вначале
        new_name = 'Ледяной_дождь_из_нарвалов'
        bird_tornado.set_name(new_name)
        new_type = 'BFG9000_Только_дебафф'
        bird_tornado.set_type(new_type)
        new_diff = 7
        bird_tornado.set_difficult(new_diff)
        new_desc = 'Сверху падает рыба,больно,но не смертельно'
        bird_tornado.set_description(new_desc)
        print(bird_tornado) #И конечные изменения
########################################################################################################################
###########################################ЗЛОЕ_КОЛДУНСТВО ЗАКОНЧИЛОСЬ##################################################
##################################################ЗАДАНИЕ 2#############################################################

        new_employeeee = Employee('Никитос Пылесос', 'fullstack-junior-developer', 'Батальон белые носки', 80000.00, 1, [])
        project = 'Похоронные qr-коды'

###################GET_методы объекта класса EMPLOYEER##################################################################

        new_employeeee.get_name()
        new_employeeee.get_salary()
        new_employeeee.get_position()
        new_employeeee.get_department()
        new_employeeee.get_experience()
        new_employeeee.get_completed_projects()

###################SET_методы объекта класса EMPLOYEER##################################################################


        print(new_employeeee)
        name = 'Никитос Антипос'
        new_employeeee.set_name(name)
        zarplata = 60000.01
        new_employeeee.set_salary(zarplata)
        pos = 'Тыжпрограмист'
        new_employeeee.set_position(pos)
        exp = 3
        new_employeeee.set_experience(exp)
        dep = 'Темная сторона серверной комнаты'
        new_employeeee.set_department(dep)
        print(new_employeeee)

##################OTHER_методы объекта класса EMPLOYEER#################################################################

        new_employeeee.add_project(project)
        new_employeeee.remove_project(project)
        mnogo_denyak = 3000
        new_employeeee.increase_salary(mnogo_denyak)

###################################################КОНЕЦ_ЗАДАНИЯ 2######################################################
###################################################ЗАДАНИЕ 3############################################################

        robot = Robot('TM102', '404')

        print(robot)

        robot.assign_task('Запокемонить вон ту штуку')

        robot.change_battery_level(-20)

        robot.start_working()

        print(robot)

        robot.take_break()
####################################################КОНЕЦ_ЗАДАНИЯ 3#####################################################
###################################################ЗАДАНИЕ 4############################################################

        achivka = Achievement("Чемпионат нижних Сатанинок", 2022, "Золотая медаль")
        kachok_nosok = Athlete("ВсеТотЖе Никитос", 25, "Водное поло", [achivka])

        print(kachok_nosok)

        achivka2 = Achievement("Паралимпийские игры", 2024, "Шоколадная медаль")

        kachok_nosok.add_achievement(achivka2)

        kachok_nosok.remove_achievement(achivka2)

        print(kachok_nosok)













Program.main()





