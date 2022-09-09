import csv
from curses.ascii import isupper
from Sym import Sym
from num import Num

filename = open('source.csv', 'r')
file = csv.DictReader(filename)

Clndrs = []
Volume = []
Hp = []
Lbs = []
Acc = []
Model = []
origin = []
Mpg = []

for col in file:
    Clndrs.append(col["Clndrs"])
    Volume.append(col["Volume"])
    Hp.append(col["Hp:"])
    Lbs.append(col["Lbs-"])
    Acc.append(col["Acc+"])
    Model.append(col["Model"])
    origin.append(col["origin"])
    Mpg.append(col["Mpg+"])

df = {"Clndrs": Clndrs, "Volume": Volume, "Hp:": Hp, "Lbs-": Lbs, "Acc+": Acc, "Model": Model, "origin": origin, "Mpg+": Mpg}

colPosition = 0
for colName, data in df.items():
    if colName[0].islower():
        sym = Sym(colPosition, colName)
        for value in data:
            sym.add(value)
        div = sym.div()
        mid = sym.mid()
        sym.print_Sym(div, mid)
    if colName[0].isupper():
        num = Num(colPosition, colName)
        for value in data:
            num.add(value)
        div = num.div()
        mid = num.mid()
        num.print_Num(div, mid)
    colPosition+=1
