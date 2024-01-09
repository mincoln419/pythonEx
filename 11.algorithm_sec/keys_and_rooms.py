import sys;
input = sys.stdin.readline
sys.setrecursionlimit(999999)

class Solution(object):
      
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        
        visited = [0] * (n + 1)
        
        def dfs(node):
            visited[node] = 1
            for nextRoom in rooms[node]:
                if visited[nextRoom] == 0 :
                    dfs(nextRoom)
        
        dfs(0)
        
        return sum(visited) == n
        
sampleroom = [[1],[2],[3],[]]
print(Solution().canVisitAllRooms(rooms = sampleroom))
        
        
        
        
        