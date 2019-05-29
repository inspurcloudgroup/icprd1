# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:07:15 2019

@author: congwensheng
"""

import sys
from collections import Counter

class Person(object):
    
    def __init__(self,name):
        self.name=name
        
    def get_details(self):
        return self.name
    
    def get_grade(self):
        return 0
    
class Student(Person):
     
    def __init__(self,name,branch,year,grade):
        Person.__init__(self,name)
        self.branch=branch
        self.year=year
        self.grade=grade
        
    def get_details(self):
        return "{} studies {} and is in {} year.".format(self.name,self.branch,self.year)
        
    def get_grade(self):
        common=Counter(self.grade).most_common(4)
        n1=0
        n2=0
        for item in common:
            if item[0]!='D':
                n1+=item[1]
            else:
                n2+=item[1]
        print("Pass:{},Fail:{}".format(n1,n2))
        
class Teacher(Person):
    
    def __init__(self,name,papers,grade):
        Person.__init__(self,name)
        self.papers=papers
        self.grade=grade
        
    def get_details(self):
        return "{} teaches {}".format(self.name,','.join(self.papers))
    
    def get_grade(self):
        s=[]
        common=Counter(self.grade).most_common(4)
        for i,j in common:
            s.append("{}:{}".format(i,j))
        print(','.join(s))
 
person1=Person("Sachin")
if sys.argv[1]=="student":
    student1=Student('Kushal','CSE',2005,sys.argv[2])
    student1.get_grade()
else:
    teacher1=Teacher('Prashad',['C','C++'],sys.argv[2])
    teacher1.get_grade()
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        