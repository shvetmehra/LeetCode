class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = 0
        for x in nums:
            sum += x
        ls = 0
        for i in range (0,n):
            
            rs = sum - ls - nums[i]
            if ls == rs:
                return i
            ls += nums[i]
        return -1
        