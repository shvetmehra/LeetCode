class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total = 0
        minimum = float('inf')
        negative_count = 0

        for row in matrix:
            for col in row:
                total += abs(col)

                if col <0:
                    negative_count +=1
                minimum = min(abs(col), minimum)
        
        if negative_count%2 == 0:
            return total
        else:
            return total - 2*minimum

            
        