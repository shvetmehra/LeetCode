import sys
import heapq
class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        mod = 10**9+7

        adjList = [[] for _ in range (n)]
        for u, v, w in roads:
            adjList[u].append([v,w])
            adjList[v].append([u,w])
        distance = [sys.maxsize for _ in range (n)]
        ways = [0 for _ in range (n)]

        distance[0]=0
        ways[0]=1

        pq = [[0,0]]

        while len(pq)!=0:
            dist, node = heapq.heappop(pq)
            for adjNode, weight in adjList[node]:
                newDist = dist + weight
                if newDist<distance[adjNode]:
                    distance[adjNode]= newDist
                    heapq.heappush(pq,[newDist, adjNode])
                    ways[adjNode]= ways[node]
                elif newDist == distance[adjNode]:
                    ways[adjNode]+=ways[node]
        
        return ways[n-1]%mod
        