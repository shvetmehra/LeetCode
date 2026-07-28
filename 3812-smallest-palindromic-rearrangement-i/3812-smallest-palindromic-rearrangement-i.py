class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)//2
        base = sorted(s[:n])
        mid = []
        if len(s)%2==1:
            mid = [s[n]]
        else:
            mid = []
        reversedstring = base[::-1]
        return "".join(base+mid+reversedstring)