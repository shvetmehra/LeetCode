import heapq
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct_nums = set(nums) # Remove duplicates so we only track distinct maximums
        h = []
        for x in distinct_nums:
            heapq.heappush(h,x)
            if len(h)>3:
                heapq.heappop(h)
        if len(h)==3: # If we have 3 distinct numbers, the top of our min-heap is the 3rd max.
            return h[0]
        return max(h) # Otherwise, return the absolute maximum
        