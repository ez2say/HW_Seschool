from __future__ import annotations

import random


class HogwartsStudent:
    def __init__(self, name: str, house: str, mana: int = 100, spellbook: list = None, is_paralyzed=False, turns_paralyzed=0):
        self.__name = name
        self.__house = house
        self.__mana = mana
        self.__spellbook = spellbook
        self.__is_paralyzed = is_paralyzed
        self.__turns_paralyzed = turns_paralyzed

    def get_name(self):
        return self.__name

    def get_house(self):
        return self.__house

    def get_mana(self):
        return self.__mana

    def get_spellbook(self):
        return self.__spellbook

    def is_paralyzed(self):
        return self.__is_paralyzed

    def set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError
        else:
            self.__name = name

    def set_house(self, house: str):
        if not isinstance(house, str):
            raise TypeError
        else:
            self.__house = house

    def set_mana(self, mana: int):
        if not isinstance(mana, int):
            raise TypeError
        else:
            self.__mana = mana

    def set_paralyzed(self, is_paralyzed: bool):
        self.__is_paralyzed = is_paralyzed

    def set_paralyzed_turns(self,turns: int):
        if not isinstance(turns, int):
            raise TypeError
        else:
            self.__turns_paralyzed = turns
    def reduce_paralyzed_turns(self):
        if self.__turns_paralyzed > 0:
            self.__turns_paralyzed -= 1
            if self.__turns_paralyzed == 0:
                self.__is_paralyzed = False

    def learn_spell(self,spell: Spell):
        if not isinstance(spell, Spell):
            raise TypeError
        else:
            self.__spellbook.append(spell)

    def cast_spell(self, target: HogwartsStudent):
        if self.__mana > 0 and not self.__is_paralyzed:
            if self.__spellbook:
                spell = random.choice(self.__spellbook)
                if self.__mana >= spell.get_mana_cost():
                    print(f'{self.__name} использовал заклинание {spell.get_title()}')
                    spell.cast_spell(self,target)
                    self.__mana -= spell.get_mana_cost()
                else:
                    print(f'{self.__name} не хватает маны для заклинания {spell.get_title()}')
            else:
                print(f'{self.__name} не знает ни одного заклинания')
        elif self.__is_paralyzed:
            print(f'{self.__name} парализован ')
        else:
            print(f'{self.__name} не хватает маны')

    def __str__(self):
        return f"""
                Имя: {self.__name}
                Факультет: {self.__house}
                Количество маны: {self.__mana}
                Заклинания >>>>
                {'\n'.join([str(spell) for spell in self.__spellbook])}
                """


class Spell:
    def __init__(self, title: str, description: str, mana_cost: int):
        self.__title = title
        self.__description = description
        self.__mana_cost = mana_cost

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_mana_cost(self):
        return self.__mana_cost

    def set_title(self, title: str):
        if not isinstance(title, str):
            raise TypeError
        else:
            self.__title = title

    def set_description(self, description: str):
        if not isinstance(description, str):
            raise TypeError
        else:
            self.__description = description

    def set_mana_cost(self, mana_cost: int):
        if not isinstance(mana_cost, int):
            raise TypeError
        else:
            self.__mana_cost = mana_cost

    def cast_spell(self, caster:HogwartsStudent, target: HogwartsStudent):
        if self.__title == 'Expeliarmus':
            target.set_paralyzed(True)
            print(f'{target.get_name()} обезоружен,он пропускает ход')
        elif self.__title == 'Stupefy':
            target.set_paralyzed(True)
            print(f'{target.get_name()} оглушен,он пропускает ход')
        elif self.__title == 'Avada Kedavra':
            target.set_mana(0)
            print(f'{target.get_name()} умер')
        elif self.__title == 'Protego':
            print(f'{caster.get_name()} отразил заклинание защитным щитом')
        elif self.__title == 'Petrificus Totalus':
            target.set_paralyzed(True)
            target.set_paralyzed_turns(2)
            print(f'{target.get_name()} парализован на два хода')
        elif self.__title == 'Lumos':
            print(f'{caster.get_name()} посветил в лицо {target.get_name()}')
        elif self.__title == "Expecto Patronum":
            print(f"{caster.get_name()} призвал(а) патронуса для защиты!")


    def __str__(self):
        return f"""
                Название: {self.__name}
                Эффект: {self.__description}
                Стоимость маны: {self.__mana_cost}
                """


class Hogwarts:
    def __init__(self, students: list , spells: list ):
        self.__students = students
        self.__spells = spells

    def get_students(self):
        return self.__students

    def get_spells(self):
        return self.__spells

    def enroll_student(self, student: HogwartsStudent):
        self.__students.append(student)

    def teach_spell(self, spell: Spell):
        self.__spells.append(spell)

    def simulate_duel(self, student1: HogwartsStudent, student2: HogwartsStudent):
        print(f"\n--- Дуэль между {student1.get_name()} из {student1.get_house()} и {student2.get_name()} из {student2.get_house()} ---")

        turn = 1

        while student1.get_mana() > 0 and student2.get_mana() > 0:
            print(f'{turn}й раунд!')

            student1.reduce_paralyzed_turns()
            student2.reduce_paralyzed_turns()

            if not student1.is_paralyzed():
                student1.cast_spell(student2)
            if not student2.is_paralyzed():
                student2.cast_spell(student1)

            if student1.get_mana() <= 0:
                print(f'Победил {student2.get_name()} !')
                break
            elif student2.get_mana() <= 0:
                print(f'Победил {student1.get_name()} !')
                break

            turn += 1

        print(f"\n--- Конец дуэли ---\n")



class Program:
    @staticmethod
    def main():
        Expelliarmus = Spell('Expelliarmus', 'Дизармирование противника на один ход', 10)
        Stupefy = Spell('Stupefy','Оглушение противника на один ход', 30)
        Avada_Kedavra = Spell('Avada Kedavra', 'Ваншот', 80)
        Protego = Spell('Protego', 'Отражает заклинания', 15)
        Petrificus_Totalus = Spell('Petrificus Totalus', 'Паралич на два хода', 20)
        Lumos = Spell('Lumos','Фонариком в глаз,урона нет', 5)
        Expecto_Patronum = Spell('Expecto Patronum', 'Вызывает тотемное животное,бесполезно против людей,мастхев против дементоров',50)

        student1 = HogwartsStudent('Никитос Пылесос', 'пуффенДуй',100,[])
        student2 = HogwartsStudent('Ноунейм Лохов', 'слизерин',100, [])

        hogwarts = Hogwarts([student1,student2],[Expelliarmus, Stupefy, Avada_Kedavra, Protego, Petrificus_Totalus, Lumos, Expecto_Patronum])

        student1.learn_spell(Expelliarmus)
        student2.learn_spell(Expelliarmus)
        student1.learn_spell(Stupefy)
        student2.learn_spell(Stupefy)
        student1.learn_spell(Avada_Kedavra)
        student2.learn_spell(Avada_Kedavra)
        student1.learn_spell(Protego)
        student2.learn_spell(Protego)
        student1.learn_spell(Expecto_Patronum)
        student2.learn_spell(Lumos)

        hogwarts.simulate_duel(student1,student2)


Program.main()






