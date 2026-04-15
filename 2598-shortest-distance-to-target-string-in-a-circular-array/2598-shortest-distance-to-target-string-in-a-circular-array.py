class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        mindist = float('inf')
        for i in range (n):
            if words[i] == target:
                dist = abs(i - startIndex)
                dis = min(dist, n-dist)
                mindist = min(mindist, dis)
        if mindist!= float('inf'):
            return mindist
        else:
            return -1