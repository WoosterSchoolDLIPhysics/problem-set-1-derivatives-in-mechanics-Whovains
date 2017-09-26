# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 07:31:11 2017

@author: brian.sullivan
"""

a = arange(10)

for i in arange(0, len(a)):
    print i, a[i]-a[i-1]