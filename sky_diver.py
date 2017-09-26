# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:19:19 2017
@author: Justin
"""
from pylab import *

#define constants
g = 9.8 #meters per seconds sqr of course.
b = .10 #drag coeff.
m = 1.0 #kg

t0 = 0.0 #inital time
tf = 50.0 #how long I fall
dt = 1. #time step size

t = arange(t0,tf,dt)
v = zeros(len(t))
v0 = 0 
v[0] = v0

for i in range(1,len(t)):
    dv = (-(b/m)*v[i-1]-g)*dt #modify this line to have a quadratic drag term
    v[i] = v[i-1] + dv
figure(1)
clf()
vt = -m*g/b
plot(t,vt*(1-exp(-b*t/m)),'k')
text(20,-38,r"$v(t) = V_T(e^{-\frac{bt}{m}}-1)$", size=20, color ='brown')
plot(t,v,'bo',markersize=5)
plot(t,0*t+vt,'k--') #this is the horizontal asyomtoe
plot(t,-g*t,'c.')
ylim(-120,0)