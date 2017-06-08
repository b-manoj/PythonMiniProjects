# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 20:36:10 2017

@author: manoj
"""

import math
    


def is_palindrome(input_str):
    st = input_str
    ln_st = len(st)
    for i in range(math.floor(ln_st/2)):
        if st[i] != st[ln_st-i-1]:
            return False
    return True

if __name__ == '__main__':
    print(is_palindrome("123321"))         
        
     