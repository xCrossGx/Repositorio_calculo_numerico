#Estudiante Cristian González C.I: 31.256.662
import math
import sympy as sp

def riemann(f, a, b, n):
    h = (b - a) / n
    icont = 0
    lista = []
    area = 0
    lista.append(a)
    while icont <= n - 1:
        icont += 1
        lista.append(lista[icont - 1] + h)
    if not math.isclose(lista[icont], b, rel_tol=1e-9):
        print(f"hubo un problema para calcular las x,  x[{icont}] = {lista[icont]} no es igual a b = {b}")
        return
    else:
        icont = 0
        f_numerica = sp.lambdify(x, f)
        while icont < n:
            area += h * f_numerica(lista[icont])
            icont += 1
        resultado_int = sp.integrate(f, (x, a, b)).evalf()
        errel = sp.Abs((resultado_int - area) / resultado_int)
        print(f"El area total calculada es la siguiente = {area}")
        print(f"El valor real de la integracion es el siguiente = {resultado_int}")
        print(f"Y el error relativo es el siguiente = {errel}")
        print(f"expresado dicho error en porcentaje: {errel * 100}%")
x = sp.Symbol('x')
f = 3*x * (sp.sqrt(x**2 + 1))

riemann(f, 0, 1, 10000000)