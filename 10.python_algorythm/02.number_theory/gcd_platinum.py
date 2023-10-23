N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

def _gcd(a, b) :
    if b > a :
        tmp = a
        a = b
        b = tmp
    
    while a % b !=0:
        tmp = a%b
        a = b
        b = tmp
    return b

count = 0
for i in range(1, N):
    if _gcd(numbers[i - 1], numbers[i]) != 1 :
        for j in range(numbers[i - 1] + 1, numbers[i]):        
            if _gcd(numbers[i - 1], j) == 1:
                if _gcd(numbers[i], j) == 1:
                    count += 1
                    break
            if j == numbers[i] - 1:
                count += 2
            
print(count)