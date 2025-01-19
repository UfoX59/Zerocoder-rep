#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.
#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Издаёт звук"

    def eat (self):
        return "Животное ест"

class Bird(Animal):
    def __init__(self, name, age, wing_span, voice):
        super().__init__(name, age)
        self.wing_span = wing_span
        self.voice = voice

    def make_sound(self):
        return self.voice

    def eat(self):
        return "Клюёт зерно"

class Mammal(Animal):
    def make_sound(self):
        return "Звук млекопитающего"

    def eat(self):
        return "Пьёт молоко"

class Reptile(Animal):
    def __init__(self, name, age, voice):
        super().__init__(name, age)
        self.voice = voice

    def make_sound(self):
        return self.voice

    def eat(self):
        return "Твоя кровь на моих зубах"

bird1 = Bird("Дятел Вудди", 3, 45, "Тук-тук-тук")
mammal1 = Mammal("Кот Матроскин", 4)
reptile1 = Reptile("Сайзот", 25, "За Затерру!")

animal1 = Animal("Животное1", 14)
print (f"{animal1.name},  {animal1.make_sound()}, {animal1.eat()}")

print(bird1.name, bird1.age, bird1.wing_span)
print(bird1.make_sound())
print (bird1.eat())

#3
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


#animal_sound(bird1, mammal1, reptile1)

#4
class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_aminal(self, animal_speices):
        self.animals.append(animal_speices)

    def add_staffl(self, new_employees):
        self.staff.append(new_employees)

#5
