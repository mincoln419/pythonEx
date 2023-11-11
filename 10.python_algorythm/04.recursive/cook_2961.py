import sys;
input = sys.stdin.readline
sys.setrecursionlimit(999999)

N = int(input())
ingre = [list(map(int, input().split())) for _ in range(N)]

answer = [1_000_000_000]
def recur(idx, sweet, salty, useYn):
    
    if idx == N :
        if answer[0] > abs(sweet  - salty):
            if(useYn == 0):
                return
            answer[0] = abs(sweet  - salty)
        return
    
    recur(idx + 1, sweet * ingre[idx][0], salty + ingre[idx][1], useYn + 1)
    
    recur(idx + 1, sweet, salty, useYn)

recur(0, 1, 0, 0)

print(*answer)