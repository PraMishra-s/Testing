def checkLength(word):
    totalWords= []
    for letter in word:
        if letter in word:
            return len(totalWords)
        else:
            totalWords.append(letter)






word = input()