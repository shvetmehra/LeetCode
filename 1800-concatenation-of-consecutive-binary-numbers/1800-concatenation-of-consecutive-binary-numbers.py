class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9+7
        add = ""
        for i in range(1,n+1):
            i = bin(i)[2:]
            add =add+str(i) 
        return int(add,2)%mod