class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = float('inf')
        n = len(landStartTime)
        m = len(waterStartTime)
        

        for i in range(n):
            land_finish = landStartTime[i] + landDuration[i]
            for j in range(m):
                water_start = max(land_finish, waterStartTime[j])
                total_finish = water_start + waterDuration[j]
                res = min(res, total_finish)
                

        for j in range(m):
            water_finish = waterStartTime[j] + waterDuration[j]
            for i in range(n):
                land_start = max(water_finish, landStartTime[i])
                total_finish = land_start + landDuration[i]
                res = min(res, total_finish)
                
        return res