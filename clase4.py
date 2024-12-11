import turtle
import time
import random

# configuracion de la pantalla
pantalla= turtle.Screen()
pantalla.title("Juego de la Viborita")
pantalla.bgcolor("violet")
pantalla.setup(width=600, height=600)
pantalla.tracer(0)


#"Nombre" del cuadrado; "Ingrese su nombre:" ingresar datos 
jugador_nom = pantalla.textinput("Nombre","Ingrese su nombre: ")

if not jugador_nom:
    jugador_nom = "Jugador 1"


# elige un color de tu serpiente:
colores_disponibles = ["yellow","red","green","brown","orange","blue","white"]
color_serpiente = None

while color_serpiente not in colores_disponibles:
    seleccion_color = pantalla.textinput("Selccion de color",f"Elige el color de la serpiente:\n {','.join(colores_disponibles)}")

    if seleccion_color:
        seleccion_color = seleccion_color.lower()
        if seleccion_color in colores_disponibles:
            color_serpiente = seleccion_color
        else:
            pantalla.textinput("Seleccion de color",f"Color Invalido. Por favor, eliga uno de los siguientes colores:\n{',' .join(colores_disponibles)}")
    else:
        color_serpiente = "blue"
    break

borde=turtle.Turtle()
borde.speed(0) #movimiento (rapido) -10
borde.color("purple")
borde.pensize(8)
borde.penup() #mover el curson sin dibujar al hacerlo
borde.goto(-280, 280)
borde.pendown()
borde.pensize(6)


for limite in range (4):
    borde.forward(555)
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


# comida
comida=turtle.Turtle()
comida.speed(0) 
comida.shape("circle") 
comida.color("red")
comida.penup()
comida.goto(0, 200)


# obstaculos 
obstaculos = []

for i in range (4):
    obstaculo = turtle.Turtle()
    obstaculo.shape("square")
    obstaculo.color("black")
    obstaculo.penup()
    obstaculo.goto(random.randint(-240, 240), random.randint(-240, 240) )
    obstaculo.speed = random.choice([1, 2]) #velocidad de los obstáculos
    obstaculo.direction = random.choice(["up", "down", "left", "right"])
    obstaculos.append(obstaculo)



# puntaje
puntaje = 0
puntajeMaximo = 0
nivel = 1
velocidad = 0.1


# carter game over
game_over = turtle.Turtle()
game_over.color("red")
game_over.hideturtle()
game_over.penup()


# Mostrar puntaje y el nombre del jugador
texto=turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup() 
texto.hideturtle()
texto.goto(0, 250)
texto.write(f"Jugador: {jugador_nom}      Puntaje: {puntaje}      Puntaje Maximo: {puntajeMaximo}     Nivel: {nivel}", align="center", font=("Calibri",13, "normal"))



# Crear segmentos iniciales de la serpiente
for i in range (0):
    nuevo_segmento=turtle.Turtle()
    nuevo_segmento.speed(0) #movimiento (rapido)
    nuevo_segmento.shape("turtle") #forma a la serpiente ("circle","triangle","arrow","turtle","classic","square")
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

    # Envoltura de los bordes
    if vibora.xcor() > 260: # en X
        vibora.setx(-260)
    elif vibora.xcor() < -260:
        vibora.setx(260)

    if vibora.ycor() > 260: # en Y
        vibora.sety(-260)
    elif vibora.ycor() < -260:
        vibora.sety(260)


# funcion para actualizar el puntaje en la pantalla
def actualizar_puntaje():
    texto.clear()
    texto.write(f"Jugador: {jugador_nom}      Puntaje: {puntaje}      Puntaje Maximo: {puntajeMaximo}     Nivel: {nivel}", align="center", font=("Calibri",13, "normal"))



def reiniciar_juego():
    global puntaje, puntajeMaximo, nivel, velocidad
    time.sleep(1)
    vibora.goto(0, 0)
    vibora.direction = "stop"

    # Ocultar los segmentos
    for segmento in segmentos: #(i)
        segmento.goto(1000,1000)

    # Limpiar la lista de segmentos
    segmentos.clear()

    # Recetear puntaje y niveles
    if puntaje > puntajeMaximo:
        puntajeMaximo = puntaje
    puntaje = 0
    nivel = 1
    velocidad = 0.1
    actualizar_puntaje()

