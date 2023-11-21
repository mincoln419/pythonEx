import sys;
input = sys.stdin.readline

A = input().strip()
B = input().strip()

dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

for y in range(1, len(A) + 1):
    for x in range(1, len(B) + 1):
        if A[y - 1] == B[x - 1]:
            dp[y][x] = dp[y - 1][x - 1] + 1
        else :
            dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])

print(dp[len(B)][len(A)])
    