#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 20:50:33 2022

@author: mvp
"""

class A:
      pass
   class B(A):
      pass
   class C(B):
      pass

   print(issubclass(A,C))