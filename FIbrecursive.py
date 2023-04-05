#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 16:05:36 2022

@author: sharikaloganathan
"""

import datetime
import timeit
import time


def F(n):
     if (n == 0):
             return 0
     elif (n == 1):
             return 1
     elif (n > 1):
             return (F(n-1) + F(n-2))
     else:
             return -1
         
            
st = datetime.datetime.now()

n=F(41)
end=time.time()
time.sleep(1)





# get the end datetime
et = datetime.datetime.now()

# get execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')         