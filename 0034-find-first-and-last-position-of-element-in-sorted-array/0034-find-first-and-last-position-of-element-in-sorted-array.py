class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.firstindex (nums, target, 0), self.lastindex(nums, target, 0)]
    
    def firstindex(self, nums, target, index):
        if len (nums) == index:
            return -1
        if nums[index] == target:
            return index
        return self.firstindex (nums, target, index +1)

    def lastindex(self, nums, target, index):
        if len (nums) == index:
            return -1
        ans = self.lastindex (nums, target, index +1)
        if ans != -1:
            return ans
        if nums[index]== target:
            return index
        return -1
        
        