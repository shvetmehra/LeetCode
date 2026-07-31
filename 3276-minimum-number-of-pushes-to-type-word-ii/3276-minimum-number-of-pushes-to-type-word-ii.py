from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        char_count = Counter(word).most_common()
        group_1 = char_count[:8]   # Gets items 1 to 8
        group_2 = char_count[8:16]  # Gets items 9 to 16
        group_3 = char_count[16:24] # Gets items 17 to 24
        group_4 = char_count[24:26]
        total_count = 0
        total_count += sum(count*1 for char, count in group_1)
        total_count += sum(count*2 for char, count in group_2)
        total_count += sum(count*3 for char, count in group_3)
        total_count += sum(count*4 for char, count in group_4)
        return total_count