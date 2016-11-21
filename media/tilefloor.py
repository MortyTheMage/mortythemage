#! /usr/bin/python
#  tilefloor.py
def menuChoice0():
	valid = [1,2]
	choice = ['What is the square footage of the area you plan on tiling? ',
			  'How much is a single square foot of tile? ',
			  'Would you like to get another estimate? ',
			  'The total cost of the tile would be $%s',
			  'Sorry, I didn\'t catch that. Try again.',
			  '1. Yes',
			  '2. No']
	while True:
		print choice[0]
		try:
			area = float(input(': '))
		except SyntaxError:
			area = None
			print choice[4]
			break
		print choice[1]
		try:
			price = float(input(': '))
		except SyntaxError:
			price = None
			print choice[4]
			break
		
		print choice[3] % calcPrice(area, price)
		
		print choice[2]
		print choice[5]
		print choice[6]
		while True:
			try:
				userChoice = input(': ')
				if userChoice in valid:
					if userChoice == 1:
						break
					if userChoice == 2:
						exit()
				else:
					break
			except SyntaxError:
				print choice[4]
				break

def calcPrice(area, price):
	estimate = area * price
	return round(estimate, 2)

menuChoice0()