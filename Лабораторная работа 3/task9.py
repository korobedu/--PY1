def calculate_pillow(salary, spend, months, increase):
    pillow = 0
    for _ in range(months):
        pillow += salary - spend
        spend *= 1 + increase
    # Мы в минусе на pillow рублей
    # Тогда чтобы прожить 10 месяцев нам нужно минимум (-1)*pillow рублей
    return -pillow


salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = calculate_pillow(salary, spend, months, increase)

print(round(need_money))
