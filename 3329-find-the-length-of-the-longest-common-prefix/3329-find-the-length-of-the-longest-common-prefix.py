from typing import List
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for num in arr1:
            s = str(num)
            for i in range (1, len(s)+1):
                prefix =s[:i]
                prefixes.add(prefix)
        maxlength =0
        for  num in arr2:
            str(num)
            s = str(num)
            for i in range (len(s), maxlength, -1):
                prefix = s[:i]
                if prefix in prefixes:
                    if i>maxlength:
                        maxlength = i
                    break
        return maxlength