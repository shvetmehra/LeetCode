class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        sortedgrid = [val for row in grid for val in row]
        sortedgrid.sort()
        n = len(sortedgrid)
        count = 0
        median = sortedgrid[n//2]
        rem = sortedgrid[0]%x
 
        for i in sortedgrid:
            if i %x !=rem:
                return -1
            
            count += abs(i-median)//x

        return count
