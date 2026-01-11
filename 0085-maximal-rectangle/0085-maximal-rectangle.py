class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        cols = len(matrix[0])
        height = [0]*(cols+1)
        maxArea = 0

        for row in matrix:
            for i in range(cols):
                height[i] = height[i]+1 if row [i] =='1' else 0

            stack = [-1]
            for i in range(len(height)):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i-stack[-1]-1
                    maxArea = max(maxArea, h*w)
                stack.append(i)
        return maxArea
        