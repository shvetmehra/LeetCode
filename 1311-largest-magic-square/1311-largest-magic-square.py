class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n= len(grid), len(grid[0])
        rowsum = [[0]*(n+1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                rowsum[i][j+1]=rowsum[i][j]+grid[i][j]
        colsum = [[0]*n for _ in range(m+1)]
        for j in range(n):
            for i in range(m):
                colsum[i+1][j]=colsum[i][j] + grid[i][j]
        
        for edge in range(min(m,n), 1, -1):
            for i in range(m-edge+1):
                for j in range(n-edge+1):
                    d1=sum(grid[i+k][j+k] for k in range(edge))
                    d2=sum(grid[i+k][j+edge-1-k] for k in range(edge))
                    if d1!=d2:
                        continue
                    is_magic = True
                    for k in range(edge):
                        rsum = rowsum[i+k][j+edge]-rowsum[i+k][j]
                        csum = colsum[i+edge][j+k]-colsum[i][j+k]
                        if rsum!=d1 or csum!=d1:
                            is_magic = False
                            break
                    if is_magic:
                        return edge
        return 1