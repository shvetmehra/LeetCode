class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        prev_row = [poured]
        for row in range (1, query_row+1):
            curr_row = [0]*(row+1)
            for i in range (row):
                extra = prev_row[i]-1
                if extra>0:
                    curr_row[i]+= extra*0.5
                    curr_row[i+1]+= extra*0.5
            prev_row = curr_row
        return min(1, prev_row[query_glass])
        