class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []
        cur = 0

        for ch in s:
            if ch == '*':
                if cur:
                    cur -= 1
            elif ch == '#':
                cur *= 2
            elif ch == '%':
                pass
            else:
                cur += 1

            lengths.append(cur)

        if not lengths or k >= lengths[-1]:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            L = lengths[i]

            if ch.isalpha():
                if k == L - 1:
                    return ch

            elif ch == '%':
                k = L - 1 - k

            elif ch == '#':
                half = L // 2
                if k >= half:
                    k -= half

            elif ch == '*':
                pass

        return '.'