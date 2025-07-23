# Kattis link
# https://open.kattis.com/problems/baconeggsandspam


while True:
    items={}
    n = int(input())
    if n == 0:
        break
    for _ in range(n):
        order = input().split()
        name = order[0]
        for item in order[1:]:
            if item in items:
                items[item].append(name)
            else:
                items[item] = [name]
    items = sorted(items.items())
    for key, value in items:
        value.sort()
        print(key, end=" ")
        print(*value)
    print()



