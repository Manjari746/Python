import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Flower")
screen
board= turtle.Turtle()
board.speed("fastest")
board.width(2)
board.hideturtle()

def draw_petal():
    for i in range(2):
        board.circle(80, 60)
        board.left(120)
    

board.goto(0,0)
Petal_colors = ["cyan", "lime", "violet", "orange", "deeppink"]
length = len(Petal_colors)
for i in range(36):
    board.color(Petal_colors[i%length],Petal_colors[(i+2)%length])
    board.pendown()
    board.begin_fill()
    draw_petal()
    board.end_fill()
    board.right(10)

board.penup()
board.goto(0,-30)
board.pendown()
board.color("white")
board.begin_fill()
board.circle(25)
board.end_fill()

turtle.done()

