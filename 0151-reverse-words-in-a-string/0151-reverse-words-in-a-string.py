class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        chars = self.cleanSpace(s)
        n = len(chars)

        
        self.reverseSegment(chars, 0, n - 1)

        
        start = 0
        for end in range(n + 1):
        
            if end == n or chars[end] == ' ':
                self.reverseSegment(chars, start, end - 1)
                start = end + 1
        
        return "".join(chars)

    def cleanSpace(self, s):
        n = len(s)
        chars = list(s)
        slow = 0
        fast = 0

        while fast < n:
            if chars[fast] != ' ':  # Found a character
                if slow != 0:       # If it's not the first word, add a single space
                    chars[slow] = ' '
                    slow += 1

        
                while fast < n and chars[fast] != ' ':
                    chars[slow] = chars[fast]
                    slow += 1
                    fast += 1
            fast += 1
        return chars[:slow]

    def reverseSegment(self, chars, left, right):
        
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1