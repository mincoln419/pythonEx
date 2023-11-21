import sys;
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
target = int(input())

# cursor
s = 0
e = N - 1

cnt = 0
while s < e :
    #target
    if arr[s] + arr[e] == target:
       cnt += 1
    
    if arr[s] + arr[e] >= target:
        e -= 1
    else:
        s += 1
        
print(cnt)

