class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        pref = [[0]* (cols - k + 1) for _ in range (rows - k +1) ]

        for i in range (rows - k+1):
            for j in range (cols - k+1):
                gridN = []
                for x in range (i, i+k):
                    for y in range (j, j+k):
                        gridN.append(grid[x][y])
                kmin = float("inf")
                gridN.sort()

                for t in range(1, len(gridN)):
                    if gridN[t]==gridN[t-1]:
                        continue
                    kmin = min(kmin, gridN[t]-gridN[t-1])

                if kmin != float("inf"):
                    pref[i][j] = kmin
        return pref
        