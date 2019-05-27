# -*- coding: utf-8 -*-
"""
Created on Sun May 26 10:41:16 2019

@author: congwensheng
"""

n=int(input("enter the nuber of students:"))
data={}
subjects=('physics','math','history')
for i in range(0,n):
    name=input('enter the name of student{}:'.format(i+1))
    marks=[]
    for x in subjects:
        marks.append(int(input('enter marks of{}:'.format(x))))
    data[name]=marks
for x,y in data.items():
    total=sum(y)
    print("{}'s total marks{}".format(x,total))
    if total<120:
        print(x,"failed")
    else:
        print(x,"passed")