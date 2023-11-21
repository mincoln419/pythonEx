import sys;
input = sys.stdin.readline

N , M = map(int,input().split())
trees = list(map(int, input().split()))


s = 0
e = max(trees)
while s <= e :
    mid = (s + e)//2
    
    tot = 0
    for i in range(N):
        if trees[i] - mid > 0:
            tot += trees[i] - mid
            if tot > M:
                break
    if tot >= M:
        s = mid + 1
    else :
        e = mid - 1
    
print(e)
