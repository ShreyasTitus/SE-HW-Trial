import math
import re
import sys
import random
from code import Num 

help = " \n\
CSV : summarized csv file \n\
(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license\n\
USAGE: lua seen.lua [OPTIONS]\n\
OPTIONS:\n\
-e  --eg        start-up example                      = nothing\n\
-d  --dump      on test failure, exit with stack dump = false\n\
-f  --file      file with csv data                    = ../data/auto93.csv\n\
-h  --help      show help                             = false\n\
-n  --nums      number of nums to keep                = 512\n\
-s  --seed      random number seed                    = 10019\n\
-S  --seperator feild seperator                       = , "



def message(status):
    if status:
        return "PASS"
    else:
        return "FAIL"

def coerce(s):
    s = s.strip()
    if s.isnumeric():
        return int(s)
    else:
        try:
            return float(s)
        except ValueError:
            if s in ['true', 'TRUE', 'True']:
                return True
            elif s in ['false', 'FALSE', 'False']:
                return False
            return re.match("\s*(.*)\s*", s).string

def parse_csv(src, separator):
    lines = src.split('\n')
    for line in lines:
        line_split = line.split(separator)
        ans = []
        for val in line_split:
            val = coerce(val)
            ans.append(val)

def copy(t):
    if type(t) is not dict:
        return t
    u = {}
    for k, v in t.items():
        u[k] = copy(v)
    return u


def create_the():
    the = {}
    tup_list = re.findall(r'[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)', help)

    for k,x in tup_list:
        the[k] = coerce(x)
    return the

the = create_the()