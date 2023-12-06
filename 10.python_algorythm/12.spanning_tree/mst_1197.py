import sys;
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
visited = [ 0 for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())    
    graph[A].append([C, B])
    graph[B].append([C, A])
    
answer = 0
cnt = 0
    
q = [[0, 1]]

while q:
    
    if cnt == V:
        break
    
    weight, node = heapq.heappop(q)
    
    if visited[node] == 0 :
        visited[node] = 1
        answer += weight
        cnt += 1
        for nxt in graph[node]:
            heapq.heappush(q, nxt)


print(answer)