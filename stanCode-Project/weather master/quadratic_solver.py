"""
File: quadratic_solver.py
Name: Rita Tang
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program calculates if the quadratic function: ax^+bx+c, (a != 0)
	have one root, two roots or none.
	"""
	print('stanCode Quadratic Solver!')
	# user will type the number of a, b, c
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	# if one root
	if b**2-4*a*c == 0:
		one_root = float(-b / (2 * a))
		print('One root: '+str(one_root))
	# if no root
	if b**2-4*a*c < 0:
		print('No real roots')
	# if two roots
	if b**2-4*a*c > 0:
		# calculate two roots
		# e equals the square root of b^-4ac
		d = b**2-4*a*c
		e = math.sqrt(d)
		# naming two roots: n1,n2
		n1 = float((-b+e)/(2*a))
		n2 = float((-b-e)/(2*a))
		print('Two roots: '+str(n1)+', '+str(n2))






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
