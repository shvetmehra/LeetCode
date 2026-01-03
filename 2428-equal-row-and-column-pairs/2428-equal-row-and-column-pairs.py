import collections
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_count = collections.Counter(tuple(row) for row in grid)
        n = len(grid)
        count = 0
        for c in range (n):
            col = tuple(grid[r][c] for r in range(n))

            count += row_count[col]
        return count
        