"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
Dict_l = []                   # words in Dict


def main():
    read_dictionary()
    while True:
        print('Welcome to stanCode \"Anagram Generator:\" (or -1 to quit)')
        s = input('Find anagrams for:')
        if s == EXIT:
            break
        else:
            ana_l = []
            find_anagrams(s, ana_l)
            print('Searching.....')
            print(len(ana_l), 'anagrams:', ana_l)


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            word = line.split()
            Dict_l.append(word[0])


def find_anagrams(s, ana_l):
    """
    :param s:
    :return:
    """
    for word in Dict_l:
        # check if same len
        if len(s) == len(word):
            a = ''.join(sorted(s))
            b = ''.join(sorted(word))
            # check if contains same alphabets
            if a == b:
                ana_l.append(word)
                print('Searching.....')
                print('Found:' + str(word))


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    global Dict_l
    if Dict_l.startwith(sub_s):
        return True
    return False


if __name__ == '__main__':
    main()
