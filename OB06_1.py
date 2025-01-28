# Консольная игра "Битва героев"

class Hero:
    def __init__(self, name, health = 100 , attack_power = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -=self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона!")
        #print(f"У {other.name} осталось {other.health} здоровья")

    def is_alive(self):
        return self.health >0

class Game():
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print(f"{self.player.name} против {self.computer.name}")
        print("Да начнется битва!\n")

        current_turn =0
        while self.player.is_alive() and self.computer.is_alive():
            if current_turn == 0:
                self.player.attack(self.computer)
                print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")
            else:
                self.computer.attack(self.player)
                print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")

            current_turn = 1 - current_turn

        if self.player.is_alive():
            print (f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")


player_name = "Рыцарь Вася"
game = Game(player_name)
game.start()
