# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:25:20 2019

@author: congwensheng
"""

#实验十二  模块

import requests

def download(url):
    try:
        req=requsts.get(url)
    except requests.exceptions.MissingSchema:
        print('invalid URL "{}"'.format(url))
        return 
    if req.status_code==403:
        print('you do not have the authority to access this page.')
        return
    filename=url.split('/')[-1]
    with open(filename,'w') as fobj:
        fobj.write(req.content.decode('utf-8'))
    print('download over')
    
if __name__=='__main__':
    url=input('enter a url:')
    download(url)





































