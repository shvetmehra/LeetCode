class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        fac = []

        for pos, limit in factory:
            for _ in range (limit):
                fac.append(pos)
        m, n = len(robot), len(fac)
        dp = [0] * (n + 1)
        
        for i in range(m - 1, -1, -1):
            next_row = [0] * (n + 1)
            next_row[n] = float('inf')
            for j in range(n - 1, -1, -1):
                pick = abs(robot[i] - fac[j]) + dp[j + 1]
                not_pick = next_row[j + 1]
                next_row[j] = min(pick, not_pick)
            dp = next_row
            
        return dp[0]