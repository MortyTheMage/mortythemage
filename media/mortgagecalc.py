#! /usr/bin/python
#  mortgagecalc.py
#  M = monthly mortgage payment -- solve for this
#  P = principal, initial amount you borrorwed
#  i = your monthly interest rate. Interest is generally compounded yearly (divide by 12)
#  n = number of payments, or the payment period in months.
#  Formula:
#  M = P(i(1+i)**n) / ((1+i)**n - 1)
#  Goal:
def menuChoice0():
	valid = [1,2]
	choice = ['Would you like to get another estimate?',
			  'Sorry, I didn\'t catch that. Try again.',
			  '1: Yes',
			  '2: No',
			  'What is the initial amount you borrowed?',
			  'What is your yearly interest rate?',
			  'How long is the payment period [in months]?',
			  'Your monthly mortgage payment would be $%s per month.']
	while True:
		print choice[4]
		try:
			principal = float(input(': '))
		except SyntaxError:
			principal = None
			print choice[1]
			break
		print choice[5]
		try:
			interest = float(input(': '))
			interest /= 12 # Monthly interest rate
		except SyntaxError:
			interest = None
			print choice[1]
			break
		print choice[6]
		try:
			payments = float(input(': '))
		except SyntaxError:
			payments = None
			print choice[1]
			break
		
		print choice[7] % calcPayment(principal, interest, payments)
		
		print choice[0]
		print choice[2]
		print choice[3]
		while True:
			try:
				userChoice = int(input(': '))
				if userChoice in valid:
					if userChoice == 1:
						break
					if userChoice == 2:
						exit()
				else:
					break
			except SyntaxError:
				print choice[1]
				break

def calcPayment(p, i, n):
	M = (p*(i*(1+i)**n)) / ((1+i)**n - 1)
	return M

menuChoice0()
					