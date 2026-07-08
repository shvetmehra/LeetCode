from typing import List
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9+7
        n = len(s)
        power_of_ten = [1]*(n+1)
        for i in range(1, n+1):
            power_of_ten[i] = (power_of_ten[i-1]*10)%MOD
        digit_prefix = [0]*(n+1)
        nonZeroPrefix = [0]*(n+1)
        concatPrex = [0]*(n+1)
        for i in range(n):
            digit = int(s[i])
            digit_prefix[i+1]=digit_prefix[i]+digit
            nonZeroPrefix[i+1]=nonZeroPrefix[i]+(1 if digit>0 else 0)
            if digit>0:
                concatPrex[i+1]=(concatPrex[i]*10+digit)%MOD
            else:
                concatPrex[i+1]=concatPrex[i]
        answer = []
        for left, right in queries:
            nonZero = nonZeroPrefix[right+1]-nonZeroPrefix[left]
            totalDigitSum=digit_prefix[right+1]-digit_prefix[left]
            number_x=((concatPrex[right+1])-concatPrex[left]*power_of_ten[nonZero])%MOD
            answer.append((number_x*totalDigitSum)%MOD)
        return answer