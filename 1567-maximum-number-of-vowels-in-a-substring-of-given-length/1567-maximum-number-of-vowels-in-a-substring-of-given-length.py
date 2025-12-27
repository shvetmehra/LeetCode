class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiouAEIOU')
        curr = 0
        maxVowels = curr

        for i in range (k):
            if s[i] in vowels:
                curr +=1
        maxVowels = curr
        for i in range (k, len(s)):
            if s[i] in vowels:
                curr +=1
            if s[i-k] in vowels:
                curr -=1
            maxVowels = max(curr, maxVowels)
        return maxVowels