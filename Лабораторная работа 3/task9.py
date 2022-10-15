def calculate_pillow(wage, expenses, months, inflation):
    pillow = 0
    for month in range(1, months + 1):
        if month > 1:
            expenses *= 1 + inflation
        pillow += wage - expenses
    # Мы в минусе на pillow рублей
    # Тогда чтобы прожить 10 месяцев нам нужно минимум (-1)*pillow рублей
    return (-1) * pillow


salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = calculate_pillow(salary, spend, months, increase)

print(round(need_money))
