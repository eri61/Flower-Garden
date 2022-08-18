from sympy import Symbol, pprint, solve

x = Symbol('x')
f = x**3 -  1
pprint(solve(f, x))
