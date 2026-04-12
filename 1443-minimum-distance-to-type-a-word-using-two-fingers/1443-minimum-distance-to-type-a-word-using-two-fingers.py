class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(curr, prev):
            if prev == None:
                return 0
            x1 = (ord(prev) - ord('A'))//6
            x2 = (ord(curr) - ord('A'))//6
            y1 = (ord(prev) - ord('A'))%6
            y2 = (ord(curr) - ord('A'))%6
            return abs(y2-y1) + abs(x2-x1)
        @lru_cache(None)

        def finger(i, l, r):
            if i == len(word):
                return 0
            n1 = dist(word[i],l) + finger(i+1, word[i],r)
            n2 = dist(word[i],r) + finger(i+1,l, word[i])
            return min(n1, n2)
        return finger(0, None, None)