class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        res = 0
        for i in range (n):
            distance = i if (colors[i]!= colors[0]) else 0
            distancer = (n-1-i) if(colors[i]!=colors[n-1]) else 0
            res = max(res, distance, distancer)

        return res