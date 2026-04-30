# Memoization  

class Solution:
    def solve(self, i, j, k, grid, dp):
        if k<0:
            return float('-inf')
        if i == 0 and j == 0:
            cost = 1 if grid[0][0] in [1,2] else 0
            if k>=cost:
                return grid[0][0]
            return float('-inf')
            
        if i<0 or j<0:
            return float('-inf')
        curr_score = grid[i][j]
        curr_cost = 1 if grid[i][j] in [1,2] else 0
        if dp[i][j][k]!=-1:
            return dp[i][j][k]
        up = self.solve(i-1, j,k-curr_cost, grid, dp)
        left= self.solve(i, j-1,k-curr_cost, grid, dp)
        res = curr_score + max(left, up)
        dp[i][j][k]=res
        return res
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[-1 for _ in range (k+1)] for _ in range (n)] for _ in range (m)]
        
        result= self.solve(m-1,n-1,k, grid, dp)
        return int(result) if result>float('-inf') else -1