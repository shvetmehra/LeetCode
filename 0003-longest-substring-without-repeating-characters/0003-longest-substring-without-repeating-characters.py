class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        """
        n = len(s)
        if n ==0:
            return 0
        ans = 0
        st = set()
        left = 0
        
        for right in range (n):
            while s[right] in st:
                st.remove(s[left])
                left +=1
            st.add(s[right])
            ans = max(ans, right - left+1)
        return ans