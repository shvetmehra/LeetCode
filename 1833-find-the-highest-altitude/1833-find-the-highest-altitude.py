class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest = 0
        current = 0
        for g in gain:
            current += g
            if current > highest:
                highest = current
        return highest
        