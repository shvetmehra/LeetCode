from typing import List 
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        num_set = set(nums)
        if not nums:
            return []
        for i in range (min(nums), max(nums)+1):
            if i not in num_set:
                res.append(i)
        return res