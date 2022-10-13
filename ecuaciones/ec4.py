import sympy

def ecuacion4():
    x = sympy.Symbol('x')
    y = sympy.Function('y')
    f4 = sympy.Eq(2*x*y(x).diff(x) - y(x), 3*x**2)
    solucion = sympy.dsolve(f4, y(x))
    print("Solucion a la ecuacion 4: \n")
    sympy.pprint(solucion)