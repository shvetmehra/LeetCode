from copy import deepcopy
from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        distance = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()

        for r in range (rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append([r,c,0])
                    visited[r][c]=1
        while len(queue)!=0:
            i,j,d = queue.popleft()
            distance [i][j]= d

            for x,y in [(-1,0),(0,-1),(0,1),(1,0)]:
                newi, newj = i+x, j+y
                if newi<0 or newi>=rows or newj<0 or newj>=cols:
                    continue
                if visited[newi][newj]==1:
                    continue
                queue.append([newi, newj, d+1])
                visited[newi][newj]=1
        return distance