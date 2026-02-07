class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        deletion = 0
        b_count = 0
        for ch in s:
            if ch == 'b':
                b_count +=1
            else:
                deletion = min(deletion+1, b_count)
        return deletion
        