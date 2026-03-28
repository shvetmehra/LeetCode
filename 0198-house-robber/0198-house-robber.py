# Tabulation Space Optimaztion
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len (nums)
        prev = nums[0]
        prev2 = 0

        for index in range (1, n):
            if index>1:
                pick = nums[index]+prev2
            else:
                pick = nums[index]
            notpick = prev
        
            curr = max (pick, notpick)
            prev2 = prev
            prev = curr
        return prev