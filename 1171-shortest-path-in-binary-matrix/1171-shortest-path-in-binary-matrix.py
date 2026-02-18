import sys
from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0]==1:
            return -1
        rows = len(grid)
        cols = len(grid[0])

        distance = [[sys.maxsize for _ in range (cols)] for _ in range (rows)]
        distance[0][0]=1
        queue = deque()
        queue.append([1, 0,0])

        while len(queue)!=0:
            dist,i,j = queue.popleft()
            for x, y in [[1,0], [1,-1],[0,-1],[-1,-1],[-1,0], [-1,1], [0,1], [1,1]]:
                newi, newj = i+x, j+y
                if newi<0 or newi>=rows or newj<0 or newj>=cols:
                    continue
                if grid[newi][newj]==1:
                    continue
                dist_trav = dist+1
                if dist_trav<distance[newi][newj]:
                    if newi==rows-1 and newj==cols-1:
                        return dist_trav
                    distance[newi][newj] = dist_trav
                    queue.append([dist_trav, newi, newj])
        if distance[rows-1][cols-1]==sys.maxsize:
            return -1
        return distance[rows-1][cols-1]

        