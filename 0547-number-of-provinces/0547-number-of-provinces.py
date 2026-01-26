class Solution(object):
    #Helper
    def dfs(self, i, adjMatrix, visited):
        visited[i]=True
        for x in range(len(adjMatrix)):
            if adjMatrix [i][x]==1 and not visited [x]:
                self.dfs(x, adjMatrix, visited)
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        ans = 0
        visited = [False]*n
        for x in range (n):
            if not visited[x]:
                self.dfs(x, isConnected, visited)
                ans +=1
        return ans
        