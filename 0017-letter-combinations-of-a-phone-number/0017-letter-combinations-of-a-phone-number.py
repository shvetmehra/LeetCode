class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone_keys = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': '',
            '1': ''
        }
        ans = []
        if digits == "":
            return []

        if len(digits)== 1:
            return list(phone_keys[digits[0]])
            
        smallInputWords = self.letterCombinations(digits[1:])

        keyLetters = phone_keys[digits[0]]

        for char in keyLetters:
            for words in smallInputWords:
                ans.append(char + words)
        return ans
        