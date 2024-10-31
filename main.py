import turtle
import time
import random

SNAKE_COLOR = "white"
BG_COLOR = "black"
INITIAL_LENGTH = 5
THICKNESS = 1
SPEED = 15
MOVEMENT_DELAY = 0.05

def create_screen():
    screen = turtle.Screen()
    screen.title("Snake Game")
    screen.bgcolor(BG_COLOR)
    screen.setup(width=600, height=600)
    screen.tracer(0)
    return screen

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.shapesize(0.8, 0.8)
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score}", align="center", font=("Consolas", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Consolas", 32, "bold"))
        self.goto(0, -40)
        self.color("white")
        self.write("PRESS SPACE TO PLAY AGAIN", align="center", font=("Consolas", 16, "normal"))

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

    def grow(self):
        segment = turtle.Turtle("square")
        segment.color(SNAKE_COLOR)
        segment.shapesize(stretch_wid=THICKNESS, stretch_len=1)
        segment.penup()
        self.segments.append(segment)

    def check_wall_collision(self):
        x, y = self.segments[0].xcor(), self.segments[0].ycor()
        return x > 290 or x < -290 or y > 290 or y < -290

    def check_self_collision(self):
        return any(self.segments[0].distance(seg) < 10 for seg in self.segments[1:])

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()

screen = create_screen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.go_up, "w")
screen.onkeypress(snake.go_down, "s")
screen.onkeypress(snake.go_left, "a")
screen.onkeypress(snake.go_right, "d")
screen.onkeypress(lambda: play_again(), "space")

def play_again():
    scoreboard.score = 0
    scoreboard.clear()
    scoreboard.goto(-230, 260)
    scoreboard.update_scoreboard()
    snake.reset()
    game_loop()

def game_loop():
    screen.update()
    snake.move()

    if snake.segments[0].distance(food) < 20:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    if snake.check_wall_collision() or snake.check_self_collision():
        scoreboard.game_over()
        return

    time.sleep(MOVEMENT_DELAY)
    screen.ontimer(game_loop, 1)

game_loop()
screen.mainloop()