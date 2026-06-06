class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        for i in range (n):
            prefix = len(set(nums[:i+1]))
            suffix = len(set(nums[i+1:]))
            ans[i] = prefix-suffix
        return ans
        