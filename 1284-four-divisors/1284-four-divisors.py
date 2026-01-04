import math
class Solution(object):
    def findSumOfDivisor(self, n):
        divisor = []
        
        for fact in range (1, int(math.sqrt(n))+1):
            if n % fact == 0:
                divisor.append(fact)
                if fact*fact != n:
                    divisor.append(n//fact)
                     
            if len(divisor) > 4:
                return 0
        
        if len(divisor) == 4:
            return sum(divisor)
        return 0

    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalSum = 0
        
        for i in nums:
            totalSum += self.findSumOfDivisor(i)
        
        return totalSum