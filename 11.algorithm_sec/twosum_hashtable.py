class Solution(object):
    def twoSum(self, nums, target):
        answer = []
        n = len(nums)
        dics = {}
        for i in range(n):
            dics[nums[i]] = (i , nums[i])
        
        for i , num in enumerate(dics):
            if target - num in dics:
                answer.append(i)
                answer.append(dics[target - num][0])
                break
        answer.sort()
        return answer

print(Solution().twoSum(nums = [2,7,11,15], target = 9))