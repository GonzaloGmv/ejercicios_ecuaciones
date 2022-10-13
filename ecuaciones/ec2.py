import sympy
import math

def ecuacion2():
    x = sympy.Symbol('x')
    y = sympy.Function('y')
    f2 = sympy.Eq(y(x).diff(x) * sympy.sin(x), y(x)*sympy.log(y(x)))
    ics = {y(math.pi/2):math.e}
    solucion = sympy.dsolve(f2, y(x), ics=ics)
    print("Solucion a la ecuacion 2: \n")
    sympy.pprint(solucion)