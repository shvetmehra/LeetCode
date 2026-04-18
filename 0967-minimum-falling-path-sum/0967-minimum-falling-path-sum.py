class Solution:
    def solve(self, i, j, matrix, dp):
        if j<0 or j>=len(matrix[0]):
            return float('inf')
        if i==0:
            return matrix[0][j]
        if dp[i][j]!= None:
            return dp[i][j]
        up = matrix[i][j]+self.solve(i-1, j, matrix, dp)
        left = matrix[i][j] +self.solve(i-1, j-1, matrix, dp)
        right = matrix[i][j] +self.solve(i-1, j+1, matrix, dp)
        dp[i][j]=min(up, left, right)
        return dp[i][j]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[None for _ in range (m)] for _ in range(n)] 
        ans = float('inf')
        for j in range (0, n):
            ans = min(ans, self.solve(m-1, j, matrix, dp))
        return ans