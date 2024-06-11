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

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"добавлено животное {animal.name} , возраст {animal.age} года")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"добавлен сотрудник {employee.name}")

    def __repr__(self):
        return f"Зоопарк с {len(self.employees)} сотрудниками и {len(self.animals)} животными"


zoo = Zoo()

bird = Bird("Глаша", 2)
cat = Cat("Мурзик", 3)
serpent = Serpent("Скоропея", 4)

zoo.add_animal(bird)
zoo.add_animal(cat)
zoo.add_animal(serpent)

zookeeper = ZooKeeper("Иван Сергеевич")
veterinarian = Veterinarian("Павел Семенович")

zoo.add_employee(zookeeper)
zoo.add_employee(veterinarian)

zookeeper.feed_animal(bird)
veterinarian.heal_animal(cat)


print(zoo)

# Выводим информацию о животных и демонстрируем их действия
for animal in zoo.animals:
    print(f"{animal.name}, возраст {animal.age} года")
    animal.make_sound()
    animal.eat()



