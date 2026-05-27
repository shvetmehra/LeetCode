class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        firstupper = {}
        lastlower = {}
        
        for i, char in enumerate (word):
            if char.islower():
                lastlower[char]=i
            elif char.isupper() and char.lower() not in firstupper:
                firstupper[char.lower()]=i
        count = 0
        for char in lastlower:
            if char in firstupper and lastlower[char]<firstupper[char]:
                count +=1
        return count
        