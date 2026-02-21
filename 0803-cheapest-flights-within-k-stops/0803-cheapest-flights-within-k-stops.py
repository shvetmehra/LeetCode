from collections import deque
import sys
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        adjList = [[] for _ in range (n)]
        for u, v, cost in flights:
            adjList[u].append([v, cost])
        minCost = [sys.maxsize for _ in range (n)]
        minCost[src]=0

        queue = deque()
        queue.append([0, src, 0]) # steps, source, code

        while len(queue)!=0:
            steps, node, cost = queue. popleft()
            for adjNode, price in adjList[node]:
                newCost = cost+price
                if newCost<minCost[adjNode]:
                    minCost[adjNode] = newCost 
                    newsteps = steps+1
                    if newsteps == k+1:
                        if adjNode!=dst:
                            continue

                    queue.append([newsteps, adjNode, newCost])
        if minCost[dst]==sys.maxsize:
            return -1
        else:
            return minCost[dst]