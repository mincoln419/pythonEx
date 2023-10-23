A, B = map(int, input().split())

def _gcd(a,b) :
    while a % b !=0:
        tmp = a%b
        a = b
        b = tmp
    return b

def _lcm(a,b) :
    return a*b//_gcd(a,b)


print(_lcm(A, B))