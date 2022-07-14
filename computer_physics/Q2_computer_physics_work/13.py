from sympy import Symbol, factor

x = Symbol('x')
y = Symbol('y')
f = x*x - y*y
factor(f)
