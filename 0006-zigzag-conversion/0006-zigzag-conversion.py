class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n =len(s)
        res = [[] for _ in range (numRows)]
        if numRows == 1:
            return s
        down = True
        j = 0
        for i in range(0,n):
            res[j].append(s[i])
    
            if down == True:
                if j == numRows-1:
                    j-=1
                    down = False
                else:
                    j+=1
            else:
                if j==0:
                    j+=1
                    down = True
                else:
                    j-=1
        s = ""
        for lst in res:
            for c in lst:
                s+=c
        return s