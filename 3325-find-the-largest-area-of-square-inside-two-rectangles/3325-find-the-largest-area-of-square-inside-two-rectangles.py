class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        n = len(bottomLeft)
        max_side = 0
        for i in range(n):
            for j in range(i + 1, n):
                # 1. Find the boundaries of the intersection rectangle
                inter_bl_x = max(bottomLeft[i][0], bottomLeft[j][0])
                inter_bl_y = max(bottomLeft[i][1], bottomLeft[j][1])
                inter_tr_x = min(topRight[i][0], topRight[j][0])
                inter_tr_y = min(topRight[i][1], topRight[j][1])
                width = inter_tr_x - inter_bl_x
                height = inter_tr_y - inter_bl_y
                
                if width > 0 and height > 0:
                    side = min(width, height)
                    max_side = max(max_side, side)
        return max_side * max_side        