class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range (n):
            uodd = set()
            ueve= set()
            for j in range (i, n):
                if nums[j]%2==0:
                    ueve.add(nums[j])
                else:
                    uodd.add(nums[j])
                if len(ueve) == len(uodd):
                    result = max(result, j-i+1)
        return result