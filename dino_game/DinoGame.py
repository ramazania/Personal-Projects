import turtle
import random
import time

# set up screen
screen = turtle.Screen()
screen.title("Chrome Dinosaur Game")
screen.bgcolor("lightgray")
screen.tracer(0)

# create player turtle
player = turtle.Turtle()
screen.addshape("dino.gif")
player.shape("dino.gif")
player.penup()
player.speed(10)
player.setposition(-250, 115)

# create ground
ground = turtle.Turtle()
ground.color("green")
ground.shape("square")
ground.penup()
ground.speed(0)
ground.shapesize(stretch_wid=1, stretch_len=500)
ground.setposition(0, 80)

# create obstacles
obstacle_count = 5
obstacle_width = 2
obstacle_start_x = 250
obstacle_start_y = 100

obstacles = []
for i in range(obstacle_count):
    obstacle = turtle.Turtle()
    obstacle.color("red")
    obstacle.shape("triangle")
    obstacle.left(90)
    obstacle.penup()
    obstacle.speed(0)
    obstacle.setposition(obstacle_start_x + i * (obstacle_width + random.randint(100, 150)), obstacle_start_y)
    obstacles.append(obstacle)


#move player up
def move_up():
    y = player.ycor()
    x = player.xcor()
    y += 80
    x -= 10
    player.sety(y)
    screen.update()
    player.setx(x)
    time.sleep(.1)  
    y = player.ycor()
    y -= 80
    x += 20
    if x > 250:
        x = -250
        player.setx(x) 
    player.sety(y)
    player.setx(x) 
  
# bind key events
screen.listen()
screen.onkeypress(move_up, "space")


# create lives
lives = 10
lives_pen = turtle.Turtle()
lives_pen.speed(100)
lives_pen.color("black")
lives_pen.penup()
lives_pen.setposition(-280, 250)
lives_string = "lives: {}".format(lives)
lives_pen.write(lives_string, False, align="left", font=("Arial", 14, "normal"))
lives_pen.hideturtle()


# game loop
while lives > 0:
    screen.update()
    for obstacle in obstacles:
        x = obstacle.xcor()
        x -= 1
        obstacle.setx(x)
        screen.update()
        # reset obstacle if it hits the edge
        if x < -350:
            x = obstacle_start_x + (obstacle_count - 1) * (obstacle_width + random.randint(50, 100))
            obstacle.setx(x)
            screen.update()
        # check for collision
        if abs(player.xcor() - obstacle.xcor()) < 1:
            lives -= 1
            lives_pen.clear()
            lives_pen.write("lives: {}".format(lives), False, align="left", font=("Arial", 14, "normal"))

    if lives <= 0:
        # game over
        end_pen = turtle.Turtle()
        end_pen.setposition(0, 200)
        end_pen.write("Game Over!", False, align="left", font=("Arial", 14, "normal"))
        time.sleep(3)
        break