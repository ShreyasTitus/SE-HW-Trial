import math

class Sym:
    def __init__(self, c="", s=0):
        self.n = 0                  # items seen
        self.at = c if c else 0     # column  position
        self.name = s or ""         # column name
        self._has = {}              # kept data

    def add(self, v):
        if v != "?":
            self.n += 1
            if v in self._has:
                self._has[v]+=1
            else:
                self._has[v] = 1

    def mid(self):
        most = -1
        for k, v in self._has.items():
            if v > most:
                mode = k
                most = v
        return mode

    def div(self):
        def fun(p):
            return p * math.log(p, 2)
        e = 0
        for _, _n in self._has.items():
            if _n > 0:
                e = e - fun(_n/self.n)
        return e


if __name__ == '__main__':
    sym = Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
