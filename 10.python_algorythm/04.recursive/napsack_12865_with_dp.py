import sys;
input = sys.stdin.readline
sys.setrecursionlimit(999999)

A, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(A)]

dp = [[-1] * 100_001 for _ in range(A + 1)]
def recur(idx, w):
    if w > B :
        return -9999999999999
    if idx == A :
        return 0
    
    if dp[idx][w] > 0:
        return dp[idx][w]
    
    dp[idx][w] = max(recur(idx + 1, w + arr[idx][0]) + arr[idx][1], recur(idx + 1, w))
    
    return dp[idx][w]

print(recur(0, 0))
#print(dp)