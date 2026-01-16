class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
# Switch n and m to match the problem definition
        hFences.append(1)
        hFences.append(m) 
        vFences.append(1)
        vFences.append(n) 

        def get_gaps(bars):
            gaps = set()
            bars.sort()
            for i in range(len(bars)):
                for j in range(i + 1, len(bars)):
                    gaps.add(bars[j] - bars[i])
            return gaps
        
        h_gaps = get_gaps(hFences)
        v_gaps = get_gaps(vFences)

        max_side = -1
        for gap in v_gaps:
            if gap in h_gaps:
                max_side = max(max_side, gap)
        
        if max_side == -1:
            return -1
        return (max_side * max_side) % (10**9 + 7)