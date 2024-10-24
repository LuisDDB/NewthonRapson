import sympy as sp
#poniendo los simbolos a usar
x, y = sp.symbols('x y')


#convertir una funcion string a sympify
def to_sympify(funcion_str):
    return sp.sympify(funcion_str)

#derivar la funcion en base a la letra
def derivar(funcion, letra):
    return sp.diff(to_sympify(funcion), letra)

#sustituir valores
def sustituir(funcion, valores):

    return funcion.subs(valores)

#calcular la determinante
def calcular_determinante_jacobiana(duX, dvY, duY, dvX):
    return ((duX*dvY)-(duY*dvX))

def newtonRapshon(funcion1, funcion2, xi, yi, limitex,limitey):
    iteracion=1
    while limitex!=xi and limitey!=yi:
        #Obteniedno las derivadas de du
        funduX=derivar(funcion1,"x")
        funduY=derivar(funcion1,"y")

        #Obteniedno las derivadas de dv
        fundvX=derivar(funcion2, "x")
        fundvY=derivar(funcion2,"y")

        #Sustituyendo valores
        valores={x:xi, y:yi}
        duX=sustituir(funduX, valores)
        duY=sustituir(funduY, valores)
        dvX=sustituir(fundvX, valores)
        dvY=sustituir(fundvY, valores)
        u1=sustituir(to_sympify(funcion1), valores)
        v1=sustituir(to_sympify(funcion2), valores)

        #determinante
        derteminante=calcular_determinante_jacobiana(duX, dvY, duY, dvX)

        # calculando xi+1 y yi+1
        x0 = (xi - (((u1 * dvY) - (v1 * duY)) / derteminante))
        y0 = (yi - (((v1 * duX) - (u1 * dvX)) / derteminante))

        #imprimir valores
        print(f'-------------iteracion numero ${iteracion} ----------')
        print(f'x1={xi},    y1={yi}')
        print(f'U1= {funcion1} = {u1}')
        print(f'v1= {funcion2} = {v1}')
        print(f'Du/dx= {funduX} = {duX}')
        print(f'Du/dy= {funduY} = {duY}')
        print(f'Dv/dx= {fundvX} = {dvX}')
        print(f'Dv/dy= {fundvY} = {dvY}')
        print(f'Determinante= {derteminante}')
        print(f'xi+1={x0},   yi+1={y0}')
        #Poniendo los nuevos valores de "x" y "y"
        xi=x0
        yi=y0

        #aumenta la iteracion
        iteracion=iteracion+1



funcion1_str=input("Escribe la primera función") #x**2+x*y-10 x**2+x*y-2
funcion2_str=input("Escribe la segunda función") #y+3*x*y**2-57 2*x**2-3*x*y+1
xi=float(input("Escribe el valor de xi")) #1.5
yi=float(input("Escribe el valor de yi")) #3.5
limiteX=float(input("Escribe hasta donde debe de llegar xi")) #2
limiteY=float(input("escribe hasta donde debe de llegar yi")) #3
newtonRapshon(funcion1_str, funcion2_str, xi, yi, limiteX,limiteY)




