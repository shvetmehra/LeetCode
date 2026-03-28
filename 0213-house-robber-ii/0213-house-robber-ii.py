class Solution:
    
    def func(self, index, start, end, nums, dp):
        
        if index == start:
            return nums[index]
        if index<start:
            return 0
        if dp[index] !=-1:
            return dp[index]

        pick = nums[index]+self.func(index - 2, start, end, nums, dp)
        notpick = 0+self.func(index-1, start, end, nums, dp)
        dp[index] =  max(pick, notpick)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [-1]*(len(nums))
        first = self.func(len(nums)-1, 1, len(nums)-1, nums, dp)
        dp = [-1]*(len(nums))
        second = self.func(len(nums)-2, 0, len(nums)-2, nums, dp)
        
        return max(first, second)

        
        