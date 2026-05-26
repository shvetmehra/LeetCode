class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        uniqueChar = set(word)
        ans = 0
        for char in uniqueChar:
            if char.islower() and char.upper() in uniqueChar:
                ans +=1
        return ans