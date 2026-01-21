import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        h = []
        for x in nums:
            heapq.heappush(h,x)
            if len(h)>k:
                heapq.heappop(h)
        return h[0]
        