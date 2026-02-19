import sys
import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows = len(heights)
        cols = len(heights[0])
        efforts = [[sys.maxsize for _ in range (cols)] for _ in range (rows)]
        efforts[0][0]=0
        queue = [[0,0,0]]

        while len(queue)!=0:
            eff, i, j = heapq.heappop(queue)
            if i==rows-1 and j==cols-1:
                return eff
            for x, y in [[-1,0],[1,0],[0,-1],[0,1]]:
                newi, newj = i+x, j+y
                if newi<0 or newj<0 or newi>=rows or newj>=cols:
                    continue
                new_eff = max(eff, abs(heights[newi][newj]- heights[i][j]))
                if new_eff < efforts[newi][newj]:
                    efforts[newi][newj]=new_eff
                    heapq.heappush(queue, [new_eff, newi, newj])        