def deadline(pillow, wage, expenses, inflation):
    months = 0
    balance = pillow
    while True:
        balance += wage - expenses
        if balance < 0:
            break
        months += 1
        expenses *= 1 + inflation
    return months


money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = deadline(money_capital, salary, spend, increase)

print(month)
