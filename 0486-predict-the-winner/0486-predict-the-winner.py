class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = list(nums)
        for i in range (2, n+1):
            for j in range (n-i+1):
                k = j + i-1
                dp[j] = max(nums[j] - dp[j + 1], nums[k] - dp[j])
        return dp[0]>=0