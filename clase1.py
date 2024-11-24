'''
# cadena de texto
saludo = "hola, como estas?"

# numero entero
num = 25
# numero decimal
num1 = 3.14

# imprime el resultado
print (saludo)

# booleano
verdadero = True
falso = False
print(falso)

falso = False, 4    #se almacena como tupla
miLista =[1, 2, 3, 4, 5, 6]
miTupla = (1, "hola", "chau")

# conjuntos "set"
miConjunto = {"hola"}
# print(type(miConjunto)) "para saber que tipo es"

# diccionario (: y ,)
nombre = input("Ingre un nombre: ")
miDiccionario = {"Nombre:": nombre }
print(nombre)

# operaciones
suma = 2 + 2
resta = 2 - 2
multiplicacion = 2 + 2
division = 2 / 2
divisionEntera = 2 // 2
residuo = 10 % 3
potencia = 2 ** 3
'''



# nombre de usuario y color, los guarde e imprima las dos cosas juntas; despues guardarlo en un diccionario y que se imprima como uno.

nom_usuario1 = input("Ingrese 4 nombre de usuarios: ")
color1 = input("Ingrese 4 colores: ")
# print(nom_usuario, "," , color)
nom_usuario2 = input("Ingrese su nombre de usuario: ")
color2 = input("Ingrese un color: ")
nom_usuario3= input("Ingrese su nombre de usuario: ")
color3 = input("Ingrese un color: ")
nom_usuario4 = input("Ingrese su nombre de usuario: ")
color4 = input("Ingrese un color: ")

 



miDiccionario = {"Nombre de Usuario1": nom_usuario1, "Color1": color1,
"Nombre de Usuario2": nom_usuario2, "Color2": color2,
"Nombre de Usuario3": nom_usuario3, "Color3": color3,
"Nombre de Usuario4": nom_usuario4, "Color4":color4
}

print(miDiccionario)