class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        fac = []

        for pos, limit in factory:
            for _ in range (limit):
                fac.append(pos)
        m, n = len(robot), len(fac)
        dp = [[-1 for _ in range (n)] for _ in range (m)]

        def solve(i, j):
            if i == m:
                return 0
            if j == n:
                return float('inf')
            if dp[i][j] != -1:
                return dp[i][j]
            pick = abs(robot[i] - fac[j]) + solve(i+1, j+1)
            notpick = solve(i, j+1)
            dp[i][j] = min(pick, notpick)
            return dp[i][j]
        return solve (0,0)
        