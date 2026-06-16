class Solution:
    def processStr(self, s: str) -> str:
        n = len(s)
        ans = ""
        for ch in s:
            if ch=='*':
                if ans:
                    ans = ans[:-1]
            elif ch=='#':
                ans = ans+ans
            elif ch=='%':
                ans = ans[::-1]
            else:
                ans +=ch
        return ans