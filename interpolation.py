'''
This file contains some methods for numerical interpolation without splines.
Author: Janike Katter
Version: 09.01.2021
'''
import numpy as np
import scipy.linalg as linalg
import matplotlib.pyplot as plt

def calc_polynom(points):
    '''
    Polynom interpolation of n points with a polynom of exponential n-1
    '''
    n = len(points)
    xs = []
    ys = []
    for x,y in points:
        xs.append(x)
        ys.append(y)
    A = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append( xs[i]**j )
        A.append(row)
    cs = linalg.solve(A,ys)
    return cs

def polynom(x, args):
    '''
    Polynomfunction with args from calc_polynom
    '''
    ret = 0
    for i in range(len(args)):
        ret += args[i]* (x**i)
    return ret

def calc_newton_polynom(points):
    '''
    Calculates the parameters for newton_polynom
    '''
    n = len(points)
    xs = []
    ys = []
    for x,y in points:
        xs.append(x)
        ys.append(y)
    A = np.zeros((n,n))
    for i in range(n):
        A[i,0] = 1
    for i in range(1,n):
        for j in range(1,i+1):
            A[i,j] = A[i,j-1]*(xs[i]-xs[j-1])
    bs = linalg.solve(A,ys)
    return bs

def newton_polynom(x, args, xs):
    ret = args[0]
    currx = 1
    for i in range(len(xs)-1):
        currx = currx*(x-xs[i])
        nret = args[i+1]*currx
        ret += nret
    return ret

def lagrange_polynom(x, points):
    xs = []
    ys = []
    for xks, yks in points:
        xs.append(xks)
        ys.append(yks)
    if not ((x >= xs[0]) and (x <= xs[-1])):
        print('Fehler!!!')
    fx = 0
    for i in range(len(xs)):
        zahler = 1
        nenner = 1
        for j in range(i):
            zahler = zahler * (x-xs[j])
            nenner = nenner * (xs[i]-xs[j])
        for j in range(i+1,len(xs)):
            zahler = zahler * (x-xs[j])
            nenner = nenner * (xs[i]-xs[j])
        fx += ys[i]*(zahler/nenner)
    return fx
    

def plot_newton_and_polynom(points):
    pol_args = calc_polynom(points)
    newton_args = calc_newton_polynom(points)
    xs = [x for x,y in points]
    xrange = np.arange(xs[0],xs[-1]+0.01,0.1)
    yrange_pol = []
    yrange_newt = []
    for x in xrange:
        yrange_pol.append(polynom(x,pol_args))
        yrange_newt.append(newton_polynom(x,newton_args,xs))
    plt.plot(xrange, yrange_pol, 'g--', label='Polynom Interpolation')
    plt.plot(xrange, yrange_newt, 'b.', label='Newton Polynom')
    for x,y in points:
        plt.plot(x,y,'ro', label=f"Point {x}|{y}")
    plt.legend(bbox_to_anchor=(1.25, 0, 0.5, 1), loc='center left')
    plt.title('Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    return pol_args, newton_args

def plot_polynom_and_lagrange(points):
    pol_args = calc_polynom(points)
    xs = [x for x,y in points]
    ys = [y for x,y in points]
    xrange = np.arange(xs[0], xs[-1]+0.01,0.1)
    yrange_pol = []
    yrange_lagrange = []
    for x in xrange:
        yrange_pol.append(polynom(x,pol_args))
        yrange_lagrange.append(lagrange_polynom(x, points))
    plt.plot(xrange, yrange_pol, 'g--', label='Polynom Interpolation')
    plt.plot(xrange, yrange_lagrange, 'b.', label='Lagrange')
    plt.plot(xs, ys, 'ro', label='Punkte')
    plt.legend(bbox_to_anchor=(1.25, 0, 0.5, 1), loc='center left')
    plt.title('Lagrange and Polynom Interpolation')
    plt.xlabel('x')
    plt.ylabel('y')
    return pol_args
        