import sys;
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())

link = [list(map(int, input().split())) for _ in range(E)]


link.sort(key = lambda x:x[2])


par = [i for i in range(1_000_001)]
rank = [0 for _ in range(1_000_000)]

def _find(x):
    while par[x] != x:
        x = par[x]
    return x

def _union(a, b):
    a = _find(a)
    b = _find(b)
    if a == b:
        return
    if rank[a] < rank[b]:
        par[a] = b
    elif rank[b] < rank[a]:
        par[b] = a
    else:
        par[a] = b
        rank[b] += 1

ans = 0
#[A, B, C]
for i in range(E):
    A = link[i][0]
    B = link[i][1]
    weight = link[i][2]
    A = _find(A)
    B = _find(B)
    
    if A == B:
        continue
    else:
        _union(A, B)
        ans += weight
        
print(ans)
     
        
