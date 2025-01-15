'''
## Variables
- Son espacios de memoria que almacenan valores
- Se pueden reasignar
- No se pueden iniciar con numeros
- No se pueden usar palabras reservadas
- No se pueden usar caracteres especiales
- Se pueden usar guiones bajos
- Se pueden usar mayusculas y minus

## Tipos de datos

- Cadena de texto
saludo = "hola, como estas?"

- Enteros
num = 25

- Decimal
num1 = 3.14

- Print
    # sep = "-" (es un parametro para separar los argumentos)
    # end = " " (es un parametro para renderizar en una sola linea)
print (saludo)

- Booleano
verdadero = True
falso = False
print(falso)

falso = False, 4    #se almacena como tupla
miLista =[1, 2, 3, 4, 5, 6] 
miTupla = (1, "hola", "chau") #no se pueden modificar

- Conjuntos "set"
miConjunto = {"hola"}
# print(type(miConjunto)) "para saber que tipo es"

- Diccionario (: y ,)
nombre = input("Ingre un nombre: ")
miDiccionario = {"Nombre:": nombre }
print(nombre)

- Operaciones
suma = 2 + 2
resta = 2 - 2
multiplicacion = 2 + 2
division = 2 / 2
divisionEntera = 2 // 2
residuo = 10 % 3
potencia = 2 ** 3



## Casting de types
print(2 + int("100"))
print(type(float("3.1416")))
print(int(3.1416))

print(round(3.5)) #redondea al par más cercano

print(bool(3))
print(bool(-1))
print(bool(0))
print(bool(0.0))
print(bool(" "))
print(bool("False"))


# Tipado dinamico: el tipo de dato se determina en tiempo de ejecución que no tiene que ser declarado explicitamente
name = "Juan"
print(type(name))

name = 10
print(type(name))


# Tipado fuerte: Python no realiza conversiones automaticas de tipos de datos
print(10 + "2")


# f-string (formateo de cadenas)
print(f"La suma de 2 + 2 es: {suma}")

# No recomendada forma de asignar variables
name, age, city, address = "Juan", 25, "Bogota", "Calle 123"

# Converciones de nombre de variables
mi_nombre_de_variable = "hola" #snake_case
nombre = "hola" #camelCase


MiNombreDeVariable = "hola" #PascalCase
minombredevariable = "hola" #todojunto

MI_CONSTANTE = 3.1416 #constante


['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


## Input 
nombre = input("Hola, ¿cómo te llamas? \n")
print(f"Mucho gusto, {nombre}")

age = int(input("¿Cuántos años tienes? \n"))
print(f"Que bien, tienes {age} años")

country, city = input("¿De qué país y ciudad eres? \n").split() # recupera la cadenas de texto y las separa por espacio
print(f"Vives en {country}, {city}")



'''


