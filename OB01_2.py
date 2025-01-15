class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар {item_name} добавлен в магазин {self.name}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} удалён из магазина {self.name}")
        else:
            print(f"Товар {item_name} не найден в ассортименте магазина {self.name}")

    def get_price(self, item_name):
        if item_name in self.items:
            return self.items.get (item_name)
        else:
            return None
    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар {item_name} не найден")

store1 = Store("Гастроном №1", "Улица, 1, дом 1")
store1.add_item("Яблоки", 50)
store1.add_item("Бананы", 100)
store1.add_item("Груши", 150)

store2 = Store("Гастроном №2", "Улица, 2, дом 2")
store2.add_item("Молоко", 200)
store2.add_item("Кефир", 250)
store2.add_item("Сметана", 300)

store3 = Store("Гастроном №3", "Улица, 3, дом 3")
store3.add_item("Яйца", 350)
store3.add_item("Сыр", 400)
store3.add_item("Колбаса", 450)

print(f"\nТовары в {store1.name} : {store1.items}")
store1.add_item("Мандарины", 175)
print(f"Товары в {store1.name} : {store1.items}\n")

store1.update_price("Ябл", 75)
store1.update_price("Яблоки", 75)
print(f"Товары в {store1.name} : {store1.items}\n")

store1.remove_item("банана")
store1.remove_item("Бананы")
print(f"Товары в {store1.name} : {store1.items}\n")

print(store1.get_price("яблоки"))
price = store1.get_price("Яблоки")
print(f"Цена на яблоки в магазине {store1.name}: {price}\n")

print(f"Товары в {store2.name} : {store2.items}\n")
print(f"Товары в {store3.name} : {store3.items}\n")
