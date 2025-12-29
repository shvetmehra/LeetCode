class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        n = len(bottom)
        map = defaultdict(list)

        for a,b,c in allowed:
            map[a+b].append(c)
        seen = set()

        def backTracking(bottom, row, i):
            n = len(bottom)
            if n == 1: return True
            if i==n:
                if row in seen: return False
                seen.add(row)
                return backTracking(row, "", 1)
            pair = bottom[i-1]+bottom[i]
            for curr in map[pair]:
                if backTracking (bottom, row+curr, i+1): return True
            return False
        return backTracking(bottom, "", 1)
        