import sys;
input = sys.stdin.readline
sys.setrecursionlimit(999999)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dp = [0 for _ in range(N + 1)]

for idx in range(N)[::-1]:
    if idx + arr[idx][0] > N:
        dp[idx] = dp[idx + 1]
    else:
        dp[idx] = max(dp[idx + arr[idx][0]] + arr[idx][1], dp[idx + 1])
        
print(dp[0])
