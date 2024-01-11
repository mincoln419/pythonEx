class Solution(object):
    def climbStairs(self, n):

        memo = {}
        def dfs(n):
            if n in {1, 2}:
                memo[n] = n          
            if n not in memo:
                memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]
        return dfs(n)

        