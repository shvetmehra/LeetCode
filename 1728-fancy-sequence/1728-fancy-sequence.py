import numpy as np

class Fancy:

    def __init__(self):
        self.arr = np.array([], dtype=np.int64)
        self.mod = 10**9 + 7

    def append(self, val: int) -> None:
        self.arr = np.append(self.arr, val % self.mod)

    def addAll(self, inc: int) -> None:
        self.arr = (self.arr + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.arr = (self.arr * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return int(self.arr[idx] % self.mod)