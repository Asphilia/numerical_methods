# Interpolation.py
Author: Janike Katter  
Version: 11.01.2021

## Method summary
* methods to calculate parameters and function evaluation
  * calc_polynom(points)
  * polynom(x, args)
  * calc_newton_polynom(points)
  * newton_polynom(x, args, xs)
  * lagrange_polynom(x, points)
* methods to print formulas
  * print_polynom(points)
  * print_newton(points)
  * print_lagrange(points)
* methods for plotting
  * plot_newton_and_polynom(points)
  * plot_polynom_and_lagrange(points)
  
## Method describtion
### Methods for calculation and function evaluation
#### calc_polynom
calc_polynom(points) calculates the parameters for the interpolation polynom based on the interpolation points 'points'. These points are given in the array 'points' in the form : (x0,y0). The method returns an array with the parameters 'c'.

The general formula for the polynom is:

`p(x) = c0 + c1 * x + c2 * x**2 + ... `

#### polynom
polynom(x, args) evaluates the polynom at the given x coordinate and returns its y coordinate. The 'args' are in the form that calc_polynom(points) returns.

#### calc_newton_polynom
calc_newton_polynom(points) calculates the parameters for the newton interpolation polynom based on the interpolation points 'points'. These points are given in the array 'points' in the form : (x0,y0). The method returns an array with the parameters 'b'.

The general formula for the polynom is:

`p(x) = b0 + b1 * (x-x0) + b2 * (x-x0) * (x-x1) + ... `

#### newton_polynom
newton_polynom(x, args, xs) evaluates the newton polynom at the given x coordinate and returns its y coordinate. The 'args' are in the form that calc_newton_polynom returns. The 'xs' are the x coordinates of the interpolation points.

#### lagrange_polynom
lagrange_polynom(x, points) evaluates the interpolation polynom based on lagrange polynoms at the given x coordinate and returns its y coordinate. There is no method to calculate polynom arguments, as they are obtained from the interpolation points.

The general formula is:

`p(x) = y_0 * L_0(x) + y_1 * L_1(x) + ...`

where

`L_i(x) = ((x - x_0)(x - x_1)...(x - x_i-1)(x - x_i+1)...(x - x_n))/((x_i - x_0)...(x_i - x_i-1)(x_i - x_i+1)...(x_i - x_n))`

### methods to print formulas
#### print_polynom
print_polynom(points) prints the formula with its arguments, which are obtained by calc_polynom(points), onto the console.

#### print_newton
print_newton(points) prints the formula with its arguments, which are obtained by calc_newton_polynom(points), onto the console.

#### print_lagrange
print_lagrange(points) prints the formula of the interpolation polynom based on the lagrange polynoms onto the console.

### methods for plotting
#### plot_newton_and_polynom
plot_newton_and_polynom(points) plots the interpolation polynom and the newton interpolation polynom and the interpolation points with matplotlib.

#### plot_polynom_and_lagrange
plot_polynom_and_lagrange(points) plots the interpolation polynom and the lagrange polynom and the interpolation points with matplotlib.




###### change history
* 11.01.2021: creation
* 04.08.2021: link back to README

[Back](../README.md)
