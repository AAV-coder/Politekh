money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0

while money_capital + salary - spend > 0:
	month += 1
	salary = salary * month
	spend = spend * (1 + increase) * month
	#print("Прожил ", month, " мес., осталось ", (money_capital + salary - spend), "руб.")

if money_capital + salary - spend < 0:
	print(month)


