#Task_1
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
# #Task_2
# class Book():
#     def __init__(self, title, author,num_page):
#         self.title = title
#         self.author = author
#         self.num_page = num_page
#
#     def open(self,page:int):
#         if page <= self.num_page:
#             print(f'Страница {page} открыта')
#         else:
#             print('В этой книге нет такой страницы')
#
#     def info(self):
#         print(f"""
#                 Название: {self.title}
#                 Автор: {self.author}
#                 Количество страниц: {self.num_page}
#                 """)
#
#
#
# title = input('Введите название книги: ')
# author = input('Введите автора книги: ')
# num = int(input('Введите количество страниц: '))
#
# new_book = Book(title,author,num)
#
# while True:
#     chs = int(input('Введите(цифру),что бы вы хотели сделать'
#                     '\n[1]Открыть определенную страницу страницу'
#                     '\n[2]Показать информацию о книге'
#                     '\n[3]Выход '
#                     '\n>>> '))
#     while chs == 1:
#         page = int(input('Введите номер страницы или 110011 для возврата в предыдущее меню:'))
#         new_book.open(page)
#         if page == 110011:
#             break
#     if chs == 2:
#         new_book.info()
#     elif chs == 3:
#         print('Досвидули')
#         break
#     else:
#         print('Нормально вводи')
# ================================================================================================
#Task_3
# class PassengerPlane():
#     def __init__(self, manufacturer, model, capacity,height=0,speed=0):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.capacity = capacity
#         self.height = height
#         self.speed = speed
#
#     def info(self):
#         print(f"""
#                 Производитель: {self.manufacturer}
#                 Модель самолета: {self.model}
#                 Вместимость самолета: {self.capacity}
#         """)
#
#     def takeoff(self):
#         print('Самолет взлетел!')
#
#     def takedown(self):
#         print('Самолет приземлился!')
#
#     def change_height(self,height:int):
#         self.height = height
#         print(f'Самолет поднялся на {self.height} км')
#
#     def change_speed(self,speed:float):
#         self.speed = speed
#         print(f'Скорость самолета {self.speed} км/ч')
#
#
# manufacturer = input('Введите производителя: ')
# model = input('Введите модель: ')
# capacity = input('Введите вместимость самолета: ')
#
# airplane = PassengerPlane(manufacturer, model, capacity)
#
# while True:
#     chs = int(input('Введите цифру для продолжения:'
#                     '\n[1]Информация о самолете'
#                     '\n[2]Взлететь'
#                     '\n[3]Посадить самолет'
#                     '\n[4]Выход'
#                     '\n>>> '))
#     if chs == 1:
#         airplane.info()
#     elif chs == 2:
#         print('Для того чтобы самолет взлетел нужно набрать скорость и высоту')
#         speed = float(input('Введите скорость самолета: '))
#         hght = int(input('Введите высоту: '))
#         airplane.takeoff()
#         airplane.change_height(hght)
#         airplane.change_speed(speed)
#     elif chs == 3:
#         if airplane.speed != 0 and airplane.height != 0:
#             print('Для того,чтобы посадить самолет нужно снизить скорость и высоту до нуля')
#             speed = float(input('Введите скорость самолета: '))
#             hght = int(input('Введите высоту'))
#             if speed == 0 and hght == 0:
#                 airplane.takedown()
#         else:
#             print('Самолет и так не летит')
#===============================================================================================
#Task_4

class MusicAlbum():
    def __init__(self, artist, album_title, genre):
        self.artist = artist
        self.album_title = album_title
        self.genre = genre
        self.track_list = []

    def info(self):
        print(f"""
                Исполнитель: {self.artist}
                Название альбома: {self.album_title}
                Жанр: {self.genre}
                Список произведений: {self.track_list}
                """)

    def add_track(self, track:str):
        self.track_list.append(track)
        print(f'Вы добавили {track} в список произведений данного исполнителя')
        print(f'Теперь список состоит из {self.track_list}')

    def delete_track(self,track:str):
        self.track_list.remove(track)
        print(f'Вы удалили {track} из списка произведений данного исполнителя')
        print(f'Теперь список состоит из {self.track_list}')




artist = input('Введите исполнителя: ')
title = input('Введите альбом: ')
genre = input('Введите жанр: ')

music = MusicAlbum(artist, title, genre)

while True:
    chs = int(input('Введите цифру для продолжения:'
                    '\n[1]Информация музыкальном альбоме'
                    '\n[2]Добавить трек'
                    '\n[3]Удалить трек'
                    '\n[4]Воспроизвести трек'
                    '\n[4]Выход'
                    '\n>>> '))
    if chs == 1:
        music.info()
    if chs == 2:
        name = input('Введите название трека,который нужно добавить: ')
        music.add_track(name)
    if chs == 3:
        name = input('Введите название трека,который нужно удалить: ')
        if name in music.track_list:
            music.delete_track(name)
        else:
            print('Такого трека тут и нет')




