class Student:
    def __init__(self, name: str, surname: str, age: int, average_grade: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def get_average_grade(self):
        return self.average_grade

    def set_name(self, name: str):
        self.name = name

    def set_surname(self, surname: str):
        self.surname = surname

    def set_age(self, age: int):
        self.age = age

    def set_average_grade(self, average_grade: float):
        self.average_grade = average_grade

    def __str__(self):
        return f"""
                Студент: {self.name} {self.surname} 
                Возраст: {self.age} 
                Средний балл: {self.average_grade}
                """

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade == other.average_grade
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade < other.average_grade
        return False

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade > other.average_grade
        return False

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade <= other.average_grade
        return False

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_grade >= other.average_grade
        return False

class Program:
    @staticmethod
    def main():
        first_stud = Student('Студент','Студентов', 18, 4.5)
        sec_stud = Student('Не_студент', 'Не_студентов', 19, 4.1)

        print(first_stud == sec_stud)
        print(first_stud > sec_stud)
        print(first_stud <= sec_stud)
        print(first_stud)


Program.main()