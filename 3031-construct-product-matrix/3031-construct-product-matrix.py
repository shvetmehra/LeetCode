class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        MOD = 12345
        p = [[0]*cols for _ in range (rows)]

        suffix =1
        for r in range (rows-1,-1,-1): #going backwards
            for c in range (cols-1, -1, -1):
                p[r][c] = suffix
                suffix = (suffix * grid[r][c])%MOD
        prefix = 1

        for r in range (rows): # Going Forward
            for c in range (cols):
                p[r][c] = (p[r][c] * prefix) %MOD
                prefix = (prefix * grid[r][c])%MOD
        return p