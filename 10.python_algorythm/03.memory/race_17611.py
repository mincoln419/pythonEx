import sys;
input = sys.stdin.readline

N, H = map(int, input().split())

dp = [int(N/2)] * (H + 1)

for i in range(N):
    num = int(input());
    if i % 2 == 0 :
        dp[0] = dp[0] + 1
        dp[num + 1] = dp[num + 1] - 1;
    else :
        dp[num - 1] = dp[num - 1] + 1
        dp[H] = dp[H] - 1;

minNo = min(dp[0:H])
cnt = 0
print(dp)
for i in range(H):
    if dp[i] == minNo :
        cnt += 1

print(minNo, cnt)