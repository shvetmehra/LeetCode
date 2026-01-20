class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in nums:
            if n%2 == 0:
                ans.append(-1)
            else:
                lowestZeroBit = (~n)&-(~n)
                ans.append(n-(lowestZeroBit>>1))
        return ans
        