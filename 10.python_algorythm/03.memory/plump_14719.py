H, W = map(int, input().split())
arr = list(map(int, input().split()))

if(W <= 3):
    print(0)
else:
    minus = 0
    topH = 0
    topIndex = 0
    for i in range(W):
        minus = minus + arr[i]
        if topH < arr[i]:
            topH = arr[i]
            topIndex = i
            
    answer = topH
    curTop = arr[0]
    for i in range(1, topIndex + 1):
        answer += curTop
        if curTop < arr[i]:
            curTop = arr[i]
    
    curTop = arr[W - 1]
    for i in range(W - 2, topIndex - 1, -1):
        answer += curTop
        if curTop < arr[i]:
            curTop = arr[i]
    
    print(answer - minus)




