import heapq
class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        h = []
        for x in nums:
            val = int(x) # in th code, nums contains strings. So, converting string in to number
            heapq.heappush(h,val)
            if len(h)>k:
                heapq.heappop(h)
        return str(h[0]) # Converting back to Strin :-)