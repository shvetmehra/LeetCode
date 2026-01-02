class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inventory = {}
        for n in nums:
            if n in inventory:
                return n
            inventory[n]=1
        