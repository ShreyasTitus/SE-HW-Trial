import math
import random
from code import Utils

def per(t, p):
    p = math.floor(((p or 0.5) * len(t)) + 0.5)
    return t[max(1, min(len(t), p))]

class Num:
    def __init__(self, c=0, s=""):
        self.n = 0  # items seen
        self.at = c  # column  position
        self.name = s  # column name
        self._has = {}  # kept data
        self.lo = float('inf')  # minimum seen
        self.hi = -float('inf')  # maximum seen
        self.isSorted = True  


    def nums(self):
        if not self.isSorted:
            self._has = sorted(self._has)
            self.isSorted = True
        return self._has

    def add(self, v):
        pos = None
        if v != "?":
            v = float(v)
            self.n += 1
            self.lo = min(self.lo, v)
            self.hi = max(self.hi, v)
            if len(self._has) < Utils.the['nums']:
                pos = 1 + len(self._has)
            else:
                if random.random() < Utils.the['nums'] / self.n:
                    pos = random.randint(1, len(self._has))
            if pos:
                self.isSorted = False
                self._has[pos] = int(v)

    def div(self):
        a = self.nums()
        ans = (per(a, 0.9) - per(a, 0.1))/2.58
        return ans

    def mid(self):
        return per(self.nums(), 0.5)
