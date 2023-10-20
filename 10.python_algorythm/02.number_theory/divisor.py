n = int(input())

cnt = 0
answer = []
for i in range(2, int(n ** 0.5) + 1) :
    if n % i == 0 :
        cnt += 1
        answer.append(i)
        
print(cnt)
print(*answer)
