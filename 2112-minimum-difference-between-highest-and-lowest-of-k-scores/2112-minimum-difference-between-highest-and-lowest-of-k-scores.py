class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans = float('inf')
        if n == 0 or n == 1:
            return 0
        nums = sorted(nums)[::-1]
        for i in range (n-k+1):
            result = nums[i]-nums[i+k-1]
            ans = min(ans, result)
        return ans