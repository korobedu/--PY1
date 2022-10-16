def deadline(money_capital, salary, spend, increase):
    months = 0
    balance = money_capital
    while True:
        balance += salary - spend
        if balance < 0:
            break
        months += 1
        spend *= 1 + increase
    return months


money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = deadline(money_capital, salary, spend, increase)

print(month)
