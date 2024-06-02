class Car:
    def __init__(self, brand:str, model:str, year:int, price:float, status:str = 'в наличии'):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price
        self.__status = status

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_price(self):
        return self.__price

    def get_status(self):
        return self.__status

    def set_status(self, status:str):
        if not isinstance(status, str):
            raise TypeError
        else:
            self.__status = status

    def set_price(self,price:float):
        if not isinstance(price, float):
            raise TypeError
        else:
            self.__price = price

    def __str__(self):
        return f"""
                Бренд: {self.__brand}
                Модель: {self.__model}
                Год выпуска: {self.__year}
                Цена: {self.__price}
                Статус: {self.__status}
                """


class Salesperson:
    def __init__(self, name: str, experience: int, sold_cars: list = None):
        self.__name = name
        self.__experience = experience
        self.__sold_cars = sold_cars

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def get_sold_cars(self):
        return self.__sold_cars

    def add_sold_car(self, sold_car: Car):
        if not isinstance(sold_car, Car):
            raise TypeError('Неподходящий тип данных!')
        else:
            self.__sold_cars.append(sold_car)

    def remove_sold_car(self, car):
        if car in self.__sold_cars:
            self.__sold_cars.remove(car)
        else:
            print(f"Автомобиль {car.get_brand()} {car.get_model()} не продавался {self.__name}.")

    def __str__(self):
        return f"""
                Имя: {self.__name}
                Стаж работы: {self.__experience} лет
                Проданные автомобили: {', '.join([str(car) for car in self.__sold_cars])}
                """


class Customer:
    def __init__(self, name: str, phone: int, email: str, cars: list ):
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__cars = cars

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_cars(self):
        return self.__cars

    def set_name(self, name:str):
        if not isinstance(name, str):
            raise TypeError
        else:
            self.__name = name

    def set_email(self,email:str):
        if not isinstance(email, str):
            raise TypeError
        else:
            self.__email = email

    def set_phone(self,phone:int):
        if not isinstance(phone,int):
            raise TypeError
        else:
            self.__phone = phone

    def add_car(self, car: Car):
        if not isinstance(car, Car):
            raise TypeError('Неподходящий тип данных!')
        else:
            self.__cars.append(car)

    def remove_car(self, car: Car):
        if car in self.__cars:
            self.__cars.remove(car)
        else:
            print(f"Автомобиль {car.get_brand()} {car.get_model()} не был приобретен или заказан {self.__name}.")

    def __str__(self):
        return f"""
                Имя: {self.__name}
                Телефон: {self.__phone}
                Э-почта: {self.__email}
                Автомобили: {'\n '.join([str(car) for car in self.__cars])}
                """


class Dealership:
    def __init__(self, cars: list = None, salespeople: list = None, customers: list = None):
        self.__cars = cars
        self.__salespeople = salespeople
        self.__customers = customers

    def get_cars(self):
        return self.__cars

    def get_salespeople(self):
        return self.__salespeople

    def get_customers(self):
        return self.__customers

    def add_car(self, car: Car):
        self.__cars.append(car)

    def add_salesperson(self, salesperson: Salesperson):
        self.__salespeople.append(salesperson)

    def add_customer(self, customer: Customer):
        self.__customers.append(customer)

    def sell_car(self, car: Car, salesperson: Salesperson, customer: Customer):
        if car in self.__cars and car.get_status() == "в наличии":
            car.set_status("продано")
            salesperson.add_sold_car(car)
            customer.add_car(car)
            print(f"Автомобиль {car.get_brand()} {car.get_model()} продан {customer.get_name()}!")
            self.__cars.remove(car)
        else:
            print(f"Автомобиль {car.get_brand()} {car.get_model()} недоступен для продажи.")

    def fire_salesperson(self, salesperson: Salesperson):
        if salesperson in self.__salespeople:
            self.__salespeople.remove(salesperson)
            print(f"Продавец {salesperson.get_name()} уволен.")
        else:
            print(f"Продавец {salesperson.get_name()} не работает в автосалоне.")

    def __str__(self):
        return f"""
                Автомобили: {', '.join([str(car) for car in self.__cars])}
                Продавцы: {', '.join([str(salesperson) for salesperson in self.__salespeople])}
                Клиенты: {', '.join([str(customer) for customer in self.__customers])}
                """


class Program:
    @staticmethod
    def main():

        car1 = Car("Honda", "s2000", 2001, 50000)

        salesperson1 = Salesperson("Продавец Богов", 5, [car1])

        customer1 = Customer("Покупатель Некрух", 89999992244, "normalniy_mark_bil@email.com",[car1])

        dealership1 = Dealership([car1], [salesperson1], [customer1])

        dealership1.sell_car(car1, salesperson1, customer1)

        print(dealership1)


Program.main()