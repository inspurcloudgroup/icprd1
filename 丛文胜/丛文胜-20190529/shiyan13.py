# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:00:24 2019

@author: congwensheng
"""

#实验十三  Collections模块

import collections
from collections import Counter
print(Counter("dsshadhasdhasdash").most_common(3))

from collections import defaultdict
s=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
d=defaultdict(list)
for k,v in s:
    d[k].append(v)
print(d.items())    

from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(10,y=20)
print(p)
print(p.x+p.y)
print(p[0]+p[1])














































