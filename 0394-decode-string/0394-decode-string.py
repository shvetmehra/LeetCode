class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        numberStack = []
        stringStack = []
        currentString = ""
        k = 0

        for char in s:
            if char.isdigit():
                k = k*10 + int(char)
            elif char == '[':
                numberStack.append(k)
                stringStack.append(currentString)
                currentString = ""
                k=0                
            elif char == ']':
                count = numberStack.pop()
                prevString = stringStack.pop()
                currentString = prevString + (currentString*count)
            else:
                currentString +=char
        return currentString