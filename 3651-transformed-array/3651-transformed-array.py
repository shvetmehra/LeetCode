class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        result = [0]*n
        if n==0:
            return []

        for i in range (n):
            target = (i+nums[i])%n
            result[i]=nums[target]        
        return result

        