class Solution(object):
    def dfs(self, r,c, rows, cols, visited, grid):
        if r < 0 or c<0 or r>=rows or c>=cols:
            return
        if grid[r][c]=="0":
            return
        if visited[r][c]==1:
            return
        visited[r][c]=1
        self.dfs(r+1,c, rows, cols, visited, grid)
        self.dfs(r-1,c, rows, cols, visited, grid)
        self.dfs(r,c+1, rows, cols, visited, grid)
        self.dfs(r,c-1, rows, cols, visited, grid)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range (cols)] for _ in range (rows)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and visited[r][c]==0:
                    count +=1
                    self.dfs(r,c, rows, cols, visited, grid)
    
        return count