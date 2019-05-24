# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:22:57 2019

@author: congwensheng
"""

N=10
sum=0
count=0
print("please input 10 numbers:")
while count<N:
    number=float(input())
    sum=sum+number
    count=count+1
average=sum/N
print(average)