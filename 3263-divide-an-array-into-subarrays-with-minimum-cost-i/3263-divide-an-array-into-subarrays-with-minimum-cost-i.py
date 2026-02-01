class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_val = nums[0]
        remaining = nums[1:]
        remaining.sort()
        return first_val + remaining[0]+remaining[1]

        