class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixsum = [0] * (n + 1)
        suffixsum = [0] * (n + 1)
        for i in range(n):
            prefixsum[i + 1] = prefixsum[i] + nums[i]
        for i in range (n-1, -1, -1):
            suffixsum[i]=suffixsum[i+1]+nums[i]
        ans = [0]*n
        for i in range (n):
            ans[i] = abs(prefixsum[i]-suffixsum[i+1])
        return ans        