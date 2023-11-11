import sys;
input = sys.stdin.readline
sys.setrecursionlimit(999999)
import copy

N = int(input())
min_cal = list(map(int, input().split()))
cal = [list(map(int, input().split())) for _ in range(N)]

answer = [1_000_000_000]
answerArr = []
def recur(idx, prot, carbo, prov, vita, price, idxArr):
    global answerArr
    if idx == N :
        if prot >= min_cal[0] and carbo >= min_cal[1] and prov >= min_cal[2] and vita >= min_cal[3] and  answer[0] > price:
            if(len(idxArr) == 0):
                return
            
            answer[0] = price
            answerArr = copy.deepcopy(idxArr)
        return   
        
    
    if cal[idx][0] == 0 and cal[idx][1] == 0 and cal[idx][2] == 0 and cal[idx][3] == 0:
        recur(idx + 1, prot, carbo, prov, vita, price, idxArr)
    else:
        idxArr.append(idx + 1)
        recur(idx + 1, prot + cal[idx][0], carbo + cal[idx][1], prov + cal[idx][2], vita + cal[idx][3], price + cal[idx][4], idxArr)
        idxArr.pop()
        recur(idx + 1, prot, carbo, prov, vita, price, idxArr)
    

recur(0, 0, 0, 0, 0, 0, [])
if answer[0] == 1_000_000_000:
    print(-1)
else:    
    print(*answer)
    answerArr.sort()
    print(*answerArr)