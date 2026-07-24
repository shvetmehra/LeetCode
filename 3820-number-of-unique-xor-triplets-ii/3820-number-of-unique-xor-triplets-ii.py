from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX_XOR = 2048
        
        unique_nums = list(set(nums))
        
        dp = [False] * MAX_XOR
        dp[0] = True
        
        for _ in range(3):
            nxt = [False] * MAX_XOR
            
            for cur in range(MAX_XOR):
                if not dp[cur]:
                    continue
                
                for v in unique_nums:
                    nxt[cur ^ v] = True
                    
            dp = nxt
            
        return sum(dp)