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
        return f"Заклинания: {'\n'.join(str(spell) for spell in self._spellbook)}"

    def get_status(self):
        return f'Статус волшебника {self._name} >>> {self._status}'

    def set_faculty(self, faculty:str):
        if not isinstance(faculty,str):
            raise TypeError
        else:
            self._faculty = faculty
            print(f'Факультет сменён на: {self._faculty}')

    def set_spellforce(self, spellforce:int):
        if not isinstance(spellforce,int):
            raise TypeError
        else:
            if not spellforce >= 0:
                raise ValueError
            else:
                self._spellforce = spellforce
                print(f'Теперь сила волшебника: {self._spellforce}')

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
        if not amount >= 0:
            raise ValueError
        else:
            self._spellforce = amount
            print(f'Сила заклинаний теперь: {self._spellforce}')

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
        while True:
            chs_first = int(input('[1]Действия с объектом класса волшебником'
                                  '\n[2]Действия с объектом класса заклинаний'))
            if chs_first == 1:
                chs = int(input('[1]<<< Узнать имя волшебника'
                                '\n[2]<<< Узнать факультет волшебника'
                                '\n[3]<<< Узнать уровень магической силы волшебника'
                                '\n[4]<<< Показать список заклинаний волшебника'
                                '\n[5]<<< Показать статус волшебника'
                                '\n[6]<<< FULL_INFO'
                                '\n>>> '))
                if chs == 1:
                    print(new_wizard.get_name())
                elif chs == 2:
                    print(new_wizard.get_faculty())
                    while True:
                        chs_faculty = int(input('[1]Изменить факультет'
                                             '\n[2]Назад'
                                             '\n>>> '))
                        if chs_faculty == 1:
                            faculty = input('Введите название факультета: ')
                            new_wizard.set_faculty(faculty)
                        elif chs_faculty == 2:
                            break
                        else:
                            raise ValueError
                elif chs == 3:
                    print(new_wizard.get_spellforce())
                    while True:
                        chs_force = int(input('[1]Изменить силу волшебника'
                                              '[2]\nНазад'
                                              '\n>>>'))
                        if chs_force == 1:
                            spellforce = int(input('Введите новое значение силы: '))
                            new_wizard.set_spellforce(spellforce)
                        elif chs_force == 2:
                            break
                        else:
                            raise ValueError or TypeError
                elif chs == 4:
                    print(new_wizard.get_spellbook())
                    while True:
                        chs_spell = int(input('[1]Добавить заклинание'
                                              '\n[2]Удалить заклинание'
                                              '\n[3]Назад'
                                              '\n>>> '))
                        if chs_spell == 1:
                            spell = input('Какое заклинание добавить [Птичья буря, Лечащий лист]: ')
                            if spell == 'Птичья буря':
                                new_wizard.add_spell(bird_tornado)
                            elif spell == 'Лечащий лист':
                                new_wizard.add_spell(healing_leaf)
                            else:
                                raise ValueError
                        elif chs_spell == 2:
                            spell = str(input(f'Какое заклинание удалить:  {new_wizard.get_spellbook()}'))
                            if spell == 'Птичья буря':
                                new_wizard.remove_spell(bird_tornado)
                            elif spell == 'Лечащий лист':
                                new_wizard.remove_spell(healing_leaf)
                            else:
                                raise ValueError
                        else:
                            break
                elif chs == 5:
                    print(new_wizard.get_status())
                    chs_status = int(input('[1]Сменить статус'
                                           '\n[2]Назад'
                                           '\n>>>'))
                    while True:
                        if chs_status == 1:
                            status = input('Введите новый статус(В Хогвартсе/Выпущен):'
                                               '\n>>> ')
                            new_wizard.set_status(status)
                            break
                        elif chs_status == 2:
                            break
                        else:
                            continue
                elif chs == 6:
                    print(new_wizard)
                else:
                    raise ValueError or TypeError
            elif chs_first == 2:
                chs_spells = int(input('[1]'))



Program.main()





