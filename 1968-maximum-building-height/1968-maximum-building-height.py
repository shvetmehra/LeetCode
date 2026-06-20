from typing import List
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if n == 1:
            return 0
        points = [(1,0)]
        for index, h in restrictions:
            points.append((index, h))
        if not any(index == n for index, _ in restrictions):
            points.append((n, n - 1)) 
        points.sort()
        pos = [p[0] for p in points]
        lim = [p[1] for p in points]
        m = len(pos)
        for i in range(1, m):
            lim[i] = min(lim[i], lim[i - 1] + pos[i] - pos[i - 1])

        for i in range(m - 2, -1, -1):
            lim[i] = min(lim[i], lim[i + 1] + pos[i + 1] - pos[i])

        ans = 0
        for i in range(m - 1):
            d = pos[i + 1] - pos[i]
            ans = max(ans, (lim[i] + lim[i + 1] + d) // 2)

        return ans