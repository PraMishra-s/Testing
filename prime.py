def isPrime(n):
    if n<= 1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i= 5
    while i*i <= n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=5
    return True



primeList =[]
for i in range(1000):
    if isPrime(i):
        primeList.append(i)
print(primeList)