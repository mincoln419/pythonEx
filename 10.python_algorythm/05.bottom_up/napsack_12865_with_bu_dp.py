import sys;
input = sys.stdin.readline
sys.setrecursionlimit(999999)

A, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(A)]

dp = [[-1] * 100_001 for _ in range(A + 1)]

for idx in range(1, A + 1):
    for w in range(1 , B + 1):
        if w > B :
            dp[idx][w] = dp[idx - 1][w]
        else :
            dp[idx][w] = max(dp[idx - 1][w - arr[idx - 1][0]] + arr[idx - 1][1], dp[idx - 1][w])    

print(max(dp[A]))
