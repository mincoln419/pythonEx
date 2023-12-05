import sys;
input = sys.stdin.readline
sys.setrecursionlimit(99999)


N, M = map(int, input().split())
parents = [i for i in range(N + 1)]

def _union(parent, child):
    parents[_find(child)] = _find(parent)

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