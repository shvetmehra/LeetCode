class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = 0
        for x in nums:
            sum +=x
        cs = 0
        for i in range (0,n):
            ls = cs
            rs = sum - cs - nums[i]
            if ls == rs:
                return i
            cs +=nums[i]
        return -1
        