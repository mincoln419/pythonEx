import sys;
input = sys.stdin.readline
from collections import deque

Y, X = map(int, input().split())

board = [list(input().rstrip()) for _ in range(Y)]

maxLen = 0

for y in range(Y):
    for x in range(X):
        if board[y][x] == 'L':
            visited = [[0] * X for _ in range(Y)]
            dist = [[0] * X for _ in range(Y)]
            
            q = deque()
            q.append([y, x])
            visited[y][x] = 1
            while q :
                ey, ex = q.popleft()                
                for dy, dx in [[0, 1],[0, -1], [1, 0], [-1, 0]]:
                    ny, nx = ey + dy, ex + dx
                    if 0 <= ny < Y and 0 <= nx < X:
                        if board[ny][nx] == 'L':
                            if visited[ny][nx] == 0:
                                visited[ny][nx] = 1
                                dist[ny][nx] = dist[ey][ex] + 1
                                maxLen = max(maxLen, dist[ny][nx])
                                q.append([ny, nx])
print(maxLen)