class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev, curr, ans = 0,1,0
        for i in range(1, len(s)):
            if s[i]!=s[i-1]:
                ans += min(prev, curr)
                prev = curr
                curr=1
            else:
                curr+=1
        ans += min(prev,curr)
        return ans
        