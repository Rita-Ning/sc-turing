"""
File: similarity.py
Name: Rita Tang
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program compares a short dna sequence to the longer dna sequence that one enters,
    and find the sequence in the longer dna which has the highest similarity to the short one.
    """
    long_s = input('Please give me a DNA sequence to search: ')
    long_s = long_s.upper()
    short_s = input('What DNA sequence would you like to match? ')
    short_s = short_s.upper()
    ans = find_similar(long_s, short_s)
    print('The best match is ' + str(ans))


def find_similar(long_s, short_s):
    """
    This function will find the sequence in the longer dna which has the highest
    similarity to the short ones.
    """
    maximum = 0
    similar_s = ''

    for i in range((len(long_s)) - len(short_s) + 1):
        match_s = long_s[i:i+int(len(short_s))]
        right = 0
        for j in range(len(short_s)):
            if match_s[j] == short_s[j]:
                right += 1
            if maximum < right:
                maximum = right
                similar_s = match_s

    return similar_s









###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
