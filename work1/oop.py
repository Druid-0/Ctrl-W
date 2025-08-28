
class Person:

    def __init__(self, age=0):
        self._age = age

    # @staticmethod
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("age cannot be negative >:( ")
            return()

    # @staticmethod
    def get_age(self):
        return self._age

    # @staticmethod
    # def get_age(set_age, age):
    #     if age < 0:
    #         return age
    #     else:
    #         print("cannot be > 0")
    #         return ()




class Animal:

    def speak(self):
        print("I am an animal")


class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("woof woof")

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Meow meow, imma cat")


class Vehicle:
    @staticmethod
    def move(self):
        print("vehicle is moving")

class Car:
    def move(self):
        print("Car is driving")

class Bicycle:
    def move(self):
        print("Bicycle is pedaling")

# vehicle = Vehicle()
def move(vehicle):
    vehicle.move()


# ----
p = Person()
p.set_age(25)
print(p.get_age())  # Вывод: 25
p.set_age(-5)  # Должна быть ошибка или предупреждение
# ----
print(" ---- ")

dog = Dog("Buddy")
cat = Cat("Kitty")

print(cat.name, cat.speak())
print(dog.name, dog.speak())
# ----
print(" ---- ")

car = Car()
bike = Bicycle()

print(move(car))  # Вывод: Car is driving
print(move(bike))  # Вывод: Bicycle is pedaling