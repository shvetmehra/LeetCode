class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        flat_list = sum(grid, [])
        
        for num in flat_list:
            if num<0:
                ans +=1
        return ans