class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        
        res = 0
        for i in range (left, right+1):
            count1 = 0
            bin_str = '{:032b}'.format(i)
            for j in bin_str:
                if j=='1':
                    count1 +=1
            if count1 > 1 and all(count1 % x != 0 for x in range(2, int(count1**0.5) + 1)):

                res+=1
        return res

        