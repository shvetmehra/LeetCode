class Solution(object):
    def dfs(self, currentNode, visited, graph, color):
        visited[currentNode]=color
        for adjNode in graph[currentNode]:
            if visited [adjNode]!=-1:
                if visited[adjNode]==color:
                    return False
            else:
                ans = self.dfs(adjNode, visited, graph, 1-color )
                if ans == False:
                    return False
        return True

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        totalNodes = len(graph)
        visited = [-1]*totalNodes
        for i in range(0, totalNodes):
            if visited[i]==-1:
                ans = self.dfs(i, visited, graph, 0)
                if ans == False:
                    return False
        return True
        