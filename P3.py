#Practica 3
#Nombre Completo
#Cervantes Humberto
V1=str(input("Ingrese tu primer nombre: "))
IF=str(input("¿Tienes un segundo nombre? SI/NO: "))
if IF == "SI":
    V2=str(input("Ingrese su segundo nombre: "))
    V3=str(input("Ingrese tu primer apellido: "))
    V4=str(input("Ingrese tu segundo apellido: "))
    print("Tu nombre completo es: ", V1, V2, V3, V4)
else:
    V3=str(input("Ingrese tu primer apellido: "))
    V4=str(input("Ingrese tu segundo apellido: "))
    print("Tu nombre completo es: ", V1, V3, V4)

