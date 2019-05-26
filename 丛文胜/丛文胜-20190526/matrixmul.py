# -*- coding: utf-8 -*-
"""
Created on Sun May 26 11:01:14 2019

@author: congwensheng
"""

n=int(input("enter the value of n:"))
print("enter values for the matrix A")
a=[]
for i in range(n):
    a.append([int(x) for x in input().split()])
b=[]
for i in range(n):
    b.append([int(x) for x in input().split()])    
c=[]
for i in range(n):
    c.append([a[i][j]*b[i][j] for j in range(n)])
for x in c:
    for y in x:
        print(str(y).rjust(5),end=' ')
    print()