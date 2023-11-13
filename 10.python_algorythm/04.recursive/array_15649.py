import sys;
input = sys.stdin.readline

N, M = map(int, input().split())

def makeArr(number, arr, answer):    
    if number == M:
        if sorted(arr) in answer:
            return
        answer.append(sorted(arr))
        return
    for i in range(1, N + 1):
        if i in arr:
            continue
        arr.append(i)
        makeArr(number + 1, arr, answer)
        arr.pop()
        
arr = []
answer = []
makeArr(0, arr, answer)
for i in range(len(answer)):
    print(*answer[i])

###15649, #15650, #15651, # 15652, # 15654, # 15655, # 15656 