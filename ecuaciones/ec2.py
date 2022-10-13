import sympy

def ecuacion2():
    x = sympy.Symbol('x')
    y = sympy.Function('y')

    f2 = sympy.Eq(y(x).diff(x) * sympy.sin(x), y(x)*sympy.log(y(x)))
    solucion = sympy.dsolve(f2, y(x))
    sympy.pprint(solucion)