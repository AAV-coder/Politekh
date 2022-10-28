money_capital = 10000
salary = 5000
spend = 6000
KOEF_INFL = 1.05

month = 1

rest = (money_capital + (salary - (spend * KOEF_INFL)) * month)

while True:
    rest > 0
    rest = (money_capital + (salary - (spend * KOEF_INFL)) * month)
    month += 1
    print("Можно жить, осталось ...", rest)
    if rest <= 0:
        break
print(month)
