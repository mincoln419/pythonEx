import sys;
input = sys.stdin.readline

N, M = map(int, input().split())
table = [[0] * (N + 1)]
for _ in range(N):
    table.append([0] + [int(x) for x in input().split()])
    
answerArr = [[0] * (N + 1) for _ in range(N + 1)]
for y in range(1 , N + 1) :
    for x in range(1, N + 1):        
        answerArr[y][x] = answerArr[y - 1][x] + answerArr[y][x - 1] - answerArr[y-1][x-1] + table[x][y] 

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = answerArr[y2][x2] - answerArr[y1 - 1][x2] - answerArr[y2][x1 - 1] + answerArr[y1 - 1][x1 - 1]
    print(ans)

