#Practica 6
#Calculadora
#Cervantes Humberto

#N1=int(input("Ingrese el primer numero: "))
#N2=int(input("Ingrese el segundo numero: "))

from tracemalloc import take_snapshot


def suma(N1, N2):
    print("Suma de dos números")
    print("La suma de: " + str(N1) + " + " + str(N2) + " Es igual a: " )
    RS=N1+N2
    print("" + str(RS))

def resta(N1, N2):
    print("Resta de dos números")
    print("La Resta de: " + str(N1) + " - " + str(N2) + " Es igual a: " )
    RS=N1-N2
    print("" + str(RS))

def multiplicacion(N1, N2):
    print("Multiplicacion de dos números")
    print("La Multiplicacion de: " + str(N1) + " * " + str(N2) + " Es igual a: " )
    RS=N1*N2
    print("" + str(RS))

def division(N1, N2):
    print("Division de dos números")
    print("La Division de: " + str(N1) + " / " + str(N2) + " Es igual a: " )
    RS=N1/N2
    print("" + str(RS))

suma(30,2)

resta(30,2)

multiplicacion(30, 2)

division(30, 2)