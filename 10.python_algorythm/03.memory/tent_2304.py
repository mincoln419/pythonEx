N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda lists: lists[0])

topIndex = 0
topH = 0
for i in range(N):
    if topH < arr[i][1]:
        topH = arr[i][1]
        topIndex = i

answer = topH

# print(arr)

if N == 2 :
    answer = abs(arr[1][0] - arr[0][0]) * min(arr[1][1], arr[1][0]) + max(arr[1][1], arr[1][0])

if N > 2 :    
    curTop = arr[0][1]
    for i in range(1, topIndex + 1):
        # print("arr[i][1]:{} , arr[i - 1][1]:{}".format(arr[i][1] , arr[i - 1][1]))
        answer += curTop * (arr[i][0] - arr[i - 1][0])        
        # print("answer : {}".format(answer))
        if curTop < arr[i][1]:
            curTop = arr[i][1]
    
    curTop = arr[N - 1][1]
    for i in range(N - 2, topIndex - 1, -1):
        # print("arr[i + 1][1]:{} - arr[i][1]:{}".format(arr[i + 1][0] ,arr[i][0]))
        answer += curTop * (arr[i + 1][0] - arr[i][0])        
        # print(answer)
        if curTop < arr[i][1]:
            curTop = arr[i][1]

print(answer)