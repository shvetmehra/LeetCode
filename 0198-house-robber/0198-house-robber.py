# Tabulation - Bottoms Up
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        dp[0] = nums[0]
        if n == 0:
            return 0
        if n == 1:
            return nums[0]        

        for index in range (1, n):
            if index>1:
                pick = nums[index] + dp[index-2]
            else:
                pick = nums[index] +0
        
            notpick = 0+dp[index-1]

            dp[index] = max(pick, notpick)
        return dp[n-1]