class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        i0 = x # top pointer , start row
        i1 = x+k-1 # end pointer, end row
        while i0<i1:
            for j in range (y, y+k):
                grid[i0][j],grid[i1][j] = grid[i1][j], grid[i0][j]
            i0 = i0+1
            i1=i1-1
        return grid