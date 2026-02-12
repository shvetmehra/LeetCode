class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        for i in range (n):
            count = defaultdict(int)
            for j in range (i,n):
                count[s[j]]+=1
                if len(set(count.values()))==1:
                    res = max(res, j-i+1)
        return res
        
        