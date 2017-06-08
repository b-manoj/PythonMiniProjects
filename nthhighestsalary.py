# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 07:19:28 2017

@author: manoj
"""
from operator import itemgetter

empl_list = [{'ID':1,'Name':'Jon','Salary':45000},
             {'ID':2,'Name':'Claire','Salary':95000},
             {'ID':3,'Name':'abc','Salary':200},
             {'ID':4,'Name':'got','Salary':200},
             {'ID':5,'Name':'Subbu','Salary':100000},
             {'ID':6,'Name':'Paddu','Salary':68000},
             {'ID':7,'Name':'Manoj','Salary':87800},
             {'ID':8,'Name':'Swathi','Salary':10000}]

def Nhighest(n,empl):
    emp_sortedlist = sorted(empl_list, key=itemgetter('Salary','Name'))
    print (emp_sortedlist)
    print("\n\n")
    ln_list = len(emp_sortedlist)
    return emp_sortedlist[ln_list-n]
    

if __name__ == '__main__':
    print(Nhighest(8,empl_list))    