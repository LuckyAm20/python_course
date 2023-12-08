money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month_money_limit = money_capital
total_months = 0

while (month_money_limit := (month_money_limit + salary - spend)) > 0:
    spend += spend * increase
    total_months += 1

print("Количество месяцев, которое можно протянуть без долгов:", total_months)
