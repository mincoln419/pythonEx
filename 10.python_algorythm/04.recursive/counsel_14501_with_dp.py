import sys;
input = sys.stdin.readline
sys.setrecursionlimit(999999)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dp = [-1 for _ in range(N + 1)]
def recur(idx):
    if idx == N:
        return 0
    if idx > N:
        return -999999999999999
    
    if dp[idx] > 0:
        return dp[idx]
    
    dp[idx] = max(recur(idx + arr[idx][0]) + arr[idx][1], recur(idx + 1))
    
    return dp[idx]

print(recur(0))