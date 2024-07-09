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
#
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


    def play(self,track:str):
        if track in self.track_list:
            print(f'Вы выбрали произведение {track} исполнителя {self.artist}')
            print(f'дждждж--оууууууууууууооаоаа-звуки_воспроизведения----пшш'
                f'\nвжж---играет трек {track}--вжжжж')
        else:
            print('Трек не найден')
#[---------------------------------------------------------------------------------------------------------------------]
class Program:
    @staticmethod
    def main():
####################################################Задание_1##########################################
        animal_name = input('Введите имя: ')
        animal_species = input('Введите тип животного: ')
        animal_age = int(input('Введите сколько лет:'))

        animal = Animal(animal_name, animal_species, animal_age)

        while True:
            chs = int(input('Введите что вы хотите знать'
                            '\n 1. Информацию о животном'
                            '\n 2.ЗВУКИ ЖИВОТНЫХ(одного)'
                            '\n 3.Стоп'
                            '\n>>> '))
            if chs == 1:
                print(animal.info())
            elif chs == 2:
                print(animal.make_sound())
            elif chs == 3:
                break
            else:
                print('ЛИБО 1 ЛИБО 2 либо на худой конец 3')
                continue
################################################Конец_задания_1#########################################################
###############################################Задание_2################################################################
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
############################################Конец_задания_2#############################################################
############################################Задание_3###################################################################
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
        #         airplane.takeoff()
        #     elif chs == 3:
        #         airplane.takedown()
        #     elif chs == 4:
        #         break
##########################################Конец_задания_3###############################################################
##########################################Задание_4####################################################################
        # artist = input('Введите исполнителя: ')
        # title = input('Введите альбом: ')
        # genre = input('Введите жанр: ')
        #
        # music = MusicAlbum(artist, title, genre)
        #
        # while True:
        #     chs = int(input('Введите цифру для продолжения:'
        #                     '\n[1]Информация музыкальном альбоме'
        #                     '\n[2]Добавить трек'
        #                     '\n[3]Удалить трек'
        #                     '\n[4]Воспроизвести трек'
        #                     '\n[5]Выход'
        #                     '\n>>> '))
        #     if chs == 1:
        #         music.info()
        #     if chs == 2:
        #         name = input('Введите название трека,который нужно добавить: ')
        #         music.add_track(name)
        #     if chs == 3:
        #         name = input('Введите название трека,который нужно удалить: ')
        #         if name in music.track_list:
        #             music.delete_track(name)
        #         else:
        #             print('Такого трека тут и нет')
        #     if chs == 4:
        #         name = input('Введите трек для воспроизведения: '
        #                      f'\nCписок треков({music.track_list})'
        #                      f'\n>>>')
        #         music.play(name)
        #     if chs == 5:
        #         break
#############################################################Конец_заданания_4##########################################

Program.main()



