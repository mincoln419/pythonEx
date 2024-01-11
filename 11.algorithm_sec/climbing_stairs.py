class Solution(object):
    def climbStairs(self, n):

        memo = {}
        def bottom_up(n):
            
            for i in range(1, n + 1):
                if i in {1, 2}:
                    memo[i] = i
                if i not in memo:
                    memo[i] = memo[i - 1] + memo[i - 2]
            return memo[n]
        return bottom_up(n)

        