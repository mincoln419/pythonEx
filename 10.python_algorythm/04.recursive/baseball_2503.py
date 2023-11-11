import sys;
input = sys.stdin.readline
sys.setrecursionlimit(999999)


N = int(input())
hint = [list(map(int, input().split())) for _ in range(N)]

answer = [0]

def recur(i, target):

    if i == N :
        if '0' not in str(target) and str(target)[0] != str(target)[1] and str(target)[1] != str(target)[2] and str(target)[2] != str(target)[0]:
            answer[0] += 1
        recur(0, target + 1)
        return
    
    if target > 999:
        return
    
    ball_point = 0
    strike_point = 0
    if str(hint[i][0])[0] in str(target) :
        if str(hint[i][0])[0] == str(target)[0]:
            strike_point +=1 
        else : 
            ball_point +=1
    if str(hint[i][0])[1] in str(target) :
        if str(hint[i][0])[1] == str(target)[1]:
            strike_point +=1 
        else : 
            ball_point +=1
    if str(hint[i][0])[2] in str(target) :
        if str(hint[i][0])[2] == str(target)[2]:
            strike_point +=1 
        else : 
            ball_point +=1
    if strike_point == hint[i][1] and ball_point == hint[i][2]:
        recur(i + 1, target)
    else :
        recur(0, target + 1)
        
recur(0, 100)
print(*answer)
    
    

