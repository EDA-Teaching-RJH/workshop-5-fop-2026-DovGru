word = input("Enter a word in camel case:")

newWord = ''.join(['_' + char.lower() if char.isupper() else char for char in word])

if newWord.startswith("_"):
    newWord = newWord[1:]

print(newWord)
