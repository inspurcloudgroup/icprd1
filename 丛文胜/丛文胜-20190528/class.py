# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:32:46 2019

@author: congwensheng
"""

#实验11 类

class Person(object):
    
    def __init__(self,name):
        self.name=name
    
    def get_details(self):
        return self.name
    
class Student(Person):
    
    def __init__(self,name,branch,year):
        Person.__init__(self,name)
        self.branch=branch
        self.year=year
        
    def get_details(self):
        return"{} studies {} and is in{} year.".format(self.name,self.branch,self.year)

class Teacher(Person):
    
    def __init__(self,name,papers):
        Person.__init__(self,name)
        self.papers=papers
        
    def get_details(self):
        return "{} teaches{}".format(self.name,','.join(self.papers))

person1=Person('sachin')
student1=Student('dfdjf','CSE',2005)
teacher1=Teacher('hgfj',[   '   C',  '  C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        