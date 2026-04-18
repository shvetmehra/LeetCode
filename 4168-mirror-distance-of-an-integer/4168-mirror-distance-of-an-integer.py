class Solution:
    def mirrorDistance(self, n: int) -> int:
        d = abs(n-(int(str(n)[::-1])))
        return d
        