class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortednums = sorted(nums)

        for i in range (0, len(sortednums)-1,2):
            sortednums[i], sortednums[i+1] = sortednums[i+1], sortednums[i]
        return sortednums
        