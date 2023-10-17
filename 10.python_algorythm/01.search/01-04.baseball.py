tryN = int(input())

hint = [list(map(int, input().split())) for _ in range(tryN)]

answer = 0
for a in range(1, 10):
    for b in range(1,10):
        for c in range(1,10):
            cnt = 0
            if( a == b or b == c or c == a):
                continue
            

            for arr in hint:
                number = str(arr[0])
                strike = arr[1]
                ball = arr[2]
                ball_cnt = 0
                strike_cnt = 0
                
                
                if number[0] == str(a):
                    strike_cnt += 1
                elif str(a) in number:
                    ball_cnt += 1
                    
                if number[1] == str(b) :
                    strike_cnt += 1
                elif str(b) in number:
                    ball_cnt += 1
                    
                if number[2] == str(c) :
                    strike_cnt += 1
                elif str(c) in number:
                    ball_cnt += 1

                if ball == ball_cnt and strike == strike_cnt:
                    cnt += 1         
                        
            if cnt == tryN:
                answer += 1

print(answer)