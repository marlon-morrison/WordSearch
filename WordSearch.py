#C:\Users\...\Python\WordSearch
import sys
print("")
word = input("Search for a word: ")

with open("WordSearch\dict.txt") as f:
	for line in f:
		if word in line:
			print(line)