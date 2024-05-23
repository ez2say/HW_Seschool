class Spell:
    def __init__(self,name:str,difficult:int, type:str, description:str):
        self._name = name
        self._difficult = difficult
        self._type = type
        self._description = description

    def get_name(self):
        return f'Название заклинания: {self._name}'

    def get_difficult(self):
        return f'Сложность заклинания: {self._difficult}'

    def get_type(self):
        return f'Тип заклинания {self._type}'

    def get_description(self):
        return (f'Заклинание --*{self._name}*-- имеет эффект :'
                f'\n{self._description}')

    def set_name(self,new_name:str):
        if not isinstance(new_name, str):
            raise TypeError
        else:
            self._name = new_name
            print(f'Название заклинания сменено на {self._name}')

    def set_difficult(self, new_dfficult:int):
        if not isinstance(new_dfficult, int):
            raise TypeError
        else:
            if new_dfficult >= 1 and new_dfficult <= 10:
                self._difficult = new_dfficult
                print(f'Сложность заклинания {self._name} изменена на {self._difficult}')
            else:
                raise ValueError

    def set_type(self, new_type:str):
        if not isinstance(new_type, str):
            raise TypeError
        else:
            self._type = new_type
            print(f'Тип заклинания {self._name} изменен на {self._type}')

    def set_description(self, new_desc:str):
        if not isinstance(new_desc, str):
            raise TypeError
        else:
            self._description = new_desc
            print(f'Теперь описание способности {self._name} -->'
                  f'\n{self._description}')

    def __str__(self):
        return f"""
                Название: {self._name}
                Сложность:{self._difficult}
                Тип заклинания: {self._type}
                Описание заклинания: {self._description}
                """


class Wizard:
    def __init__(self, name:str, faculty:str, spellforce:int, spells:list = None, status:str = 'В Хогвартсе'):
        self._name = name
        self._faculty = faculty
        self._spellforce = spellforce
        self._spellbook = spells
        self._status = status

    def get_name(self):
        return f'Имя волшебника >>>  {self._name}'

    def get_faculty(self):
        return f'Факультет волшебника {self._name} >>> {self._faculty}'

    def get_spellforce(self):
        return f'Уровень магической силы у волшебника {self._name} >>> {self._spellforce}'

    def get_spellbook(self):
        return f"Заклинания>>>> {'\n'.join(str(spell) for spell in self._spellbook)}"

    def get_status(self):
        return f'Статус волшебника {self._name} >>> {self._status}'

    def set_faculty(self, faculty:str):
        if not isinstance(faculty,str):
            raise TypeError
        else:
            self._faculty = faculty
            print(f'Факультет сменён на: {self._faculty}')


    def set_status(self, status:str):
        self._status = status
        print(f'Статус изменен на: {self._status}')

    def add_spell(self,spell):
        self._spellbook.append(spell)
        print(f'Заклинание {spell._name} добавлено')

    def remove_spell(self,spell):
        self._spellbook.remove(spell)
        print(f'Заклинание {spell._name} удалено из списка заклинаний.')

    def increase_spellforce(self, amount:int):
        if not isinstance(amount, int):
            raise TypeError
        else:
            if not amount >= 0:
                raise ValueError
            else:
                self._spellforce = amount
                print(f'Теперь сила волшебника: {self._spellforce}')

    def __str__(self):
        return f"""
                Имя: {self._name}
                Факультет: {self._faculty}
                Уровень магической силы: {self._spellforce}
                Заклинания:{'\n'.join(str(spell) for spell in self._spellbook)}
                Статус: {self._status}"
                
               """

class Program:

    @staticmethod
    def main():
#####################################################ТАНЯ_ГРОТТЕР#######################################################

        new_wizard = Wizard('Никитос Пылесос', 'Нормальный-такой', 666, [], 'В Хогвартсе')
        bird_tornado = Spell('Птичья буря',5, 'Наносит урон', 'Вихрь состояший из тысяч птиц начинает кружить вокруг цели,нанося урон ценой жизни')
        healing_leaf = Spell('Лечащий лист', 3, 'Лечение', 'Призывает с близжайшей обочины лист подорожника,вроде лечит даже')

#############GET_методы объекта класса Wizard########################################################################

        new_wizard.get_name()
        new_wizard.get_status()
        new_wizard.get_spellbook()
        new_wizard.get_faculty()
        new_wizard.get_spellforce()

############SET_методы объекта класса Wizard#########################################################################

        status = 'Выпущен'
        new_wizard.set_status(status)
        faculty = 'Другой, но тоже ничего такой,пойдет'
        new_wizard.set_faculty(faculty)

##########OTHER_методы объекта класса Wizard##########################################################################

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
###########################################ЗЛОЕ_КОЛДУНСТВО ЗАКОНЧИЛОСЬ#################################################









Program.main()





