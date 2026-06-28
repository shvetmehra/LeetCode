class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        res = 0
        for i in arr:
            res = min(res+1, i)
        return res
        