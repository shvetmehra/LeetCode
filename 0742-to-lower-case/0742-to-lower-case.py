class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        for char in s:
            if 'A' <= char <='Z':
                lower_Char = chr(ord(char)+32)
                result.append(lower_Char)
            else:
                result.append(char)
        return "".join(result)
        