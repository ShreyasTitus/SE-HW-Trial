import imp
import unittest
from num import Num
from Sym import Sym
from config import t

class testReturnValues(unittest.TestCase):

    # def testThe(self):
    #     assert True
    
    def testNum(self):
        t["nums"] = 1000
        numData = {"Cldrs":list(range(1,100+1))}
        for colName, data in numData.items():
            if colName[0].isupper():
                num = Num(0, colName)
                for value in data:
                    num.add(value)
                mode = num.mid()
                div = num.div()
        
                self.assertTrue(50 <= mode <= 52) and self.assertTrue(30.5 <= div <= 32)
                num.print_Num(div, mode)

    def testSym(self):
        symFreq = {"origin":["a", "a", "a", "a", "b", "b", "c"]}
        for colName, data in symFreq.items():
            if colName[0].islower():
                # This column is a symbol
                sym = Sym(0, colName)
                for value in data:
                    sym.add(value)
                mode = sym.mid()
                entropy = sym.div()
                entropy = (1000*entropy) // 1/1000
                sym.print_Sym(entropy, mode)
                self.assertEqual(mode, "a") and self.assertTrue(1.37 <= entropy <= 1.38)

    def testBigNum(self):
        t["nums"] = 32
        numData = {"Cldrs":list(range(1,1000+1))}
        for colName, data in numData.items():
            if colName[0].isupper():
                num = Num(0, colName)
                for value in data:
                    num.add(value)
            print(num._has)
            num.print_BigNum()
        # self.assertEqual(32, len(num._has))

if __name__  == '__main__':
    unittest.main()
