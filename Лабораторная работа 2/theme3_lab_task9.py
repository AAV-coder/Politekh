salary = 5000     # зарплата
spend = 6000      # траты
months = 10       # количество месяцев
increase = 0.03   # рост цен

KOEF_INFL = (1 + increase)
zapas = 0

for i in range(months):
    zapas = zapas + spend
    spend = spend * KOEF_INFL

need_money = zapas - salary * months

print(round(need_money))
