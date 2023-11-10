import sys;
input = sys.stdin.readline

N, H = map(int, input().split())

dp = [0] * (H + 1)

for i in range(N):
    num = int(input());
    if i % 2 == 0 :
        dp[0] = dp[0] + 1
        dp[num] = dp[num] - 1;
    else :
        dp[H - num] = dp[H - num] + 1
        dp[H] = dp[H] - 1;

answer = [0] * (H + 1)
answer[0] = dp[0]
for i in range(1, H):
    answer[i] = answer[i - 1] + dp[i]
minNo = min(answer[0:H])    

cnt = 0
for i in range(0, H):
    if answer[i] == minNo:
        cnt += 1

print(minNo, cnt)