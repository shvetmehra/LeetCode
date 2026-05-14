from typing import List
from collections import Counter
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        if n ==1:
            return False
        counts = Counter(nums)
        for num in range (1, n):
            if num == n-1:
                if counts[num]!=2:
                    return False
            else:
                if counts[num]!=1:
                    return False
        return True
