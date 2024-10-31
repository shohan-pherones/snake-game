import turtle
import time

# Constants for adjustable settings
SNAKE_COLOR = "white"
BG_COLOR = "black"
INITIAL_LENGTH = 5
THICKNESS = 1
SPEED = 10
MOVEMENT_DELAY = 0.05

# Screen setup
def create_screen():
    screen = turtle.Screen()
    screen.title("Snake Game")
    screen.bgcolor(BG_COLOR)
    screen.setup(width=600, height=600)
    screen.tracer(0)
    return screen

# Snake class
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(INITIAL_LENGTH):
            segment = turtle.Turtle("square")
            segment.color(SNAKE_COLOR)
            segment.shapesize(stretch_wid=THICKNESS, stretch_len=1)
            segment.penup()
            segment.goto(-20 * i, 0)
            self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(SPEED)

    def go_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def go_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def go_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def go_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

# Screen and snake setup
screen = create_screen()
snake = Snake()

# Key bindings
screen.listen()
screen.onkeypress(snake.go_up, "w")
screen.onkeypress(snake.go_down, "s")
screen.onkeypress(snake.go_left, "a")
screen.onkeypress(snake.go_right, "d")

# Game loop
def game_loop():
    screen.update()
    snake.move()
    time.sleep(MOVEMENT_DELAY)
    screen.ontimer(game_loop, 1)

# Start the game loop
game_loop()
screen.mainloop()