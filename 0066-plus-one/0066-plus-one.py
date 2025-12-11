class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        lst=[]
        smallAns = "".join(str(x) for x in digits)
        new_num = str(int(smallAns)+1)
        return [int(x) for x in new_num]
        