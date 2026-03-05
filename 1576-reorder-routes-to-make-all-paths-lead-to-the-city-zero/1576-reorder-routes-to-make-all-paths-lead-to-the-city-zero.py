class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(dict)
        for a, b in connections:
            graph[a][b]=1
            graph[b][a]=0
        queue = collections.deque([0])
        ans = 0
        vis = set()
        vis.add(0)

        while queue:
            curr_node = queue.popleft()
            for adjnode, score in graph[curr_node].items():
                if adjnode not in vis:
                    ans +=score
                    queue.append(adjnode)
                    vis.add(adjnode)
        return ans