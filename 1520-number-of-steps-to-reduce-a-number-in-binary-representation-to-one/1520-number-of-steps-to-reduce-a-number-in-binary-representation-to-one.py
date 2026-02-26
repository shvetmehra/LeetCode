class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = int(s,2)
        count = 0
        while s >1:
            
            if s%2 ==0:
                s//=2
                count +=1
            else:
                s +=1
                count +=1
    
        return count
        