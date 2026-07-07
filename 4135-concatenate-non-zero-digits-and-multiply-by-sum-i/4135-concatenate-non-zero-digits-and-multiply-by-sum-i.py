class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=0
        ans =0
        placeValue=1
        if n == 0:
            return 0
        while n>0:
            digit=n%10
            if digit!=0:
                x+=digit
                ans +=digit*placeValue
                placeValue*=10
            n//=10
        return ans*x

