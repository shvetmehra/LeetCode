class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x):
            res = 0
            while x>0:
                x,d = divmod(x, 10)
                res = 10* res+d
            return res
        hashmap = {}
        mod = inf
        for i, x in enumerate(nums):
            rev = reverse(x)
            if x in hashmap:
                mod = min(mod, i-hashmap[x])
            hashmap[rev]=i
        return -1 if mod==inf else mod

        