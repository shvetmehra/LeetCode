class Solution:
    mod = 10**9+7
    def dfs(self, a, b, c): #gxf
        depth = 0
        for y in a[b]:
            if y == c:
                continue
            depth = max(depth, self.dfs(a,y,b)+1)
        return depth
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        if not edges:
            return 1
        n = len(edges)+1
        a =[[]for _ in range (n+1)]
        for u, v in edges:
            a[u].append(v)
            a[v].append(u)
        depth = self.dfs(a,1,0)
        return pow(2, depth-1, self.mod)