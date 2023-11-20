import sys;
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
    for RGB in range(3):
        if RGB == 0 :
            dp[i][RGB] = min(dp[i-1][1], dp[i-1][2]) + arr[i - 1][RGB]
        if RGB == 1 :
            dp[i][RGB] = min(dp[i-1][0], dp[i-1][2]) + arr[i - 1][RGB]
        if RGB == 2 :
            dp[i][RGB] = min(dp[i-1][1], dp[i-1][0]) + arr[i - 1][RGB]

print(min(dp[N]))