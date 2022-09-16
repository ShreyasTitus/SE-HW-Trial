from Cols import Cols
from Rows import Row
from Utils import parse_csv

class Data:
    def __init__(self, src, nums, separator):
        self.rows = []
        self.cols = None
        self.n = nums

        if type(src) == str:
            parse_csv(src, separator)
        else:
            for row in (src or []):
                self.add(row)
    
    def add(self, xs):
        if not self.cols:
            self.cols = Cols(xs)
        else:
            if hasattr(xs,'cells'):
                self.rows.append(xs)
            else:
                self.rows.append(Row(xs))
            row = self.rows[-1]
            for todo in (self.cols.x, self.cols.y):
                for col in todo:
                    col.add(row.cells[col.at], self.n)

    def stats(self, places=2, showCols="data.cols.x", fun = 'mid'):
        showCols = showCols or self.cols.y
        t= {}
        for col in showCols:
            if fun == 'mid':
                v = col.mid()
            else:
                v = fun(col)
            if isinstance(v, float):
                v = round(v, places)
            t[col.name] = v
        return t