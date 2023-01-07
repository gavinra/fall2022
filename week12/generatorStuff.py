def randomGenerator(wordList, character):
    for word in wordList:
        if word.startswith(character):
            yield word

wordList = []

for something in range(0, 5):
    item = input("Please type a random word: ")
    wordList.append(item)

wordList.sort()

alphabet= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
 "m", "n", "o", "P", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

l = iter(alphabet)

print("Here are your words in alphabetical order:")

for letter in range(0,26):
    character = next(l)
    for word in randomGenerator(wordList, character):
        print(word)


