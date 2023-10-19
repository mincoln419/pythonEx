from operator import itemgetter, attrgetter
N = int(input())

members = [list(map(int, input().split())) for _ in range(N)]

locX = []
locY = []
for i in range(N) :
    memX = members[i][0]
    memY = members[i][1]
    if memX not in locX: 
        locX.append(memX)
    if memY not in locY:
        locY.append(memY)
        
memberLen = []

for i in range(N) :
    memberLen.append([])

for y in locY:
    for x in locX:
        lenAdd = 0
        for i in range(len(members)):
            lenAdd += abs(x - members[i][0]) + abs(y - members[i][1])
            memberLen[i].append([x, y, lenAdd])     


for answer in memberLen :
    answer = sorted(answer, key=itemgetter(2))
    print(answer[0][2])


            

