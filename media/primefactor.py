#! /usr/bin/python
def menuChoice0():
	valid = 5
	while True:
		number = input('Pick an integer and I\'ll list all of its prime factors!')
		if type(number) == int:
			genPrime(number)
		else:
			print "That's not an integer!"

def genPrime(number):
	n=5
	p=[2,3]
	for i in range(n, number):
		isPrime = True
		for b in p:
			if i%b==0:
				isPrime = False
				break
		if isPrime:
			p.append(i)
	for i in p:
		if number % i == 0:
			print i
	
menuChoice0()