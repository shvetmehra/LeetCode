class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_val = float('inf')
        for num in nums:
            currentsum = 0
            while num>0:
                currentsum += num%10
                num//=10
            min_val = min(min_val, currentsum)
        return min_val
        