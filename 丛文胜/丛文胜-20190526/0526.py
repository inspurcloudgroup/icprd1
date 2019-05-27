# -*- coding: utf-8 -*-
"""
Created on Sun May 26 10:06:39 2019

@author: congwensheng
"""

#实验六   数据结构
a=[23,45,1,-3434,43624,234]
a.append(45)
a.insert(0,1)
a.count(45)
a.remove(234)
a.reverse()
b=[45,56,90]
a.extend(b)
a.sort()
del a[-1]

squares=[]
for x in range(10):
    squares.append(x**2)

square=[x**2 for x in range(10)]

combs=[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))
            

for i,j in enumerate(['a','b','c']):
    print(i,j)
   
#实验七
s="shi yan lou"
print(s.title())

z=" we all love python"
z.split

s="www.foss.in"
s.lstrip("cwsd.")
s.rstrip("cnwdi.")

s=input("please enter a string:")
z=s[::-1]
if s==z:
    print("the string is a palindrome")
else:
    print("the string is not a palindrone")



