def mostrar_cartel():
    game_over.clear()
    game_over.goto(0, 0)
    game_over.write("¡GAME OVER!", align="center", font=("Courier",30, "bold"))

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


velocidad_obstaculos = 1.3 #velocidad de los obstaculos

def mover_obstaulos():
    for obstaculo in obstaculos:
        if obstaculo.direction == "up":
            obstaculo.sety(obstaculo.ycor() + obstaculo.speed * velocidad_obstaculos)

        if obstaculo.direction == "down":
            obstaculo.sety(obstaculo.ycor() - obstaculo.speed * velocidad_obstaculos)

        if obstaculo.direction == "left":
            obstaculo.setx(obstaculo.xcor() - obstaculo.speed * velocidad_obstaculos)

        if obstaculo.direction == "right":
            obstaculo.setx(obstaculo.xcor() + obstaculo.speed * velocidad_obstaculos)

    #Cambiar de dirección si choca con el borde
        if obstaculo.xcor() > 260 or obstaculo.xcor() < -260:
            obstaculo.direction = "left" if obstaculo.direction == "right" else "right"

        if obstaculo.ycor() > 260 or obstaculo.ycor() < -260:
            obstaculo.direction = "down" if obstaculo.direction == "up" else "up"


def detector():
    global nivel
    for segmento in segmentos:
        if segmento.distance(vibora) < 20:
            mostrar_cartel()
            time.sleep(2)
            game_over.clear()
            reiniciar_juego()
            return
    
    for obstaculo in obstaculos:
        if obstaculo.distance(vibora) < 20:
            mostrar_cartel()
            time.sleep(2)
            game_over.clear()
            reiniciar_juego()
            return

#asignar las teclas
pantalla.listen() #escuchar al teclado
pantalla.onkeypress(arriba,"Up") #funcion y la tecla
pantalla.onkeypress(abajo,"Down")
pantalla.onkeypress(izquierda,"Left")
pantalla.onkeypress(derecha,"Right")



while True:
    pantalla.update()

    ultima_posicion = vibora.position() #guarda la posicion actual antes de mover


    if vibora.distance(comida) < 20:
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0) 
        nuevo_segmento.shape("turtle") 
        nuevo_segmento.color(color_serpiente)
        nuevo_segmento.penup()


        if len(segmentos) > 0:
            ultimo_segmento = segmentos[-1]
            nuevo_segmento.goto (ultimo_segmento.position())
        else:
            nuevo_segmento.goto(ultima_posicion)
        segmentos.append(nuevo_segmento)

        # Mover la comida aleatoriamente
        while True:
            x = random.randint(-240, 240)
            y = random.randint(-240, 240)
            nueva_posicion = (x,y)
            # verificacion de la nueva posicion que no este cerca
            distancia_serpiente = vibora.distance(nueva_posicion)
            distancia_segmentos = all(segmento.distance(nueva_posicion) > 20 for segmento in segmentos)
            if distancia_serpiente > 20 and distancia_segmentos:
                comida.goto(x,y)
                break

        # Aumentar puntaje y nivel
        puntaje += 10
        actualizar_puntaje()

        # Aumentar nivel cada 50 puntos
        if puntaje % 50 == 0: # % resto
            nivel += 1
            if nivel % 5 == 0: #aumentar la velocidad segun nivel o tiempo 
                velocidad_obstaculos += 1.0
            velocidad *= 0.9
            actualizar_puntaje()


    # mover los segmentos en orden inverso
    for i in range (len(segmentos) -1, 0, -1):
        x = segmentos [i-1].xcor ()
        y = segmentos [i-1].ycor ()
        segmentos[i].goto(x, y)

    #mover el primer segmento al lugar donde estaba la serpiente
    if len (segmentos) > 0:
        x = vibora.xcor()
        y = vibora.ycor()
        segmentos[0].goto(x,y)

    mover_obstaulos()
    
    mover() #siempre que se define algo se coloca al final

    detector()

    # # Detecta colision con los segmentos
    # for segmento in segmentos:
    #     if segmento.distance(vibora) < 20:
    #         reiniciar_juego()
    #         break

    # # Detecta colision con los obstaculos
    # for obstaculo in obstaculos:
    #     if obstaculo.distance(vibora) < 20:
    #         reiniciar_juego()
    #         break

    time.sleep(velocidad)
