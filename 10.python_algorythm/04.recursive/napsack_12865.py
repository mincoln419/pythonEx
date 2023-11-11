import sys;
input = sys.stdin.readline
sys.setrecursionlimit(999999)
import copy

A, B = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(A)]

answer = 0
def recur(idx, w, price):
    global answer
    if idx == A:
        if w > B :
            return
        answer = max(answer, price)
        return
    
    recur(idx + 1, w + arr[idx][0], price + arr[idx][1])
    recur(idx + 1, w, price)
    
recur(0, 0, 0)
print(answer)