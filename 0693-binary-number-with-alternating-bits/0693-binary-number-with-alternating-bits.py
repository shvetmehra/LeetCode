class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = bin(n)[2:]
        x = len(n)
        for i in range (x-1):
            if n[i]==n[i+1]:
                return False
        return True

        