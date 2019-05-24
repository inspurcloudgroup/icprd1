# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:29:17 2019

@author: congwensheng
"""

fahrenheit=0
print("Fahrenheit Celsius")
while fahrenheit<=250:
    celsius=(fahrenheit-32)/1.8
    print("{:5d}{:7.2f}".format(fahrenheit,celsius))   
    fahrenheit=fahrenheit+25