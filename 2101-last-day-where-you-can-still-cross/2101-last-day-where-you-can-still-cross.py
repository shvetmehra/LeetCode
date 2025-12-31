class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        left = 0
        n = len(cells)
        right = n-1
        ans = 0

        while left<=right:
            grid = [[0 for _ in range(col)] for _ in range(row)]
            mid = (left+right)//2

            for i in range (0, mid+1):
                x = cells[i][0]
                y = cells[i][1]
                grid [x-1][y-1] = 1

            possible = False
            visited = [[False for _ in range(col)] for _ in range(row)]

            for i in range (0, col):
                if grid[0][i]==0 and self.dfs(grid, 0, i, visited):
                    possible = True
                    break
            
            if possible: 
                ans = mid+1
                left = mid+1
            else:
                right = mid-1
        return ans

    def dfs(self, grid, row, col, visited):
        if row < 0 or col <0 or row>=len(grid) or col >=len(grid[0]) or grid[row][col]==1 or visited[row][col]:
            return False

        if row == len(grid)-1:
            return True
        visited[row][col]=True
        return (self.dfs(grid, row-1, col, visited) or self.dfs(grid, row+1, col, visited) or self.dfs(grid, row, col-1, visited) or self.dfs(grid, row, col+1, visited))

        
        