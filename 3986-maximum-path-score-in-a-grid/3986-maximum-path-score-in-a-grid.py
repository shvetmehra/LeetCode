# Tabulation   

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[-float('inf')] * (k + 1) for _ in range(n)] for _ in range(m)]
        val = grid[0][0]
        start = grid[0][0]
        cost = 1 if grid[0][0] in [1,2] else 0
        if cost <=k:
            dp[0][0][cost]= val
        for i in range (m):
            for j in range(n):
                for c in range (k+1):
                    if dp[i][j][c]==-float('inf'):
                        continue
                    if j + 1 < n:
                        val = grid[i][j+1]
                        cost = 1 if val in [1, 2] else 0
                        if c + cost <= k:
                            dp[i][j+1][c + cost] = max(dp[i][j+1][c + cost], dp[i][j][c] + val)
                            
                    # Try moving Down
                    if i + 1 < m:
                        val = grid[i+1][j]
                        cost = 1 if val in [1, 2] else 0
                        if c + cost <= k:
                            dp[i+1][j][c + cost] = max(dp[i+1][j][c + cost], dp[i][j][c] + val)
                                
        ans = max(dp[m-1][n-1])
        return int(ans) if ans > -float('inf') else -1
