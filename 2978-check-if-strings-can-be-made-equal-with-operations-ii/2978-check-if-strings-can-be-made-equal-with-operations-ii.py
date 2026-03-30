class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        e1 = sorted(s1[i] for i in range (0, n, 2))
        e2 = sorted(s2[i] for i in range (0, n, 2))
        o1 = sorted(s1[i] for i in range (1, n, 2))
        o2 = sorted(s2[i] for i in range (1, n, 2))

        return e1==e2 and o1==o2
        