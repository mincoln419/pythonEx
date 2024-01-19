class Solution(object):
    def uniquePaths(self, m, n):
        memo = [[-1] * (n + 1) for _ in range(m + 1)]
        def dfs(y, x):
            if memo[y][x] >= 0:
                return memo[y][x]
            if y == 0 or x == 0 :
                memo[y][x] = 1
            else :
                memo[y][x] = dfs(y - 1, x) + dfs(y, x - 1)
            
            return memo[y][x]

        return dfs(m -1 , n - 1)


print(Solution().uniquePaths(3, 7))