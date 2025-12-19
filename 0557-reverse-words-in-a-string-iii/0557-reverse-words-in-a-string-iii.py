class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        n = len(chars)
        start = 0
        for end in range (n+1):
            if end == n or chars[end]==' ':
                left = start
                right = end-1
                while left<right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left +=1
                    right -=1
                start = end+1
        return "".join(chars)
        