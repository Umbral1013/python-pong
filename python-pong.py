#!/usr/bin/python3

""" TÍTULO DEL DOCUMENTO: Pong en Python 3 para principiantes.
NOMBRE DEL ARCHIVO: pong_v2.py
AUTOR: Umbral1013.
PROPÓSITO: Hacer una versión del Pong de @TokyoEdTech usando programación
    orientada a objetos.
    
    Enlace a la saga de vídeos original:
    https://www.youtube.com/playlist?list=PLlEgNdBJEO-kXk2PyBxhSmo84hsO3HAz2
FECHA: mié 03 ago 2022 21:00:18
HISTORIAL DEL DOCUMENTO:
	Versión - Fecha - Comentarios
    02 - 03/07/2022 - Pasar el código a POO.
"""

import turtle

# Ventana.
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# Previene que la ventana se actualice. Ayuda con el rendimiento.
wn.tracer(0)

players = ["Jugador A", "Jugador B"]
# El primero es el jugador A, el segundo es el jugador B.
score = [0, 0]


class Clay(turtle.Turtle):
    """ Nunca se usa esta clase directamente en el juego. Es para hacer el
    código más breve.

    Se llama Clay (arcilla, en inglés) porque todas las clases usadas en el
    juego son 'modeladas' a partir de ésta.
    """
    def __init__(self, tint="white"):
        # Quiero que turtle.Turtle se encargue de manejar las cosas que Clay
        # heredó de ella.
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color(tint)
        self.penup()


class Paddle(Clay):
    """ NOTAS:
    - Para hacer una clase hija que sea una ligera modificación de otra clase
      padre, usa sus mismos métodos.
    - No variables, MÉTODOS.
    - Si quieres cambiar el valor de un keyword argument de la clase superior,
      debes pasar literalmente el valor en la posición donde se le espera.
    """
    def __init__(self, x_pos, y_pos=0):
        Clay.__init__(self)
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


class Ball(Clay):
    def __init__(self):
        Clay.__init__(self)
        self.goto(0, 0)
        # Controlan la rapidez de la pelota.
        self.dx = -0.1
        self.dy = 0.1

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)


class Text(Clay):
    # Se encarga de mostrar texto dentro del programa.
    def __init__(self, tint):
        Clay.__init__(self, tint)
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
    # Colisiones entre la paleta y la pelota.
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 40 < ball.ycor() <
                                      paddle_b.ycor() + 40):
        ball.setx(340)
        ball.dx *= -1
        
    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 40 < ball.ycor() <
                                        paddle_a.ycor() + 40):
        ball.setx(-340)
        ball.dx *= -1

def borderChecking():
    if ball.ycor() > 290:
        ball.sety(290)
        # Invierte la dirección al tocar el muro superior.
        ball.dy *= -1

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
    """ Revisa si la distancia entre la pelota y la raqueta es mayor a 25
    píxeles.
    """
    if abs(paddle_b.ycor() - ball.ycor()) > 25:
        return True

def robot():
    """ Revisa si la raqueta está en la misma coordenada 'y' que la pelota. Si
    no lo está, mueve la raqueta hacia allá.
    """
    if (paddle_b.ycor() < ball.ycor()) and checkDistance():
        paddle_b.move_up()
    elif (paddle_b.ycor() > ball.ycor()) and checkDistance():
        paddle_b.move_down()

# Creando instancias.
paddle_a = Paddle(-350)
paddle_b = Paddle(350)
ball = Ball()
scoreboard = Text("Yellow")
scoreboard.show_score()

# Asignación de teclas.
wn.listen()
# Cuando el usuario presiona "w", la función paddle_a_up es llamada.
wn.onkeypress(paddle_a.move_up, "w")
wn.onkeypress(paddle_a.move_down, "s")
wn.onkeypress(paddle_b.move_up, "Up")
wn.onkeypress(paddle_b.move_down, "Down")

while True:
    # Actualiza la pantalla cada vez que el bucle corre.
    wn.update()
    ball.move()
    collisions()
    borderChecking()
    robot()
