#! /usr/bin/python
def menuChoice0():
	invalid = 2
	while True:
		places = input('How many places in the fibonacci sequence would you like to display: ')
		if places > invalid:
			return places
			break
		else:
			if places < 1:
				print 'I can\'t show less than one place! I am not a wizard!'
			else:
				print 'That\'s too easy!'
	
def menuChoice1():
	valid = [1,2]
	while True:
		print 'Would you like to display the whole sequence or just the place you chose?'
		print '1. The whole thing!'
		print '2. Just my place, man.'
		userChoice = int(input('What would you like to do? '))
		if userChoice in valid:
			return userChoice
			break
		else:
			print 'Sorry, I couldn\'t catch that. Try again.'

def menuChoice2():
	valid = [1,2]
	while True:
		print 'Are you finished?'
		print '1. Yes'
		print '2. No'
		userChoice = int(input(': '))
		if userChoice in valid:
			if userChoice == 1:
				exit()
			if userChoice == 2:
				sequence()
		else:
			print 'Sorry, I couldn\'t catch that. Try again.'
		
def sequence():
	places = menuChoice0() # get length of sequence
	choice = menuChoice1() # entire sequence or just one number
	n = [0, 1] # create the first two places

	for i in range(2, places): # create this monster
		n.append(n[i-1] + n[i-2])
	
	if choice == 1:
		for i in range(0, len(n)):
			print str(i+1) + ":", n[i]
	if choice == 2:
		print str(places) + ":", n[places - 1]
		
	menuChoice2()

sequence()