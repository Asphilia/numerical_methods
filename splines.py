'''
This file contains some methods for splines.
Author: Janike Katter
Version: 08.01.2021
'''

import numpy as np
import scipy.linalg as linalg
import matplotlib.pyplot as plt
from decimal import Decimal
from fractions import Fraction

def spline_function(x, point_arr, args_arr):
    '''
    The spline function for the points with the args.
    @author: janike katter
    -----------
    Parameters:
    x: float
        the parameter for which a y value shall be returned. Has to be between x0 and xn
    point_arr: array
        The points with which the spline args were defined
    args_arr: array
        The spline parameters. args_arr[0] are the as, ...
    -----------
    Returns:
    y: float
        The value of the function at point x
    '''
    xs = [xx for xx,yy in point_arr]
    a = args_arr[0]
    b = args_arr[1]
    c = args_arr[2]
    d = args_arr[3]
    if x < xs[0] or x > xs[-1]:
        print(f'Out of range. x must be between {xs[0]} and {xs[-1]}, but is {x}')
        return False
    for i in range(len(xs)-1):
        if x<xs[i+1]:
            y = a[i] + b[i]*(x-xs[i]) + c[i]* (x-xs[i])**2 + d[i]* (x-xs[i])**3
            return y
    print(f'Should not end up here... Something went wrong...')
    return False

def calc_cs(y_arr, h_arr, n):
    '''
    Calculates the c parameters for the spline parameters
    '''
    A = []
    r = []
    for i in range(1,n-1):
        #print(i)
        row = np.zeros(n+1)
        row[i-1] = h_arr[i-1]
        row[i] = 2*(h_arr[i-1]+h_arr[i])
        row[i+1] = h_arr[i]
        A.append(row[1:-2])
    for i in range(0,n-2):
        ri = 3*(y_arr[i+2]-y_arr[i+1])/h_arr[i+1] - 3*(y_arr[i+1]-y_arr[i])/h_arr[i]
        r.append(ri)
    #print(A)
    cs = linalg.solve(A,r)
    return cs

def calc_spline_args(point_arr):
    '''
    calculates the spline parameters for the spline points
    '''
    n = len(point_arr)
    xs = [x for x,y in point_arr]
    ys = [y for x,y in point_arr]
    a = ys[:-1]
    h = []
    for i in range(1,n):
        h.append(xs[i]-xs[i-1])
    #print(len(h))
    c_s = calc_cs(ys, h, n)
    c = [0]
    for _c_ in c_s:
        c.append(_c_)
    c.append(0)
    b = []
    d = []
    for i in range(n-1):
        bi = (ys[i+1]-ys[i])/h[i] - (h[i]/3) * (c[i+1] + 2*c[i])
        di = (c[i+1] - c[i])/(3*h[i])
        b.append(bi)
        d.append(di)
    c = c[:-1]
    return [a,b,c,d], n

def spline_and_plot(points):
    '''
    plots and prints the spline and its parameters
    '''
    args_, n = calc_spline_args(points)
    for i in np.arange(points[0][0], points[-1][0], 0.1):
        yn = spline_function(i, points, args_)
        plt.plot(i, yn, 'g.')
    for px, py in points:
        plt.plot(px,py,'ro')
    
    print('Variables in the spline function:')
    for i in range(n-1):
        a = Fraction(Decimal(str(args_[0][i]))).limit_denominator()
        b = Fraction(Decimal(str(args_[1][i]))).limit_denominator()
        c = Fraction(Decimal(str(args_[2][i]))).limit_denominator()
        d = Fraction(Decimal(str(args_[3][i]))).limit_denominator()
        print(f"a{i}: {a}, b{i}: {b}, c{i}: {c}, d{i}: {d}")