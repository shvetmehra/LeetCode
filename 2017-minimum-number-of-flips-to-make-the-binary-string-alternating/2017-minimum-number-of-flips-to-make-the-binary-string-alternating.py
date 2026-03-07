class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        
        i = 0
        j = 0
        flip1 = 0
        flip2 = 0
        res = float('inf')
        s1 = ""
        s2 = ''
        for x in range (2*n):
            s1 += '0' if x%2 == 0 else '1'
            s2 += '1' if x%2 == 0 else '0'
              
        while j <2*n:
            if s[j%n]!= s1[j]:
                flip1+=1
            if s[j%n]!= s2[j]:
                flip2+=1
            
            if (j-i+1)>n:
                if s[i%n]!=s1[i]:
                    flip1 -=1
                if s[i%n]!=s2[i]:
                    flip2 -=1
                i+=1
            if (j-i+1)==n:
                res = min(res, flip1, flip2)
            j +=1
        return res