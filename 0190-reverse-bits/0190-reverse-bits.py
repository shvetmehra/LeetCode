class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_str = '{:032b}'.format(n)
        reverse =bin_str[::-1]

        return int(reverse, 2)
        