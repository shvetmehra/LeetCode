class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[None for _ in range(cols)] for _ in range (rows)]
        for j in range(cols):
            dp[0][j] = matrix[0][j]
        for i in range(1, rows):
            for j in range(cols):
                if j==0:
                    left = float('inf')
                else:
                    left = matrix[i][j]+dp[i-1][j-1]
                if j==cols-1:
                    right =  float('inf')
                else:
                    right = matrix[i][j] + dp[i-1][j+1]
                up = matrix[i][j]+dp[i-1][j]
                dp[i][j]=min(up, left, right)
        ans = float('inf')
        for j in range(cols):
            ans = min(ans, dp[rows-1][j])
        return ans 
        