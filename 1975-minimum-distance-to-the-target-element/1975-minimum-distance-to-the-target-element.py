class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        min_d = float('inf')
        b = 0
        for i in range (0,n):
            if nums[i]==target:
                b = i
                res = abs(b-start)
                if res < min_d:
                    min_d = res
        return min_d
            