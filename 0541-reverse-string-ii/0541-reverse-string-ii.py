class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        chars = list(s)
        for i in range(0, len(chars), 2*k):
            left = i
            right = min(i+k-1, len(chars)-1)

            while left<right:
                chars[left], chars[right] = chars[right], chars[left]
                left +=1
                right -=1
        return "".join(chars)
        