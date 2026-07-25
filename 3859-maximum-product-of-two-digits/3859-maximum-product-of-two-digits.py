class Solution:
    def maxProduct(self, n: int) -> int:
        max1 = 0
        max2 = 0
        while n>0:
            dig = n%10
            if dig>max1:
                max2 = max1
                max1 = dig
            elif dig>max2:
                max2=dig
            n//= 10
        return max1*max2
        