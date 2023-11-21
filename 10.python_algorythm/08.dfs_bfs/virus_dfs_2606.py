import sys;
input = sys.stdin.readline
sys.setrecursionlimit(999999)

N = int(input())
M = int(input())
links = [list(map(int, input().split())) for _ in range(M)]

visited = [0] * (N + 1)
board = [[] for _ in range(N + 1)]
for link in links:    
    board[link[0]].append(link[1])
    board[link[1]].append(link[0])

answer = 0
def dfs(node):
    global answer
    for toNode in board[node]:   
        if visited[toNode] == 0 :
            visited[toNode] = 1
            answer += 1
            dfs(toNode)

visited[1] = 1
dfs(1)
print(answer)