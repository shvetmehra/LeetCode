from collections import Counter
from typing import List
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = Counter()
        left = 0
        maxlength = 0
        for right in range (len(nums)):
            freq[nums[right]]+=1
            while freq[nums[right]]>k:
                freq[nums[left]]-=1
                left +=1
            maxlength = max(maxlength, right-left+1)
        return maxlength