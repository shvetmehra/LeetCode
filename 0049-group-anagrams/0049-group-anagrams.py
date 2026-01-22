class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict1 = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in dict1:
                dict1[key].append(s)
            else:
                dict1[key]= [s]
        return list(dict1.values())
        