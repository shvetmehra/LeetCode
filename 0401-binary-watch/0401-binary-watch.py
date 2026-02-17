class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        res = []
        for hours in range(12):
            for minutes in range(60):
                if ((bin(hours)+bin(minutes))).count('1')==turnedOn:
                    time = '%d:%02d'%(hours, minutes)
                    res.append(time)
        return res
        