class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bits = bin(n)[2:]
        res = []

        for char in bits:
            if char == '0':
                res.append('1')
            else:
                res.append('0')

        flipped = ''.join(res)
        return int(flipped, 2)
        
        