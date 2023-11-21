import sys;
input = sys.stdin.readline

N , X= map(int, input().split())
arr = sorted(list(map(int, input().split())))


# cursor
s = 0
e = N - 1

cnt = 0
left = 0
while s <= e :    
    if arr[e] == X:
        cnt +=1
        e -= 1
        continue
    #target
    if s == e :
        left += 1
        break;
        
    if arr[s] + arr[e] >= X/2:
        cnt += 1
        s += 1
        e -= 1 
    else:
        s += 1
        left +=1

print(cnt + left//3)

