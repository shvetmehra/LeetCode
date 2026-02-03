# Solution with BFS
from collections import deque
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = [[0 for _ in range (cols)] for _ in range (rows)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if r==0 or c==0 or r==rows-1 or c==cols-1:
                    if grid[r][c]==1:
                        queue.append((r,c))
                        visited[r][c]=1
        while len(queue)!=0:
            i,j = queue.popleft()
            for x,y in [(-1,0),(1,0), (0,-1), (0,1)]:
                newi, newj = i+x, j+y
                if newi<0 or newj<0 or newi>=rows or newj>=cols:
                    continue
                if grid[newi][newj]==0:
                    continue
                if grid[newi][newj]==1 and visited[newi][newj]==0:
                    queue.append((newi, newj))
                    visited[newi][newj]=1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and visited[r][c]==0:
                    count +=1
        return count
        