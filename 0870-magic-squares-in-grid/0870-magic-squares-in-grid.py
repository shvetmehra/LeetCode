class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        count = 0

        if row <3 or col <3:
            return 0

        for r in range (row-2):
            for c in range (col-2):
                number = []

                for i in range (r, r+3):
                    for j in range (c, c+3):
                        number.append(grid[i][j])
                if sorted(number)==[1,2,3,4,5,6,7,8,9]:
                    row1 = grid[r][c] + grid[r][c+1] + grid[r][c+2]
                    row2 = grid[r+1][c]+ grid[r+1][c+1] + grid[r+1][c+2]
                    row3 = grid[r+2][c]+ grid[r+2][c+1] + grid[r+2][c+2]

                    col1 = grid[r][c] + grid[r+1][c] + grid[r+2][c]
                    col2 = grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1]
                    col3 = grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2]

                    diag1 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
                    diag2 = grid[r][c+2]+ grid[r+1][c+1] + grid[r+2][c]

                    if len({row1, row2, row3, col1, col2, col3, diag1, diag2}) == 1:
                        count +=1
        return count