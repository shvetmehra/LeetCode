class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        n = len(cost)
        i = 0
        totalcost = 0
        while i < n:
            totalcost += cost[i]
            if i +1 <n:
                totalcost +=cost[i+1]
            i +=3
        return totalcost
        