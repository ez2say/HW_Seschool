# class Animal():
#     def __init__(self,name,species,age):
#         self.name = name
#         self.species = species
#         self.age = age
#
#     def make_sound(self):
#         if self.species == 'собака':
#             return 'woof woof woof woof'
#         elif self.species == 'кошка':
#             return 'meow meow'
#         elif self.species == 'т1000':
#             return 'bib blop kill the human'
#         else:
#             return 'Unknown sound'
#
#     def info(self):
#         print(f"""
#                 Имя: {self.name}
#                 Вид: {self.species}
#                 Возраст: {self.age}
#                 """)
#
#
# animal_name = input('Введите имя: ')
# animal_species = input('Введите тип животного: ')
# animal_age = int(input('Введите сколько лет:'))
#
# animal = Animal(animal_name,animal_species,animal_age)
#
# while True:
#     chs = int(input('Введите что вы хотите знать'
#                 '\n 1. Информацию о животном'
#                 '\n 2.ЗВУКИ ЖИВОТНЫХ(одного)'
#                 '\n 3.Стоп'
#                 '\n>>> '))
#     if chs == 1:
#         print(animal.info())
#     elif chs == 2:
#         print(animal.make_sound())
#     elif chs == 3:
#         break
#     else:
#         print('ЛИБО 1 ЛИБО 2 либо на худой конец 3')
#         continue
#====================================================================================================
class Book():
    def __init__(self, title, author,num_page):
        self.title = title
        self.author = author
        self.num_page = num_page

    def open(self,page):
        if page <= self.num_page:
            print(f'Страница {page} открыта')
        else:
            print('В этой книге нет такой страницы')

    def info(self):
        print(f"""
                Название: {self.title}
                Автор: {self.author}
                Количество страниц: {self.num_page}                
                """)



title = input('Введите название книги: ')
author = input('Введите автора книги: ')
num = int(input('Введите количество страниц: '))

new_book = Book(title,author,num)

while True:
    chs = int(input('Введите(цифру),что бы вы хотели сделать'
                    '\n[1]Открыть определенную страницу страницу'
                    '\n[2]Показать информацию о книге'
                    '\n[3]Выход '
                    '\n>>> '))
    while chs == 1:
        page = int(input('Введите номер страницы или 110011 для возврата в предыдущее меню:'))
        new_book.open(page)
        if page == 110011:
            break
    if chs == 2:
        new_book.info()
    elif chs == 3:
        print('Досвидули')
        break
    else:
        print('Нормально вводи')

