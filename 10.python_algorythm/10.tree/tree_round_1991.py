import sys;
input = sys.stdin.readline
from collections import deque

N = int(input())

graph = [[] for _ in range(130)]

for _ in range(N):
    a, b, c = map(str,input().split())
    # 아스키 코드로
    a = ord(a)
    b = ord(b)
    c = ord(c)
    
    graph[a].append(b)
    graph[a].append(c)
    


def preRecur(node):
    if node == 46:
        return    
    print(chr(node), end = "")
    preRecur(graph[node][0])
    preRecur(graph[node][1])
    
def midRecur(node):
    if node == 46:
        return    
    midRecur(graph[node][0])
    print(chr(node), end = "")
    midRecur(graph[node][1])
    
def postRecur(node):
    if node == 46:
        return    
    postRecur(graph[node][0])
    postRecur(graph[node][1])
    print(chr(node), end = "")


preRecur(65)
print()
midRecur(65)
print()
postRecur(65)


