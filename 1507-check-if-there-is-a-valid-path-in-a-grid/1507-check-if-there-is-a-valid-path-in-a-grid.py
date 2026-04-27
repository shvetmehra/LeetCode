class Solution:
    def dfs(self, r,c,grid,visited, rows, cols, directions):
        if r == rows-1 and c==cols-1:
            return True
        visited.add((r,c))

        for dr, dc in directions[grid[r][c]]:
            newRow, newCol = r+dr, c+dc
            if 0 <= newRow < rows and 0 <= newCol < cols and (newRow, newCol) not in visited:
                if (-dr,-dc) in directions[grid[newRow][newCol]]:
                    if self.dfs(newRow, newCol, grid, visited,rows, cols, directions  ):
                        return True
        return False
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        visited = set()
        return self.dfs(0,0,grid, visited, rows, cols, directions)