"""
File: caesar.py
Name: Rita Tang
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program decipher the ciphered string.
    """
    s_number = int(input('Secret number: '))
    string = input('What\'s the ciphered string? ')
    string = string.upper()
    new_alph = create_alph(s_number)
    real_string = find_string(string, new_alph)
    print('The deciphered string is: ' + str(real_string))


def create_alph(s_number):
    """
    This function creates the new arranged alphabet order
    """
    move_alph = ALPHABET[(26-int(s_number)):]
    ans = ''
    ans += move_alph
    ans += ALPHABET[:(26-int(s_number))]
    return ans


def find_string(string, new_alph):
    """
    :param string: the string that the user types.
    :return: the deciphered string
    """
    ans = ''
    for i in range(len(string)):
        ch = string[i]
        if ch not in ALPHABET:
            ans += ch
        else:
            number = new_alph.find(ch)
            ans += ALPHABET[int(number)]
    return ans










#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
