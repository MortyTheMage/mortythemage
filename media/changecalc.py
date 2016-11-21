#! /usr/bin/python
#  change calculator
from decimal import *
def menuChoice0():
	getcontext().prec = 2
	valid = [1,2]
	choice = ['Would you like to start over?',
			  'Sorry, I didn\'t catch that. Try again.',
			  '1: Yes',
			  '2: No',
			  'How much did the item cost?',
			  'How much money did you hand over?',
			  'You\'re change will be $%s split between \n%s dollars, \n%s quarters, \n%s dimes, \n%s nickels and \n%s pennies.'
			  ]
	while True:
		print choice[4]
		try:
			cost = float(input(': '))
		except SyntaxError:
			cost = None
			print choice[1]
			break
		print choice[5]
		try:
			amnt = float(input(': '))
		except SyntaxError:
			amnt = None
			print choice[1]
			break
		
		print choice[6] % calcChange(cost, amnt)
		
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

def calcChange(cost, amnt):
	doll = 0
	change = amnt*100 - cost*100
	quar = change // 25
	qnum = change - quar * 25
	dime = qnum // 10
	dnum = qnum - dime * 10
	nick = dnum // 05
	nnum = dnum - nick * 05
	penn = nnum // 01
	pnum = nnum - penn * 01
	if quar >= 4:
		doll = int(quar)/int(4)
		quar = quar % 4
	change = round(change / 100, 2)
	return (change, doll, quar, dime, nick, penn)

menuChoice0()