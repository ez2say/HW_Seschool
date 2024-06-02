class Library:
    def __init__(self, name: str, address: str, books: list = None , employees: list = None):
        self.__name = name
        self.__address = address
        self.__books = books
        self.__employees = employees

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_books(self):
        return self.__books

    def get_employees(self):
        return self.__employees

    def set_address(self, address: str):
        self.__address = address

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book):
        if book in self.__books:
            self.__books.remove(book)
        else:
            print(f"Книга '{book.get_title()}' отсутствует в библиотеке.")

    def add_employee(self, employee):
        self.__employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.__employees:
            self.__employees.remove(employee)
        else:
            print(f"Сотрудник '{employee.get_name()}' отсутствует в библиотеке.")

    def __str__(self):
        return f"""
                Название: {self.__name}
                Адрес: {self.__address}
                Книги: {'\n '.join(str(book) for book in self.__books)}
                Сотрудники: {'\n '.join(str(employee) for employee in self.__employees)}
                """

class Book:
    def __init__(self, title: str, author: str, year: int, id: int, genres: list = None):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__id = id
        self.__genres = genres

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def get_id(self):
        return self.__id

    def get_genres(self):
        return self.__genres

    def set_year(self, year:int):
        if not isinstance(year, int):
            raise TypeError
        else:
            self.__year = year

    def add_genre(self,genre):
        self.__genres.append(genre)

    def remove_genre(self, genre):
        if genre in self.__genres:
            self.__genres.remove(genre)
        else:
            print(f'{genre} нет в списке жанров')

    def __str__(self):
        return f"""
                Название: {self.__title}
                Автор: {self.__author}
                Год издания: {self.__year}
                ID: {self.__id}
                Жанры: {'\n'.join([genre.get_name() for genre in self.__genres])}
                """

class Employee:
    def __init__(self, name: str, position: str, id: int, contact_info: list = None):
        self.__name = name
        self.__position = position
        self.__id = id
        self.__contact_info = contact_info

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_id(self):
        return self.__id

    def get_contact_info(self):
        return self.__contact_info

    def set_position(self, position: str):
        self.__position = position

    def add_contact_info(self, contact_info):
        self.__contact_info.append(contact_info)

    def remove_contact_info(self, contact_info):
        if contact_info in self.__contact_info:
            self.__contact_info.remove(contact_info)
        else:
            print(f"Контактная информация '{contact_info.get_type()}: {contact_info.get_value()}' отсутствует у сотрудника '{self.__name}'.")

    def __str__(self):
        return f"""
                Имя: {self.__name}
                Должность: {self.__position}
                ID: {self.__id}
                Контактная информация: {'\n '.join([str(info) for info in self.__contact_info])}
                """


class Genre:
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def __str__(self):
        return f"""
                Название: {self.__name}
                Описание: {self.__description}
                """


class ContactInfo:
    def __init__(self, type: str, value: str):
        self.__type = type
        self.__value = value

    def get_type(self):
        return self.__type

    def get_value(self):
        return self.__value

    def __str__(self):
        return f"{self.__type}: {self.__value}"



class Program:
    @staticmethod
    def main():
        genre = Genre('Фантастика','Лазоры,кометы, год больше 2050. Всякие штуки странные')

        book1 = Book('Название книги', 'Автор Авторов', 2025, 1, [genre])
        book1 = Book('sdafsasfa', 'asfasfв', 2025, 1, [genre])

        contact1 = ContactInfo('Телефон', '+79996663366')

        employee = Employee('Ванька Странный','Главный по заглавным буквам', 3, [contact1])

        library = Library('Главная библиотека', 'Дом Пушкина,Улица Колотушкина',[book1], [employee])
        library.add_book('')

        print(library)

Program.main()
