import turtle

# Configurar la pantalla
pantalla= turtle.Screen()
pantalla.title("Dibujar una linea recta")
pantalla.bgcolor("pink")

# Crear una tortuga (como el puntero del mouse)
tortuga=turtle.Turtle()
tortuga.color("purple")
tortuga.pensize(4)

# Dibujar una linea recta

# for triangulo in range (3):
#     # largo de la recta
#     tortuga.forward(200)
#     # longitud del puntero
#     tortuga.left(120)
#     print(triangulo)

# for cuadrado in range (2):
#     tortuga.right(-90)
#     tortuga.forward(175)
#     tortuga.right(-90)
#     tortuga.forward(175)
#     print(cuadrado)



# tortuga.right(-90)
# tortuga.setx(-50)


# for triangulo in range (5):
#     tortuga.left(71)
#     tortuga.forward(100)
#     tortuga.left(217)
#     tortuga.forward(100)


# for triangulo1 in range (5):
#     tortuga.forward(200)
#     tortuga.right(144)
#     print(triangulo1)


for triangulo3 in range (1):
    tortuga.left(71) # arriba
    tortuga.right(71) #abajo
    tortuga.forward(300)

    # tortuga.forward()

for i in range (1):
    tortuga.circle(30)


# Mantiene la ventana abierta
pantalla.mainloop()





