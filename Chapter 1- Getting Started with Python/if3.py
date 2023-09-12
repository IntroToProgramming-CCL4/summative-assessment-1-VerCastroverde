word = input("Enter word: ")
while True:
	for letter in word:
		if letter == "e" or letter == "u" or letter == "a" or letter == "o":
			continue
		if letter == "x":
			break
		print(letter)
	print("End")
	word = input("Enter word: ")
