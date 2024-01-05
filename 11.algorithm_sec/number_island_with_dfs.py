class Solution(object):

    _grid = []
    _m = 0
    _n = 0
    _visited = []
    _dx = [-1, 1, 0, 0]
    _dy = [0, 0, 1, -1]

    def numIslands(self, grid):

        self._grid = grid
        self._m = len(grid)
        self._n = len(grid[0])
        self._visited = [[0] * self._n for _ in range(self._m)]
        print(self._visited)
        cnt = 0
        for y in range(self._m):
            for x in range(self._n):
                if self._visited[y][x] == 0 :
                    self._visited[y][x] = 1
                    if self._grid[y][x] == "1" :
                        
                        self.dfs(y, x)
                        cnt += 1
        return cnt

    def dfs(self, fy, fx):
        self._visited[fy][fx] = 1

        for i in range(4):
            print(fy, fx)
            dy = fy + self._dy[i]
            dx = fx + self._dx[i]
            print("dy,dx",dy, dx)
            print("m, n",self._m, self._n)

            if dy >= self._m or dy < 0 or dx >= self._n or dx < 0:
                continue
            if self._grid[dy][dx] == "1" and self._visited[dy][dx] == 0:                
                self.dfs(dy, dx)
        
        return
                
grid = [["1","1"],["1","1"]]
print(Solution().numIslands(grid = grid))