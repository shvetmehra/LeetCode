class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        # OPTIMIZED

        res = 0
        mod = 10**9 + 7
        bit_length = 0
        
        for i in range(1, n + 1):

            if i & (i - 1) == 0:
                bit_length += 1
            
            # Shift existing result to the left to make room, then add i
            res = ((res << bit_length) | i) % mod
            
        return res
        