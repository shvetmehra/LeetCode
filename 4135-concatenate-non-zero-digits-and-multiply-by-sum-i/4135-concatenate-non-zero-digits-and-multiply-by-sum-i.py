class Solution:
    def sumAndMultiply(self, n: int) -> int:
        res = 0
        ans = []

        for i in str(n):
            if i!="0":
                res +=int(i)
                ans.append(i)
        if not ans:
            return 0
        x = int("".join(ans))
        return res*x