import heapq
import collections

class Solution(object):
    def minCost(self, n, edges):
        # adj[u] will store (neighbor, cost, is_reverse)
        adj = collections.defaultdict(list)
        for u, v, w in edges:
            # Normal: u -> v
            adj[u].append((v, w, False))
            # Reverse: u can use switch to go back to v if the edge was v -> u
            adj[v].append((u, 2 * w, True))

        # Because n is large, we cannot use a bitmask.
        # But wait! If we use node u's switch, we move to v. 
        # The switch is used AT u. 
        # Since we want the MINIMUM cost, we only need to track:
        # dist[u][0] = min cost to reach u without using u's switch yet
        # dist[u][1] = min cost to reach u after having used u's switch
        
        # Actually, the simplest interpretation for n = 50,000 is 
        # that the "once per node" limit applies to that specific visit.
        # Let's use a 2-state Dijkstra:
        # State: (cost, node, switch_used_at_this_node_specifically)
        
        pq = [(0, 0, 0)] # (cost, u, used_at_u)
        # dist[(u, used_at_u)]
        dist = collections.defaultdict(lambda: float('inf'))
        dist[(0, 0)] = 0
        
        while pq:
            d, u, used = heapq.heappop(pq)
            
            if d > dist[(u, used)]:
                continue
            if u == n - 1:
                return d
            
            for v, w, is_reverse in adj[u]:
                if is_reverse:
                    # If this move requires a switch at u, 
                    # we can only do it if used == 0
                    if used == 0:
                        if d + w < dist[(v, 0)]: # After move, v's switch is fresh (0)
                            dist[(v, 0)] = d + w
                            heapq.heappush(pq, (d + w, v, 0))
                else:
                    # Normal move: doesn't use u's switch
                    # u's switch status doesn't transfer to v
                    if d + w < dist[(v, 0)]:
                        dist[(v, 0)] = d + w
                        heapq.heappush(pq, (d + w, v, 0))
                        
        return -1