class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        return 2*sum(set(nums))- sum(nums)
        