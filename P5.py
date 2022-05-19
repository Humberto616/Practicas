#Practica 5
#Manejo de métodos
#Cervantes Humberto
#--------------------#
#Manipulación de las luces e interiroes de una casa en un ciclo de 60 minutos
#--------------------#

VT = 15

VCI = "#F7FF87"
VCF = "#FFF"

VT1 = .25
VT2 = .5
VT3 = .75
VT4 = 1

#------------------------#

def inicio():
    etapa1()

def finalizar():
    print("Luces encendidad a todo color.")

#------------------------#

def timer(minutos):
    print("Inicio conteo de 15" + str(minutos))
    #TODO falta funcion que cuente los 15 minutos 
    print("Finalizado conteo de 15")

def luces(tono, color): #tono, color 
    print("Se establece el color y tono")
    print("Color establecido: " + color)
    print("Tono establecido: " + str(tono))

#-------------------------#

def etapa1():
    print("Etapa uno iniciada")
    timer(VT)
    luces(VT1,VCI)
    print("Etapa uno finalizada")
    etapa2()

def etapa2():
    print("Etapa dos iniciada")
    timer(VT)
    luces(VT2,VCI)
    print("Etapa dos finalizada")
    etapa3()

def etapa3():
    print("Etapa tres iniciada")
    timer(VT)
    luces(VT3,VCF)
    print("Etapa tres finalizada")
    etapa4()

def etapa4():
    print("Etapa cuatro iniciada")
    timer(VT)
    luces(VT4,VCF)
    print("Etapa cuatro finalizada")
    finalizar()

#------------------------#

#Trigger inicial
print("Inicio de la manipulación de luces")

inicio()


#Declaración de variables
#VT = variable de tiempo
#VCI = variable de color inicial
#VCF = variable de color final
#VT1 = variable de tono 1
#VT2 = variable de tono 2
#VT2 = variable de tono 3
#VT2 = variable de tono 4