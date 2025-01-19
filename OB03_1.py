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
        pass

    def eat (self):
        pass

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print ("Пение птицы")

    def eat(self):
        print("Клюёт зерно")

class Mammal(Animal):
    def make_sound(self):
        print("Звук млекопитающего")

    def eat(self):
        print("Пьёт молоко")

class Reptile(Animal):
    def make_sound(self):
        print("За Затерру!")

    def eat(self):
        print("Твоя кровь на моих зубах")

bird1 = Bird("Дятел Вудди", 3, 45)
mammal1 = Mammal("Кот Матроскин", 4)
reptile1 = Reptile("Сайзот", 25)

print(bird1.name, bird1.age, bird1.wing_span)
bird1.make_sound()
bird1.eat()

