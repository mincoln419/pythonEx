import sys;
input = sys.stdin.readline

div_num = 10_007
N = int(input())
dp = [0] * (N + 1)

dp[0] = 1
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % div_num

print(dp[N])
