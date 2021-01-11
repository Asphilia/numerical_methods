# Integration
Author: Janike Katter
Version: 11.01.2021

## Method summary
* integration.py
  * integral calculation
    * trapez_rule(p1, p2)
    * simpson_rule(a, b, f)
    * newton_cotes(a, b, n, f, alpha)
    * additive_nc(a, b, f, k, n, alpha)
  * plotting
    * plot_under(points)
    * plot_and_integral(a, b, f, n, k, alpha, step)
* integration_additions.py
  * romberg(f, a, b, depth)
  * adaptiv(a, b, f, tol, plot_function=True)
  * adaptiv_loop(a, b, f, tol, tree, parent_index)
  * gauss_quadratur_parameter(a, b, n)
  
## integration.py
### integral calculation
#### trapez_rule
Calculates the integral with the trapez rule.
* Input:
  * p1: (x1, y1); the left integral border point
  * p2: (x2, y2); the right integral border point
* Output:
  * trap: float; the integral value
  * points: array; stützstellenpunkte

#### simpson_rule
Calculates the integral with the simpson rule.
* Input:
  * a: float; the left integral border x value
  * b: float; the right integral border x value
  * f: callable; the function of which the integral is made
* Output:
  * simps: float; the integral value
  * points: array; stützstellenpunkte
  
#### newton_cotes
Calculates the integral with a newton_cotes formula. a b n f alpha
* Input:
  * a: float; the left integral border x value
  * b: float; the right integral border x value
  * n: int; the number of stützstellen used (n=2 -> trapez, n=3 -> simpson)
  * f: callable; the function of which the integral is made
  * alpha: array; the weights of the stützstellen
* Output:
  * s: float; the integral value
  * points: array; stützstellenpunkte
  
```
alpha lists for 4, 5, and 6 stützstellen
alpha_4 = [1/8,3/8,3/8,1/8] #3/8 Regel
alpha_5 = [7/90,32/90,12/90,32/90,7/90] # Milne/Boole
alpha_6 = [19/288,75/288,50/288,50/288,75/288,19/288] # 6-Punkt
```

#### additive_nc
Calculates the integral with newton-cotes formula for teilintervalle.
* Input:
  * a: float; the left integral border x value
  * b: float; the right integral border x value
  * n: int; the number of stützstellen used (n=2 -> trapez, n=3 -> simpson)
  * k: int; the number of teilintevalle
  * f: callable; the function of which the integral is made
  * alpha: array; the weights of the stützstellen
* Output:
  * s: float; the integral value
  * points: array; stützstellenpunkte

### plotting
#### plot_under
Plots the area under the stützstellen. (Trapeze)
* Input:
  * points: array; the stützstellenpunkte
* Output:
  * None
  
#### plot_and_integral
Plots the function, the stützstellen and the area. Prints the calculated integral value.
* Input:
  * a: float; the left integral border x value
  * b: float; the right integral border x value
  * n: int; the number of stützstellen used (n=2 -> trapez, n=3 -> simpson)
  * k: int; the number of teilintevalle
  * f: callable; the function of which the integral is made
  * alpha: array; the weights of the stützstellen
  * step: float; the step between two function evaluations for plotting
* Output:
  * None
  
## integration_additions.py
#### romberg
Calculates the integral using the romberg verfahren and prints the steps.
* Input:
  * f: callable; the function of which the integral is made
  * a: float; the left integral border x value
  * b: float; the right integral border x value
  * depth: int; how deep the algorithm should go
* Output:
  * None
  
#### adaptiv
Calculates the integral using an adaptive algorithm based on the simpson rule.
Prints the resulting tree with help of treelib.
* Input:
  * a: float; the left integral border x value
  * b: float; the right integral border x value
  * f: callable; the function of which the integral is made
  * tol: float; the tolerance of the algorithm
  * plot_function: bool; wether it should be plotted
* Output:
  * integral_value: float; the integral value
  
#### adaptiv_loop
Recursive step of the adaptive algorithm.
* Input:
  * a: float; the left integral border x value
  * b: float; the right integral border x value
  * f: callable; the function of which the integral is made
  * tol: float; the tolerance of the algorithm
  * tree: treelib.Tree; tree instance for later printing the tree
  * parent_index: str; the index of the parent node in the tree
* Output:
  * integral_value: float; the current integral value in the teilinterval 
  * points: array; stützstellen
  
#### gauss_quadratur_parameter
Calculates the gauss-quadratur-parameters x and alpha. Gauss-Quadratur means that:
```
Integral_(a)^(b) f(x)dx ≈ α0 * f(x0) + α1 * f(x1)
```
* Input:
  * a: float; the left integral border x value
  * b: float; the right integral border x value
  * n: int; number of weights (α), maximum is 4
* Output:
  * x_ret: array; the x parameters
  * a_ret: array; the alpha parameters
  
  
##### change history
* 11.01.2021: creation