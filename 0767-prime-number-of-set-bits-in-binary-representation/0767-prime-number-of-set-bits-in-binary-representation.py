class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # Optimized Version

        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        res = 0
        for i in range (left, right+1):
            count1 = bin(i).count('1')
            # Fatest built-in way in pythong to count!
            if count1 in primes:
                res +=1
        return res 
        