# Tabulation - Space Optimization
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prev = [0]*n

        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return 0
        for r in range (m):
            curr = [0]*n
            for c in range (n):
                if obstacleGrid[r][c]==1:
                    curr[c]=0
                elif r == 0 and c == 0:
                    curr[c]=1
                else:
                    up = prev[c] if r>0 else 0
                    left = curr[c-1] if c>0 else 0
                    curr[c] = up+left
            prev = curr
        return prev[n-1]
                
