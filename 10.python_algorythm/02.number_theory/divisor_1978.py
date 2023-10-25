n = int(input())
numbers= list(map(int, input().split()))


answer = 0
for number in numbers:
    if number <= 1 : continue
    cnt = 0
    for i in range(2, int(number ** 0.5) + 1) :
        if number % i == 0 :
            cnt += 1
    if cnt == 0 :
        answer += 1
print(answer)
