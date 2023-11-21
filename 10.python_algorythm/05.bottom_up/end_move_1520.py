import sys;
input = sys.stdin.readline
sys.setrecursionlimit(999999)

Y, X = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(Y)]

dp = [[-1] * X for _ in range(Y)]

def recur(y, x):
    
    if y == Y - 1 and x == X - 1:
        return 1
    
    if dp[y][x] != -1 :
        return dp[y][x]
    
    route = 0
    for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ey = y + dy
        ex = x + dx
        if ey < 0 or ey >= Y or ex < 0 or ex >= X:            
            continue
        if arr[y][x] <= arr[ey][ex]:
            continue
        route += recur(ey, ex)
    dp[y][x] = route
    return dp[y][x]

print(recur(0, 0))
