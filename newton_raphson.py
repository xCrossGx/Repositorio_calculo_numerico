#Estudiante Cristian González C.I: 31.256.662
import sympy as sp

def newton_raphson(x0, error):
    x = sp.Symbol('x')
    f = sp.exp(x**3) - sp.ln(x**24)
    f_derivada = sp.diff(f, x)
    f_2derivada = sp.diff(f_derivada, x)
    errel = 1 #error relativo
    itercont = 0 #contador de iteraciones
    m = [] #lista donde se van a guardar los valores
    m.append(x0)

    resultado_f = f.subs(x, x0).evalf()
    resultado_df = f_derivada.subs(x, x0).evalf()
    resultado_2df = f_2derivada.subs(x, x0).evalf() 
    resultado_Total = sp.Abs((resultado_f*resultado_2df)/(resultado_df**2)) #esta variable almacena el resultado del teorema de convergencia
    print(resultado_Total)

    if resultado_Total < 1: #verifica si se pueden iniciar las iteraciones
        print("Se puede resolver por Newton-Raphson")
        while errel > error:
            m.append(m[itercont] - (f.subs(x, m[itercont]).evalf())/(f_derivada.subs(x, m[itercont]).evalf())) #le pasa a la lista el resultado de la formula
            errel = sp.Abs((m[itercont + 1] - m[itercont])/m[itercont + 1])
            itercont += 1
        if len(m) > 0:
            print(f"El valor obtenido es {m[itercont]} con un error relativo del {errel}, su valor en la funcion es de {f.subs(x, m[itercont]).evalf()}")
            print(f"El total de iteraciones fue: {itercont}")
        else:
            print("debido a un error en los parametros iniciales no se pudo iniciar con las iteraciones")
    else:
        print("No se puede resolver esta funcion por el método de Newton-Raphson")

newton_raphson(1.5, 0.02)