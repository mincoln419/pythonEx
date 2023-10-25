N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda lists: lists[0])
print(*arr)


topIndex = 0
topH = 0
for i in range(N):
    if topH < arr[i][1]:
        topH = arr[i][1]
        topIndex = i
    
prefix = [0 for _ in range(N + 1)]

answer = topH
for i in range(topIndex):
    prefix[i + 1] = max(prefix[i], arr[i][1])
    
for i in range(N, topIndex, -1):
    prefix[i - 1] = max(prefix[i] + arr[i][1], arr[i][1])
    
print(topIndex)
print(topH)
print(max(prefix))