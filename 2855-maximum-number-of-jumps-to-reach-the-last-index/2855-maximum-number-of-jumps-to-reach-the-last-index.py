# Memoization 
class Solution:
    def solve(self, i, nums, target, n, dp):
        if i == n-1:
            return 0
        if dp[i]!=-1:
            return dp[i]
        max_jump = float('-inf')
        for j in range(i+1, n):
            if abs(nums[j]-nums[i])<=target:
                res = self.solve(j, nums, target, n, dp)
                if res != float('-inf'):
                    max_jump = max(max_jump, res+1)
        dp[i]=max_jump
        return dp[i]
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1]* n
        ans = self.solve(0, nums, target, n, dp)
        return ans if ans> float('-inf') else -1