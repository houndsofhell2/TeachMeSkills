import datetime
from email.policy import default


class Car:

    car_count = 0 # атрибут класса
    default_color = "white"

    def __init__(self, name, color=None):
        print("Adding new car")
        self.name = name # атрибут экземпляра
        Car.car_count += 1
        if color is None:
            self.color = Car.default_color
        else:
            self.color = color
        self.car_date = datetime.datetime.now()
        # Если цвет не передали при создании автомобиля то использовать дефолтный цвет
        # Создать аттрибут объекта который хранит время создания объекта и дату



print(Car.car_count)
car1 = Car("BMW")
print(car1.name, car1.color, car1.car_date)
print(Car.car_count)
car2 = Car("Mercedes", color="Red")
print(car2.name, car2.color, car2.car_date)
print(Car.car_count)
