class Solution:
    def solve(self, i, j, grid, dp):
        if i==0 and j==0:
            return grid[i][j]
        if i<0 or j<0:
            return float('inf')
        if dp[i][j] !=-1:
            return dp[i][j]
        
        up = self.solve(i-1, j,grid, dp)
        left = self.solve(i, j-1, grid, dp)
        dp[i][j] = grid[i][j]+min(up,left)  
        return dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp = [[-1 for _ in range (n)] for _ in range (m)]
        return self.solve(m-1, n-1,grid, dp)

        