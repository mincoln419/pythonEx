class Solution(object):
    def dailyTemperatures(self, temperatures):
        
        stack = []
        answer = [0] * len(temperatures)
        for cur_day, cur_temp in enumerate(temperatures):            
            while stack and stack[-1][1] < cur_temp:
                prev_day, _ = stack.pop()
                answer[prev_day] = cur_day - prev_day
            else:
                stack.append((cur_day, cur_temp))       
        return answer
    
print(Solution().dailyTemperatures( temperatures = [73,74,75,71,69,72,76,73]))