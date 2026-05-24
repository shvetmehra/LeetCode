# emoization 
class Solution:
    def solve(self, i, arr, d, n, dp):
        maxjump = 1
        if dp[i]!=-1:
            return dp[i]
        for x in range (1, d+1):
            j = i+x
            if j>=n:
                break
            if arr[j]>=arr[i]:
                break
            maxjump = max(maxjump, 1+self.solve(j, arr, d, n, dp))

        for x in range (1, d+1):
            j = i-x
            if j<0:
                break
            if arr[j]>=arr[i]:
                break
            maxjump = max(maxjump, 1+self.solve(j, arr, d, n, dp))
        dp[i] = maxjump
        return dp[i]

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1]*n
        ans = 0
        for i in range (n):
            ans = max(ans, self.solve(i, arr, d, n, dp))
        return ans