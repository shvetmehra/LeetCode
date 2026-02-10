# Now with DFS
class Solution:
    def dfs(self, currentNode, adjList, vis, pathVis, isSafe):
        vis[currentNode]=1
        pathVis[currentNode]=1

        for adjNode in adjList[currentNode]:
            if vis[adjNode]==0:
                ans = self.dfs(adjNode, adjList, vis, pathVis, isSafe)
                if ans == False:
                    return False
            elif pathVis[adjNode]==1:
                return False

        isSafe[currentNode]=1
        pathVis[currentNode]=0
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v = len(graph)
        vis = [0 for _ in range (v)]
        pathVis = [0 for _ in range (v)]
        isSafe = [0 for _ in range(v)]

        for i in range (0,v):
            if vis[i]==0:
                self.dfs(i, graph, vis, pathVis, isSafe)

        result = []
        for i in range(v):
            if isSafe[i]==1:
                result.append(i)
        return result