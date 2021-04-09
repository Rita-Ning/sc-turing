"""
File: boggle.py
Name: Rita Tang
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
Dict_l = []                   # words in Dict


def main():
	"""
	TODO:
	"""
	read_dictionary()

	boggle = []
	for i in range(4):
		words = input(str(i+1)+' row of letters:')
		words = words.split()
		row = []
		for letter in words:
			if letter.islower():
				letter.upper()
			if len(letter) != 1:
				print('Illegal input')
				break
			else:
				row.append(letter)
		boggle.append(row)

	found = []
	for x in range(4):
		for y in range(4):
			game(boggle, x, y, "", [], found)
	print("There are " + str(len(found)) + " words in total.")


neighbor_p = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def game(boggle, x, y, word, visited, found):
	if not has_prefix(word):
		return
	# check if letter already used
	if [x, y] in visited:
		return
	if word in found:
		return

	if word in Dict_l:
		found.append(word)
		print('Found', word)

	letter = boggle[x][y]
	word += letter
	visited.append([x, y])

	# get neighbor position
	for p in neighbor_p:
		new_x = x + p[0]
		new_y = y + p[1]
		if new_x >= 4 or new_x < 0 or new_y >= 4 or new_y < 0:
			continue

		game(boggle, new_x, new_y, word, visited, found)

	# give the last word back
	visited.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			word = line.split()
			if 16 >= len(word[0]) >= 4:
				Dict_l.append(word[0])


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in Dict_l:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
