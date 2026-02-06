class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        i= 0
        l = 0
        if n ==0:
            return 0
        for j in range (n):
            while nums[j]>nums[i]*k:
                i+=1
            l = max(l, j-i+1)
        return n - l
