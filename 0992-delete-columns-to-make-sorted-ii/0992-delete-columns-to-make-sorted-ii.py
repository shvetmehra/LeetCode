class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        rows = len(strs)
        cols = len(strs[0])
        ans = 0
        is_settled = [False] * (rows-1)

        for i in range (cols):
            is_bad = False
            for j in range (rows-1):
                if not is_settled[j] and strs[j][i]>strs[j+1][i]:
                    is_bad = True
                    break
            if is_bad:
                ans+=1

            else:
                for j in range(rows-1):
                    if strs[j][i]<strs[j+1][i]:
                        is_settled[j] = True

        return ans
        