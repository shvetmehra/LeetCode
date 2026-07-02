from typing import List
from collections import deque
import heapq
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n = len(grid)
        m = len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        best =[[-1]*m for _ in range (n)]
        startingHealth = health-grid[0][0]
        if startingHealth<=0:
            return False
        best[0][0]=startingHealth
        pq = [(-startingHealth, 0, 0)] 
        while pq:
            safe, i, j = heapq.heappop(pq)
            safe = -safe
            if safe <best[i][j]:
                continue
            if i == n-1 and j == m-1:
                return True 
            for dx, dy in directions:
                newi, newj = i + dx, j +dy
                if 0<=newi<n and 0<=newj<m:
                    newsafe = safe- grid[newi][newj]
                    if newsafe >best[newi][newj] and newsafe>=1:
                        best[newi][newj]=newsafe
                        heapq.heappush (pq, (-newsafe, newi, newj))
        return False