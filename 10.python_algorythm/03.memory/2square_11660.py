N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
targetXy = [list(map(int, input().split())) for _ in range(M)] #x1, y1, x2, y2

print(table)
print(targetXy)


answerArr = [[0 for j in range(N)] for i in range(N)]

answerArr[0][0] = table[0][0]


for i in range(1 , N):       
    answerArr[0][i] = answerArr[0][i - 1] + table[0][i]
    answerArr[i][0] = answerArr[i - 1][0] + table[i][0]            
            

for y in range(1, N) :
    for x in range(1, N):        
        answerArr[y][x] = answerArr[y - 1][x] + answerArr[y][x - 1] - answerArr[y - 1][x - 1] + table[y][x] 


print(answerArr)

for x1, y1, x2, y2 in targetXy:
    print("{}{}{}{}".format(x1, y1, x2, y2))
    
    if x1 > 1 and y1 > 1 :
        answer =  answerArr[y2-1][x2-1] - answerArr[y1 - 2][x2 - 1] - answerArr[y2 - 1][x1 - 2] + answerArr[y1 - 2][x1 - 2]
        print(answer)
    


    