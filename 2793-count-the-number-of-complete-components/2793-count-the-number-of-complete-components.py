from typing import List
class Solution:
    def dfs(self, node, adjList, visited, comp_nodes):
        visited[node]=1
        comp_nodes.append(node)
        for adjNode in adjList[node]:
            if visited[adjNode]==0:
                self.dfs(adjNode, adjList, visited, comp_nodes)

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList= [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        visited = [0]*n
        complete_comp = 0

        for i in range(n):
            if visited[i]==0:
                comp_nodes = []
                self.dfs(i,adjList,visited,comp_nodes)
                count = len(comp_nodes)
                edgesum = 0
                for u in comp_nodes:
                    edgesum +=len(adjList[u])
                if edgesum == count *(count-1):
                    complete_comp+=1
        return complete_comp