#C:\Users\...\Python
import sys

word = input("Search for a word: ")

with open("dict.txt") as f:
	for line in f:
		if word in line:
			print(line)