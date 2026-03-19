class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        prefx = [[0] * (cols+1) for _ in range (rows+1)]
        prefy = [[0] * (cols+1) for _ in range (rows+1)]
        for r in range (rows):
            for c in range (cols):
                is_x =1 if grid[r][c] == 'X' else 0
                prefx[r+1][c+1]= is_x+prefx[r+1][c]+prefx[r][c+1]-prefx[r][c]

                is_y =1 if grid[r][c] == 'Y' else 0
                prefy[r+1][c+1]= is_y +prefy[r+1][c]+prefy[r][c+1]-prefy[r][c]

                if prefx[r+1][c+1] == prefy[r+1][c+1] and prefx[r+1][c+1] > 0:
                    ans +=1
        return ans 