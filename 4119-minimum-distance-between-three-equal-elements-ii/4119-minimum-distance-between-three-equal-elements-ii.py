class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        ans = float('inf')

        for indices in pos.values():
            if len(indices)<3:
                continue
            for i in range (len(indices)-2):
                a = indices[i]
                c = indices[i+2]
                dist = 2*(c-a)
                ans = min(ans, dist)
        if ans != float('inf'):
            return ans
        else:
            return -1

        