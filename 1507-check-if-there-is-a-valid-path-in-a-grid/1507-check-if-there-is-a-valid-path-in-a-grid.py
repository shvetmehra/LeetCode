from collections import deque
from typing import List
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        directions = {
                    1: [(0, -1), (0, 1)],
                    2: [(-1, 0), (1, 0)],
                    3: [(0, -1), (1, 0)],
                    4: [(0, 1), (1, 0)],
                    5: [(0, -1), (-1, 0)],
                    6: [(0, 1), (-1, 0)]
                }
        queue = deque([(0,0)])
        visited = set([(0,0)])
        # for r in range (rows):
        #     for c in range (cols):
        #         if r==0 or c==0 or r==rows-1 or c==cols-1:
        #             queue.append((r,c))
        #             visited[r][c]=1
        while len(queue)!=0:
            i,j=queue.popleft()
            if (i,j)==(rows-1, cols-1):
                return True
            for dr,dc in directions[grid[i][j]]:
                newi,newj=i+dr, j+dc
                if 0<=newi<rows and 0<= newj<cols:
                    if( newi, newj) in visited:

                        continue
                
                    if (-dr,-dc) in directions[grid[newi][newj]]:
                        visited.add((newi, newj))
                        queue.append((newi, newj))
        return False
   