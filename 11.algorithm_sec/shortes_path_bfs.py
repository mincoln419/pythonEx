from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        nx = [1, -1, 1, -1, 0, 0, 1, -1]
        ny = [1, -1, -1, 1, 1, -1, 0, 0]
        
        n = len(grid)

        q.append((0, 0, 0))
        visited = [[0] * n for _ in range(n)]
        visited[0][0] = 1
        answer = 0
        while q :
            fy, fx, cnt = q.popleft()
            print(fx, fy, cnt)
            if fy == n - 1 and fx == n - 1 :
                answer = cnt
                break;

            for i in range(8) :
                dx = fx + nx[i]
                dy = fy + ny[i]
                if dx < 0 or dx >= n or dy < 0 or dy >= n:
                    continue
                if visited[dy][dx] == 1 or grid[dy][dx] == 1:
                    continue
                visited[dy][dx] = 1
                q.append((dy, dx, cnt + 1))
        
        return answer
                    
                    
grid = [[0,1],[1,0]]
print(Solution().shortestPathBinaryMatrix(grid))