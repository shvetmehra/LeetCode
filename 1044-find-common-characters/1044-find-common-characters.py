class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        map = {}
        for char in words[0]:
            map[char] = map.get(char,0)+1

        ans = []
        for i in range(1, len(words)):
            CurrentMap = {}
            for char in words[i]:
                CurrentMap[char]=CurrentMap.get(char, 0)+1
        
            for char in map:
                count = CurrentMap.get(char, 0)
                map[char] = min(count, map[char])

        for char in map:
            for _ in range (map[char]):
                ans.append(char)
        return ans
        