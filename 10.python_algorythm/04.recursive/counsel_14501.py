import sys;
input = sys.stdin.readline
sys.setrecursionlimit(999999)
import copy

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def recur(idx, price):
    global answer
    if idx == N:
        if answer < price:
            answer = price
        return
    if idx > N:
        return
    recur(idx + arr[idx][0], price + arr[idx][1])
    recur(idx + 1, price)
    

recur(0, 0)
print(answer)