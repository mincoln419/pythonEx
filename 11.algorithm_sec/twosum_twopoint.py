class Solution(object):
    def twoSum(self, nums, target):
        answer = []
        n = len(nums)
        nums_copy = [[nums[i], i] for i in range(n)]
        nums_copy.sort()
        s = 0
        e = n - 1 
        while True:
            n_sum = nums_copy[s][0] + nums_copy[e][0]
            if n_sum == target:
                answer.append(nums_copy[s][1])
                answer.append(nums_copy[e][1])
                break
            elif n_sum > target:
                e = e - 1
            elif n_sum < target:
                s = s + 1
            if s == e :
                break
        return answer