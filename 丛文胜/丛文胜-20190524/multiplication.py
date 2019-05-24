# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:49:53 2019

@author: congwensheng
"""

i=1
print("-"*50)
while i<11:
    n=1
    while n<=10:
        print("{:5d}".format(i*n),end=" ")
        n=n+1
    print()
    i=i+1
print("-"*50)