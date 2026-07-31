from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        char_count = Counter(word).most_common()
        total_count = 0
        for i, (char,count) in enumerate(char_count):
            total_push = (i//8)+1
            total_count += count*total_push
        return total_count