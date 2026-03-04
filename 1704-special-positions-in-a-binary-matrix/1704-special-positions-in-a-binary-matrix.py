from collections import deque
class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows = len(mat)
        cols = len(mat[0])
        res = 0

        row_total = [sum(row) for row in mat]
        col_total = [sum(mat[i][j] for i in range(rows)) for j in range(cols)]
        for i in range (rows):
            for j in range (cols):
                if mat[i][j]==1:
                    if row_total[i] == 1 and col_total[j] == 1:
                        res +=1
        return res

        