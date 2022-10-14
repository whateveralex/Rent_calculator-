def start():
    print("Welcome to the the rent calculator")
    print('-' * 15)
    print("""Enter in \"Yes\" if you would like to calculate 
    how much you can afford to pay in rent!""")
    print('-' * 15)
    print("Enter \"No\" if you would not like to continue.")

    choice = input('> ').lower()

    if 'yes' in choice:
        rent_type()

    else:
        print("Okay, lets try again later")


def rent_type():
	stuff = ['Yearly Salary', 'Monthly Income', 'Hourly Wage']
	print('Let\'s calculate how much you can afford for rent every month!')
	print('To start lets first find out how you want to calculate your rent.')
	print('-' * 15)
	print('Here are your choices')
	for index, stuff in enumerate(stuff, start=1):
		print(index, stuff)

	rent_answer = input('Please type in the type of income you would like to use: ').lower()

	if rent_answer == 'yearly salary':
		print('-' * 15)
		yearly_salary()
	
	elif rent_answer == 'monthly income':
		print('-' * 15)
		monthly_income()

	elif rent_answer == 'hourly wage':
		print('-' * 15)
		hourly_wage()

	else: 
		print('Please try again, enter in your answer carefully')
		rent_type()


def yearly_salary():
	ys = float(input("Please enter your yearly salary before tax:  "))
	a = ys / 12
	b = a * .3
	print(f"You can afford {b} a month in rent!")


def monthly_income():
	ms = float(input("Please enter your monthly income before tax:  "))
	a = ms * .3
	print(f"You can afford {a} a month in rent!")


def hourly_wage():
	hw = float(input("Please enter how much you make an hour: "))
	a = hw * 8 
	b = a * 5
	c = b * 4
	d = c * .3
	print(f"You can afford {d} a month in rent!")


start()

