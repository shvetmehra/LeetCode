class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentStreak = 0
        maxStreak = 0
        
        for n in nums:
            if n == 1:
                currentStreak +=1
                maxStreak = max(currentStreak, maxStreak)
            else:
                currentStreak = 0
        return maxStreak
        