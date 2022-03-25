"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""
# Importe de librerias turtle y freegames
from turtle import up, goto, down, circle, update, setup, hideturtle, tracer,\
                   onscreenclick, done, color

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
    color('red')
    line(x + 33, y + 33, x + 100, y + 100)
    line(x + 33, y + 100, x + 100, y + 33)


# Añade un circulo de uno de los jugadores
def drawo(x, y):
    """Draw O player."""
    color('blue')
    up()
    goto(x + 66, y + 33)
    down()
    circle(33)


# Valor redondeado a la cuadrícula con tamaño cuadrado 133
def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
places_on_grid = [
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " "]


# Dibuja una X u O en el cuadro seleccionado
def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

    player = state['player']
    draw = players[player]

    if x == -200 and y == 66:
        if places_on_grid[0] == " ":
            places_on_grid[0] = 1
            draw(x, y)
            update()
            state['player'] = not player
            print("Lugar Valido")

        elif places_on_grid[0] != "":
            print("OCUPADO")

    elif x == -67 and y == 66:
        if places_on_grid[1] == " ":
            places_on_grid[1] = 1
            draw(x, y)
            update()
            state['player'] = not player
            print("Lugar Valido")

        elif places_on_grid[1] != "":
            print("OCUPADO")

    elif x == 66 and y == 66:
        if places_on_grid[2] == " ":
            places_on_grid[2] = 1
            draw(x, y)
            update()
            state['player'] = not player
            print("Lugar Valido")

        elif places_on_grid[2] != "":
            print("OCUPADO")

    elif x == -200 and y == -67:
        if places_on_grid[3] == " ":
            places_on_grid[3] = 1
            draw(x, y)
            update()
            state['player'] = not player
            print("Lugar Valido")

        elif places_on_grid[3] != "":
            print("OCUPADO")

    elif x == -67 and y == -67:
        if places_on_grid[4] == " ":
            places_on_grid[4] = 1
            draw(x, y)
            update()
            state['player'] = not player
            print("Lugar Valido")

        elif places_on_grid[4] != "":
            print("OCUPADO")

    elif x == 66 and y == -67:
        if places_on_grid[5] == " ":
            places_on_grid[5] = 1
            draw(x, y)
            update()
            state['player'] = not player
            print("Lugar Valido")

        elif places_on_grid[5] != "":
            print("OCUPADO")

    elif x == -200 and y == -200:
        if places_on_grid[6] == " ":
            places_on_grid[6] = 1
            draw(x, y)
            update()
            state['player'] = not player
            print("Lugar Valido")

        elif places_on_grid[6] != "":
            print("OCUPADO")

    elif x == -67 and y == -200:
        if places_on_grid[7] == " ":
            places_on_grid[7] = 1
            draw(x, y)
            update()
            state['player'] = not player
            print("Lugar Valido")

        elif places_on_grid[7] != "":
            print("OCUPADO")

    elif x == 66 and y == -200:
        if places_on_grid[8] == " ":
            places_on_grid[8] = 1
            draw(x, y)
            update()
            state['player'] = not player
            print("Lugar Valido")

        elif places_on_grid[8] != "":
            print("OCUPADO")


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
