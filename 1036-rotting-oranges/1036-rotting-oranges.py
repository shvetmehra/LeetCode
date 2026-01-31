from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        grid_copy = deepcopy(grid)

        freshCount = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid_copy[r][c]==2:
                    queue.append((r,c))
                elif grid_copy[r][c]==1:
                    freshCount +=1
        minute = 0
        while len(queue)!=0 and freshCount>0:
            minute+=1
            totalRotten = len(queue)

            for i in range (totalRotten):
                i,j = queue.popleft()
                for dx, dy in [(0,1), (1,0),(-1,0), (0,-1)]:
                    newi, newj = i+dx, j+dy
                    if newi<0 or newi==rows or newj<0 or newj==cols:
                        continue
                    if grid_copy[newi][newj] == 0 or grid_copy[newi][newj]==2:
                        continue
                    freshCount -=1
                    grid_copy[newi][newj]=2
                    queue.append((newi,newj))
        if freshCount>0:
            return -1
        return minute

        