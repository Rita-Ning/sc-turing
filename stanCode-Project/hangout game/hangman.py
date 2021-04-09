"""
File: hangman.py
Name: Rita Tang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program will display hanger game.
    """
    correct = random_word()
    dash = ''
    for i in range(len(correct)):
        dash += '-'
    print('The word looks like: '+str(dash))
    print('You have '+str(N_TURNS)+' guesses left')
    guess = N_TURNS
    temp_word = dash
    while True:
        word_guess = input('Your guess: ')
        word_guess = word_guess.upper()
        if not word_guess.isalpha():
            print('illegal format.')
        elif len(word_guess) > 1:
            print('illegal format.')
        elif correct.find(word_guess) == -1:
            guess -= 1
            if guess == 0:
                print('There is no ' + str(word_guess) + '\'s in the word.')
                print('You are completely hung :(')
                print('The word was: '+str(correct))
                break
            else:
                print('There is no '+str(word_guess)+'\'s in the word.')
                print('The word looks like: ' + str(temp_word))
                print('You have '+str(guess)+' guesses left.')
        else:
            print('You are correct!')
            word_game = ''
            for j in range(len(temp_word)):
                ch1 = correct[j]
                ch2 = temp_word[j]
                if ch2.isalpha():
                    word_game += ch2
                if ch2 == '-':
                    if ch1 == word_guess:
                        word_game += word_guess
                    else:
                        word_game += '-'
            temp_word = word_game
            if temp_word.isalpha():
                print('You win!!')
                print('The word was: ' + str(correct))
                break
            else:
                print('The word looks like: ' + str(word_game))
                print('You have ' + str(guess) + ' guesses left.')



def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
