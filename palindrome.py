def checkPalindrome(word):
    return word == word[::-1]

def checkAnagram(word1, word2):
    return sorted(word1) == sorted(word2)

def generateFibonacci(n):
    if n<= 0:
        print('Enter a valid Number')
    elif n == 1:
        print(0)
    else:
        fibonnaci= []
        a = 0
        b = 1

        for _ in range(n):
            fibonnaci.append(a)
            a, b = b, a+b
        return fibonnaci

    




# word = 'malayalam'
# word1 = 'listen'
# word2 = 'silent'
# print(checkPalindrome(word))
# print(checkAnagram(word1, word2))
result = generateFibonacci(9)
print(*result)