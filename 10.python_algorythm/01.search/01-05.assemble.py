N = int(input())

members = [list(map(int, input().split())) for _ in range(N)]


minX = 1_000_000
minY = 1_000_000
loc = [[0 for j in range(N)] for i in range(N)]
for y in range(members.len()) :
    for x in range(members.len()) : 
        loc[y][x] = members[y][x]
        
print(loc)

answer = []
answer.sort()


            
            

