"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""
# Importe de librerias turtle y freegames
from turtle import up, goto, down, circle, update, setup, hideturtle, tracer,\
                   onscreenclick, done

from freegames import line

# Añade 4 lineas para formar el campo de juego
def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

# Añade dos lineas para formar la X de uno de los jugadores
def drawx(x, y):
    """Draw X player."""
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)

# Añade un circulo de uno de los jugadores
def drawo(x, y):
    """Draw O player."""
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)

# Valor redondeado a la cuadrícula con tamaño cuadrado 133
def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]

# Draw X or O in tapped square
def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
