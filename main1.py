# У нас продаются только яблоки
# 1кг яблок стоит 200р
# 1кг бананов стоит 250р
# 1кг Апельсинов стоит 150р
# Написать функцию которая принимает вес яблок и высчитывает их стоймость
balance = 1000
product_list = ['Яблоко', 'Банан', 'Аппельсин']
total_price = 0
basket = []


def product_calc(fruit_price: int, total_price: float, basket: list, product_list):
    weight = float(input("Введите какой вес вас интересует(кг/гр):\n>"))
    price = fruit_price * weight
    total_price += price
    basket.append(f"{product_list}/{weight}кг")
    return total_price


while True:
    choice = int(input(f"""
* * * * * * * * * * * * * * * * * * * * * * * * * 
    Товары в корзине: {basket}
    К оплате: {total_price}
* * * * * * * * * * * * * * * * * * * * * * * * * 
    Введите цифру продукта:
    
    1.Яблоко (200р/кг).
    2.Банан (250р/кг).
    3.Апельсин (150р/кг).
    4.Оплатить.
* * * * * * * * * * * * * * * * * * * * * * * * * 
    > """))
    if choice == 1:
        total_price = product_calc(200, total_price, basket, product_list[0])
    elif choice == 2:
        total_price = product_calc(250, total_price, basket, product_list[1])
    elif choice == 3:
        total_price = product_calc(150, total_price, basket, product_list[2])
    elif choice == 4:
        if total_price == 0:
            print('Вы не положили ничего в корзину')
        elif (balance - total_price) >= 0:
            balance -= total_price
            print(f'Успешно!\nВаш баланс {balance}р.')
            break
        else:
            print("Недостаточно средств на балансе")
            break
    else:
        raise "ВЫ ВВЕЛИ ЧТО ТО НЕ ТО"
