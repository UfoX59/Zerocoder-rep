# 11. Доходность
# Напишите функцию, которая высчитывает размер прибыли по
# заданной себестоимости и цены, по которой продают товар.

def calculate_profit(cost, price):
    profit = price - cost
    return profit

cost = 77
price = 100
print (f"Прибыль составляет: {calculate_profit (cost, price)} руб.")
