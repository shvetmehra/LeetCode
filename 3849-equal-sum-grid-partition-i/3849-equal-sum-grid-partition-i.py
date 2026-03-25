class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        totalSum = 0
        rowSum = [0] * rows
        colSum = [0] * cols

        for r in range (rows):
            for c in range (cols):

                totalSum += grid[r][c]
                rowSum[r] += grid[r][c]
                colSum[c] += grid[r][c]
                
        if totalSum %2 != 0:
            return False
        #Horizontal Split
        upperSum = 0
        for i in range (rows-1):
            upperSum += rowSum[i]
            if upperSum == totalSum-upperSum: #calculating and validating lowersum in a single go
                return True

        #Horizontal Split
        leftSum = 0
        for j in range (cols-1):
            leftSum += colSum[j]
            if leftSum == totalSum-leftSum: #calculating and validating rightsum in a single go
                return True
        return False