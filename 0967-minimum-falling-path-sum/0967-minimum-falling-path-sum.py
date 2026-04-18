class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        prev = [None for _ in range (cols)]
        for j in range (cols):
            prev[j] = matrix[0][j]
        for i in range(1, rows):
            curr = [None]*cols
            for j in range(cols):
                if j==0:
                    left = float('inf')
                else:
                    left = prev[j-1]
                if j==cols-1:
                    right =  float('inf')
                else:
                    right = prev[j+1]
                up = prev[j]
                curr[j] = matrix[i][j]+min(up, left, right)
            prev = curr
        return min(prev)