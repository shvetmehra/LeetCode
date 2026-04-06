# A. Recursion 

class Solution:
    def solve(self, i, j, obstacleGrid, dp):
        
        if i<0 or j<0 or obstacleGrid[i][j]==1:
            return 0
        if i == 0 and j==0:
            return 1
        if dp[i][j] !=-1:
            return dp[i][j]
        up = self.solve(i-1, j, obstacleGrid, dp)
        left = self.solve(i, j-1, obstacleGrid, dp)
        dp[i][j] = up+left
        return dp[i][j]


    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range (m)]
        return self.solve(m-1, n-1, obstacleGrid, dp)