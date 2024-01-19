import sys;
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
links = [list(map(int, input().split())) for _ in range(M)]

visited = [0] * (N + 1)
board = [[] for _ in range(Nppp + 1)]
for link in links:    
    board[link[0]].append(link[1])
    board[link[1]].append(link[0])

q = deque()
q.append(1)

while len(q) > 0 :
    node = q.popleft()
    visited[node] = 1
    
    for nextNode in board[node]:
        if visited[nextNode] == 1:
            continue
        q.append(nextNode)
 
 
print(sum(visited) - 1)
