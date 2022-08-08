#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 20:34:32 2022

@author: mvp
"""

def fun(x,y):
        if x == y:
            return x
        else:
            return fun(x,y-1)
print(fun(0,3))

