class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1]*n for _ in range (n)]
        for j in range (0,n):
            dp[n-1][j] = triangle[n-1][j]
        for i in range (n-2, -1, -1):
            for j in range (0, i+1):
                down = (triangle [i][j])+dp[i+1][j]
                diag = (triangle [i][j])+dp[i+1][j+1]
                dp[i][j] = min(down, diag)
        return dp[0][0] 
        