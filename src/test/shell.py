# -*- coding: utf-8 -*-

import os

def test_mult_cmd():
    os.system("cd d:/ && dir")

def test_var_num():
    path = ""
    if(1 == 1):
        path = "111"
    print(path)

if "__main__" == __name__:
    test_var_num()
