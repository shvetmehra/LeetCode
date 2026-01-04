class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if stack and stack[-1]== char:
                stack.pop()
            else:
                stack.append(char)
        result = "".join(stack)
        return result
        