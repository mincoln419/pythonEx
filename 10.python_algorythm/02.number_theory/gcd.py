A, B = map(int, input().split())

def _gcd(a,b) :
    while a % b !=0:
        tmp = a%b
        a = b
        b = tmp
    return b

print(_gcd(A, B))