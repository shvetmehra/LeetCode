class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False]*n
        dp[0]=True
        last =0

        for i in range(n):
            if dp[i]==True:
                low = max(i + minJump, last+1)
                high = min(i+maxJump, n-1)
                if low<=high:
                    for j in range (low, high+1):
                        if s[j]=='0':dp[j]=True
                        last = high
        return dp[-1]
        