class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            maxdiff = float('-inf')
            currentsum = 0
            for k in range(1,4):
                if i+k<=n:
                    currentsum+=stoneValue[i+k-1]
                    maxdiff = max(maxdiff, currentsum-dp[i+k])
            dp[i]=maxdiff
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"