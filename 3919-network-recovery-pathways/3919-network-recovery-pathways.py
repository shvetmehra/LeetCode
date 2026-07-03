from typing import List
import heapq 
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adjlist = [[] for _ in range (n)]
        min_c= float('inf') 
        max_c=-float('inf')
        for u, v, cost in edges:
            if v == n-1 or online [v]:
                adjlist[u].append((v, cost))
                min_c = min(min_c, cost)
                max_c = max(max_c, cost)
        if min_c == float('inf'):
            return -1
        def solve(targetscore):
            pq = [ (0, 0)]
            mincost = [float('inf')]*n
            mincost[0]=0
            
            while pq:
                totalcost, node = heapq.heappop(pq)
                if totalcost>mincost[node]:
                    continue
                   
                if node == n-1:
                    return totalcost<=k

                for v, edgecost in adjlist[node]:
                    if edgecost<targetscore:
                        continue
                    newcost = totalcost+edgecost
                    if newcost<=mincost[v] and newcost<=k:
                        mincost[v]=newcost
                        heapq.heappush(pq, (newcost, v))
            return False
        low, high = min_c, max_c
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if solve(mid):
                ans = mid  # Yeh score possible hai, aur bada try karte hain
                low = mid + 1
            else:
                high = mid - 1
                
        return ans