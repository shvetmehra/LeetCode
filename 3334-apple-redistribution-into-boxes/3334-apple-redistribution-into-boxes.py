class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        totalBoxes = 0
        totalApple= sum(apple)
        sortedCapacity = sorted(capacity)[::-1]

        for i in sortedCapacity:
            totalApple -= i
            totalBoxes +=1

            if totalApple<=0:
                return totalBoxes

        return totalBoxes