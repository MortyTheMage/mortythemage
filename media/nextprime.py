#! /usr/bin/python
#  nextprime.py
def menuChoice0():
	valid = [1,2,'']
	p = [2,3]
	while True:
		print 'My list of prime numbers includes ', p
		print 'Would you like me to show you the next prime number?'
		print '1. Yes'
		print '2. No'
		try:
			userChoice = input(': ')
			if userChoice in valid:
				if userChoice == 1:
					nextPrime(p)
				if userChoice == 2:
					exit()
			else:
				print 'Sorry, I didn\'t catch that.'
		except SyntaxError:
			userChoice = None
			if userChoice == None:
				nextPrime(p)
def nextPrime(p):
	n = p[len(p)-1]
	while True:
		n+=1
		isPrime = True
		for b in p:
			if n%b==0:
				isPrime = False
				break
		if isPrime:
			p.append(n)
			break

menuChoice0()