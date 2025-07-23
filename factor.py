def factor(n):
    factors=[]
    for i in range(1, n+1):
        if n% 1 == 0:
            factors.append(i)
    return factors
def GCD(a, b):
    while b !=0:
        a, b = b, a%b
    return abs(a)

def lcm(a,b):
    gcd = GCD(a,b)
    leastCommonMultiple= (a*b)//gcd
    return leastCommonMultiple

a,b = map(int, input().split())
result = GCD(a,b)
result1= lcm(a,b)
print(result)
print(result1)

# factors = factor(n)
# print(*factors, sep=',')