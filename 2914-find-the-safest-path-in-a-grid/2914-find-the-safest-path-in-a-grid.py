from typing import List
from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            i, j = q.popleft()
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < n and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))

        if dist[0][0] == 0 or dist[n - 1][n - 1] == 0:
            return 0

        best = [[-1] * n for _ in range(n)]
        best[0][0] = dist[0][0]

        pq = [(-dist[0][0], 0, 0)]

        while pq:
            safe, i, j = heapq.heappop(pq)
            safe = -safe

            if safe < best[i][j]:
                continue

            if i == n - 1 and j == n - 1:
                return safe

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < n:
                    new_safe = min(safe, dist[ni][nj])
                    if new_safe > best[ni][nj]:
                        best[ni][nj] = new_safe
                        heapq.heappush(pq, (-new_safe, ni, nj))

        return 0