class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = []
        t1= []

        for ch in list(s):
            if ch != '#':
                s1.append(ch)
            elif len(s1)>0:
                s1.pop() 
        for ch in list(t):
            if ch!= '#':
                t1.append(ch)
            elif len(t1)>0:
                t1.pop()

        if s1 == t1:
            return True
        else:
            return False
        