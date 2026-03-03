class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s="0"
        table = string.maketrans('01', '10')
        for i in range (1,n):
            invt = s.translate(table)[::-1]
            s = s+'1'+invt
        return s[k-1]
        