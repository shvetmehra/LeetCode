class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        res = [1]*length
        leftProduct = 1
        for i in range (length):
            res[i] = leftProduct
            leftProduct *= nums[i]
        rightProduct =1
        for i in range(length-1,-1,-1):
            res[i] *= rightProduct
            rightProduct *= nums[i]
        return res

        