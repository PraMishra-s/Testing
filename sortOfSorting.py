while (True):
    n = int(input())
    W = []
    if (n == 0):
        break
    for i in range(n):
        W.append(input())
    W.sort(key=lambda x:(x[0:2]))
    for word in W:
        print(word)
    print()