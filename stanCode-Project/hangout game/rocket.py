"""
File: rocket.py
Name: Rita Tang
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 4


def main():
	"""
	This program build a rocket.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def lower():
	"""
	This function makes the lower body of the rocket.
	"""
	for i in range(SIZE):
		print('|', end ="")
		for k in range(i):
			print('.', end="")
		for j in range((SIZE-i)*2):
			if j % 2 == 0:
				print('\\', end="")
			else:
				print('/', end="")
		for k in range(i):
			print('.', end="")
		print('|', end="")
		print("")


def upper():
	"""
	This function makes the upper body of the rocket.
	"""
	for i in range(SIZE):
		print('|', end ="")
		for k in range(SIZE - i - 1):
			print('.', end="")
		for j in range(2*(i+1)):
			if j % 2 == 0:
				print('/', end="")
			else:
				print('\\', end="")
		for k in range(SIZE - i - 1):
			print('.', end="")
		print('|', end="")
		print("")


def head():
	"""
	This function makes the head of the rocket.
	"""
	for i in range(SIZE):
		for l in range(SIZE - i):
			print(' ', end="")
		for j in range(2*i+1):
			if j % 2 == 0:
				print('/', end="")
		for k in range(2*i+1):
			if k % 2 == 0:
				print('\\', end="")
		for l in range(SIZE - i):
			print(' ', end="")
		print("")


def belt():
	"""
	This function makes the belt of the rocket.
	"""
	print('+', end="")
	for i in range(SIZE * 2):
		print('=', end="")
	print('+')






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()