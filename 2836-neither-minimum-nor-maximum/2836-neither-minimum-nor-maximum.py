class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = sorted(nums)[:-1]
        m = n[1:]
        if len(m)== 0:
            return -1
        else:
            return m[0]
        