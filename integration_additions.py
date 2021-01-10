'''
This file contains methods for romberg-verfahren and adaptives-verfahren
Author: Janike Katter
Version: 10.01.2021
'''
import integration as itg
from treelib import Tree, Node
import matplotlib.pyplot as plt
import numpy as np


def romberg(f,a,b,depth=2):
    t = []
    strt = []
    n=depth+1
    t0 = []
    strt0 = []
    for i in range(n):
        k = 2**i
        ti,_ = itg.additive_nc(a,b,f,k=k)
        t0.append(ti)
        strt0.append(f"T(0)h/{k} = {ti}")
    t.append(t0)
    strt.append(strt0)
    for i in range(depth):
        td = []
        strtd = []
        ke = 2**(2*(i+1))
        for j in range(1,len(t[i])):
            te = (ke*t[i][j]-t[i][j-1])/(ke-1)
            td.append(te)
            strtd.append(f"T({i+1})h/{j} = {te}")
        t.append(td)
        strt.append(strtd)
    # now showing a graph tree
    for i in range(len(strt)):
        strtd = strt[i]
        print_str = ""
        for string in strtd:
            print_str += string + '  |  '
        print(print_str)
            
def adaptiv(a,b,f,tol=1e-3, plot_function=True):
    tree_ = Tree()
    tree_.create_node(f'Adaptives Verfahren für das Integral von {a} bis {b}', 'start')
    integral_value, points = adaptiv_loop(a,b,f,tol,tree_, 'start')
    tree_.create_node(f'Das Integral von {a} bis {b} hat den Wert \033[32m{integral_value}\033[0m', 'solution', parent='start')
    tree_.show()
    if plot_function:
        xrange = np.arange(a,b+tol,tol)
        yrange = [f(x) for x in xrange]
        yyy = [f(x) for x in points]
        plt.fill_between(points, yyy, 0, color=(1,0,1,0.5))
        plt.plot(xrange, yrange, 'black', label='Funktion')
        plt.plot(points, yyy, 'ro', label='Stützstellen')
        plt.legend()
        plt.title('Adaptives Verfahren, Stützstellen')
        plt.xlabel('x')
        plt.ylabel('y')
    
    return integral_value
    
def adaptiv_loop(a,b,f,tol,tree, parent_index):
    s0, _ = itg.simpson_rule(a,b,f)
    s10, _ = itg.simpson_rule(a, (a+b)/2, f)
    s11, _ = itg.simpson_rule((a+b)/2, b, f)
    s1 = s10+s11
    err = abs(s0-s1)
    curr_index = f'{a},{b}'
    points = []
    if err > 15*tol:
        tree.create_node(f'[{a},{b}] -> {err}', curr_index, parent=parent_index)
        ilinks, plinks = adaptiv_loop(a, (a+b)/2, f, tol/2, tree, curr_index)
        irechts, prechts = adaptiv_loop((a+b)/2, b, f, tol/2, tree, curr_index)
        points = plinks
        for p in prechts[1:]:
            points.append(p)
        return ilinks + irechts, points
    sfin = (16*s1-s0)/15
    tree.create_node(f'[{a},{b}] -> \033[32m★ | {sfin}\033[0m', curr_index, parent=parent_index)
    return sfin, [a,b]