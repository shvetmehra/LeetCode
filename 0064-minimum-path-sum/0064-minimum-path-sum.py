class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        prev = [0] * c  # Previous row's DP
        for i in range(0, r):
            curr = [0] * c  # Current row's DP
            for j in range(0, c):
                # Start cell
                if i == 0 and j == 0:
                    curr[0] = grid[0][0]
                    continue
                # Value from the cell above (prev row, same col)
                if i == 0:
                    up = float("inf")
                else:
                    up = prev[j]
                # Value from the left (current row, prev col)
                if j == 0:
                    left = float("inf")
                else:
                    left = curr[j - 1]
                curr[j] = grid[i][j] + min(up, left)
            prev = curr  # Move current row to prev
        return prev[c - 1]  # Last cell of last row