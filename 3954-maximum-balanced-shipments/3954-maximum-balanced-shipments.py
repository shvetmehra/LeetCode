class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        count = 0
        max_weight = 0
        for w in weight:
            if max_weight >w:
                count +=1
                max_weight = 0
            else:
                max_weight = max(max_weight, w)
        return count
                
