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

    def add_spell(self, spell):
        self.__spellbook.append(spell)
        print(f'Заклинание {spell.__name} добавлено')

    def remove_spell(self, spell):
        self.__spellbook.remove(spell)
        print(f'Заклинание {spell.__name} удалено из списка заклинаний.')

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
###################################################ЗАДАНИЕ 3###########################################################












Program.main()





