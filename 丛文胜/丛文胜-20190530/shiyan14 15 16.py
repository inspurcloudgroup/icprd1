# -*- coding: utf-8 -*-
"""
Created on Thu May 30 21:03:10 2019

@author: congwensheng
"""

#实验15 迭代器、生成器、装饰器 
#迭代器
class Counter(object):
    def __init__(self,low,high):
        self.current=low
        self.high=high
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current>self.high:
            raise StopIteration
        else:
            self.current+=1
            return self.current-1
c=Counter(5,10)
for i in c:
    print(i,end=' ')

#Generators
def counter_generator(low,high):
    while low<=high:
        yield low
        low+=1
for i in counter_generator(5,10):
    print(i,end=' ')
    
def infinite_generator(start=0):
    while True:
        yield start
        start+=1
for num in infinite_generator(4):
    print(num,end=' ')
    if num>20:
        break
 
print(sum([x*x for x in range(1,10)]))
sum(x*x for x in range(1,10))

#闭包
def add_number(num):
    def adder(number):
        return num+number
    return adder
    
#Decorators
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("befor call")
        result=func(*args,**kwargs)
        print("after call")
        return result
    return wrapper
@my_decorator
def add(a,b):
    return a+b
print(add(1,3))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        