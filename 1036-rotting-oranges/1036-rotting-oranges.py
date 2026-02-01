from collections import deque
from copy import deepcopy
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols= len(grid[0])
        gridCopy = deepcopy(grid)

        freshCount = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if gridCopy[r][c]==2:
                    queue.append((r,c))
                elif gridCopy[r][c]==1:
                    freshCount +=1

        minute = 0
        while len(queue)!=0 and freshCount>0:
            minute+=1
            totalRotten=len(queue)
            for i in range(totalRotten):
                i,j = queue.popleft()
                for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                    newi = i+dx
                    newj = j+dy
                    if newi<0 or newi==rows or newj<0 or newj==cols:
                        continue
                    if gridCopy[newi][newj]==0 or gridCopy[newi][newj]==2:
                        continue
                    freshCount-=1
                    gridCopy[newi][newj]=2
                    queue.append((newi,newj))
        if freshCount>0:
            return -1
        return minute