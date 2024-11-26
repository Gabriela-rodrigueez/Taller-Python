import turtle
import time
import random

# configuracionde la pantalla
pantalla= turtle.Screen()
pantalla.title("Juego de la viborita")
pantalla.bgcolor("violet")
pantalla.setup(width=600, height=600)
pantalla.tracer(0)


#"Nombre" del cuadrado; "Ingrese su nombre:" ingresar datos 
jugador_nom = pantalla.textinput("Nombre","Ingrese su nombre: ")


if not jugador_nom:
    jugador_nom = "Jugador 1"

# elige un color de tu serpiente:
colores_disponibles = ["yellow","red","green","brown","orange","blue"]
color_serpiente = None

while color_serpiente not in colores_disponibles:
    seleccion_color = pantalla.textinput("Selccion de color",f"Ingrese su nombre:\n {','.join(colores_disponibles)}")
    if seleccion_color:
        seleccion_color =seleccion_color.lower()
        if seleccion_color in colores_disponibles:
            color_serpiente = seleccion_color
        else:
            pantalla.textinput("Seleccion de color",f"Color Invalido. Por favor, eliga uno de los siguientes colores:\n{',' .join(colores_disponibles)}")
    else:
        color_serpiente = "blue"
    break

borde=turtle.Turtle()
borde.speed(-10) #movimiento (rapido)
borde.color("purple")
borde.pensize(11)
borde.penup() #mover el curson sin dibujar al hacerlo
borde.goto(-295, 295)
# borde.goto(-250, -250)
borde.pendown()

# for limite in range (2):
#     borde.forward(669)
#     borde.right(90)
#     borde.forward(563)
#     borde.right(90)

for limite in range (4):
    borde.forward(582)
    borde.right(90)
borde.hideturtle()

#cabeza vibora
vibora=turtle.Turtle()
vibora.speed(0) #movimiento (rapido)
vibora.shape("turtle") #forma a la serpiente ("circle","triangle","arrow","turtle","classic","square")
vibora.color(color_serpiente)
vibora.penup() #mover el curson sin dibujar al hacerlo
vibora.goto(0,0)
vibora.direction = "stop"


# cuerpo vibora
segmentos = []

for i in range (3):
    nuevo_segmento=turtle.Turtle()
    nuevo_segmento.speed(0) #movimiento (rapido)
    nuevo_segmento.shape("square") #forma a la serpiente ("circle","triangle","arrow","turtle","classic","square")
    nuevo_segmento.color(color_serpiente)
    nuevo_segmento.penup() #mover el curson sin dibujar al hacerlo
    nuevo_segmento.goto(-20 * (i+1), 0)
    segmentos.append(nuevo_segmento)


# funcion para mover a la serpiente
def mover():
    if vibora.direction == "up": #arriba
        y = vibora.ycor()
        vibora.sety(y+20)
    if vibora.direction == "down": #abajo
        y = vibora.ycor()
        vibora.sety(y-20)
    if vibora.direction == "left": #izquierda
        x = vibora.xcor()
        vibora.setx(x-20)
    if vibora.direction == "right": #derecha
        x = vibora.xcor()
        vibora.setx(x+20)

    # mover los segmentos en orden inverso
    for i in range (len(segmentos) -1,0,-1):
        x = segmentos [i-1].xcor ()
        y = segmentos [i-1].ycor ()
        segmentos[i].goto(x,y)

    #mover el primer segmento al lugar donde estaba la serpiente
    if len (segmentos) > 0:
        x = vibora.xcor()
        y = vibora.ycor()
        segmentos[0].goto(x,y)


#funciones para cambiar la direccion 
def arriba():
    if vibora.direction != "down":
        vibora.direction = "up"
def abajo():
    if vibora.direction != "up":
        vibora.direction = "down"
def izquierda():
    if vibora.direction != "right":
        vibora.direction = "left"
def derecha():
    if vibora.direction != "left":
        vibora.direction = "right"


#asignar las teclas
pantalla.listen() #escuchar al teclado
pantalla.onkeypress(arriba,"Up") #funcion y la tecla
pantalla.onkeypress(abajo,"Down")
pantalla.onkeypress(izquierda,"Left")
pantalla.onkeypress(derecha,"Right")


# comida
comida=turtle.Turtle()
comida.speed(0) 
comida.shape("circle") 
comida.color("red")
comida.penup()
comida.goto(0,200)


# puntaje
puntaje=0
puntajeMaximo=0
nivel=1
velocidad = 0.1


# Mostrar puntaje y el nombre del jugador
texto=turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup() 
texto.hideturtle()
texto.goto(0,250)
texto.write(f"Jugador: {jugador_nom}      Puntaje: {puntaje}      Puntaje Maximo: {puntajeMaximo}     Nivel: {nivel}", align="center", font=("Calibri",13, "normal"))


# funcion para actualizar el puntaje en la pantalla
def actualizar_puntaje():
    texto.clear()
    texto.write(f"Jugador: {jugador_nom}      Puntaje: {puntaje}      Puntaje Maximo: {puntajeMaximo}     Nivel: {nivel}", align="center", font=("Calibri",13, "normal"))


while True:
    pantalla.update()
    mover() #siempre que se define algo se coloca al final
    time.sleep(0.1)

    ultima_posicion = vibora.position() #guarda la posicion actual antes de mover

    
    if len(segmentos) >0:
        ultimo_segmento = segmentos[-1]
        nuevo_segmento.goto (ultimo_segmento.position())
    else:
        nuevo_segmento.goto(ultima_posicion)
    segmentos.append(nuevo_segmento)

    if vibora.distance(comida) <20:
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0) 
        nuevo_segmento.shape("square") 
        nuevo_segmento.color(color_serpiente)
        nuevo_segmento.penup()

        # Aumentar puntaje y nivel
        puntaje += 10
        actualizar_puntaje()



        if puntaje % 50 == 0: # % resto 
            nivel += 1
            velocidad *= 1.2
            actualizar_puntaje()

        while True:
            x = random.randint(-295, 295)
            y = random.randint(-295, 295)
            nueva_posicion = (x,y)
            break








# vibora.shapesize(10) (tamaño del cursor)


pantalla.mainloop()
