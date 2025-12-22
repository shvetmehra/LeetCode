class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0
        i=0
        while i<len(chars):
            start = i
            while i<len(chars) and chars[i]==chars[start]:
                i+=1
            chars[write] = chars[start]
            write+=1

            count = i-start
            if count >1:
                for digit in str(count):
                    chars[write]= digit
                    write +=1

                        
        return write

            