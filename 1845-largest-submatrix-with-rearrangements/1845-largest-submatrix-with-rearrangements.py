from collections import deque
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        count = 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for r in range (rows):
            for c in range (cols):
            
                if matrix[r][c]==1 and r>0:
                    matrix[r][c]+=matrix[r-1][c]
            curr_row = sorted(matrix[r], reverse=True)

            for i in range(cols):
                height = curr_row[i]
                width = i+1
                count = max(count, height * width)
        return count