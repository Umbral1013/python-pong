#!/usr/bin/python3

""" TÍTULO DEL DOCUMENTO: Pong en Python 3 para principiantes.
NOMBRE DEL ARCHIVO: python-pong.py
AUTOR: Umbral1013.
PROPÓSITO: Hacer una versión del Pong de @TokyoEdTech usando programación
    orientada a objetos.
    
    Enlace a la saga de vídeos original:
    https://www.youtube.com/playlist?list=PLlEgNdBJEO-kXk2PyBxhSmo84hsO3HAz2
FECHA DE CREACIÓN: mié 03 ago 2022 21:00:18
"""

import turtle

# Ventana.
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# Previene que la ventana se actualice. Ayuda con el rendimiento.
wn.tracer(0)

players = ["Jugador 1", "Jugador 2"]

# El primero es el jugador A, el segundo es el jugador B.
score = [0, 0]


class Paddle(turtle.Turtle):
    """ NOTAS
    - Para hacer una clase hija que sea una ligera modificación de otra
    clase padre, usa sus mismos métodos.
    - No variables, MÉTODOS.
    - Si quieres cambiar el valor de un keyword argument de la clase
    superior, debes pasar literalmente el valor en la posición donde se
    le espera.
    """
    def __init__(self, x_pos, y_pos=0):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("White")
        self.penup()
        # Características personalizadas.
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x_pos, y_pos)
        
    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)
        
    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)


class Ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("White")
        self.penup()
        self.goto(0, 0)
        # Controlan la rapidez de la pelota.
        self.dx = -0.1
        self.dy = 0.1
        
    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)


class Text(turtle.Turtle):
    # Se encarga de mostrar texto dentro del programa.
    def __init__(self, tint):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color(tint)
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        
    def show_score(self):
        self.clear()
        self.write("{0}: {1} // {2}: {3}".format(
            players[0], 
            score[0], 
            players[1], 
            score[1]),
            align="center",
            font=("FreeMono", 15, "bold"))


def collisions():
    """ Colisiones entre la paleta y la pelota. """
    if ((340 < ball.xcor() < 350) and
		(second_player.ycor() - 40 < ball.ycor() < second_player.ycor() + 40)):
            ball.setx(340)
            ball.dx += 0.02 # Es para hacer el juego más entretenido.
            ball.dx *= -1
    if ((-350 < ball.xcor() < -340) and
		(player_a.ycor() - 40 < ball.ycor() < player_a.ycor() + 40)):
            ball.setx(-340)
            ball.dx += 0.02
            ball.dx *= -1

def borderChecking():
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # Invierte la dirección al tocar el muro.
        superior.
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        service()
        score[0] += 1
        scoreboard.show_score()
    if ball.xcor() < -390:
        service()
        score[1] += 1
        scoreboard.show_score()

def service():
    ball.goto(0, 0)
    ball.dx *= -1

def checkDistance():
    """ Revisa si la distancia entre la pelota y la raqueta es mayor a 
    25 píxeles. """
    if abs(player_b.ycor() - ball.ycor()) > 55:
        return True

def robot():
    """ Revisa si la raqueta está en la misma coordenada 'y' que la 
    pelota. Si no lo está, mueve la raqueta hacia allá. """
    if (player_b.ycor() < ball.ycor()) and checkDistance():
        player_b.move_up()
    elif (player_b.ycor() > ball.ycor()) and checkDistance():
        player_b.move_down()

# Creando instancias.
player_a = Paddle(-350, 20)
player_b = Paddle(350, 35)
ball = Ball()
scoreboard = Text("Yellow")
scoreboard.show_score()

# La función es llamada cuando el usuario presiona la tecla señalada.
wn.onkeypress(player_a.move_up, "w")
wn.onkeypress(player_a.move_down, "s")
wn.onkeypress(player_b.move_up, "Up")
wn.onkeypress(player_b.move_down, "Down")

# Asignación de teclas.
wn.listen()

while True:
    # Actualiza la pantalla cada vez que el bucle corre.
    wn.update()
    ball.move()
    collisions()
    borderChecking()
    robot()

turtle.mainloop()
