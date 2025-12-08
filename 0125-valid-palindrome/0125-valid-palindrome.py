class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = "".join(ch.lower() for ch in s if ch.isalnum())
        if clean == clean[::-1]:
            return True
        else:
            return False
        