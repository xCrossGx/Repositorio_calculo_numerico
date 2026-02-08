#Estudiante Cristian González C.I: 31.256.662
import math

def f(x): #se declara la funcion
    return x**2 - 5

def biseccion(x1, x2, error, imax):
    xi = x1 #1er valor
    xf = x2 #2do valor
    errel = 1 #error relativo
    itercont = 0 #contador de iteraciones
    m = [] #variable que guarda los valores en una lista simple segun la iteracion
    sigxi = 1 #Signo del primer valor en la funcion 1 = +, -1 = -, 0 = 0
    sigxf = 1 #Signo del segundo valor en la funcion 1 = +, -1 = -, 0 = 0
    sigm = 1 #Signo del primer valor medio en la funcion 1 = +, -1 = -, 0 = 0
    
    #Probar si la funcion tiene cambio de signo
    if f(xi)*f(xf) < 0:
        puede_bisec = True
    else:
        puede_bisec = False
    
    #Inician las iteraciones
    if puede_bisec: #verifica si se puede usar el metodo
        while errel > error and itercont < imax and sigm != 0: #ciclo de repeticiones
            m.append((xi + xf)/2) 
            sigxi, sigxf, sigm = signo_iter(xi, xf, m[itercont]) #llamada a la funcion que calcula los signos
            if sigxi == sigm: #corrobora si los signos son iguales y de serlo cambia los valores
                xi = m[itercont]
            else:
                if sigxf == sigm: #lo mismo que el anterior
                    xf = m[itercont]
                else: #esto es unicamente para el caso de que el signo de valor medio sea 0
                    pass
            itercont += 1    
            if itercont > 1: #verifica si se puede calcular el error
                valoract = m[itercont - 1]
                valorant = m[itercont - 2]
                errel = abs((valoract - valorant)/valoract)
        if len(m) > 0: #verifica que si se haya logrado realizar al menos 1 iteracion
            print(f"P es equivalente a m{itercont} = {m[itercont - 1]}, el resultado sustituyendo en la funcion es {f(m[itercont - 1])}")
        else:
            print("No se realizaron iteraciones: el método no avanzó por las condiciones iniciales.")
    else:
        print("No se puede hacer el metodo de biseccion")
    
    return
    
def signo_iter(a, b, c): #Esta funcion calcula los signos de cada x para la funcion
    a = 1 if f(a) > 0 else -1
    b = 1 if f(b) > 0 else -1
    c = 1 if f(c) > 0 else (-1 if f(c) < 0 else 0)
    return a, b, c

biseccion(2, 3, 0.01, 10)