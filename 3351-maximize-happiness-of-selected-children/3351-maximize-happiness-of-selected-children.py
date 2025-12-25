class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        result = 0
        happiness.sort(reverse=True)
        for i in range (k):
            calculation = max(happiness[i]- count, 0)
            count +=1
            result += calculation
        return result
        