import sympy

def ecuacion3():
    x = sympy.Symbol('x')
    y = sympy.Function('y')
    f3 = sympy.Eq(y(x).diff(x) - y(x)/(x-2), 2*(x-2)**2)
    solucion = sympy.dsolve(f3, y(x))
    print("Solucion a la ecuacion 3: \n")
    sympy.pprint(solucion)