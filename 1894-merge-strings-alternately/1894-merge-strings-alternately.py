class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = ""
        for a, b in zip(word1, word2):
            ans += a + b
        ans += word1[len(word2):]
        ans += word2[len(word1):]
        return ans


        