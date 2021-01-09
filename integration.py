'''
This file contains some methods for numerical integration.
Author: Janike Katter
Version: 08.01.2021
'''
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

##### plot area #####

def plot_under(points):
    x = []
    y = []
    for px, py in points:
        x.append(px)
        y.append(py)
    plt.fill_between(x, y, 0, color=(1,0,1,0.5))
    plt.plot(x, y, 'ro', label='Stützstellen')

##### äquidistante stützstellen #####

def trapez_rule(p1, p2):
    a = p1[0]
    b= p2[0]
    fa = p1[1]
    fb = p2[1]
    trap = (b-a)*(fa+fb)/2
    return trap, [p1,p2]
    
def simpson_rule(a, b, f):
    m = (a+b)/2
    fa = f(a)
    fb = f(b)
    fm = f(m)
    simps = (b-a)/6 * (fa + 4*fm + fb)
    return simps, [(a,fa), (m,fm), (b,fb)]

def newton_cotes(a,b,n,f,alpha):
    if n == 2:
        return trapez_rule((a,f(a)),(b,f(b)))
    if n == 3:
        return simpson_rule(a,b,f)
    
    h = b-a
    s = 0
    points = []
    for i in range(n):
        x = (i*h/(n-1))+a
        s += alpha[i]*f(x)
        points.append((x,f(x)))
    #s = s*h
    return s, points
    
def additive_nc(a,b,k,n,f,alpha):
    h = (b-a)/k
    xs = [a+i*h for i in range(k+1)]
    summe = 0
    points_ = []
    for i in range(1,k+1):
        res, points =  newton_cotes(xs[i-1], xs[i], n, f, alpha)
        summe += res
        for point in points: 
            points_.append(point) 
    if n >= 4:
        summe = summe*h
    return summe, points_

def plot_and_integral(a,b,f,n=2,k=1,alpha=[0.5,0.5], step=0.1):
    xrange = np.arange(a,b,step)
    yrange = []
    for x in xrange:
        yrange.append(f(x))
    integral_result, points = additive_nc(a,b,k,n,f,alpha)
    plt.plot(a,0,'white', label=f'The numerical integration result is {integral_result}')
    plot_under(points)
    plt.plot(xrange,yrange,'black', label='Funktion f(x)')
    plt.legend(bbox_to_anchor=(1.25, 0, 0.5, 1), loc='center left')
    plt.title('Integral')
    plt.xlabel('x')
    plt.ylabel('y')
