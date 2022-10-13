import sympy

x = sympy.Symbol('x')
y = sympy.Function('y')

f1 = ((x**2)*y(x)-y(x))/(y(x)-1)
ics = {y(3):-1}
solucion = sympy.dsolve(y(x).diff(x)-f1,ics=ics)
sympy.pprint(solucion)