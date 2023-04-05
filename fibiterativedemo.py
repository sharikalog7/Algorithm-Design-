#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 15:39:22 2022

@author: sharikaloganathan
"""
import datetime
import timeit
import time

def fibooiter(n):
      if (n == 0):
              return 0
      elif (n == 1):
              return 1
      elif (n >1 ):
              fn = 0
              fn1 = 1
              fn2 = 2
              for i in range(3, n):
                      fn = fn1+fn2
                      fn1 = fn2
                      fn2 = fn
              return fn
      else:
              return -1
          
st = datetime.datetime.now()

n=fibooiter(41)


# get the end datetime
et = datetime.datetime.now()

# get execution time
elapsed_time = et - st

print('Execution time:', elapsed_time, 'seconds')