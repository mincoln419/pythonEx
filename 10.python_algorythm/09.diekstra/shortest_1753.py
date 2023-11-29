import sys;
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())
K = int(input())
arr = [list(map(int, input().split())) for _ in range(E)]
dist = [1e9 for _ in range(V + 1)]

linkedMap = [[] for _ in range(V + 1)]

for u, v, w in arr:
    linkedMap[u].append([v, w]);
    
q = []
heapq.heappush(q, (0, K))
dist[K] = 0

while q:   
    heapq.heapify(q)
    _w, node = heapq.heappop(q)
    
    for nxt, weight in linkedMap[node]:
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = min(dist[node] + weight, dist[nxt])
        heapq.heappush(q, (dist[nxt], nxt))
        
for i in range(1, V + 1):
    
    if dist[i] == 1e9 :
        print("INF")
    else:
        print(int(dist[i]))





