class Solution(object):
    def countBits(self, n):
        # Initialize the DP array with 0s
        dp = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n + 1):
            # When we reach a new power of 2, update the offset
            if offset * 2 == i:
                offset = i
            
            # The number of bits is 1 + the bits in (current index - current power of 2)
            dp[i] = 1 + dp[i - offset]
            
        return dp
        