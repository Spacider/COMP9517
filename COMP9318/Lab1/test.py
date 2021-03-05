#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

from math import sqrt, floor
import math
import COMP9318.Lab1.submission as submission
import COMP9318.Lab1.str_to_tokens as str_to_tokens

'''
Question 01
'''
num = 0
print(floor(sqrt(num)))
result = submission.nsqrt(num)
print(result)

'''
Question 02
'''
def f(x):
    return x * math.log(x) - 16.0

def fprime(x):
    return 1.0 + math.log(x)

x = submission.find_root(f, fprime)
print(x)
print(f(x))

'''
Question 3
'''

def print_tree(root, indent=0):
    print(' ' * indent, root)
    if len(root.children) > 0:
        for child in root.children:
            print_tree(child, indent+4)

str_tree = '''
1 [2 [3 4       5          ] 
   6 [7 8 [9]   10 [11 12] ] 
   13
  ]
'''
toks = str_to_tokens.str_to_tokens(str_tree)
tt = submission.make_tree(toks)
print_tree(tt)

depth = submission.max_depth(tt)
print("depth is ", depth)



