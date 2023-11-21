import sys;
input = sys.stdin.readline
sys.setrecursionlimit(999999)

A = input().strip()
B = input().strip()

dp = [[-1] * (len(B) + 1) for _ in range(len(A) + 1)]

       
def recur(y, x):    
    if y < 0 or x < 0 : 
        return 0
    if dp[y][x] > -1 :
        return dp[y][x]
        
    if A[y] == B[x]:
        dp[y][x] = recur(y - 1, x - 1) + 1
    else :
        dp[y][x] = max(recur(y - 1, x), recur(y, x - 1))
    
    return dp[y][x]

print(recur(len(A) - 1, len(B) - 1))