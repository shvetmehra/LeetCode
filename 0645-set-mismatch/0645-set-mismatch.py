class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        s1 = sum(nums)
        s2 = sum(set(nums))
        dup = s1-s2
        miss = (n*(n+1))//2 - s2

        return [ dup, miss]
        