from collections import deque

class Solution(object):

    

    def numIslands(self, grid):
        
        cnt = 0
        
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        nx = [0, 0, 1, -1]
        ny = [1, -1, 0 , 0]
        
        def bfs(x, y):
            
            queue = deque()
            queue.append((x, y))
            while queue:
                fx, fy = queue.popleft()                
                for i in range(4):                    
                    dx = fx + nx[i]
                    dy = fy + ny[i]
                    
                    if dx >= n or dx < 0 or dy >= m or dy < 0 or visited[dy][dx] == 1 :
                        continue
                    if grid[dy][dx] == "0":
                        continue
                    
                    queue.append((dx, dy))
                    visited[dy][dx] = 1
                
            return
        
        for y in range(m):
            for x in range(n):
                if visited[y][x] == 0:
                    visited[y][x] = 1
                    if grid[y][x] == "1" :
                        print(x, y)
                        bfs(x, y)
                        cnt += 1
        
        return cnt
    
         
                
grid = [["1","1"],["1","1"]]
print(Solution().numIslands(grid = grid))