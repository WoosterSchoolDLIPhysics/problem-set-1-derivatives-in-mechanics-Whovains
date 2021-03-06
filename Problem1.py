# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 08:18:02 2017

@author: Justin
"""

from pylab import *
xa = 0
dx = .01
xb = 4 + dx
t = arange(xa,xb,dx)
f1 = t**4-4*t**3+2*t**2+3*t+6
f2 = 4*t**3-12*t**2+4*t+3
f3 = 12*t**2-24*t+4
f4 = 24*t-24

clf()
subplot(211)
plot(t,f1,'r')
plot(t,f2,'y')
plot(t,f3,'b')
xlabel('Time')

hi = subplot(212)
plot(t,f4,'b')
xlabel('Time')