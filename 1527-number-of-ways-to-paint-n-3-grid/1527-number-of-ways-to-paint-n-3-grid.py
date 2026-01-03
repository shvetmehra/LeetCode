class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        aba = 6
        abc = 6
        mod = 10**9+7
        for i in range (1,n):
            next_aba = (3 * aba + 2 * abc) % mod
            next_abc = (2 * aba + 2 * abc) % mod

            aba = next_aba
            abc = next_abc
        return(aba+abc)%mod
