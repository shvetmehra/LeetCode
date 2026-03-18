class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        prefGrid = [[0]*(cols+1) for _ in range (rows +1)]

        for r in range (rows):
            for c in range (cols):
                prefGrid[r+1][c+1] = (grid[r][c] + 
                                    prefGrid[r+1][c] + 
                                    prefGrid[r][c+1] - 
                                    prefGrid[r][c])
                if prefGrid[r+1][c+1]<=k:
                    ans +=1
                else:
                    break
        return ans
        