# -*- coding: utf-8 -*-
"""
Created on Mon May 27 14:48:20 2019

@author: congwensheng
"""
#实验八   函数
lst=[1,2,3,4,5]
def square(num):
    return num*num

print(list(map(square,lst)))

#实验九  文件处理
fobj=open("sample.txt")
fobj.read()
fobj.readline()
fobj.readlines()
fobj.close()

fobj=open("hushsh.txt",'w')
fobj.write('sahfgf\n')
fobj.write('dshv\n')
fobj.close()

fobj=open('hgbcx.txt')
s=fobj.read()
fobj.close()
print(s)


with open('sample.txt') as fobj:
    for line in fobj:
        print(line,end=' ')
        
#实验十  异常





























