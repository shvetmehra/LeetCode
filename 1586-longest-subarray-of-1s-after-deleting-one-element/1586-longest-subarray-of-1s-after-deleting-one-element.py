class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zero = 0
        result = 0

        for right in range (len(nums)):
            if nums[right]==0:
                zero +=1
            
            if zero>1:
                if nums[left]==0:
                    zero -=1
                left +=1
            
            result = max(result, right-left)
        
        return result
        