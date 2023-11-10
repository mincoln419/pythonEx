import sys;
input = sys.stdin.readline

N, M = map(int, input().split())

def makeArr(number, arr):    
    if number == M:
        print(*arr)
        return
    for i in range(1, N + 1):
        arr.append(i)
        makeArr(number + 1, arr)
        arr.pop()
        
arr = []
makeArr(0, arr)