from collections import deque
class Solution(object):
    def bfs (self, i, j, grid, visited):
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        queue = deque()
        queue.append((i,j))
        visited[i][j]=1

        while len(queue)!=0:
            x,y = queue.popleft()
            for xx, yy in [(0,1),(0,-1),(1,0),(-1,0)]:
                newi, newj = x+xx, y+yy
                if newi<0 or newj<0 or newi>=rows or newj>=cols:
                    continue
                if grid[newi][newj]=='0':
                    continue
                if visited[newi][newj]==1:
                    continue
                visited[newi][newj]=1
                queue.append((newi,newj))            

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        count = 0
        for r in range(rows):
            for c in range (cols):
                if grid[r][c]=='1' and visited[r][c]==0:
                    count+=1
                    self.bfs(r,c,grid,visited)
        return count
    