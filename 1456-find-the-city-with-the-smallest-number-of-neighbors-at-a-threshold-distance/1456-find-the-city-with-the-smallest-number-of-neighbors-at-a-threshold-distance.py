import sys
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        adjMatrix = [[sys.maxsize for _ in range (n)] for _ in range (n)]
        for u, v, w in edges:
            adjMatrix[u][v]=w
            adjMatrix[v][u]=w
        for i in range (n):
            adjMatrix[i][i]=0
        
        for via in range (n):
            for i in range (n):
                for j in range (n):
                    if adjMatrix[i][via]!= sys.maxsize and adjMatrix[via][j]!= sys.maxsize:
                        adjMatrix[i][j]= min(adjMatrix[i][j], adjMatrix[i][via] + adjMatrix[via][j])
                        
        min_neigh = n
        city = -1
        for i in range (n):
            count = 0
            for j in range (n):
                if adjMatrix[i][j]<=distanceThreshold:
                    count +=1
            if count<=min_neigh:
                min_neigh = count
                city = i
        return city