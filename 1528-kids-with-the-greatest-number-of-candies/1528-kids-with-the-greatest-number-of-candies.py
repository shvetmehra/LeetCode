class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans = []
        max_candy = max(candies)
        for i in candies:
            ans.append(i+ extraCandies >= max_candy)
        return ans
        
        