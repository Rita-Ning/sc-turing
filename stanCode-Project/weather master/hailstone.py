"""
File: hailstone.py
Name: Rita Tang
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program computes Hailstone sequences and count the steps it takes
    """
    print('This program computes Hailstone sequences.')
    print('\n')
    number = int(input('Enter a number: '))
    # to count steps
    steps = 0
    if number == 1:
        print('It took 0 steps to reach 1.')
    else:
        while True:
            if number == 1:
                break
            elif (number % 2) == 0:
                print(str(number)+' is even, so I take half: '+str(int(number/2)))
                number = int(number/2)
                steps += 1
            elif (number % 2) != 0:
                print(str(number)+' is odd, so I make 3n+1: '+str(int(number*3+1)))
                number = int(number*3+1)
                steps += 1
        print('It took '+str(steps)+' steps to reach 1.')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
