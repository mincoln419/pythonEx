import sys;
input = sys.stdin.readline
sys.setrecursionlimit(99999)

N = int(input())

graph = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(N + 1)]
def recur(node, prv):
    
    parents[node] = prv
        
    for nxt in graph[node]:
        if visited[nxt] == 1:
            return
        visited[nxt] = 1
        recur(nxt, node)
        visited[nxt] = 0
    

visited[1] = 1
recur(1, 0)

for parent in parents:
    if parent > 0:
        print(parent)

