import sys;
input = sys.stdin.readline

N = int(input())
number_cards = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

answer = []
for number in targets:
    s = 0
    e = N - 1
    flag = 0
    
    while s <= e :
        mid = (s + e)//2
        
        if number_cards[mid] == number:
            flag = 1
            break;
        elif number_cards[mid] > number:
            e = mid - 1
        else :
            s = mid + 1
    answer.append(flag)

print(*answer)