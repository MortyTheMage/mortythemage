#! /usr/bin/python
import math
n_input = input('How many places would you like to print pi to?: ')
while n_input >= 12:
	n_input = input('You have too many places for me to handle. Try a number less than 12: ')
while n_input < 1:
	n_input = input('Sorry, I can\'t round it to less than one place guy. Try again: ')
print "Pi rounded to " + str(n_input) + " decimal places:", round(math.pi, n_input)