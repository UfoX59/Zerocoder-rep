
from abc import ABC, abstractmethod

class Fighter():
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def attack(self, target):
        self.weapon.attack(target)

    def change_weapon(self):
        if isinstance(self.weapon, Sword):
            self.weapon = Bow()
            print("Боец выбирает лук")
        else:
            self.weapon = Sword()
            print("Боец выбирает меч")


class Monster():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class Weapon(ABC):
    @abstractmethod
    def attack(self, target):
        pass

class Sword(Weapon):
    def attack(self, target):
        target.hp -=11
        if target.hp <= 0:
            print("Атака мечом")
            print(f"{target.name} погиб от удара меча")
        else:
            print("Атака мечом")

class Bow(Weapon):
    def attack(self, target):
        target.hp -=4
        if target.hp <= 0 :
            print("Выстрел из лука")
            print(f"{target.name} погиб от выстрела из лука")
        else:
            print("Выстрел из лука")



f1 = Fighter("Рыцарь Вася",Sword())
m1 = Monster ("Кикимора болотная",100)

print (m1.name, m1.hp)
print (f"{f1.name}")
f1.change_weapon()


#print(f"{f1.name}  атакует {m1.name} ")
f1.attack(m1)
print (m1.name, m1.hp)

# f1.change_weapon()
# print (f"{f1.name} сменил оружие на {f1.weapon}")

f1.attack(m1)
print (m1.name, m1.hp)

while m1.hp >0:
    f1.change_weapon()
    f1.attack(m1)
