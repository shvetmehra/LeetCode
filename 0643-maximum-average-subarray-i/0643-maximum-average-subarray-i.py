class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        average = sum(nums[:k])
        maxSum = average
        for i in range (k, len(nums)):
            average = average + nums[i] - nums[i-k]
            maxSum = max(average, maxSum)
        return float(maxSum)/k
        