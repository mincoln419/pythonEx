import sys;
input = sys.stdin.readline
sys.setrecursionlimit(999999)

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (N + 1) for _ in range(N + 1)]

def recur(y, x):
    if dp[y][x] > 0 :
        return dp[y][x]
    for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ey = y + dy
        ex = x + dx
        if ey < 0 or ey >= N or ex < 0 or ex >= N:            
            continue
        if arr[y][x] >= arr[ey][ex]:
            continue
        dp[y][x] = max(dp[y][x], recur(ey, ex) + 1)
    return dp[y][x]

answer = 0
for y in range(N):
    for x in range(N):
        answer = max(answer, recur(y, x) + 1)

print(answer)