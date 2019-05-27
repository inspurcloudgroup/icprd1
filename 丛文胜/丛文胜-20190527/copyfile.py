# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:40:52 2019

@author: congwensheng
"""

#拷贝文件
#!/usr/bin/env python3
import sys
if len(sys.argv)<3:
    print("wrong parameter")
    print("./copyfiles.py file1 file2)
    sys.exit(1)
f1=open(sys.argv[1])
s=f1.read()
f1.close()
f2=open(sys.argv[2],'w')
f2.write(s)
f2.close()
