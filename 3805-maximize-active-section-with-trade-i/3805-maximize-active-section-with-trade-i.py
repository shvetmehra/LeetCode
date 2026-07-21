class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        max_gains = prev = cur = 0
        for c in s:
            if c == '0':
                cur += 1
            elif prev == 0:
                prev, cur = cur, 0
            elif prev > 0 < cur:
                max_gains = max(max_gains, prev + cur)
                prev, cur = cur, 0 
        if prev > 0 < cur:
            max_gains = max(max_gains, prev + cur)        
        return ones + max_gains