 #1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`)
 # для всех животных.

#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
 # Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()`
 # для каждого животного.

#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Д
 # олжны быть методы для добавления животных и сотрудников в зоопарк.

#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
 # (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("Кар-Кар")

    def eat(self):
        print("Ест зерно")

class Cat(Animal):
    def make_sound(self):
        print("Мур-Мур")

    def eat(self):
     print("Ест молоко")

class Serpent(Animal):
    def make_sound(self):
        print("Ши-Ши")

    def eat(self):
     print("Ест мышей")


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")




animals = [Bird("Глаша", 2), Cat("Мурзик", 3), Serpent("Скоропея", 4)]

for animal in animals:
    print(f"{animal.name}, возраст {animal.age} года")
    animal.make_sound()
    animal.eat()
