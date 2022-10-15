def function(pillow, wage, expenses, inflation):
    months = 0
    balance = pillow
    while balance > 0:
        months += 1
        if months > 1:
            expenses *= 1 + inflation
        balance += wage - expenses
    return months


money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = function(money_capital, salary, spend, increase)

print(month)
