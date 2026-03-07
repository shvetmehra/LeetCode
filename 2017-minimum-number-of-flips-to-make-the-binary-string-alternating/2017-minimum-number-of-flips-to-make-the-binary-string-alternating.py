class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        
        i = 0
        j = 0
        flip1 = 0
        flip2 = 0
        res = float('inf')
              
        while j <2*n:
            expected_s1 = '0' if j % 2 == 0 else '1'
            expected_s2 = '1' if j % 2 == 0 else '0'
            
            if s[j % n] != expected_s1:
                flip1 += 1
            if s[j % n] != expected_s2:
                flip2 += 1
            
            if (j - i + 1) > n:
                old_s1 = '0' if i % 2 == 0 else '1'
                old_s2 = '1' if i % 2 == 0 else '0'
                
                if s[i % n] != old_s1:
                    flip1 -= 1
                if s[i % n] != old_s2:
                    flip2 -= 1
                i += 1
            
            if (j - i + 1) == n:
                res = min(res, flip1, flip2)
                
            j += 1
            
        return res