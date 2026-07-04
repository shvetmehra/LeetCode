from collections import deque
from typing import List
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        adjlist = [[] for _ in range (n+1)]
        for u, v, cost in roads:
            adjlist[u].append((v, cost))
            adjlist[v].append((u, cost))
        queue = deque([1])
        visited = set([1])
        ans = float('inf')
        while len(queue)!=0:
            node = queue.popleft()
            for v, cost in adjlist[node]:
                ans = min(ans, cost)
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
        return ans