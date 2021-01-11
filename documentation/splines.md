# splines.py
Author: Janike Katter
Version: 11.01.2021

## Method summary
* calc_spline_args(point_arr)
* calc_cs(y_arr, h_arr, n)
* spline_function(x, point_arr, args_arr)
* spline_and_plot(point_arr)

## Method descriptions

### calc_spline_args
calc_spline_args(point_arr) takes the interpolation points in the array `point_arr = [(x0, y0), (x1,y1), ..., (xi, yi)], i=n-1`. It uses the method calc_cs(y_arr, h_arr, n) to calculate the c parameters for the spline. The method returns an array of parameters in the form `args = [[a0, a1, ...], [b0, b1, ...], [c0, c1, ...], [d0, d1, ...]]`.

The general spline fromula is:

`s_i(x) = a_i + b_i * (x - x_i) + c_i * (x - x_i)**2 + d_i * (x - x_i)**3, for x in [x_i, x_i+1], and i in [0, n-1]`

### calc_cs
calc_cs(y_arr, h_arr, n) calculates the c parameters of the spline function and is only called by calc_spline_args.

### spline_function
spline_function(x, point_arr, args_arr) calculates the y value for a given x value. The args_arr is in the form calc_spline_args returns.

### spline_and_plot
spline_and_plot(point_arr) calculates the spline parameters with calc_spline_args and plots the resulting spline with help of the spline_function with matplotlib. It also prints out the parameters.

##### change history
* 11.01.2021: creation