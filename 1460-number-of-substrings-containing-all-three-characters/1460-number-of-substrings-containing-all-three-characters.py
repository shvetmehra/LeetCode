class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        pos = {'a': -1, 'b': -1, 'c': -1}
        for right in range(len(s)):
            pos[s[right]] = right
            
            if pos['a'] != -1 and pos['b'] != -1 and pos['c'] != -1:
                count += min(pos['a'], pos['b'], pos['c']) + 1
                
        return count
        