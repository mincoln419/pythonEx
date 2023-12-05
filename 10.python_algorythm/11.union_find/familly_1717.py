import sys;
input = sys.stdin.readline
sys.setrecursionlimit(99999)


N, M = map(int, input().split())
parents = [i for i in range(N + 1)]
rank = [0 for _ in range(N + 1)]


def _union(A, B):
    
    A = _find(A)
    B = _find(B)
    
    if A == B :
        return
    
    if rank[A] < rank[B]:
        parents[A] = B
    elif rank[A] > rank[B]:
        parents[B] = A
    else:
        parents[A] = B
        rank[B] += 1
    
    

def _find(node):    
    if parents[node] == node:
        return node
    parents[node] = _find(parents[node])
    return parents[node] 

for _ in range(M):
    x, A, B = map(int, input().split())
    if x == 0 :
        _union(A, B)
    else:
        if _find(A) == _find(B):
            print("YES")
        else:
            print("NO")